#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <errno.h>

using namespace std;

static int
ProcessInput(int argc, char *argv[], FILE **inFile, FILE **outFile, char *buf, int bufSize)
{
  int numTestCases = 0;

  if (argc < 2 || argc > 3)
  {
    printf("Usage is %s input_file [output_file]\n", argv[0]);
    return -1;
  }

  errno = 0;
  *inFile = fopen(argv[1], "r");
  if (NULL == *inFile)
  {
    fprintf(stderr, "Error: Could not open input file %s for reading : %s\n", argv[1], strerror(errno));
    return -1;
  }

  *outFile = (3 == argc) ? fopen(argv[2], "w") : stdout;
  if (NULL == *outFile)
  {
    fprintf(stderr, "Could not open output file %s for writing : %s\n", (3 == argc) ? argv[2] : "stdout", strerror(errno));
    return -1;
  }

  fgets(buf, bufSize, *inFile);
  sscanf(buf, "%u", &numTestCases);

  return numTestCases;
}

class TrainStation
{
  private:
    vector<int> arrival;
    vector<int> departure;

  public:
    void arrived(int time) {arrival.push_back(time);}
    void departed(int time) {departure.push_back(time);}
    int min_trains(void)
    {
      int numTrains = 0;
      int minTrains = 0;

      sort(arrival.begin(), arrival.end());
      sort(departure.begin(), departure.end());

      vector<int>::const_iterator ita = arrival.begin();
      vector<int>::const_iterator itd = departure.begin();

      while (ita != arrival.end() || itd != departure.end())
      {
        if (itd == departure.end()) { numTrains++; ita++; }
        else if (ita == arrival.end()) { numTrains--; itd++; }
        else
        {
          if (*ita <= *itd) { numTrains++; ita++; }
          else { numTrains--; itd++; }
        }
        minTrains = min(minTrains, numTrains);
      }

      return ((minTrains > 0) ? 0 : (0 - minTrains));
    }
};

char *
Test(FILE *inFile)
{
  static char buf[100];
  TrainStation A, B;
  int T;
  if (NULL == fgets(buf, sizeof(buf), inFile))
  {
    fprintf(stderr, "Error reading input\n");
    exit(-1);
  }
  sscanf(buf, "%d", &T);

  int NA, NB;
  if (NULL == fgets(buf, sizeof(buf), inFile))
  {
    fprintf(stderr, "Error reading input\n");
    exit(-1);
  }
  sscanf(buf, "%d %d", &NA, &NB);

  for (int i = 0; i < NA; ++i)
  {
    int hrd, mind, hra, mina;
    if (NULL == fgets(buf, sizeof(buf), inFile))
    {
      fprintf(stderr, "Error reading input\n");
      exit(-1);
    }
    sscanf(buf, "%d:%d %d:%d", &hrd, &mind, &hra, &mina);
    A.departed(hrd*60+mind);
    B.arrived(hra*60+mina+T);
  }
  
  for (int i = 0; i < NB; ++i)
  {
    int hrd, mind, hra, mina;
    if (NULL == fgets(buf, sizeof(buf), inFile))
    {
      fprintf(stderr, "Error reading input\n");
      exit(-1);
    }
    sscanf(buf, "%d:%d %d:%d", &hrd, &mind, &hra, &mina);
    B.departed(hrd*60+mind);
    A.arrived(hra*60+mina+T);
  }

  sprintf(buf, "%d %d", A.min_trains(), B.min_trains());
  return buf;
}

int
main(int argc, char *argv[])
{
  FILE *inFile, *outFile;
  int num, numTestCases = 0;
  char buf[256];

  memset(buf, '\0', sizeof(buf));
  if (0 >= (numTestCases = ProcessInput(argc, argv, &inFile, &outFile, buf, sizeof(buf))))
  {
    fprintf(stderr, "Cannot proceed, exiting now\n");
    return -1;
  }

  for (num = 1; num <= numTestCases; ++num)
  {
    fprintf(outFile, "Case #%d: %s\n", num, Test(inFile));
  }

  return 0;
}

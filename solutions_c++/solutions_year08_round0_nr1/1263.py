#include <iostream>
#include <string>
#include <map>
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

static int
Test(FILE *inFile)
{
  char buf[101];

  if (NULL == fgets(buf, sizeof(buf), inFile))
  {
    fprintf(stderr, "Error reading input\n");
    exit(-1);
  }
  strtok(buf, "\n");
  int numEngines = atoi(buf);
  map<string, int> se;

  for (int i = 0; i < numEngines; ++i)
  {
    if (NULL == fgets(buf, sizeof(buf), inFile))
    {
      fprintf(stderr, "Error reading input\n");
      exit(-1);
    }
    strtok(buf, "\n");
    se[buf] = i;
  }
  
  if (NULL == fgets(buf, sizeof(buf), inFile))
  {
    fprintf(stderr, "Error reading input\n");
    exit(-1);
  }
  strtok(buf, "\n");
  int numQueries = atoi(buf);
  int engines[100] = {0};
  int numSwitches = 0;
  int numEngOccured = 0;
  for (int i = 0; i < numQueries; ++i)
  {
    if (NULL == fgets(buf, sizeof(buf), inFile))
    {
      fprintf(stderr, "Error reading input\n");
      exit(-1);
    }
    strtok(buf, "\n");
    int idx = se[buf];

    if (!engines[idx])
    {
      engines[idx] = 1;
      if (++numEngOccured == numEngines)
      {
        numSwitches++;
        memset(engines, 0, sizeof(engines));
        numEngOccured = 1;
        engines[idx] = 1;
      }
    }
  }

  return numSwitches;
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
    fprintf(outFile, "Case #%d: %d\n", num, Test(inFile));
  }

  return 0;
}

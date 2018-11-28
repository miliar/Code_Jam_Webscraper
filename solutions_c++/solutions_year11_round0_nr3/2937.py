
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
using namespace std;

#define MAX_NUM_CANDIES 1000000

class CandySplit {
  private:
    unsigned int candy[MAX_NUM_CANDIES];
    unsigned int num_candies;
    unsigned int min_value;
    unsigned int result;

  public:
    CandySplit() {
      num_candies = 0;
      min_value = 10000000;
      result = 0;
    }

    ~CandySplit() {
    }

    void addCandyValue(int value) {
      candy[num_candies] = value;
      ++num_candies;
      if (num_candies >= MAX_NUM_CANDIES) {
	fprintf(stderr, "Candy overflow!\n");
	exit(0);
      }
      if (value < min_value)
	min_value = value;
    }

    void divideCandies() {
      unsigned int sum = 0;
      unsigned int xor_result = candy[0];

      sum = candy[0];
      for (unsigned int i = 1; i < num_candies; i++) {
	xor_result ^= candy[i];
	sum += candy[i];
      }
      if (xor_result != 0) {
	// Division not possible
	result = 0;
	return;
      }
      else {
	result = sum - min_value;
      }
    }

    void print(FILE *fp) {
      fprintf(fp, "Candies:\n");
      for (unsigned int i = 0; i < num_candies; i++) {
	fprintf(fp, "%d ", candy[i]);
      }
      fprintf(fp, "\n");
    }

    void printResult(FILE *fp) {
      if (result > 0) {
	fprintf(fp, "%d", result);
      }
      else {
	fprintf(fp, "NO");
      }
    }
};

void skipWS(FILE *fp)
{
  char s[1024];
  fscanf(fp, "%[ \t\n]", s);
}

int main(int argc, char **argv)
{
  FILE *infile = NULL, *outfile = NULL;
  int numtests = 0, i = 0, j = 0;
  CandySplit *candy = NULL;

  if (argc != 2) {
    printf("Usage %s <input_file>\n", argv[0]);
    return -1;
  }

  infile = fopen(argv[1], "r");
  if (!infile) {
    printf("Cannot find file %s\n", argv[1]);
    return -1;
  }

  outfile = fopen("result.out", "w");
  if (!outfile) {
    printf("Cannot open output file result.out for writing.\n");
    fclose(infile);
    return -1;
  }

  fscanf(infile, "%d", &numtests);
  if (numtests <= 0) {
    fclose(infile);
    fclose(outfile);
    return 0;
  }

  candy = new CandySplit[numtests];
  for (i = 0; i < numtests; i++) {
    int num_candies = 0, value = 0;

    skipWS(infile);
    fscanf(infile, "%d", &num_candies);
    for (j = 0; j < num_candies; j++) {
      skipWS(infile);
      fscanf(infile, "%d", &value);
      candy[i].addCandyValue(value);
    }
  }
  fclose(infile); infile = NULL;

  for (i = 0; i < numtests; i++) {
    candy[i].divideCandies();

    fprintf(outfile, "Case #%d: ", i + 1);
    candy[i].printResult(outfile);
    fprintf(outfile, "\n");
#if 0
    /* Test */
    candy[i].print(stdout);
#endif
  }

  delete [] candy;

  fclose(outfile);
  return 0;
}


#include <stdio.h>
#include <math.h>
#include <iostream>

using namespace std;

int getNumberLength(int number)
{
  int length = 0;
  while(number != 0)
  {
    length++;
    number /= 10;
  }
  return length;
}

bool isValid(int upperBound, int lowerBound, int number, int newNumber)
{
  return (newNumber >= lowerBound) && (newNumber <= upperBound) && (newNumber > number);
}

int moveDigits(int number, int digits, int numberLength)
{
  int digitsPow = pow(10, digits);
  int digitsToMove = number % digitsPow;
  int remainingNumber = number / digitsPow;
  int newNumber = digitsToMove * pow(10, numberLength) / digitsPow + remainingNumber;
  return newNumber;
}

int main()
{
  FILE *in = fopen("input", "r");
  FILE *out = fopen("output", "w");
  int testcases;
  fscanf(in, "%d", &testcases);
  for(int i = 0; i < testcases; i++)
  {
    int lowerBound, upperBound, count = 0;
    fscanf(in, "%d%d", &lowerBound, &upperBound);
    for(int number = lowerBound; number <= upperBound; number++)
    {
      int numberLength = getNumberLength(number);
      for(int digits = 1; digits < numberLength; digits++)
        if(isValid(upperBound, lowerBound, number, moveDigits(number, digits, numberLength))) { cout << number << " " << moveDigits(number, digits, numberLength) << endl;  count++; }
    }
    fprintf(out, "Case #%d: %d\n", i + 1, count);
  }
  fclose(in);
  fclose(out);
  return 0;
}

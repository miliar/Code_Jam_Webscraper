#include <iostream>
#include <fstream>

using namespace std;

int main()
{
  int n, k;
  int value = 0;
  int counter = 0;
  int total_cases = 0;

  ifstream input("A-large.in");
  ofstream output("output.txt");

  if ((!input) || (!output))
  {
    cerr << "error opening file(s)";
    exit(1);
  }

  n = k = 0;

  input >> total_cases;
  while (counter != total_cases)
  {
    counter++;

    input >> n >> k;

    value = (k + 1) % (2 << (n - 1));


    output << "Case #" << counter << ": " << (value == 0? "ON" : "OFF") << endl;
  }

  input.close();
  input.close();
  return 0;
}

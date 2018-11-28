#include <iostream>
#include <fstream>

using namespace std;

bool light_on(int, int);
int init_k(int);

int main(int argc, char** argv)
{
  ifstream input; 
  ofstream output;
  if(argc > 1) {
    input.open(argv[1]);
    output.open("output.txt");
  }
  else
    exit(1);
  int i = 0;
  input >> i;
  for(int c = 1; i > 0; i--, c++) {
    int n = 0, k = 0;
    input >> n >> k;
    output << "Case #" << c << ": ";
    output << (light_on(n,k) ? "ON" : "OFF") << endl;
  }
  output.close();
}

bool light_on(int n, int k)
{
  int K0 = init_k(n);
  double j = 0;
  if(k < 1)
    return false;
  if(k == K0)
    return true;
  else 
    for(int i = 1; j < k; i++)
      j = K0 * i + (i - 1);
  return j == k ? true : false;
}

int init_k(int i)
{
  return i == 1 ? 1 : init_k(i - 1) * 2 + 1;
}

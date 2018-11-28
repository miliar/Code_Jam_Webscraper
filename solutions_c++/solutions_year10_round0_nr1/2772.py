#include <stdio.h>
#include <math.h>
#include <fstream>
#include <iostream>
using namespace std;

void calccases();

long long border = pow(10, 8);

int main(int argc, char *argv[])
{
  calccases();

  return 0;
}

bool snapperchain(long long n, long long k)
{
 if (n < 1 || n > 30 || k < 0 || k > border)
 {
  //cout<<"input is invalid!"<<endl;

  return false;
 }

 long long deadline = pow(2, n);

 if ((k % deadline) == deadline - 1)
 {
  return true;
 }

 return false;
}

void calccases()
{
 ifstream input("C:\\Users\\randysheriff\\Desktop\\GoogleJam\\A-large.in");

 ofstream output("C:\\Users\\randysheriff\\Desktop\\GoogleJam\\A-large.output");

 int cases;

 input >> cases;

 cout << cases << endl;

 int i = 0;

 while (i < cases)
 {
  long long n;

  input >> n;

  long long k;

  input >> k;

//  cout << n << "," << k << endl;

  output << "Case #" << i + 1 << ": ";

 // output << n << "," << k << " ";

  if (snapperchain(n, k))
  {
   output << "ON" << endl;
  }
  else
  {
   output << "OFF" << endl;
  }

  i++;
 }

 //cin >> cases;
}

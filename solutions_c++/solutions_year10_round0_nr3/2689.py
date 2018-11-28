#include <stdio.h>
#include <vector>
#include <iostream>
#include <fstream>

using namespace std;

void themepark();

int main(int argc, char *argv[])
{
 int i;

 themepark();

 cin >> i;

 return 0;
}

unsigned long long rollercoaster(
unsigned long long r, unsigned long long c_r, unsigned long long k,
vector<unsigned long long>& gps, vector<unsigned long long>::iterator& iter)
{
 if (c_r > r)
 {
  return 0;
 }

 unsigned long long sum = 0;

 if(iter == gps.end())
 {
  iter = gps.begin();
 }

 vector<unsigned long long>::iterator start_iter = iter;

 while(sum + *iter <= k)
 {
    sum += *iter;

    *iter++;

    if(iter == gps.end())
    {
     iter = gps.begin();
    }

    if(iter == start_iter)
    {
     break;
    }
 }

 sum += rollercoaster(r, c_r + 1, k, gps, iter);

 return sum;
}

void themepark()
{
 unsigned long long n;

 unsigned long long k;

 unsigned long long gp;

 ifstream input("C:\\Users\\randysheriff\\Desktop\\GoogleJam\\themepark\\C-small-attempt0.in");

 ofstream output("C:\\Users\\randysheriff\\Desktop\\GoogleJam\\themepark\\output.out");

 unsigned long long count;

 input >> count;

 unsigned long long i = 0;

 while(i < count)
 {
  input >> n;

  input >> k;

  input >> gp;

  vector<unsigned long long> gps;

  for(int i = 0; i < gp; i++)
  {
   unsigned long long j;

   input >> j;

   gps.push_back(j);
  }

  vector<unsigned long long>::iterator iter = gps.begin();

  output << "Case #" << i + 1 << ": ";

  output << rollercoaster(n, 1, k, gps, iter) << endl;

  i++;
 }
}

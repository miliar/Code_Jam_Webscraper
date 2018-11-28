#include <iostream>
#include <fstream>
#include <vector>
#include <numeric>
using namespace std;
int PAdd(int a, int b)
{
  return a^b;
}
int SeanMax=0;
void docandy(const int* A, int length, int sean, int patrik, int psean, int ppatrik)
{
  if (length==0)
  {
    if (psean==ppatrik && sean!=0 && patrik!=0) {SeanMax = max(SeanMax, sean);}
    return;
  }
  //1. Sean gets next
  docandy(A+1,length-1, sean + A[0], patrik, psean ^ A[0], ppatrik); 
  //2. Sean does not get next
  docandy(A+1,length-1, sean, psean+A[0], psean, patrik^A[0]); 
}

void candy(int casenumber, const int* A, int length)
{
  //printf("candy ");
  //for(int i=0;i<length;i++)
  //{
  //  printf("%d ", A[i]);
  //}
  //
  int psum = accumulate(A, A+length, 0, PAdd);
//  printf("psum %d", psum);
  if (psum!=0)
  {
  cout << "Case #"<<casenumber<<": NO" << endl;
  return;
  }
  SeanMax = 0;
  docandy(A, length, 0, 0, 0, 0);
  cout << "Case #"<<casenumber<<": " << SeanMax << endl;
}

int main(int argc, char** argv)
{
  if (argc!=2) return -1;

  ifstream f(argv[1]);
  //ifstream f("d:\\jam\\magicka\\test.in");
  int lines;
  f >> lines;
  for (int i=0;i<lines;i++)
  {
    int length;
    f>>length;
    int * A = new int[length];
    for(int j=0;j<length;j++)
    {
      f>>A[j];
    }
    candy(i+1, A, length);
    delete [] A;
  }
}
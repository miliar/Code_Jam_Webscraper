#include <fstream>
#include <cstring>
#include <sstream>
#include <map>
#include <iostream>

using namespace std;

long long solve(char *buf)
{

    map<char,int> kirjaimet;
    int mika[1000];


    int len = strlen(buf);

    int diff = 1;
    mika[0] = 1;
    int eri = 1;
    long long  vals[1000];



    for(int i = 1; i < len; i++)
    {
         mika[i] = 0;
         for(int j = 0; j < i; j++)
         {
           if(buf[i] == buf[j])
                mika[i] = mika[j];

         }

         if(mika[i] == 0)
            mika[i] = ++eri;


    }

    vals[1] = 1;
    vals[2] = 0;
    for(int i = 2; i < eri; i++)
     vals[i+1] = i;


    long long luku = 0;
    long long base  = eri;
    if(base == 1)
        base = 2;
    long long fact = 1;

    for(int i = len-1; i >= 0; i--)
        {
            luku+=fact*vals[mika[i]];
            fact*=base;
        }


    return luku;
}


int main()
{
  ifstream filein("input1.txt");
  ofstream fileout("output1.txt");


  int t;
  filein>>t;
  char buff[511];
  filein.getline(buff,500);

  for(int i = 0; i < t; i++)
  {
    filein.getline(buff,500);
    long long res = solve(buff);

    fileout<<"Case #"<<i+1<<": "<<res<<endl;
    cout<<"Case #"<<i+1<<": "<<res<<endl;
    cout<<buff<<endl;
  }



  filein.close();
  fileout.close();

  return 0;
}

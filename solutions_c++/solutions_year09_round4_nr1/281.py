#include <fstream>
#include <cstring>
#include <sstream>
#include <map>
#include <iostream>
#include <algorithm>

using namespace std;

int square[100];


int solve(ifstream &filein)
{
    int n;
    filein>>n;
    char buff[512];
    filein.getline(buff,500);
    for(int i = 0; i < n; i++)
    {
        square[i] = 0;
        filein.getline(buff,500);
        //cout<<buff<<endl;
        for(int j = 0; j < n; j++)
        {
            if(buff[j] == '1')
            square[i] = j+1;
        }

    }

    int swaps = 0;
    for(int i = 0; i < n; i++)
    {
        int i2 = i;
        while(square[i2] > i+1) i2++;

        while(i2 > i)
        {
            swap(square[i2],square[i2-1]);
            swaps++;
            i2--;
        }

    }
    return swaps;
}


int main()
{
  ifstream filein("input1.txt");
  ofstream fileout("output1.txt");


  int t;
  filein>>t;

  for(int i = 0; i < t; i++)
  {
    int res = solve(filein);

    fileout<<"Case #"<<i+1<<": "<<res<<endl;
    cout<<"Case #"<<i+1<<": "<<res<<endl;
  }



  filein.close();
  fileout.close();

  return 0;
}

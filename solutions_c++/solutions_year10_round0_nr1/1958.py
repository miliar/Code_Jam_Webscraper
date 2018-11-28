#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

////file selection
void SetInputFile()
{ char filename[32], infile[32], outfile[32]; scanf("%s", filename);
  strcpy(infile, filename); strcpy(outfile, filename); strcat(infile, ".in"); strcat(outfile, ".out");
  freopen(infile, "r", stdin); freopen(outfile, "w", stdout);
}

long testcase,cases=1;
long long k,value;
int n;

int main()
{
    SetInputFile();
    cin>> testcase;
    cases=1;
    while(testcase--)
    {
      cin>>n>>k;
      value = (long long)pow(2.0,n);
      k++;
      if(k%value==0)
            cout<<"Case #"<<cases++<<": "<<"ON"<<endl;
      else
            cout<<"Case #"<<cases++<<": "<<"OFF"<<endl;                    
    }
    
}

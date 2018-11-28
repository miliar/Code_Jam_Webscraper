#include<vector>
#include<stdio.h>
#include<iostream>
#include<fstream>
#include<bitset>
#include<algorithm>
#include<string.h>

using namespace std;

int main()
{
    long long int temp,sum=0,max;
    int n_test_cases,z,i,j,k,N;
    char ch;
    
    long long int a[1002],b[1002];
    
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    fin>>n_test_cases;
    for(z=1;z<=n_test_cases;z++)
    {
                                fin>>N;
                                for(i=0;i<=N-1;i++)
                                fin>>a[i]>>b[i];
                                sum=0;
                                for(i=0;i<=N-1;i++)
                                {
                                                   for(j=0;j<=N-1;j++)
                                                   {
                                                                      if(a[j]<a[i] && b[j]>b[i])
                                                                      sum++;
                                                                      else if(a[j]>a[i] && b[j]<b[i])
                                                                      sum++;
                                                   }
                                }
                                
                                
                                
                                fout<<"Case #"<<z<<":";
                                fout<<' '<<sum/2;
                                fout<<endl;
                                                 
                                
    }
    fout.close();
    fin.close();
    
    
}

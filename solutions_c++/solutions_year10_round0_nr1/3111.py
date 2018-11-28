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
    int temp,sum=0,max;
    int n_test_cases,z,i,j,k,n;
    char ch;
    
    int K,N,Kmod2;
    
   
    
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    fin>>n_test_cases;
    cout<<n_test_cases;
    for(z=1;z<=n_test_cases;z++)
    {
                                fin>>N>>K;
                                for(i=0;K!=0;i++)
                                {
                                 Kmod2=K%2;
                                 if(i==N || Kmod2==0)
                                 break;
                                 K=K/2;
                                }
                                if(i==N)
                                fout<<"Case #"<<z<<": ON";
                                else
                                fout<<"Case #"<<z<<": OFF";
                                //cout<<"Case #"<<z<<": ON";
                                
                                fout<<endl;
                                                 
                                
    }
    fout.close();
    fin.close();
    
    
    
}

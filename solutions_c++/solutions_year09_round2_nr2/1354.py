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
    long long int num,temp,sum=0,max,tempi,a;
    int n_test_cases,z,i,j,k,tempb[15],b[15];
    char ch;
    
    long long int freq[1002];
    
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    fin>>n_test_cases;
    for(z=1;z<=n_test_cases;z++)
    {
                                fin>>num;
                                temp=num;
                                for(j=0;j<=10;j++)
                                b[j]=0;
                                
                                while(num!=0)
                                {
                                             a=num%10;
                                             b[a]++;
                                             num=num/10;
                                }
                                for(i=temp+1;1;i++)
                                {
                                                  tempi=i;
                                                  for(j=0;j<=10;j++)
                                                  tempb[j]=0;
                                                  while(tempi!=0)
                                                  {                                                            
                                                  a=tempi%10;
                                                  tempb[a]++;
                                                  tempi=tempi/10;
                                                  }
                                                  for(j=1;j<=9;j++)
                                                  {
                                                                   if(tempb[j]!=b[j])
                                                                   break;
                                                  }
                                                  if(j==10)
                                                  {
                                                           fout<<"Case #"<<z<<":";
                                                           fout<<' '<<i;
                                                           fout<<endl;
                                                           break;
                                                  }
                                                  
                                                  
                                                  
                                }

                                
                                
                                
                                
                                                 
                                
    }
    fout.close();
    fin.close();
    
    
}

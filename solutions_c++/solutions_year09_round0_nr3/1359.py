#include<iostream>
#include<stdio.h>
#include<fstream>
#include <string.h>
#include <algorithm>
#include <stdlib.h>
#include <vector>


#define STRSIZE      501
#define ASIZE        19
#define MAX          10000

using namespace std;

char  d[STRSIZE];
char w[]="welcome to code jam";
int a[ASIZE];//for every char in above string
int N;


int main(int argc, char* argv[])
{
    int i,l,j,k;
    cin>>N;
    cin.getline(d,STRSIZE);
    for(k=0;k<N;k++)
    {
            cin.getline(d,STRSIZE);
            cout<<"Case #"<<k+1<<": ";
            l = strlen(d);
            l--;
            for(i=0;i<ASIZE;i++)
                        a[i]=0;
            while (l>=0)
            {
                  for(j=0;j<ASIZE;j++)
                  {
                                      if(w[j]==d[l])
                                      {
                                                    if(j==ASIZE-1)//last element
                                                                         a[j]=(a[j]+1)%MAX;
                                                    else
                                                        a[j]=(a[j]+a[j+1])%MAX;
                                      }
                  }
                  l--;
                  
            }

            printf("%04d\n",a[0]);
            
    }
    //system("PAUSE");
    return 1;
}

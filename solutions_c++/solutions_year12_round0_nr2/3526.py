/*
 *Developed using vim text editor
 *VIM - Vi IMproved 7.3
 * Compile using g++
 * Command to compile : g++ -o jam2 jam2.cpp
 * Usage: ./jam2 < INPUTFILE > OUTPUTFILE
 * */
#include<iostream>
#include<algorithm>
using namespace std;
int main()
  { int t,s,p,score[150];
    int i,j,k,counter=0;
    int pleast[11],pleastwsurp[11];
    int n;
    cin>>n;
    for(j=1;j<=n;j++)
    {counter=0;
    cin>>t>>s>>p;
    for(i=1;i<=t;i++)
    {cin>>score[i];}
    for(i=0;i<=10;i++)
    {if((i-2)>=0)pleast[i]=i-2;
     else pleast[i]=0;
    }
    for(i=0;i<=10;i++)
    {if((i-1)>=0)pleastwsurp[i]=i-1;
     else pleastwsurp[i]=0;
    }

    for(i=1;i<=t;i++)
   {   if((score[i]-p-2*pleast[p])>=0)
       { if((score[i]-p-2*pleastwsurp[p])>=0)
         counter++;
         else if (s>0)
         {counter++;
          s--;
         }
       }
   }
   cout<<"Case #"<<j<<": "<<counter<<endl;
  }
  }

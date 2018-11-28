/*
Task:A
Lang:C++
*/

#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <string>
#include <queue>
#include <stack>

#define SP system("pause")

using namespace std;

ifstream ff;
ofstream of;

int Sq[]={0,1,4,9,16,25,36,49,64,81};
int num[10];
int t,k;
 int gen(int ch , int base)
{//SP;
     string v;
     //cout<<ch<<" ";
      while(ch!=0)
   {
        v+=char(ch%base+'0');
        ch/=base;
   }
  // cout<<v<<" ";
   for(int i=0; i<v.size(); i++)
   {
       ch+=Sq[v[i]-'0'];    
   }
  // cout<<ch<<endl;SP;
   return ch;
}
int rek(int base,int n,int ch)
{
   // cout<<base<<" "<<n<<" "<<ch<<endl;SP;
    if (n==0)return 1;
    int z=ch;
   int j=0;
   while(j<12)
   {
   z=gen(z,base);
   j++;
   if(z==1)break;
   }
   //cout<<c<<endl;
  // SP;
  
  if(z==1)return rek(num[n-1],n-1,ch);
  return 0;
     
}
int main()
{
    ff.open("A-small.in");
    of.open("A-small2.out");
    
    ff>>t;
    string a;
    getline(ff,a);
    for(int z=0; z<t; z++)
    {
            getline(ff,a);
            stringstream str;
            str<<a;
            k=1;
            while(str)
            {
                    str>>num[k];k++; 
                    
            }
            k-=2;
            //cout<<num[k-1]<<endl;SP;
            int otg=1;
            while(1)
            {
                    otg++;
                    
             if(rek(num[k],k,otg)==1)break;
           //  cout<<otg<<endl;SP;
            }
            of<<"Case #"<<z+1<<": "<<otg<<endl;
            
    }
   // SP;
    return 0;
}

#include<iostream>
#include<vector>
#include<string>
#include<cstring>
#include<map>
#include<fstream>
#include<sstream>
#include<algorithm>
using namespace std;

int main()
{
   ifstream fin;
   ofstream fout;
   fin.open("input.in");
   fout.open("outputlarge.out");
   int kase;
   fin>>kase;
   for(int ee=0;ee<kase;ee++)
   {
   	 long int p,k,na;
   	vector<long int>arr;
   	fin>>p;fin>>k;fin>>na;
   	for(int i=0;i<na;i++)
   	{
           int x;
           fin>>x;
           arr.push_back(x);
        }
        
        if(p*k<na)
        {
           fout<<"Case #"<<ee+1<<": Impossible"<<endl;
           continue;
        }
        else
        {
            sort(arr.begin(),arr.end());
            reverse(arr.begin(),arr.end());
            long int var=1;
      
            unsigned long int result=0;
            
            for(int i=0;i<arr.size();i+=k)
            {
                for(int j=i;j<i+k;j++)
                {
                  if(j>=arr.size()) break;
                  result+=arr[j]*var;
             
                }
                ++var;
            }
            fout<<"Case #"<<ee+1<<": "<<result<<endl;
           
      	}
    }
}
                
        

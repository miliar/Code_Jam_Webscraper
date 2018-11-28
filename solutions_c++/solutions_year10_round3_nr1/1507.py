#include<fstream>
#include<iostream>
using namespace std;
int main()
{
    int n,t,a[1000],b[1000],i,j,l=0,count;
    ifstream fin("vj.in");
	ofstream fout("output.out");
	fin>>t;
	while(t--)
	{
              count=0;
              fin>>n;
              for(i=0;i<n;i++)
                    fin>>a[i]>>b[i];
              for(i=0;i<n;i++)
              {
                              for(j=0;j<n;j++)
                              {               
                                              if(i!=j)
                                              {
                                                      if(a[i]<=a[j])
                                                      {
                                                                   if(b[i]>b[j])
                                                                               count++;
                                                                   else if(b[i]=b[j])
                                                                   {
                                                                        if(a[j]<a[i])
                                                                                     count++;
                                                                   }
                                                      }          
                                              }
                              }
              }
              fout<<"Case #"<<++l<<": "<<count<<endl;
              }
 fin.close();
 fout.close();
 return 0;
}
                                                      

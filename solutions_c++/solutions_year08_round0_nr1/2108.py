#include<iostream>
#include<vector>
#include<string>
#include<fstream>
#include<conio.h>
using namespace std;
int main()
{
	ifstream f("A-large.in");
	ofstream g("vijay.txt");
	string s;
    getline(f,s);
	int k,n,sw,count,i,j;
	n=atoi(s.c_str());
	for(int t=0;t<n;t++)
	{
                    vector<string> a(0),b(0);
                    getline(f,s);
                    int z=atoi(s.c_str());
	                for(i=0;i< z;i++)
	                {
		                       getline(f,s);	
		                       a.push_back(s);
                               }
	             getline(f,s);
	             k=atoi(s.c_str());
	             count=0;
	             vector<int> x(a.size());
	             for(int m=0;m<a.size();m++)
		                 x[m]=0;
                 sw=0;
	             for(i=0;i<k;i++)
	             {
		                         getline(f,s);
                                 b.push_back(s);		
		                         j=0;
		                         while(a[j]!=b[i])
			                     j++;
		                         if(++x[j]==1)
			                               count++;
                                 if(count==a.size())
		                         {
			                      for(int m=0;m<a.size();m++)
				                          x[m]=0;
			                           sw++;
                                  x[j]++;			
			                      count=1;
		                          }
                  }
	              g<<"Case #"<<t+1<<": "<<sw<<endl;	
               }
                  f.close();
	              g.close();	
	              return 0;
}	              

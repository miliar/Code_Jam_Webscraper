#include<iostream>
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;

int main()
{
    
     freopen("A-small-attempt2.in","r",stdin);
     freopen("output.txt","w",stdout);
    
     string  s="abcdefghijklmnopqrstuvwxyz";	 
	 string s2="yhesocvxduiglbkrztnwjpfmaq"; 
	 
	 string st,s3="a";
     
     int n;
     
     cin>>n;
     
     for(int j=0;j<=n;j++)
     {
		 getline (cin,st);
		  int 	i=0,len=st.length();
			while(i<len)
			{
				if(st[i]!=' ')
				{
				    s3[0]=s2[s.find(st[i])];
					st.replace(i,1,s3);
				}
				i++;
				
			}
			if(j!=0)
			{
		   		cout<<"Case #"<<j<<": "<<st<<"\n";
		     }
	 }
     
  return 0;
} 

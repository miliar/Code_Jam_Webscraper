#include<iostream>
#include<string>
#include<fstream>
using namespace std;
string st;
long long f[600][600];
long long ans;
int t;
//int f[
string s1=("welcome to code jam");
int main()
 {
   
   ifstream fin;
    ofstream fout;
  // cout<<s1;
  fin.open("c.in");
  fout.open("c.out");
  fin>>t;
      getline(fin,st);	
   for (int test = 1 ; test<= t; test++)
    {
	   getline(fin,st);	
	 
	   memset(f, 0 , sizeof (f));
	   for (int i = 0; i <= st.size()-1 ; i++ )
	    {
		   if (st[i]=='w') {f[i][0]=1;}	 	
	    }
	   for (int i = 0 ; i <= st.size()-1 ; i++)
	    {
		   	
		   	for (int j = 0; j <= s1.size()-1; j++)
			    {
				 	if (j==0) continue; 
				 	if (st[i]!=s1[j]) continue;
				 //	cout<<i<<" "<<j<<endl;
					 for (int k = 0 ; k <= i - 1 ; k++ )
					  {
					   	 
								  if (st[k]==s1[j-1])
								 f[i][j] +=f[k][j-1];
								 if (f[i][j]>1000000)
								 f[i][j]=f[i][j]%1000000;
								// cout<<"asdasd"<<endl;				   	 	  
  	 	              }
			 	 }	
   		}	
   		ans=0;
   	for (int i = 0 ; i <= st.size()-1; i++)	
     {
	  if (st[i]=='m')
	  {ans+=f[i][18];}		 
     }
     ans= ans% 10000;
     fout<<"Case #"<<test<<": ";
	 if (ans>=0 &&ans <10) fout<<"000"<<ans<<endl;
      if (ans>=10 &&ans <100) fout<<"00"<<ans<<endl;
       if (ans>=100 &&ans <1000) fout<<"0"<<ans<<endl;
        if (ans>=1000 &&ans <10000) fout<<ans<<endl;
	}
	  
 }

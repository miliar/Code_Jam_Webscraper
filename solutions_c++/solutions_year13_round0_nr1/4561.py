#include<iostream>
#include<cstdio>
#include<cmath>
#include<map>
#include<string>
#include<sstream>
using namespace std;
int main()
{
  map<string,int> M;
  int t;
  cin>>t;
  for(int i=0;i<t;i++)
    {
      char  a[4][4];
      for(int k=0;k<4;k++)
	{
	  for(int l=0;l<4;l++)
	    {
	      cin>>a[k][l];
	    }
	}
      // cout<<"___________________________________________________________________"<<endl;
      M["XXXT"]=0;
      M["XXTX"]=0;
      M["XTXX"]=0;
      M["TXXX"]=0;
      M["XXXX"]=0;
      M["OOOO"]=0;
      M["OOOT"]=0;
      M["OOTO"]=0;
      M["OTOO"]=0;
      M["TOOO"]=0;
      int z=0;
      for(int k=0;k<4;k++)
	{
	  stringstream ss;string s;
	  for(int l=0;l<4;l++)
	    {
	      if(a[k][l]=='.')
		z=1;
	      ss<<a[k][l];
	    }
	  ss>>s;
	  M[s]=1;
	}
      for(int k=0;k<4;k++)
	{
	  stringstream ss;string s;
	  for(int l=0;l<4;l++)
	    {
	      if(a[l][k]=='.')
		z=1;
	      ss<<a[l][k];
	    }
	  ss>>s;
	  M[s]=1;
	}
      stringstream ss1,ss2;string s1,s2;
      ss1<<a[0][0];
      ss1<<a[1][1];
      ss1<<a[2][2];
      ss1<<a[3][3];
      ss1>>s1;
      // cout<<s1<<endl;
      M[s1]=1;

      ss2<<a[3][0];
      ss2<<a[2][1];
      ss2<<a[1][2];
      ss2<<a[0][3];
      ss2>>s2;
      // cout<<s2<<endl;
      M[s2]=1;
      
      int success=0;
      if(M["XXXT"]!=0||M["XXTX"]!=0||M["XTXX"]!=0||M["TXXX"]!=0||M["XXXX"]!=0)
        {
	  success=1;
	  cout<<"Case #"<<i+1<<":"<<" X won\n";
	}
      if(success)
	continue;
      
      if(M["OOOT"]!=0||M["OOTO"]!=0||M["OTOO"]!=0||M["TOOO"]!=0||M["OOOO"]!=0)
        {
	  success=1;
	  cout<<"Case #"<<i+1<<":"<<" O won\n";
	}
      if(success)
	continue;
      if(z)
	cout<<"Case #"<<i+1<<": Game has not completed\n";
      else
	cout<<"Case #"<<i+1<<": Draw\n";
    }
  
}

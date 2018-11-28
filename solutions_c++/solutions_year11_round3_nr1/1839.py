#include<iostream>
#include<string>
#include<vector>
using namespace std;

main()
{
  int tt;
  cin>>tt;
  for(int t=1;t<=tt;t++)
  {
    int r,c;
    string str;
    vector<string> in;
    cin>>r>>c;
    for(int i=0;i<r;i++)
    {
 	cin>>str;
	in.push_back(str);
    }
    bool ok=true;
    for(int i=0;i<r;i++)
	for(int j=0;j<c;j++)
	   if(in[i][j]=='#')
	   {
		if(i==r-1 || j==c-1)ok=false;
		else if(in[i][j+1]=='#' && in[i+1][j]=='#' && in[i+1][j+1]=='#')
		{ in[i][j]=in[i+1][j+1]='/';in[i+1][j]=in[i][j+1]='\\';}
		else
			ok=false;
	   }	
     cout<<"Case #"<<t<<":"<<endl;
     if(ok==false)
	cout<<"Impossible"<<endl;
     else
	for(int i=0;i<r;i++)
	   cout<<in[i]<<endl;	
  }
}


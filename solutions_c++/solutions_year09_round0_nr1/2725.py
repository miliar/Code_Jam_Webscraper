#include<iostream>
#include<string>
using namespace std;

int main()
{

	int N,x,y,resultado,encuentra;
	char word[5000][16],tmp[2]=" ";
	string compara;
	string cads[15];

	cin>>x>>y>>N;

	for(int i=0;i<y;i++)
	{
	   cin>>word[i];
	}
    
	for(int j=0;j<N;j++)
	{
		for(int k=0;k<x;k++)
		{
		   if((tmp[0]=cin.get())=='\n')
			   tmp[0]=cin.get();

		   if(tmp[0] == '(')
		   {
			   getline(cin,cads[k],')');
		   }
		   else
		   {
			  cads[k].assign(tmp);
		   }
		}

		resultado=0;

		for(int l=0;l<y;l++)
		{
			encuentra=0;
		   for(int m=0;m<x;m++)
		   {
			   if(cads[m].find(word[l][m])!=string::npos)
				   encuentra++;
			   else
				   m=x;
		   }
		   if(encuentra==x)
			   resultado++;
		}

		cout<<"Case #"<<j+1<<": "<<resultado<<endl;
	}




	return 0;
}
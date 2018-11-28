// final.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include<iostream>
#include<string>
#include<fstream>
#include<sstream>
#include<cmath>
using namespace std;
long long arr[100000][2];
int compute(long long n)
{
	int count=0;
	for(int y=0;y<n-2;y++)
		for(int q=y+1;q<n-1;q++)
			for(int g=q+1;g<n;g++)
			{
			

					if((arr[y][0]+arr[g][0]+arr[q][0])%3==0&&(arr[y][1]+arr[g][1]+arr[q][1])%3==0)
						count++;
			}
				
			

return count;
}
int main()
{
	ifstream cin("1.txt");
ofstream cout("2.txt");
 
	int lim;
	cin>>lim; 
     long long  n,A,B,C,D,x0,y0,M,X,Y;
	
int w=0;
	while(w<lim)
	{
		cin>>n>>A>>B>>C>>D>>x0>>y0>>M;
X = x0; Y = y0;
arr[0][0]=X;
arr[0][1]=Y;
for(int i=1;i<n;i++)
{

  X = (A * X + B)% M;
  Y = (C * Y + D) %M;
  arr[i][0]=X;
  arr[i][1]=Y;
}

		w++;
		cout<<"Case #"<<w<<": ";
		cout<<compute(n)<<endl;
		
	}
	return 0;
}
	






#include<iostream>
#include<algorithm>
#include<fstream>
#include<vector>
#include<conio.h>
using namespace std;
void getTrip(int n,int & S,int P,int & total)
{
	int a=n/3;
	int b=(n-a)/2;
	int c=n-a-b;
	if(c<P)
	{
		if(S!=0)
		{
			if(c-a==0 && c+1<=10 && a-1>=0 && c+1>=P)
			{
				total++;
				S--;
				c++;
				b--;
			}
			else if(a!=b && c-a==1  && c+1<=10 && a-1>=0 && c+1>=P)
			{
				total++;
				S--;
				c++;
				b--;
			}
		}
	}
	else
	{
		total++;
	}
}
void main()
{
	ifstream in("B-small-attempt4.in");
	ofstream out("out.txt");
	int T;
	in>>T;
	for(int i=0; i<T ; i++)
	{
		int N,S,P;
		in>>N>>S>>P;
		int total=0;
		for(int j=0; j<N; j++)
		{
			int a;
			in>>a;
			getTrip(a,S,P,total);
		}
		out<<"Case #"<<i+1<<": "<<total;
		if(i+1<T)
		{
			out<<endl;
		}
	}
}
#include<iostream>
#include <FSTREAM>
#include <MATH.H>
using namespace std;
int len(int num)
{
	int n=0;
	while(num)
	{
		num/=10;
		n++;
	}
	return n;
}
int main()
{
	int T;
	int a,b;
	int i,j,k,rj;
	int ml,tj,ttj,tk,pw;
	int totnum;
	ifstream cin("C-small-attempt1.in",ios::in);
	ofstream cout("2.txt",ios::out);
	cin>>T;
	for(i=0;i<T;i++)
	{
		cin>>a>>b;
		totnum=0;
		ml=len(a);
		for(j=a;j<=b;j++)
		{
			//ttj=j;	
			for(k=1;k<ml;k++)
			{
				tj=j;
				pw=pow(10,k);
				tk=tj%pw;
				tj/=pw;
				tj=tk*pow(10,ml-k)+tj;
				if (tj>j&&tj<=b)
					totnum++;
			}
		}
		cout<<"Case #"<<i+1<<": "<<totnum<<endl;
	}
}
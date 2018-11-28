#include<iostream>
#include<time.h>
#include <stdlib.h>
#include<cmath>
using namespace std;

void findmax(int *t, int N, int S, int p);

int main(void)
{
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	int	T,N,S,p,i,j,t[100];
	cin>>T;
	for (j=1;j<=T;j++)
	{
		cin>>N;
		cin>>S;
		cin>>p;
		for (i=0;i<N;i++)
			cin>>t[i];
		cout<<"Case #"<<j<<": ";
		findmax(&t[0], N, S, p);
		cout<<endl;
	}
	return 0;
}


void findmax(int *t, int N, int S, int p)
{
	int i,j;
	int count1=0,count2=0,sum=0;
	for (i=0;i<N; i++)
	{
		if (t[i]>3*(p-1))
			count1 +=1;
		if ( (t[i]<=3*(p-1)) && (t[i]>=( (3*(p-1)-1 > 0) ? 3*(p-1)-1 : 1)) )
			count2 +=1;
	}
	if (S<count2)
		count2=S;
	sum=count1+count2;
	cout<<sum;
}

#include <iostream>
#include <string>
#include <string.h>
#include <cstring>
#include <algorithm>
#include <math.h>
#include <set>
#include <map>
#include <vector>
#include <bitset>
#include <stdio.h>
#include <queue>



using namespace std;
int T,test,k,P,s,N,n=1,m[11][1050],i,j;
int main()
{
	

	freopen("B-small-attempt1.in","r",stdin);
	freopen("output.txt","w",stdout);

	cin>>T;
	for(test=1;test<=T;test++)
	{
		n=1;
		s=0;
		cin>>P;
		for(i=0;i<11;i++)
			for(j=0;j<1050;j++)
				m[i][j]=-1;
		for(i=0;i<P;i++)
			n*=2;
		N=n;
		for(i=0;i<n;i++)
			cin>>m[0][i];
		for(i=0;i<P;i++)
		{
			N/=2;
			for(j=0;j<N;j++)
				cin>>k;
		}
		j=0;
		while(n!=1)
		{
			n/=2;
			j++;
			for(i=0;i<n;i++)
			{
				m[j][i]=min(m[j-1][i*2],m[j-1][i*2+1]);
				if(m[j][i]==0||m[j][i]<j)
					s++;
			}
		}
		cout<<"Case #"<<test<<": "<<s<<"\n";

	}
	return 0;
}
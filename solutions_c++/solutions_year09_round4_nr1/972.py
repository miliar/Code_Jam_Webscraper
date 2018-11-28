#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <queue>
#include <map>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <sstream>

using namespace std;

int mat[100][100];
int ns[100];

int mswap(int a,int b)
{
	int t,r=0;
	for (int i=b;i>a;i--)
	{
		swap(ns[i],ns[i-1]);
		r++;
	}
	return r;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin>>T;
	for (int t=1;t<=T;t++)
	{
		memset(mat,0,sizeof(mat));
		memset(ns,0,sizeof(ns));
		int N;
		cin>>N;
		char c;
		for (int i=0;i<N;i++)
		{
			for (int j=0;j<N;j++)
			{
				cin>>c;
				mat[i][j]=(c=='1');
				if (mat[i][j])
					ns[i]=j+1;
			}
		}
		int res=0;
		for (int i=0;i<N;i++)
		{
			if (ns[i]>i+1)
			{
				for (int j=i+1;j<N;j++)
				{
					if (ns[j]<=i+1)
					{
						res+=mswap(i,j);
						break;
					}
				}
			}
		}
		cout<<"Case #"<<t<<": "<<res<<endl;
	}
	return 0;
}
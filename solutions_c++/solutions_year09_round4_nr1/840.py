#include <iostream>
#include <string>
#include <queue>
#include <map>
#include <cmath>
#include <memory.h>
#include <algorithm>
using namespace std;
char c[50][50];
int cnt[50];
void move(int *a,int j,int i)
{
	int t=a[j];
	for (int l=j;l>i;l--)
		a[l]=a[l-1];
	a[i]=t;
}
int main()
{
	int t;
	cin>>t;
	for (int k=1;k<=t;k++)
	{
		memset(c,0,sizeof(c));
		memset(cnt,0,sizeof(cnt));
		int n;
		cin>>n;
		for (int i=0;i<n;i++)
			cin>>c[i];
		for (int i=0;i<n;i++)
			for (int j=n-1;j>=0;j--)
			{
				if (c[i][j]=='1')
				{
					cnt[i]=j;
					break;
				}
			}
		int sum=0;
		for (int i=0;i<n;i++)
		{
			for (int j=i;j<n;j++)
			{
				if (cnt[j]<=i)
				{
					move(cnt,j,i);
					sum+=j-i;
					break;
				}
			}
		}
		cout<<"Case #"<<k<<": "<<sum<<endl;		
	}

}
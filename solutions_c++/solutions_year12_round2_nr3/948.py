#include <iostream>
#include <string>
#include <set>
#include <algorithm>
#include <stdio.h>
#include <map>
using namespace std;
const int mx=1<<20;
int arr[3000000];
int vis[3000000];
int wei[22];
int j;
int main()
{
	//freopen("D:\\visual studio 2008\\google code jam\\C-small-attempt3.in", "r", stdin ) ;

	//freopen("D:\\visual studio 2008\\google code jam\\C-small-attempt3.out", "w", stdout ) ;
	int cases,list[22];int index;
	int suc;
	cin>>cases;
	int n;
	for(int k=1;k<=cases;++k)
	{
		suc=0;
		memset(vis,0,sizeof(vis));
		cin>>n;
		for(int i=1;i<=20;++i)
			cin>>list[i];
		printf("Case #%d:\n",k);
		for(int i=1;i<=mx;++i)
		{
			j=i;
			 index=20;
			while(j)
			{
				wei[index--]=j%2;
				j/=2;
			}
			int s=0;
			for(j=1;j<=20;++j)
			{
				if(wei[j])
				{
					wei[j]=0;
					s+=list[j];
				}
			}
			if(vis[s])
			{
				j=arr[s];
							 index=20;
				while(j)
				{
					wei[index--]=j%2;
					j/=2;
				}
				for( j=1;j<=20;++j)
				{
					if(wei[j])
					{
						wei[j]=0;
						cout<<list[j]<<" ";
					}
				}
				cout<<endl;
				 j=i;
				 index=20;
				while(j)
				{
					wei[index--]=j%2;
					j/=2;
				}
				for(int j=1;j<=20;++j)
				{
					if(wei[j])
					{
						wei[j]=0;
						cout<<list[j]<<" ";
					}
				}
				cout<<endl;
				suc=1;
				break;
			}
			else
			{
				vis[s]=1;
				arr[s]=i;
			}
		}
		if(!suc)
			printf("Impossible\n");
	}
	return 0;
}
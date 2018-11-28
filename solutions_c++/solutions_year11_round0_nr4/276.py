/*
ID: lansen1
PROG: packrec
LANG: C++
*/

//#include<iostream>
//#include<string>
//#include<fstream>
//#include<algorithm>
//#include<map>
//#include<string.h>
//using namespace std;
//
//int main()
//{
//	//freopen("packrec.out","w",stdout);
//	//freopen("packrec.in","r",stdin);
//
//	return 0;
//}

#include<iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<map>
#include<stdlib.h>
using namespace std;

#define MAX(a,b) (a>b?a:b)
#define MIN(a,b) (a<b?a:b)

const int size=1005,inf=1<<26;
int arr[size];

int main()
{
	int t,e=1;

	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);

	scanf("%d",&t);

	while(t--)
	{
		int n;
		int i,j;
		double ans=0;

		scanf("%d",&n);
		for(i=1;i<=n;i++)
		{
			scanf("%d",&arr[i]);
			if(arr[i]!=i)
				ans++;
		}

		printf("Case #%d: %lf\n",e++,ans);
	}
	return 0;
}
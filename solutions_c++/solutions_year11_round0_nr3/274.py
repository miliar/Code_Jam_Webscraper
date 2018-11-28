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

	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);

	scanf("%d",&t);

	while(t--)
	{
		int n;
		int i,j;
		int flag=0,sum=0,small=inf;

		scanf("%d",&n);
		for(i=1;i<=n;i++)
		{
			scanf("%d",&arr[i]);
			sum+=arr[i];
			flag^=arr[i];
			small=MIN(arr[i],small);
		}

		printf("Case #%d: ",e++);
		if(flag!=0)
			printf("NO\n");
		else printf("%d\n",sum-small);
	}
	return 0;
}

/*
3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1
*/
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

const int size=20005;

struct robot_struct
{
	int time;
	int at;

	void init()
	{
		this->at=1;
		this->time=0;
	}
};
robot_struct blue,orange;

int main()
{
	int t,e=1;

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	scanf("%d",&t);

	while(t--)
	{
		int n,i;
		int at,time=0,last=0,need;
		char order[5];
		int flag=-1;

		blue.init();
		orange.init();
		scanf("%d",&n);

		for(i=0;i<n;i++)
		{
			scanf("%s%d",order,&at);

			if(order[0]=='B')
			{
				if(flag!=1)
				{
					if(last>=abs(at-blue.at))
						need=0;
					else need=abs(at-blue.at)-last;
					last=0;
				}
				else need=abs(at-blue.at);

				flag=1;
				time+=need+1;
				last+=need+1;
				blue.at=at;
			}
			else
			{
				if(flag!=0)
				{
					if(last>=abs(at-orange.at))
						need=0;
					else need=abs(at-orange.at)-last;
					last=0;
				}
				else need=abs(at-orange.at);

				flag=0;
				time+=need+1;
				last+=need+1;
				orange.at=at;
			}
		}

		printf("Case #%d: %d\n",e++,time);
	}
	return 0;
}

/*
3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1
*/
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

const int size=205;

char combine[40][5];
char clear[40][5];
char in[205],que[205];
int combine_num,clear_num,in_num,tail;

int main()
{
	int t,e=1;

	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	scanf("%d",&t);

	while(t--)
	{
		int i,j,k;
		bool flag;

		scanf("%d",&combine_num);
		for(i=0;i<combine_num;i++)
			scanf("%s",combine[i]);
		scanf("%d",&clear_num);
		for(i=0;i<clear_num;i++)
			scanf("%s",clear[i]);
		scanf("%d%s",&in_num,in);

		tail=0;
		for(i=0;i<in_num;i++)
		{
			que[tail++]=in[i];

			if(tail>1)
			{
				for(j=0;j<combine_num;j++)
					if((que[tail-1]==combine[j][0]&&que[tail-2]==combine[j][1])||((que[tail-1]==combine[j][1]&&que[tail-2]==combine[j][0])))
					{
						tail-=2;
						que[tail++]=combine[j][2];
						break;
					}
				flag=true;
				for(j=0;j<clear_num&&flag;j++)
					if(que[tail-1]==clear[j][0])
					{
						for(k=0;k<=tail-2;k++)
							if(que[k]==clear[j][1])
							{
								tail=0;
								flag=false;
								break;
							}
					}
					else if(que[tail-1]==clear[j][1])
					{
						for(k=0;k<=tail-2;k++)
							if(que[k]==clear[j][0])
							{
								tail=0;
								flag=false;
								break;
							}
					}
			}
		}

		/*if(e==50)
		{
			printf("combine num = %d\n",combine_num);
			for(i=0;i<combine_num;i++)
				puts(combine[i]);
			printf("clear num = %d\n",clear_num);
			for(i=0;i<clear_num;i++)
				puts(clear[i]);
			puts(in);
		}*/

		printf("Case #%d: [",e++);
		for(i=0;i<tail;i++)
		{
			printf("%c",que[i]);
			if(i!=tail-1)
				printf(", ");
		}
		printf("]\n");
	}
	return 0;
}

/*
3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1
*/
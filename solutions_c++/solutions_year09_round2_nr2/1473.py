#include <iostream>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
using namespace std;

#define SIZE 1000

char *strev(char *s)
{
	int i,len=strlen(s);
	for(i=0;i<=(len-1)/2;i++)
		s[len-1-i] = (s[i] + s[len-1-i]) - (s[i]=s[len-1-i]);
	return s;
}

bool comp(int a, int b)
{
	return a>b;
}

int N;

int main()
{
	freopen("B-small-attempt2.in","r",stdin);
	//freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int tcase,t,len,nn;
	char num[20],temp[20];
	scanf("%d",&tcase);
	for(t=1;t<=tcase;t++)
	{

		memset(num,0,sizeof(num));
		memset(temp,0,sizeof(temp));
		scanf("%d",&N);
		nn=N;
		len = 0;
		while(nn)
		{
			nn/=10;
			len++;
		}
		printf("Case #%d: ",t);
		/*
		if(N%10 ==N){
			printf("%d\n",N);
			continue;
		}
		*/
		sprintf(num,"%d",N);
		sprintf(temp,"%d",N);
		sort(temp,temp+len);
		do
		{
			if(strcmp(num,temp)==0)
			{
				next_permutation(temp,temp+len);
				if(strcmp(temp,num)>0)
					printf("%s\n",temp);
				else
				{
					sort(temp,temp+len);
					do
					{
						if(temp[0]!='0')
							break;
					}while(next_permutation(temp,temp+len));

					for(int i=0;i<len;i++)
					{
						printf("%c",temp[i]);
						if(i==0)
							printf("0");
					}
					printf("\n");
					break;
				}
			}
		}while(next_permutation(temp,temp+len));
		
	}
	return 0;
}
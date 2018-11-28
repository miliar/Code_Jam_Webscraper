#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>

#include <set>
#include <map>
#include <vector>
#include <string>

#include <algorithm>

using namespace std;

int len,d;
char s[5500][20];
char S[5500];

void run()
{
	scanf("%s",S);
	int Len = strlen(S);
	int res = 0;
	for(int word=0; word<d; word++)
	{
		int k = 0;
		bool good = true;
		for(int i=0; i<Len; i++)
		{
			if(k==len)
			{
				good = false;
				break;
			}
			if(S[i]=='(')
			{
				bool find = false;
				int j;
				for(j=i+1; S[j]!=')'; j++)
				{
					if(S[j]==s[word][k])
					{
						find = true;
					}
				}
				if(!find)
				{
					good = false;
					break;
				}
				i=j;
			}
			else if(s[word][k]!=S[i])
			{
				good = false;
				break;
			}
			k++;
		}
		if(good && k==len)
		{
			res++;
		}
	}
	printf("%d",res);
}


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);	
	int testCount;
	scanf("%d %d",&len,&d);
	scanf("%d\n",&testCount);
	for(int i=0; i<d; i++)
	{
		scanf("%s",s[i]);
	}
	for(int testNumber=1; testNumber<=testCount; testNumber++)
	{
		printf("Case #%d: ",testNumber);
		run();
		printf("\n");
	}
	return 0;
}
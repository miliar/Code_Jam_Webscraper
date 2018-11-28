#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;



long test,cases,M,N;
char graph[200][200];
char temp[200];
char temp1[200];


void SetInputFile()
{ char filename[32], infile[32], outfile[32]; scanf("%s", filename);
  strcpy(infile, filename); strcpy(outfile, filename); strcat(infile, ".in"); strcat(outfile, ".out");
  freopen(infile, "r", stdin); freopen(outfile, "w", stdout);
}

bool exists(char *str)
{
	for(long i=0;i<N;i++)
		if(strcmp(graph[i],str)==0)
			return true;

	return false;
}

char* Omitthelast(char *str)
{
	long len = strlen(str);
	long i;
	for(i=len-1;i>=0;i--)
	{
		if(str[i]=='/')
			break;
	}
	long j;
	for(j=0;j<i;j++)
	{
		temp1[j] = str[j];			
	}
	temp1[j] = '\0';

	return temp1;
}

int main()
{
	SetInputFile();
	
	long count;
	scanf("%ld",&test);
	cases=1;
	while(test--)
	{
		memset(graph,0,sizeof(graph));

		scanf("%ld%ld",&N,&M);

		for(long i=0;i<N;i++)
		{
			scanf("%s",graph[i]);			
		}

		count=0;
		for(long i=0;i<M;i++)
		{
			scanf("%s",temp);
			
			if(!exists(temp))
			{
				strcpy(graph[N],temp);				
				N++;
				count++;

				while(1)
				{
					if(strlen(temp)>0 && !exists(temp))
					{
						strcpy(graph[N],temp);				
						N++;
						count++;
					}

					char * test = Omitthelast(temp);
					strcpy(temp,test);
					long tempLen = strlen(temp);
					if(tempLen==0)
						break;
					else if(tempLen>0 && exists(temp))
					{
						break;
					}
					else if(tempLen>0)
					{
						strcpy(graph[N],temp);
						N++;
						count++;
						test = Omitthelast(temp);
						strcpy(temp,test);
					}
				}				
			}

		}

		printf("Case #%ld: %ld\n",cases++,count);

	}

	
	return 0;
}
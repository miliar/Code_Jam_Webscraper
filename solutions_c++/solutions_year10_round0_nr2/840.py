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
const int maxd = 50+5;
const int maxn = 1000+5;
char mine[maxd];
char mins[maxd];
char inevents[maxn][maxd];
int N;
char r[maxd];
void sub(char* s1,char* s2,char* s3)
{
	char tmp[maxd];
	int len = strlen(s1) - strlen(s2);
	strcpy(s3,s1);
	for(int i=0;i<strlen(s2);i++)
	{
		if(s3[i+len] >= s2[i])
		{
			s3[i+len] -= s2[i]-'0';
		}
		else
		{
			for(int j = i+len -1;j>=0;j--)
			{
				if(s3[j] > '0')
				{
					s3[j]--;
					for(int k=j+1;k<=i+len;k++)
					{
						if(k == i+len)
							s3[k] += 10;
						else
							s3[k] = '9';
					}
					break;
				}
			}
			s3[i+len] -= s2[i]-'0';
		}
	}
	strcpy(tmp,s3);
	int index=-1;
	for(int i=0;i<strlen(tmp);i++)if(tmp[i]>'0'){index = i;break;}
	if(index == -1)
		strcpy(s3,"0");
	else
		strcpy(s3,tmp+index);
}
int compare(char* s1,char* s2)
{
	if(strlen(s1) > strlen(s2))
		return 1;
	if(strlen(s1) < strlen(s2))
		return -1;
	return strcmp(s1,s2);
}

inline void maxmul(char* s1,char* s2,char* s3)
{
	char tmp[maxd];
	char ss1[maxd];
	char ss2[maxn];
	strcpy(ss1,s1);
	strcpy(ss2,s2);
	while(1)
	{
	if(compare(ss1,ss2)>0)
	{
		sub(ss1,ss2,tmp);
		strcpy(ss1,tmp);
	}
	else if(compare(ss2,ss1)>0)
	{
		sub(ss2,ss1,tmp);
		strcpy(ss2,tmp);
	}
	else if(compare(ss2,ss1)==0)
		break;
	}
	strcpy(s3,ss1);
	
		
}


inline void remainer(char* s1,char* s2,char* s3)
{
	char tmp[maxd];
	char tmpsub[maxd];
	char tmps1[maxd];
	strcpy(tmps1,s1);
	int pos =0;
	
	while(pos < strlen(tmps1))
	{
		if(compare(tmps1+pos,s2) < 0)
			break;
		memset(tmp,0,sizeof tmp);
		strncpy(tmp,tmps1+pos,strlen(s2)+1);
		pos += strlen(tmp);
		while(compare(tmp,s2)>=0)
		{
			sub(tmp,s2,tmpsub);
			strcpy(tmp,tmpsub);
		}
		if(compare(tmp,"0")>0)
		{
			memcpy(tmps1+pos-strlen(tmp),tmp,strlen(tmp));
			pos -=strlen(tmp);
		}
		
		
	}
	if(pos == strlen(tmps1))
		strcpy(s3,"0");
	else
		strcpy(s3,tmps1+pos);
		
}


void init()
{
	
	memset(mins,'9',sizeof mins);
	memset(mine,'9',sizeof mine);
	
	for(int i=0;i<N;i++)
	{
		if(compare(mine,inevents[i]) > 0)
			strcpy(mine,inevents[i]);
	}
	
}
int solve()
{
	char tmp[maxd];
	char tmpm[maxd];
	int count = 0;
	for(int i=0;i<N;i++)
	{
		for(int j=0;j<N;j++)
		{
			if(i!=j && compare(inevents[i],inevents[j]) > 0)
			{
				sub(inevents[i],inevents[j],tmp);
				count++;
				if(count == 1)
					strcpy(mins,tmp);
				else
				{
					if(compare(mins,"1")>0)
					{
					maxmul(mins,tmp,tmpm);
					strcpy(mins,tmpm);
					
					}
				}
			}
		}
	}
	strcpy(tmp,mine);
/*	while(compare(mine,mins)>0)
	{
		sub(mine,mins,tmp);
		strcpy(mine,tmp);
	}*/
	if(compare(mine,mins)>0)
	{
		remainer(mine,mins,tmp);
	}
	if(compare(tmp,"0") == 0)
		strcpy(r,"0");
	else
		sub(mins,tmp,r);
	
}

int main()
{
//	freopen("b-test.in","r",stdin);//freopen("b-test.out","w",stdout);
	freopen("b-small-attempt6.in","r",stdin);freopen("b-small.out","w",stdout);
//	freopen("b-large.in","r",stdin);freopen("b-large.out","w",stdout);
	int testcase;
	scanf("%d",&testcase);
	
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		scanf("%d",&N);
		for(int i=0;i<N;i++) scanf("%s",inevents[i]);
		init();
		solve();
	
		printf("Case #%d: %s\n",caseId,r);
		cerr<<caseId<<"/"<<testcase<<endl;
	}
	return 0;
}
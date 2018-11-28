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
int bark[513][513];
int cut[513][513];
int m,n;
int k;
int num[513];

using namespace std;
void display(){
char CC;
printf("\n");
	for (int i=0;i<m;i++)
	{
		for (int j=0;j<n;j++)
		{
			if (cut[i][j])
			{
				CC='.';
			}else if (bark[i][j])
			{
				CC='*';
			}else CC= '#';
			printf("%c",CC);
		}
		printf("\n");
	}
}
void Cut(int i, int j,int Size)
{
	int size=1;
	bool flag;
	flag=false;
	while (!flag)
	{
		size++;
		if (i+size>m||j+size>n)
		{
			break;
		}
		for (int l=0;l<size;l++)
		{
			if (bark[i+size-1][j+l]==bark[i+size-2][j+l]||cut[i+size-1][j+l]==1)
			{
				flag=1;break;
			}
		}
		for (int l=0;l<size;l++)
		{
			if (bark[i+l][j+size-1]==bark[i+l][j+size-2]||cut[i+l][j+size-1]==1)
			{
				flag=1;break;
			}
		}
	}
	size--;
	if (size<Size)
	{
		return ;
	}
	for (int k=i;k<i+Size;k++)
	{
		for (int l=j;l<j+Size;l++)
		{
			cut[k][l]=1;
		}
	}
	num[size]++;
}

void solve(){
	memset(cut,0,sizeof(cut));
	memset(num,0,sizeof(num));
	for (int size=min(n,m);size>0;size--)
	{
	for (int i=0;i<m;i++)
	{
		for (int j=0;j<n;j++)
		{
			if (cut[i][j]==0)
			{
				Cut(i,j,size);
			}
		}
	}
	}
	k=0;
	for (int i=min(m,n);i>0;i--)
	{
		if (num[i]!=0)
		{
			k++;
		}
	}
	printf("%d\n",k);
	for (int i=min(m,4*n);i>0;i--)
	{
		if (num[i]!=0)
		{
			printf("%d %d\n",i,num[i]);
		}
	}
}
int main()
{
//	freopen("C.in","r",stdin);
	freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
//	freopen("C-small-attempt1.in","r",stdin);freopen("C-small-attempt1.out","w",stdout);
//	freopen("C-small-attempt2.in","r",stdin);freopen("C-small-attempt2.out","w",stdout);
//	freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);
	int testcase;
	scanf("%d",&testcase);
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		printf("Case #%d: ",caseId);
		scanf("%d%d",&m,&n);
		char c;
		for (int i=0;i<m;i++)
		{
			for (int j=0;j<n/4;j++)
			{
				do{
				scanf("%c",&c);
				} while(c=='\n'||c==' ');
				if (c>='A'&&c<='F')
				{
					c='0'+10+c-'A';
				}
				if (c&8)
				{
					bark[i][4*j+0]=1;
				}else{
					bark[i][4*j+0]=0;
				}
				if (c&4)
				{
					bark[i][4*j+1]=1;
				}else{
					bark[i][4*j+1]=0;
				}
				if (c&2)
				{
					bark[i][4*j+2]=1;
				}else{
					bark[i][4*j+2]=0;
				}
				if (c&1)
				{
					bark[i][4*j+3]=1;
				}else{
					bark[i][4*j+3]=0;
				}
			}
		}
		solve();		
		fflush(stdout);
	}
	return 0;
}

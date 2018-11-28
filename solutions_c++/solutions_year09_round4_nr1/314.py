#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <string.h>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

int T,N;
char mmap[8][9];

int right[8];

map<int,int> mymap;

int q[50000][8];
int head,h,t;

int hash(int a[8])
{
	int i,ans = 0;
	for(i = 0;i < N;i++)
		ans = ans*10 + a[i];
	return ans;
}

bool judge(int a[8])
{
	int i;
	for(i = 0;i < N;i++)
	{
		if(right[a[i]] > i)
			return false;
	}
	return true;
}

int main()
{
	int i,j,k,tt,m;
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A.txt","w",stdout);
	scanf("%d",&T);
	for(tt = 1;tt <= T;tt++)
	{
		scanf("%d",&N);
		for(i = 0;i < N;i++)
			scanf("%s",mmap[i]);
		//for(i = 0;i < N;i++)
		//	puts(mmap[i]);
		for(i = 0;i < N;i++)
		{
			for(j = N - 1;j >= 0;j--)
			{
				if(mmap[i][j] == '1')
				{
					right[i] = j;
					break;
				}
			}
			if(j == -1)
				right[i] = -1;
		}
		mymap.clear();
		for(i = 0;i < N;i++)
			q[0][i] = i;
		if(judge(q[0]))
		{
			printf("Case #%d: 0\n",tt);
			continue;
		}
		mymap[hash(q[0])] = 0;
		head = h = t = 0;
		int d = 0;
		while(t <= h)
		{
			d++;
			for(i = t;i <= h;i++)
			{
				int a[8];
				memcpy(a,q[i],sizeof(a));
				for(j = 0;j < N - 1;j++)
				{
					swap(a[j],a[j + 1]);
					m = hash(a);
					if(judge(a))
					{
						printf("Case #%d: %d\n",tt,d);
						goto la;
					}
					else if(mymap.find(m) == mymap.end())
					{
						head++;
						memcpy(q[head],a,sizeof(a));
						mymap[m] = head;
					}
					swap(a[j],a[j + 1]);
				}
			}
			t = h + 1;
			h = head;
		}
		//printf("%d\n",head);
		la:;
	}
	//system("PAUSE");
	return 0;
}
					
		
	

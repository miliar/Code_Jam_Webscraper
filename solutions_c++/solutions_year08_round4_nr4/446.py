#include <cstdio>
#include <cstring>
using namespace std;

#define M 11000

char data[M],temp[M];
int L,k;
int minans;
bool used[30];
int stk[30];


void read_data()
{
	scanf("%d",&k);
	scanf("%s",&data);
}

int calc()
{
	int res = 1,i;
	for (i=1;i<L;i++) if (temp[i] != temp[i - 1]) res++;
	return res;
}

void check_ans()
{
	int begin,T = L / k;
	int i,j;
	for (i=0;i<T;i++)
	{
		begin = i * k;
		for (j=0;j<k;j++) temp[begin + j] = data[begin + stk[j]];
	}
	int tempans = calc();
	if (tempans < minans) minans = tempans;
}

void dfs(int s)
{
	if (s == k) check_ans();
	else
	{
		int i;
		for (i=0;i<k;i++) if (!used[i])
		{
			used[i] = true;
			stk[s] = i;
			dfs(s + 1);
			used[i] = false;
		}
	}
}

void work_ans()
{
	L = strlen(data);
	minans = L;
	memset(used,false,sizeof(used));
	dfs(0);
}
int main()
{
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	int t,i;
	scanf("%d",&t);
	for (i=1;i<=t;i++)
	{
		read_data();
		work_ans();
		printf("Case #%d: %d\n",i,minans);
	}
	return 0;
}
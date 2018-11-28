#include <cstdio>
#include <cstdlib>
#include <memory.h>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <cmath>
using namespace std;
#define PI 3.14159265358979323846264338327950288
#define SIZE 100000

int lt[10];
char str[1000];
int d[1000],len;
int canbe[SIZE][11];
set<int> used;
void trans(int a,int b)
{
	len = 0;
	while(a >= b)
	{
		d[len++] = a % b;
		a /= b;
	}
	d[len++] = a;
}
void calcan(int b)
{
	int t,tmp;
	for(int i = 2; i < SIZE; i++)
	{
		used.clear();
		t = i;
		while(canbe[t][b] == -1)
		{
			if(used.find(t) != used.end())
			{
				tmp = 0;
				break;
			}
			used.insert(t);
			trans(t,b);
			t = 0;
			for(int j = 0; j < len; j++)
				t += d[j]*d[j];
			if(len == 1 && d[0] == 1)
			{
				tmp = 1;
				break;
			}
			if(canbe[t][b] != -1)
			{
				tmp = canbe[t][b];
				break;
			}
		}
		for(set<int>::iterator it = used.begin(); it != used.end(); it++)
			canbe[*it][b] = tmp;
	}
}
int main()
{
	int i,T,tmp,no = 0,ans,o;
	freopen("D:\\A-small-attempt2.in","r",stdin);
	freopen("D:\\A-small-attempt2.out","w",stdout);
	memset(canbe,-1,sizeof(canbe));
	for(i = 3; i <= 10; i++)
		if(i != 4) calcan(i);
	scanf("%d",&T);
	gets(str);
	while(T--)
	{
		no++;
		gets(str);
		char *cp = str;
		o = 0;
		while(*cp != NULL && sscanf(cp,"%d",&tmp) != EOF)
		{
			if(tmp != 2 && tmp != 4)
				lt[o++] = tmp;
			while(*cp != ' ' && *cp != NULL)
				cp++;
			while(*cp == ' ' && *cp != NULL)
				cp++;
		}
		bool over = false;
		ans = 2;
		while(!over)
		{
			over = true;
			for(i = 0; i < o; i++)
			{
				if(!canbe[ans][lt[i]])
				{
					over = false;
					break;
				}
			}
			ans++;
		}
		printf("Case #%d: %d\n",no,ans-1);
	}
	return 0;
}
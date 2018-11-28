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
#define SIZE 50

int d[SIZE],n;
char str[SIZE];
void findij(int &ri,int &rj)
{
	int i,j;
	for(i = n-2; i >= 0; i--)
	{
		ri = i;
		int min = 20;
		rj = -1;
		for(j = n-1; j > i; j--)
		{
			if(d[i] < d[j] && min > d[j])
			{
				min = d[j];
				rj = j;
			}
		}
		if(rj != -1)
			return;
	}
	ri = rj = -1;
}
int main()
{
	freopen("D:\\B-large.in","r",stdin);
	freopen("D:\\B-large.out","w",stdout);
	int i,j,tmp,T,no = 0;
	scanf("%d",&T);
	while(T--)
	{
		no++;
		scanf("%s",str);
		printf("Case #%d: ",no);
		for(n = 0; str[n]; n++) d[n] = str[n] - '0';
		findij(i,j);
		if(i != -1)
		{
			tmp = d[i]; d[i] = d[j]; d[j] = tmp;
			sort(d+i+1,d+n);
		}
		else
		{
			sort(d,d+n);
			i = 0;
			while(d[i] == 0) i++;
			tmp = d[i];
			d[i] = 0;
			printf("%d",tmp);
		}
		for(i = 0; i < n; i++)
			printf("%d",d[i]);
		printf("\n");
	}
	return 0;
}
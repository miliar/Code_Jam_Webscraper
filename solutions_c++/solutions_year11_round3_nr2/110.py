#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
#define MAXN 1000005
using namespace std; 

double dis1[MAXN];
double disc[MAXN];
bool cmp(double a, double b)
{
	return (a<b);
}

int l, n, c;
double t;
int cnt;
double solve()
{
	double disns = 0;
	double tmp = 0;
	int index;
	double left;
	for(int i = 0; i < n; i++)
		disns += dis1[i];
	for(index = 0; index < n; index++){
		tmp += dis1[index];
		if (tmp * 2 > t){
			left = tmp * 2 - t;
			break;
		}
	}
	cnt = 1;
	disc[0] = left;
	for(index++; index < n; index++)
		disc[cnt++] = dis1[index]*2;
	sort(disc, disc+cnt,cmp);
	double sum = 0;
	for (int i = 0; i < l && i < cnt; i++)
	{
		sum += disc[cnt-i-1];
	}
	return (disns*2-sum/2);
}

/*
freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int tcase;
	scanf("%d", &tcase);
	for(int ts = 1; ts <= tcase; ts++){
		scanf("%d%d",&r,&c);
		for(int i = 0; i < r; i++){
			scanf("%s",map[i]);
		}
		int flag = 1;
		for(int i = 0; i < r && flag; i++){
			for(int j = 0; j < c && flag; j++){
				if(map[i][j] == '#'){
					if(!change(i,j))
						flag = 0;
				}
			}
		}
		
		printf("Case #%d:\n", ts);
		if(!flag)
			printf("Impossible\n");
		else{
			for(int i = 0; i < r; i++){
				for(int j = 0; j < c; j++)
					printf("%c",map[i][j]);
				printf("\n");
			}
		}
	}	
*/
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int tcase;
	scanf("%d", &tcase);
	for(int ts = 1; ts <= tcase; ts++)
	{
		scanf("%d%lf%d%d", &l, &t, &n, &c);
		for(int i = 0; i < c; i++){
			scanf("%lf", &dis1[i]);
		}
		for(int i = c; i < n; i++){
			dis1[i] = dis1[i-c];
		}
		double ans = solve();
		printf("Case #%d: %.0lf\n", ts, ans);
	}	
	return 0;
}


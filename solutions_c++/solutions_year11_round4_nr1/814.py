#include<stdio.h>
#include<queue>
#include<iostream>
#include<string.h>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;

void gcj()
{
	freopen("A-large.in","r",stdin);
	freopen("1.out","w",stdout);
	return ;
}
struct NODE
{
	int s;
	int t;
	double len;
	int speed;
}E[1010];
int n;

int cmp(NODE a,NODE b){
	return a.speed < b.speed;
}
int main()
{
	int t;
	int s,r;
	int T;
	int cas  = 0;
	int len;
	gcj();
	scanf("%d",&T);
	while(T--){
		cas ++;
		scanf("%d%d%d%d%d",&len,&s,&r,&t,&n);
		for(int i = 0 ; i < n; i ++){
			scanf("%d%d",&E[i].s,&E[i].t);
			len -= (E[i].t-E[i].s);
			scanf("%d",&E[i].speed);
			E[i].len = E[i].t - E[i].s;
		}
		E[n].len = len;
		E[n].speed = 0;
		n ++;
		
		sort(E,E+n, cmp);
		double ans= 0;
		double lot = t;
		//printf("%lf\n",lot);
		for(int i = 0 ; i < n; i ++){
			//cout<<len << s << r << t << n << lot << endl;
			//cout<<E[i].len<<E[i].speed<<endl;
			if( lot > 0){
				if(E[i].len/(E[i].speed+r) > lot)
				{
					ans += lot;
					E[i].len = E[i].len - lot * (E[i].speed + r);
					ans = ans + E[i].len / (E[i].speed + s);
					lot = 0;
				}
				else{
					double tmp = E[i].len / ( E[i].speed + r);
					ans += tmp;
					lot -= tmp;
				}
			}
			else{
				ans = ans + E[i].len / (E[i].speed + s);
			}
		}
		printf("Case #%d: %.10lf\n",cas,ans);
	}
	return 0;
}
#include<stdio.h>
#include<algorithm>
using namespace std;

const int maxn = 205;
int na, nb;
int t1;
struct Trip {
	int s, e;
	bool operator < (const Trip & that) const {
		if(s!=that.s) return s< that.s;
		return e<that.e;
	}
} ta[maxn], tb[maxn];
int wa[10000];
int wb[10000];

int toT(char *s){
	//printf("%s\n", s);
	int h, m;
	sscanf(s, "%d:%d", &h, &m);
	return h * 60 + m;
}

int main() {
	int cs;
	char s1[100], s2[100];
	scanf("%d",&cs);
	int step = 1;
	while(cs--){
		int i,j,k;
		scanf("%d%d%d",&t1,&na,&nb);
		//printf("%d %d %d\n", t1, na, nb);
		for(i=0;i<na;i++){
			scanf("%s%s",&s1, &s2);
			ta[i].s = toT(s1);
			ta[i].e = toT(s2);
			//printf("%d %d\n", ta[i].s, ta[i].e);
		}
		sort(ta, ta+na);
		for(i=0;i<nb;i++){
			scanf("%s%s",&s1, &s2);
			tb[i].s = toT(s1);
			tb[i].e = toT(s2);
		}
		sort(tb, tb+nb);
		memset(wa, 0, sizeof(wa));
		memset(wb, 0, sizeof(wb));
		int ans1 = 0, ans2 = 0;
		i=j=0;
		while(i<na || j<nb){
			//printf("%d %d\n", i, j);
			if(i<na && (j==nb || ta[i].s<=tb[j].s)) {
				for(k=ta[i].s;k>=0;k--)if(wa[k])break;
				if(k>=0){
					wa[k]--;
				} 
				else ans1++;
				wb[ta[i].e+t1]++;
				i++;
			} else {
				for(k=tb[j].s;k>=0;k--)if(wb[k])break;
				if(k>=0){
					wb[k]--;
				} 
				else ans2++;
				wa[tb[j].e+t1]++;
				j++;
			}
		}
		printf("Case #%d: %d %d\n", step++, ans1, ans2);
	}
	return 0;
}
#include <cstdio>
#include <algorithm>
#include <cstring>
#define FOR(i,s,e) for (int i=(s); i<(int)(e); i++)
#define FOE(i,s,e) for (int i=(s); i<=(int)(e); i++)
using namespace std;

struct word{
	int r, c, l;
	int b;
	char s[15];
	bool operator < (word const &T) const{return strcmp(s, T.s)<0;}
}	a[10005];

int C, n, m, t, occ[10005][26], ret;
char s[10005][12], list[30];

int main(){

	scanf("%d", &C);
	FOE(tc,1,C){

		scanf("%d%d", &n, &m);
		FOR(i,0,n){
			scanf("%s", s[i]);
			memset(occ[i], 0, sizeof(occ[i]));
			FOR(j,0,strlen(s[i])) occ[i][s[i][j]-'a'] = 1;
		}
		
		printf("Case #%d:", tc);
		
		while (m--){

			scanf("%s", list);
			FOR(i,0,n){
				a[i].r = i;
				a[i].c = 0;
				a[i].l = strlen(s[i]);
				FOR(j,0,a[i].l) a[i].s[j] = '?';
				a[i].s[a[i].l] = 0;
			}
			
			FOR(i,0,26){

				sort(a, a+n);
				t = list[i];
				
				FOR(j,0,n){
					if (occ[a[j].r][t-'a']) a[j].b = 1;
					else a[j].b = 0;
				}
				
				for (int j=1; j<n; j++){
					if (a[j-1].b && a[j].l == a[j-1].l && strcmp(a[j].s, a[j-1].s)==0) a[j].b = 1;
				}
				for (int j=n-2; j>=0; j--){
					if (a[j+1].b && a[j].l == a[j+1].l && strcmp(a[j].s, a[j+1].s)==0) a[j].b = 1;
				}
				
				FOR(j,0,n){
					if (!a[j].b) continue;
					if (occ[a[j].r][t-'a']){
						FOR(k,0,a[j].l)
							if (s[a[j].r][k] == t) a[j].s[k] = t;
					}
					else a[j].c++;
				}

			}
			
			ret = 0;
			FOR(i,1,n){
				t = a[i].c;
				if (t > a[ret].c || (t == a[ret].c && a[i].r < a[ret].r)) ret = i;
			}
			
			printf(" %s", s[a[ret].r]);
		}
		
		printf("\n");
	}
	
	return 0;
}

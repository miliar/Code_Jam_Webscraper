#include<stdio.h>
#include<string.h>
#include<algorithm>

using namespace std;

char dic[10100][20], s[1010000];
bool flag[20][250];
int main()
{
	freopen("A-large.in.txt", "r", stdin);
	freopen("A-small-attempt0.out.txt", "w", stdout);
	int l, d, n;
	while(scanf("%d%d%d", &l, &d, &n)!=EOF){
		for(int i=0; i<d; i++){
			scanf("%s", dic[i]);
		}
		for(int i=1; i<=n; i++){
			scanf("%s", s);
			char *t=s;
			int cnt=0;
			bool c=false;
			memset(flag, 0, sizeof(flag));
			while(*t){
				if(*t=='(') c=true;
				else if(*t==')') c=false, cnt++;
				else{
					flag[cnt][*t]=true;
					if(!c) cnt++;
				}
				t++;
			}
			int sum=0;
			for(int j=0; j<d; j++){
				bool yes=true;
				for(int k=0; k<l; k++){
					if(!flag[k][dic[j][k]]){
						yes=false;
						break;
					}
				}
				if(yes) sum++;
			}
			printf("Case #%d: %d\n", i, sum);
		}
	}
	return 0;
}
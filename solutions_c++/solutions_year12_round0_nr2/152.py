#include <cstdio>

int main(){
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	
	int n, m, s, p, ans, t=0, T, a, b, c;
	scanf("%d", &T);
	
	while (t<T){
		ans=0; t++;
		scanf("%d%d%d", &n, &m, &p);
		for (int i=0; i<n; i++){
			scanf("%d", &s);
			if (s%3==0){
				a=s/3; b=s/3; c=s/3;
				if (c>=p) ans++;
				else {
					if (c+1==p && m>0 && a>0) ans++, m--;
				}
			}
			if (s%3==1){
				a=s/3; b=s/3; c=s/3+1;
				if (c>=p) ans++;
			}
			
			if (s%3==2){
				a=s/3; b=s/3+1; c=s/3+1;
				if (c>=p) ans++; else{
					if (c+1==p && m>0 && b>0) ans++, m--;
				}
			}
		}
		printf("Case #%d: %d\n", t, ans);
	}
}

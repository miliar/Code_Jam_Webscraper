#include <stdio.h>
#include <string.h>
#include <math.h>

int a[10],n;
bool good[10000000][11];
bool was[10000000][11];

void init(){
	char s[100];
	gets(s);
	int l = strlen(s);
	n = 0;
	for (int i = 0 ; i<l ; i++){
		if (s[i]!=' '){
			if (s[i]=='1'){
				a[n++] = 10;
			} else
			{
				if (s[i]!='0')
					a[n++] = s[i]-'0';
			}
		}
	}

}

void solve(){
	int tek = 2;
	while (true){
		bool bad = false
			;
		for (int i = 0 ; i<n ; i++){
			if (!good[tek][a[i]]){
				bad = true;
				break;
			}
		}
		if (!bad) break;
		tek++;
	}
	printf("%d\n",tek);
}

int sumsq(int n,int base){
	int res = 0;
	while (n!=0){
		res+=(n%base)*(n%base);
		n/=base;
	}
	return res;
}

bool isgood(int n, int base){
	if (was[n][base])
		return good[n][base];
	was[n][base] = true;
	if (n==1) return good[n][base] = true;
	
	return good[n][base] = isgood(sumsq(n,base),base);
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	for (int i = 2 ; i<10000000 ; i++){
		for (int j = 2 ; j<=10 ; j++)
			good[i][j] = isgood(i,j);
	}
	int t;
	scanf("%d\n",&t);
	for (int i = 0 ;i<t ; i++){
		printf("Case #%d: ",i+1);
		init();
		solve();
	}
	return 0;
}
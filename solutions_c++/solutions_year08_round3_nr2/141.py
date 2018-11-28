#include <stdio.h>
#include <string.h>
#include <math.h>
#include <string>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

const int maxn = 10000;
const int INF = 1000000000;
const double eps = 1e-10;

#define nul(a) memset(a,0,sizeof(a))

char s[maxn];

long long pow10[30];

void init(){
	gets(s);
}

int l;


void solve(){
	l = strlen(s);
	int i;
	int poww = 1;
	for (i = 0 ; i<l-1 ; i++)
		poww*=3;
	int cnt = 0;
	for (i = 0 ; i<poww ; i++){
		int mas[15];
		int j = 1;
		nul(mas);
		int t = i;
		while (t){
			mas[j++] = t%3;
			t/=3;
		}
		long long res = 0;
		long long teksum = 0;
		int tekpow = 0;
		for (j = l-1 ; j>=0 ; j--){
			if (mas[j]==0){
				teksum+=pow10[tekpow]*(s[j]-'0');
				tekpow++;
			} else
				if (mas[j]==1){
					teksum+=pow10[tekpow]*(s[j]-'0');
					tekpow = 0;
					res-=teksum;
					teksum = 0;
				} else{
					teksum+=pow10[tekpow]*(s[j]-'0');
					tekpow = 0;
					res+=teksum;
					teksum = 0;
				}
		}
		res+=teksum;
		if(res%2==0 || res%3 ==0 || res%5==0 || res%7==0)
			cnt++;
	}
	printf("%d",cnt);
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,i;
	pow10
		[0] = 1;
	for (i = 1 ; i<30 ; i++)
		pow10[i] = pow10[i-1]*10;
	scanf("%d\n",&t);
	for (i = 0 ; i<t ; i++){
		printf("Case #%d: ",i+1);
		init();
		solve();
		printf("\n");
	}
	return 0;
}
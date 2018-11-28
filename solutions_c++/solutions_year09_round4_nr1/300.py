#include<stdio.h>
#include<string.h>
#include<algorithm>

using namespace std;

struct Node{
	char s[101];
	int num;
}g[101];
int main()
{
	int T;
	freopen("A-large1.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &T);
	for(int kk=1; kk<=T; kk++){
		int n;
		scanf("%d", &n);
		for(int i=0; i<n; i++){
			scanf("%s", g[i].s);
			int len=strlen(g[i].s), cnt=0;
			for(int j=len-1; j>=0; j--){
				if(g[i].s[j]=='0') cnt++;
				else break;
			}
			g[i].num=cnt;
		}
		int sum=0;
		for(int i=0, k=n-1, j; i<n; i++, k--){
			for(j=i; j<n; j++){
				if(g[j].num>=k) 	break;
			}
			while(j!=i){
				swap(g[j], g[j-1]);
				j--;
				sum++;
			}
		}
		printf("Case #%d: %d\n", kk, sum);
	}
	return 0;
}
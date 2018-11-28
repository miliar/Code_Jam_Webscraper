#include <iostream>
#include <cmath>
#include <cstdio>
#include <algorithm>

using namespace std;
char s[100000][20];
char ss[100];
int T,N,M,vis[100000],cost,Ans,a[10000];
int check(char ch){
	for (int i=0;i<N;i++)
	if (vis[i]){
		for (int j=0;j<strlen(s[i]);j++)
		if (s[i][j]==ch) return 1;
	}
	return 0;
}
void work(){
	cost=-1;
	for (int i=0;i<N;i++){
		int now=0;
		for (int j=0;j<N;j++){
			if (strlen(s[i])==strlen(s[j])) vis[j]=1;else
			vis[j]=0;
			a[j]=0;
		}
		for (int l=0;l<strlen(ss);l++)
		if (check(ss[l])){
			int flag=0;
			for (int j=0;j<strlen(s[i]);j++)
			if (s[i][j]==ss[l]){
				flag=1;
				a[i]^=(1<<j);
			}
			if (!flag) now++;
			for (int j=0;j<N;j++)
			if (j!=i){
				for (int k=0;k<strlen(s[j]);k++)
				if (s[j][k]==ss[l]) a[j]^=(1<<k);
				if (a[j]!=a[i]) vis[j]=0;
			}
		}
		if (cost<now){
			cost=now;
			Ans=i;
		}
	}
	cout << " " << s[Ans];
}
int main(){
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	cin >> T;
	for (int t=1;t<=T;t++){
		printf("Case #%d:", t);
		cin >> N >> M;
		for (int i=0;i<N;i++)
		cin >> s[i];
		for (int i=0;i<M;i++){
			cin >> ss;
			work();
		}
		printf("\n");
	}
}

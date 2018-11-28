#include<cstdio>
#include<iostream>
#include<algorithm>
#include<map>
#define INF 999999999

using namespace std;

map<string,int> nr;

int d;

int n,q;
char cstr[20000];

int t[1005];
int w[1005][105];

void alg(int c){
	scanf("%d\n",&n);
	for(int i=1;i<=n;i++){
		gets(cstr);
		string a=cstr;
		nr[a]=i;
	}
	scanf("%d\n",&q);
	for(int i=0;i<q;i++){
		gets(cstr);
		string a=cstr;
		t[i+1]=nr[a];
	}
	for(int i=1;i<=q;i++) for(int j=1;j<=n;j++) w[i][j]=INF;
	for(int i=1;i<=q;i++){
		int z=INF;
		for(int j=1;j<=n;j++){
			if(t[i]!=j){
				z=min(z,w[i-1][j]);
				w[i][j]=w[i-1][j];
			}
		}
		w[i][t[i]]=z+1;
	}
	int z=INF;
	for(int i=1;i<=n;i++) z=min(z,w[q][i]);
	printf("Case #%d: %d\n",c,z);
}

int main(){
	scanf("%d",&d);
	for(int i=1;i<=d;i++) alg(i);
}

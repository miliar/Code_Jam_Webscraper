#include<iostream>
#include<algorithm>
using namespace std;

const int N=8;
int n;
string g[N];
int c[N];
int cur[N];

bool Input(){
	scanf("%d",&n);
	int i;
	char bf[9];
	for(i=0;i<n;++i){
		scanf("%s",&bf);
		g[i]=string(bf);
	}
	return 1;
}

bool Ok(){
	int i,j,k;
	for(i=0;i<n;++i){
		for(j=i+1;j<n;++j){
			if(g[c[i]][j]=='1') return 0;
		}
	}
	return 1;
}

int Cal(){
	int i,j,k;
	int ret=0;
	for(i=0;i<n;++i){
		cur[i]=i;
	}
	for(i=0;i<n;++i){
		if(cur[i]!=c[i]){
			for(j=i+1;j<n;++j){
				if(cur[j]==c[i]){
					break;
				}
			}
			for(k=j;k>i;--k){
				swap(cur[k],cur[k-1]);
				++ret;
			}
		}
	}
	return (Ok()? ret:-1);
}

void Solve(int cn){
	int i,j,k;
	for(i=0;i<n;++i){
		c[i]=i;
	}
	int ans=Cal();
	while(next_permutation(c,c+n)){
		int r = Cal();
		if(ans<0 || r>=0 && r<ans){
			ans=r;
		}
	}
	printf("Case #%d: %d\n",cn,ans);
	return;
}

int main()
{
	freopen("A-small.in","r",stdin);
	freopen("A-small.txt","w",stdout);
	int tn,id=0;
	scanf("%d",&tn);
	while(tn--){
		Input();
		Solve(++id);
	}
	return 0;
}

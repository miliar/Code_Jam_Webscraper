#include <cstdio>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>

using namespace std;

#define pb push_back
#define inf (1e9)

char s[10000];
char ts[10000];
int perm[100];

int getsize(int l){
	int r=1;
	for(int i=1;i<l;++i)if(ts[i]!=ts[i-1])++r;
	return r;
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int n;
	cin>>n;
	for(int i=0;i<n;++i){
		int k;
		cin>>k;
		gets(s);
		gets(s);
		int l=strlen(s);
		for(int j=0;j<k;++j){
			perm[j]=j;
		}
		int res=inf;
		do{
			for(int j=0;j<l;++j){
				ts[(j/k)*k+perm[j%k]]=s[j];
			}
			res=min(res,getsize(l));
		}while(next_permutation(perm,perm+k));
		printf("Case #%d: %d\n",i+1,res);
	}

	return 0;
}
#include <iostream>
#include <cmath>
#include <string>

#define NAME "file"
using namespace std;
int test;
int p,q;
int Q[100];
int u[10];
int s[10];
int f[10];
int ans;

void check(void){
	int res=0;
	for (int i=1;i<=p;i++) f[i]=1;
	f[0]=0;
	f[p+1]=0;
	for (int i=0;i<q;i++){
		f[Q[s[i]]]=0;
		int a=Q[s[i]]-1;
		int b=Q[s[i]]+1;
		while (f[a]){
			res++;
			a--;
		}
		while (f[b]){
			res++;
			b++;
		}

		
	}
	if (res<ans) ans=res;
}

void fuck(int k){
	if (k>=q){
		
		check();
	}
	for (int i=0;i<q;i++){
		if (!u[i]){
			s[k]=i;
			u[i]=1;
			fuck(k+1);
			u[i]=0;
		}
	}
}


int main(void){
	freopen(NAME".in","r",stdin);
	freopen(NAME".out","w",stdout);
	cin>>test;
	for (int z=0;z<test;z++){
		cin>>p>>q;
		for (int i=0;i<q;i++){
			cin>>Q[i];
		}
		ans=1000000000;
		fuck(0);

		printf("Case #%i: %i\n",z+1,ans);
	}

	return 0;
}
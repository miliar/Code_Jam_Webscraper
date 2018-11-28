#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>
using namespace std;
//const int N = 1000;
int a[1000], b[1000],n,i,j;
void init(){
	scanf("%d",&n);
	for (i=0;i<n;i++){
		scanf("%d%d",&a[i],&b[i]);
	}
	for (i=0;i<n-1;i++)
		for (j=i+1;j<n;j++)
		if (a[i]>a[j])
		{
			swap(a[i], a[j]), swap(b[i], b[j]);
		}
}

int solve(){
	int ans=0;
	for (i=0;i<n-1;i++)
		for (j=i+1;j<n;j++)
		if (b[i]>b[j]) ans++;
	return ans;
}

int main(){
	int T;
	scanf("%d",&T);
	for (int i=1;i<=T;i++){
		init();
		printf("Case #%d: %d\n",i,solve());
	}
}

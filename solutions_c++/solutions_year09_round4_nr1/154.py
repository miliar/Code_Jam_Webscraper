#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
using namespace std;

const int size=50;
int a[size],n;

int solve(){
	int i,j,r=0;
	for(i=0; i<n; i++){
		for(j=i; a[j]>i; j++);
		while(j>i){
			swap(a[j],a[j-1]);
			j--;
			r++;
		}
	}
	return r;
}

int main(){
	int T;
	scanf("%d",&T);
	for(int cs=1; cs<=T; cs++){
		scanf("%d",&n);
		for(int i=0,j; i<n; i++){
			char s[size];
			scanf("%s",s);
			for(j=n-1; j>0; j--){
				if(s[j]=='1') break;
			}
			a[i]=j;
			//printf("a[%d]=%d\n",i,j); 
		}
		printf("Case #%d: %d\n",cs,solve());
	}
	return 0;
}

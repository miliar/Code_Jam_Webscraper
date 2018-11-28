#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int T,n,f=0;
int num[1010];
int v[1010];
double sum;
struct S{
    int val, idx;
}s[1010];
bool cmp1(S a,S b){
    if(a.val!=b.val) return a.val < b.val;
    else return a.idx < b.idx;
}
bool cmp2(S a,S b){
    if(a.idx!=b.idx) return a.idx < b.idx;
    else return a.val < b.val;
}

int main(){
    scanf("%d",&T);
    while(T--){
	scanf("%d",&n);
	sum = 0;
	for(int i=1;i<=n;i++){
	    scanf("%d",&s[i].val);
	    s[i].idx = i;
	}
	sort( s+1, s+n+1, cmp1);
	for(int i=1;i<=n;i++){
	    s[i].val = i;
	}
	sort(s+1,s+n+1,cmp2);
	memset(v,0,sizeof(v));
	for(int i=1;i<=n;i++){
	    if(i!=s[i].val){
		sum = sum + 1;
	    }
	}
	printf("Case #%d: %.6f\n",++f,sum);
    }

}

// Author : Muhammad Rifayat Samee
// Problem : C
// Algorithm:
#pragma warning (disable : 4786)
#pragma comment(linker, "/STACK:16777216")

#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<cstring>
#include<algorithm>
#include<string>
#include<set>
#include<vector>
#include<map>
#include<queue>
#include<stack>
#define MAX(a,b) (a>b)?a:b
#define MIN(a,b) (a<b)?a:b
#define INF 987654321
#define pi (2*acos(0.0))
#define eps 1e-7

#ifdef ONLINE_JUDGE
#define i64 long long
#else
#define i64 __int64
#endif




using namespace std;
int n,m;
char a[5];
int flag[9999999],cc=1;

int cal(int n){
	int i,j,r,k,res,t,len,num,num1;
	res = 0;
	k = 0;
	num1 = n;
	while(n!=0){
		r = n%10;
		a[k] = r + '0';
		n = n/10;
		k++;
	}
	a[k] = NULL;
	strrev(a);
	len = strlen(a);
	for(i=0;i<len-1;i++){
		t = a[0];
		for(j=0;j<len-1;j++){
			a[j] = a[j+1];
		}
		a[j] = t;
		if(a[0] == '0')continue;
		num  = atoi(a);
		if(num>num1 && num<=m ){
			//printf("%d %d\n",num,num1);
			if(flag[num]!=cc){
				flag[num] = cc;
				res++;
			}
		}
	}

	return res;
}
int main(){

	freopen("Cl.IN","r",stdin);
	freopen("out.txt","w",stdout);
	int cases,i,j,k,res,ct=1;
	scanf("%d",&cases);
	while(cases--){
		scanf("%d %d",&n,&m);
		res = 0;
		for(i=n;i<=m;i++){
			res = res + cal(i);
			cc++;
		}
		printf("Case #%d: %d\n",ct++,res);
	}
	return 0;
}
/*	Author       :	Muntasir Muzahid Chowdhury
	Problem Name :	
	Algorithm    :	
	Complexity   :	*/

//HEADERFILE
#include<iostream>
#include<stack>
#include<queue>
#include<list>
#include<vector>
#include<set>
#include<map>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cctype>
#include<cstring>
#include<ctime>
#include<cassert>
#include<string>
#include<algorithm>

using namespace std;

typedef __int64 lint;
typedef unsigned __int64 ulint;

const int SIZ = 100000;
const int INF = (1<<29);
const double EPS = 1e-11;
const double PI = acos(-1);

int MAX(int a,int b){	return a>b?a:b;	}
int MIN(int a,int b){	return a<b?a:b;	}
int GCD(int a,int b){	while(b)b^=a^=b^=a%=b;	return a;	}

int main(){
		//freopen("C-small-attempt5.in","r",stdin);
		//freopen("C-small-attempt5.out","w",stdout);
	int cases,caseno=0,i,j,result;
	int N,L,H,ar[110];
	scanf("%d",&cases);
	while(cases--){
		scanf("%d %d %d",&N,&L,&H);
		for(i=0;i<N;i++) scanf("%d",&ar[i]);
		int res1=-1,cnt;
		for(i=L;i<=H;i++){
			for(j=0,cnt=0;j<N;j++){
				if(ar[j]%i==0) ++cnt;
				else if(i%ar[j]==0) ++cnt;
				else break;
			}
			if(cnt==N) { res1=i; break; }
		}
		if(res1!=-1) printf("Case #%d: %d\n",++caseno,res1);
		else printf("Case #%d: NO\n",++caseno);
	}
	return 0;
}


#include<iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<cmath>
using namespace std;

#define F(i,n) for(i=0;i<n;i++)
#define FF(i,n) for(i=1;i<=n;i++)
#define LL __int64

int C, D, N;
char m[300][300];
char s[110], ans[110];
bool op[300][300];
int len;

void work(){
	int i, j;
	len = 0;
	F(i,N){
		if(len==0)ans[len++] = s[i];
		else if(m[ans[len-1]][s[i]])ans[len-1]=m[ans[len-1]][s[i]];
		else {
			F(j,len)if(op[ans[j]][s[i]])break;
			if(j<len)len=0;
			else ans[len++] = s[i];
		}
	}
}

int main(){
     int i, j, T, TT=1;
     
//     freopen("B-large.in", "r", stdin);
//    freopen("B-large.out", "w", stdout);
     
     scanf("%d",&T);
     while(T--){
		memset(m, 0, sizeof(m));
		scanf("%d",&C);
		F(i,C){
			scanf("%s",s);
			m[s[0]][s[1]] = m[s[1]][s[0]] = s[2];
		}
		memset(op, 0, sizeof(op));
		scanf("%d",&D);
		F(i,D){
			scanf("%s", s);
			op[s[0]][s[1]] = op[s[1]][s[0]] = true;
		}
		scanf("%d%s",&N,s);
		work();
		printf("Case #%d: [", TT++);
		F(i,len){
			if(i)putchar(' ');
			putchar(ans[i]);
			if(i!=len-1)putchar(',');
		}
		printf("]\n");
	}
//		cin>>i;
     
     return 0;
}

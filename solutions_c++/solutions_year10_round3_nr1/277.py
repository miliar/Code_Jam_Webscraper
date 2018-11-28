#include <stdio.h>
#include <iostream>
#include <memory.h>
using namespace std;
#define clr(a) memset(a,0,sizeof(a))
#define N 10003
int c[N][N];
int n= 10003;
int lowbit(int x){
    return x&(-x);
}
void Update(int x,int y,int t){
    int i,j;
    i=x;
    while(i<=n){
        j=y;
        while(j<=n){
            c[i][j]+=t;
            j+=lowbit(j);
        }
        i+=lowbit(i);
    }
}
int Query(int x,int y){
    int i,j,s=0;
    i=x;
    while(i>0){
        j=y;
        while(j>0){
            s+=c[i][j];
            j-=lowbit(j);
        }
        i-=lowbit(i);
    }
    return s;
}
int main()
{
	int kase;
	int a[1001],b[1001];
	memset(c,0,sizeof(c));
    cin>>kase;
	int X;
	for (int i=1;i<=kase;i++)
		{
			clr(c);
			cin>>X;
			for(int j=0;j<X;j++)
			{
				cin>>a[j]>>b[j];
				Update(a[j],b[j],1);
			}
			int result = 0;
			for(int j=0;j<X;j++)
			{
				result += Query(10001,b[j]) + Query(a[j],10001)	- 2* Query(a[j],b[j]);	
			}
			printf("Case #%d: %d\n",i,result/2);
		}

    return 0;
}

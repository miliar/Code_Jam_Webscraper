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

#define INF 987654321
#define pi (2*acos(0.0))
#define eps 1e-7

#define siz 10010

int a[siz];
int N, L, H;
int ABS( int a ) { return a < 0 ? -a : a ;}
int call(){
	int fl;
	int i , j;
	for( i=L; i<=H; i++){
			fl = 1;
			for( j = 0; j <N; j++){
				if(a[j]%i!=0 && i%a[j]!=0){
					fl = 0;
					break;
				}
			}
			if(fl){
				return i;
			}
		}
	return false;
}
int main()
{
	// freopen("sC.in","r",stdin);
	//freopen("out.txt","w",stdout);
	int i, j;
	int kase,ct =1;
	scanf("%d",&kase);
	while(kase--){
		scanf("%d %d %d",&N, &L, &H);
		for(i = 0;i < N; i++){
			scanf("%d",&a[i]);
		}
		int fl = call();
		if(fl){
			printf("Case #%d: %d\n",ct++,fl);
		}
		else printf("Case #%d: NO\n",ct++);
		
	}
	
	return 0;


}
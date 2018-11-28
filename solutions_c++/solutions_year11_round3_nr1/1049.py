//Author : Sushant Bhatia
#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<cmath>
#include<cstring>
#define FOR(i,j,k) for(i = j;i < k;i++)
#define RFOR(i,j,k) for(i = k-1;i >= j;i--)
#define LL long long
#define GET(x) scanf("%d",&x)
#define OUT(x) printf("%d\n",x)
#define SET(x) memset(x,0,sizeof(x))
#define S(x) x.size()
bool comp(int i,int j){ return i > j; }
using namespace std;
char a[55][55];
int main(){
	int t,r,c;
	int i,cs,j;
	GET(t);
	bool don;
	FOR(cs,1,t+1){
		printf("Case #%d:\n",cs);
		GET(r);GET(c);
		FOR(i,0,r) scanf("%s",a[i]);
		don = true;
		FOR(i,0,r){
			FOR(j,0,c){
				if(a[i][j] == '#'){
					if((j+1 < c && a[i][j+1] == '#') && (i+1 < r && a[i+1][j] == '#') && (i+1 < r && j+1 < c && a[i+1][j+1] == '#')){
						a[i][j] = a[i+1][j+1] = '/';
						a[i][j+1] = a[i+1][j] = '\\';
						//cout<<i<<" "<<j<<" ch \n";
					}
					else{
						don = false;
						//cout<<i<<" "<<j<<"\n";
						//cout<<a[i+1][j]<<" "<<a[i+1][j+1]<<" "<<a[i][j+1];
						break;
					}
				}
			}
			if(!don) break;
		}
		//FOR(i,0,r) printf("%s\n",a[i]);
		if(don){
			FOR(i,0,r) printf("%s\n",a[i]);
		}
		else printf("Impossible\n");
	}
	return 0;
}

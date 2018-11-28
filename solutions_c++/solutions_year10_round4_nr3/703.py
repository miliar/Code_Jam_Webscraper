#include<cstdio>
#include<cstring>
#include<cmath>
#include<cctype>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<numeric>
#include<fstream>
using namespace std;
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define memo(a,v) memset(a,v,sizeof(a))
#define pb push_back
#define all(a) a.begin(),a.end()
#define eps (1e-9)
#define inf (1<<29)

bool gr[1000][1000];
int main(){
	freopen("C-small.in","r",stdin);
	freopen("C-small.ans","w",stdout);
	int t,k,i,j,cs,r,c,flag,X1,X2,Y1,Y2,n;
	cin>>t;
	for(cs=1;cs<=t;cs++){
		cin>>n;
		memo(gr,0);
		for(i = 0;i<n;i++){
			cin>>Y1>>X1>>Y2>>X2;
			r = max(X2,r);
			c = max(Y2,c);
			for(;X1<=X2;X1++){
				for(j=Y1;j<=Y2;j++){
					gr[X1][j]=1;
				}
			}
		}
		for(k = 0;;k++){
			flag = 0;
			for(i = r;i>=0;i--){
				for(j=c;j>=0;j--){
					if(gr[i][j]==1){
						flag = 1;
						if(i-1>=0 && gr[i-1][j]) continue;
						if(j-1>=0 && gr[i][j-1]) continue;
						gr[i][j] = 0;
					}
					else{
						if(i>0 && j>0 && gr[i][j-1] && gr[i-1][j]) gr[i][j] = 1;
					}
				}
			}
			if(!flag) break;
		}
		printf("Case #%d: %d\n",cs,k);
	}
	return 0;
}
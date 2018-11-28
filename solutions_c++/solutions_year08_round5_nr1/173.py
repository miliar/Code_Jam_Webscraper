#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

#define eps 1e-8
#define PI 3.14159265358979323846
#define push_back(a) pb(a)
typedef long long ll;

int a[250][250];
bool wx[250][250];
bool wy[250][250];
int dx[]={0,1,0,-1};
int dy[]={1,0,-1,0};
void getac(int x,int y){
	if(x<=5 || x>=215 || y<=5 || y>=215 ) return;
	if(a[x][y]!=0) return;
	a[x][y]=1;
	if(!wx[x][y])
		getac(x,y-1);
	if(!wy[x][y])
		getac(x-1,y);
	if(!wx[x][y+1])
		getac(x,y+1);
	if(!wy[x+1][y])
		getac(x+1,y);
}

bool chkx(int x,int y){
	int ok=0;
	int i;
	for(i=x;i>=6;i--){
		if(wy[i][y]){
			ok++;
			break;
		}
	}
	if(ok==1){
		for(i=x+1;i<=215;i++){
			if(wy[i][y]){
				ok++;
				break;
			}
		}
		if(ok==2){
			return 1;
		}
	}
	return 0;
}

bool chky(int x,int y){
	int ok=0;
	int i;
	for(i=y;i>=6;i--){
		if(wx[x][i]){
			ok++;
			break;
		}
	}
	if(ok==1){
		for(i=y+1;i<=215;i++){
			if(wx[x][i]){
				ok++;
				break;
			}
		}
		if(ok==2){
			return 1;
		}
	}
	return 0;
}

int main(){
	int T,TT;
	scanf("%d",&T);
	for(TT=1;TT<=T;TT++){
		printf("Case #%d: ",TT);
		int i,l,j,k;
		memset(wx,0,sizeof(wx));
		memset(wy,0,sizeof(wy));
		memset(a,0,sizeof(a));
		scanf("%d",&l);
		char s[30];
		int t;
		int x=110,y=110;
		
		int d=0;
		for(i=0;i<l;i++){
			scanf("%s%d",s,&t);
			int len=strlen(s);
			for(k=0;k<t;k++){
			for(j=0;j<len;j++){
				if(s[j]=='F'){
					if(d==0){
						wy[x][y]=1;
					}else if(d==1){
						wx[x][y]=1;
					}else if(d==2){
						wy[x][y-1]=1;
					}else{
						wx[x-1][y]=1;
					}
					x+=dx[d];
					y+=dy[d];
				}else if(s[j]=='R'){
					d=(d+1)%4;
				}else{
					d=(d-1+4)%4;
				}
			}
		}
		}
		//printf("### %d %d\n",x,y);
		int cnt=0;
		getac(6,6);
		for(i=6;i<215;i++){
			for(j=6;j<215;j++){
				if(a[i][j]){
					if(chkx(i,j)||chky(i,j)){
						cnt++;
						//printf("## %d %d\n",i,j);
					}
				}
			}
		}
		printf("%d\n",cnt);
	}
}

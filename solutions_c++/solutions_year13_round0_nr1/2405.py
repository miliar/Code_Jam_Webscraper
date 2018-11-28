#include<set>
#include<map>
#include<cmath>
#include<queue>
#include<stack>
#include<vector>
#include<cctype>
#include<cstdio>
#include<string>
#include<sstream>
#include<cstring>
#include<cstdlib>
#include<fstream>
#include<iterator>
#include<iostream>
#include<algorithm>

using namespace std;

#pragma comment(linker,"/STACK:16777216")
#pragma warning(disable:4786)

#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))
#define myabs(a) ((a)<0?(-(a)):(a))
#define pi acos(-1.0)
#define CLR(a) memset(a,0,sizeof(a))
#define SET(a) memset(a,-1,sizeof(a))
#define pb push_back
#define all(a) a.begin(),a.end()
#define ff first
#define ss second
#define eps 1e-9
#define root 1
#define lft 2*idx
#define rgt 2*idx+1
#define cllft lft,st,mid,s,e
#define clrgt rgt,mid+1,ed,s,e
#define inf (1<<29)
#define i64 long long
#define MX 12

typedef pair<int,int> pii;

char mat[MX][MX],n=4,m=4;
char out[4][100]={"X won","O won","Draw","Game has not completed"};

bool possible(int x,int y,int dx,int dy,char val){
    if(x>=n || y>=m || x<0 || y<0)return true;
    if(mat[x][y]!='T' && mat[x][y]!=val)return false;
    return possible(x+dx,y+dy,dx,dy,val);
}

bool winPossible(int x,int y){
    if(!x && possible(x,y,1,0,mat[x][y]))return true;
    if(!x && !y && possible(x,y,1,1,mat[x][y]))return true;
    if(!x && y==m-1 && possible(x,y,1,-1,mat[x][y]))return true;
    if(!y && possible(x,y,0,1,mat[x][y]))return true;
    if(x==n-1 && !y && possible(x,y,-1,1,mat[x][y]))return true;
    if(x==n-1 && y==m-1 && possible(x,y,-1,-1,mat[x][y]))return true;
    return false;
}

int func(){
    int i,j,c=0;
    for(i=0;i<n;i++){
        for(j=0;j<m;j++){
            if(mat[i][j]=='X' && winPossible(i,j))return 0;
            if(mat[i][j]=='O' && winPossible(i,j))return 1;
            if(mat[i][j]=='.')c++;
        }
    }
    if(!c)return 2;
    return 3;
}

int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int cs,t=1,i,j;
	cin>>cs;
	while(cs--){
	    for(i=0;i<n;i++)cin>>mat[i];
	    printf("Case #%d: %s\n",t++,out[func()]);
	}
	return 0;
}



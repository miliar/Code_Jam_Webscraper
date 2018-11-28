#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstdio>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <string.h>
#include <cassert>

using namespace std;

#define GI ({int t;scanf("%d",&t);t;})
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define sz size()
#define INF (int)1e9

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<vector<int> > VVI;
typedef pair<int,int> PII;

char a[4][4];
bool tst(char c){
        bool b=false;int i,j,x;
        for(i=0;i<4;i++){ x=0;for(j=0;j<4;j++)if(a[i][j]==c || a[i][j]=='T')x++;if(x==4)return true;}
		for(i=0;i<4;i++){ x=0;for(j=0;j<4;j++)if(a[j][i]==c || a[j][i]=='T')x++;if(x==4)return true;}
		x=0;for(i=0;i<4;i++){ if(a[i][i]==c || a[i][i]=='T')x++;if(x==4)return true;}
		x=0;for(i=0;i<4;i++){ if(a[i][3-i]==c || a[i][3-i]=='T')x++;if(x==4)return true;}
		return b;
    }

int main(){
	
	freopen("large.txt","r",stdin);
	freopen("outlarge.txt","w",stdout);
	string s;
	int Kase=GI;
	FOR(kase,1,Kase+1){
		int x,y,i,j;char c;
		if(kase!=1)getline(cin,s);
		for(i=0;i<4;i++)for(j=0;j<4;j++)cin>>a[i][j];
		printf("Case #%d: ",kase);
		c='X';if(tst(c))cout<<"X won"<<endl;
		else if(tst('O'))cout<<"O won"<<endl; 
		else {
		x=0;for(i=0;i<4;i++)for(j=0;j<4;j++)if(a[i][j]=='.'){x=1;break;}
       if(x==0)cout<<"Draw"<<endl;else cout<<"Game has not completed"<<endl;
       }
		
	}
	return 0;
}

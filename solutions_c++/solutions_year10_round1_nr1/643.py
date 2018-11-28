#include<math.h>
#include<ctype.h>
#include<vector>
#include<string>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<algorithm>
#include<sstream>
#include<iostream>
using namespace std;

#define memo(a,v) memset(a,v,sizeof(a))
#define pb push_back
#define max(a,b) (a)>(b)?(a):(b)
#define min(a,b) (a)<(b)?(a):(b)

string s[55];
char a[55][55];
int n,k,flag0,flag1,mov[8][2]={-1,-1,-1,0,-1,1,0,-1,0,1,1,-1,1,0,1,1};
bool fflill(int x,int y,int d,int dx,int dy,char c){
	if(x<0 || y<0 || x>=n || y>=n || a[x][y]!=c) return false;
	if(d==k) return true;
	return fflill(x+dx,y+dy,d+1,dx,dy,c);
}
void isvalid(){
	int i,j,p;
	for(i = n - 2;i>=0;i--){
		for(j = 0;j<n;j++){
			if(a[i][j]=='.') continue;
			p = i+1;
			while(p<n && a[p][j]=='.') p++;
			p--;
			if(p==i) continue;
			a[p][j] = a[i][j];
			a[i][j]='.';
		}
	}
	for(i = 0;i<n;i++){
		for(j = 0;j<n;j++){
			if(a[i][j]=='.') continue;
			for(p = 0;p<8;p++){
				if(fflill(i,j,1,mov[p][0],mov[p][1],a[i][j])){
					if(a[i][j]=='R') flag0 = 1;
					else if(a[i][j]=='B') flag1 = 1;
				}
			}
			if(flag0 && flag1) break;
		}
		if(flag0 && flag1) break;
	}
}
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.ans","w",stdout);
	int t,cs,i,j;
	cin>>t;
	for(cs = 1;cs<=t;cs++){
		cin>>n>>k;
		for(i = 0;i<n;i++) cin>>s[i];

		flag0 = flag1 = 0;
		for(i = 0;i<n;i++){
			for(j = 0;j<n;j++){
				a[i][j] = s[n - j - 1][i];
			}
		}
		isvalid();
		printf("Case #%d: ",cs);
		if(flag0 && flag1) printf("Both\n");
		else if(flag0) puts("Red");
		else if(flag1) puts("Blue");
		else puts("Neither");
	}
	return 0;
}
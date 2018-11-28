/*
ID: harrymw1
LANG: C++
TASK: 
*/
 
#include <iostream>
#include<algorithm>
#include<string>
#include<cstring>
#include<cmath>
#include<vector>
#include <cstdio>
#include<map>
#include<stack>
#include<set>
#include<queue>
#include<cctype>
#include<assert.h>
#include<numeric>
#include<ctime>
#include<iterator>
//#include<sstream>
using namespace std;

#define PI acos(-1.0)
#define fore(i,a) for(int i=0; i<(a); i++)
#define forv(i,a) for(typeof(a.begin()) i=a.begin();i!=a.end();i++)
#define pb push_back
#define all(x) x.begin(),x.end()
typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;
/*template<class T> string toString(T n){
	ostringstream ost;ost<<n;ost.flush();
	return ost.str();
}*/

//__builtin_popcount(int x);
char mp[55][55];
char r[55][55];
int n,k,ca=1;
void rota(){
	for(int i=0;i<n;i++)for(int j=0;j<n;j++){
		r[j][n-1-i]=mp[i][j];
	}
	for(int i=n-1;i>=0;i--)for(int j=0;j<n;j++){
		if(r[i][j]=='R'||r[i][j]=='B'){
			if(i+1<n&&r[i+1][j]=='.'){
				int t=i;while(t+1<n&&r[t+1][j]=='.')t++;
				if(t<n)r[t][j]=r[i][j],r[i][j]='.';
			}
		}
	}
	int cr=0,cb=0,flagr=0,flagb=0;
	for(int i=0;i<n;i++)for(int j=0;j<n;j++){
		if(flagr==0&&r[i][j]=='R'){
			int x=i,y=j;
			//if(i-1>=0&&r[i-1][j]!='R'){
			cr=0;	
			while(x<n&&r[x][y]=='R'){
				++cr;x++;
			}
				if(cr==k)flagr=1;
			//}
			x=i,y=j,cr=0;
			//if(j-1>=0&&r[i][j-1]!='R'){
				while(y<n&&r[x][y]=='R'){++cr;y++;}
				if(cr==k)flagr=1;
			//}
			x=i,y=j,cr=0;
			while(x<n&&y>=0&&r[x][y]=='R'){++cr;x++;y--;}
			if(cr==k)flagr=1;
			x=i,y=j,cr=0;
			while(x<n&&y<n&&r[x][y]=='R'){++cr;x++;y++;}
			if(cr==k)flagr=1;
		}
		if(flagb==0&&r[i][j]=='B'){
			int x=i,y=j;cb=0;
			//if(i-1>=0&&r[i-1][j]!='B'){
				while(x<n&&r[x][y]=='B'){++cb;x++;}
				if(cb==k)flagb=1;
			//}
			x=i,y=j,cb=0;
			//if(j-1>=0&&r[i][j-1]!='B'){
				while(y<n&&r[x][y]=='B'){++cb;y++;}
				if(cb==k)flagb=1;
			//}
			x=i,y=j,cb=0;
			while(x<n&&y>=0&&r[x][y]=='B'){++cb;x++;y--;}
			if(cb==k)flagb=1;
			x=i,y=j,cb=0;
			while(x<n&&y<n&&r[x][y]=='B'){++cb;x++;y++;}
			if(cb==k)flagb=1;
		}
	}
	if(flagr&&flagb){printf("Case #%d: Both\n",ca++);}
	if(flagr&&!flagb){printf("Case #%d: Red\n",ca++);}
	if(!flagr&&flagb){printf("Case #%d: Blue\n",ca++);}
	if(!flagr&&!flagb){printf("Case #%d: Neither\n",ca++);}
	
}
int main()
{
	freopen("A.in.txt", "r", stdin);
	freopen("A.out.txt", "w", stdout);
	//clock_t start, finish;
   	//double duration;
   	//start = clock();
	int t;scanf("%d",&t);
	while(t--){
	
		scanf("%d%d",&n,&k);
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
				cin>>mp[i][j];
		rota();
	}


	//finish = clock();
   	//duration = (double)(finish - start) / CLOCKS_PER_SEC;
	//printf( "%f seconds\n", duration );
	return 0;
}

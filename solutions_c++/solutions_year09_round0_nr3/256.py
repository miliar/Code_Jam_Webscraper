#include <cstdio>
#include <cmath>
#include <map>
#include <vector>
#include <algorithm>
#include <iostream>
#include <string>
#include <set>
#include <sstream>
#include <cstdlib>
#include <stack>
#define FOR(i,j,n) for (int i=j;i<n;++i)
#define FORI(i,j,n) for (int i=j;i<=n;++i)
#define FORN(i,n) FOR(i,0,n)
#define sz size()
#define PB(a) push_back(a)
#define foreach(i, c) for( __typeof( (c).rbegin() ) i = (c).rbegin(); i != (c).rend(); ++i )
#define CPRESENT(container, element) (find(ALL(container),element) != container.end())
#define MIN(a,b) (a < b ? a : b)
#define MAX(a,b) (a > b ? a : b)
#define ALL(x) x.begin(), x.end()
#define INF 1<<30

using namespace std;

int n,l,d;
string s;

string _wel= "welcome to code jam";

void clean(){
	string res;
	FORN(i,s.size()){
		bool ap = false;
		FORN(j,_wel.size())
			if (s[i]== _wel[j]) 
				ap=true;
		if (ap)
		res+=s[i];
	}
	s=res;
}

long long  mem[2000][100];
long long inf;

long long dp(int x,int y){
	
	if (y==_wel.size())
		return 1;
	if (x==s.size())
		return 0;

	if (mem[x][y]!=inf)
		return mem[x][y];

	if (s[x]==_wel[y])
		return mem[x][y]=((dp(x+1,y+1)+dp(x+1,y))%10000);
	else 
		return mem[x][y]=(dp(x+1,y)%10000);
}
int main(){
	
 	cin>>n;
	getline(cin,s);
	FORN(__case,n){
		getline(cin,s);
		clean();
		
		memset(mem,0x7f,sizeof mem);
		inf = mem[0][0];

		printf("Case #%d: %.4d\n",__case+1,dp(0,0));

	}
    


    return 0;
}





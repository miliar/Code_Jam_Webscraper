
/*Paresh Verma*/
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
#include <cstring>
#include <queue>		//max heap implementation
#include <limits.h>

#define pub push_back
#define pob pop_back
#define puf push_front
#define pof pop_front
#define mkp make_pair
#define fi first
#define se second
#define LL long long
#define fill(x,y) memset(x, y, sizeof(x))
#define debug(a) { for( typeof(a.begin()) it = a.begin() ; it != a.end() ; it++ ) cout << *it << " "; cout << endl; }

using namespace std;

//class comparators for queue and others
class classcomp{
	public:
		bool operator() (const int& l, const int& r)const{
			return l<r;
		}
};

int dx[]={1,0,-1,0};
int dy[]={0,1,0,-1};

char s[5][5];

bool check( char c){
	int i,j,k,l;
	k=1; l=1;
	for(i=0;i<4;i++){
		if(!(s[i][i]==c || s[i][i]=='T')) k=0;
		if(!(s[i][3-i]==c || s[i][3-i]=='T')) l=0;
	}	
	if(k||l)
		return true;
	char a[4],b[4];
	memset(a,1, sizeof(a));
	memset(b,1, sizeof(b));
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			if(!(s[i][j]==c || s[i][j]=='T')) a[j]=0;
			if(!(s[i][j]==c || s[i][j]=='T')) b[i]=0;
		}
	}
	for(i=0;i<4;i++){
		if(a[i] || b[i])
			return true;
	}
	return false;
}

int main(){
	int T;
	scanf("%d",&T);
	for(int p=1; p<=T; p++){
		printf("Case #%d: ",p);
		int i,j,k,l;
		bool isdraw=true;
		for(i=0;i<4;i++){
			scanf("%s\n",s[i]);
			for(j=0;j<4;j++){
				if(s[i][j]=='.')
					isdraw=false;
			}
//			cout << s[i] << endl;
		}
//		cout << isdraw << endl;
//		scanf("%*s\n");
		if(check('X')){
			printf("X won\n");
			continue;
		}
		if(check('O')){
			printf("O won\n");
			continue;
		}
		if(isdraw){
			printf("Draw\n");
			continue;
		}
		printf("Game has not completed\n");
	}
	return 0;
}

// <-------------------[sWitCHcAsE]---------------------->
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstdlib>
#include<cmath>
#include<cassert>
#include<vector>
#include<map>
#include<cstring>
#include<cassert>
#include<queue>

#define FOR(i,n) for(int i=0;i<n;i++)
#define FORS(i,a,n) for(int i=a;i<n;i++)
#define FORR(i,a) for(int i =a;i>=0;i--)
#define foreach(it, x) for(typeof(x.begin()) it = x.begin(); it!=x.end();it++)
#define ERR(x) cerr<<#x<<" "<<x<<endl
#define pb push_back
#define FILL(a,b) memset(a,b,sizeof(a))
using namespace std;

typedef vector<int> VI;
typedef long long ll;
typedef long double ld;

inline int print(int d) { return printf("%d",d);}
inline int read(int &d) { 
	d=0;
	int sign=1,ch;
	while((ch<'0'||ch>'9') && ch!='-' && ch!=EOF)ch=getchar_unlocked();
	if(ch=='-')
		sign=-1, ch=getchar_unlocked();
	do 
		d=(d<<3)+(d<<1)+ch-'0';
	while((ch=getchar_unlocked())>='0' && ch<='9');
	d*=sign;
	return 1;
}

int board[5][5];
int checkInComplete() {
	FOR(i,4)FOR(j,4) if ( board[i][j] == -1) return 1;
	return 0;
}
int check (int v) {
	int c=0;
	FOR(i,4) {
		c=0;
		FOR(j,4) {
			if ( board[i][j] == v || board[i][j] == 2) {
				c++;
			}
		}
		if ( c == 4) return 1;
	}

	FOR(i,4) {
		c = 0;
		FOR(j,4) {
			if ( board[j][i] == v || board[j][i] == 2) c++;
		}
		if ( c==4) return 1;
	}
	c=0;
	FOR(i,4) {
		if ( board[i][i] == v || board[i][i] ==2) c++;
	}
	if ( c==4) return 1;

	c=0;
	int r = 0;
	FORR(i,3) {
		if ( board[r][i] == v || board[r][i] == 2) c++;
		r++;
	}
	if ( c==4) return 1;


	return 0;
}

void print() {
	FOR(i,4){
		FOR(j,4)printf("%d ",board[i][j]);
		printf("\n");
	}
}

int main(int argc,char** args) 
{	
	int tc;read(tc);FOR(tests,tc) {
		cout<<"Case #"<<tests+1<<": ";
		char x[100];
		FOR(i,4) {
			scanf("%s",x);
	//		printf("%s\n",x);
			FOR(j,4) {
				if ( x[j] == 'X') board[i][j] = 1;
				else if ( x[j] == 'O') board[i][j] = 0;
				else if ( x[j] == 'T') board[i][j] = 2;
				else board[i][j] = -1;
			}
		}
		//print();
		scanf("\n");
		if ( check(0)) {
			cout<<"O won\n";
		}
		else if ( check(1)) {
			cout<<"X won\n";
		}
		else if ( checkInComplete()) {
			cout<<"Game has not completed\n";
		}	
		else cout<<"Draw\n";

	}
}

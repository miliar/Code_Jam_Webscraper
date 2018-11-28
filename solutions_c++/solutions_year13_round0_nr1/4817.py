#include<iostream>
# include <cmath>
# include <algorithm>
# include <cstdio>
# include <cstring>
# include <string>
# include <cstdlib>
# include <vector>
# include <bitset>
# include <map>
# include <queue>
# include <stack>
# include <set>
# include <list>
# include <deque>
# include <functional>
using namespace std;

#define DEBUG


#define DEB(x) cout<<#x<<"="<<x<<" "
#define DEBN(x) cout<<#x<<"="<<x<<"\n"


#ifdef DEBUG
#define D(x) DEB(x)
#define DN(x) DEBN(x)
#define DA(a,n) cout<<#a<<"=["; printarray(a,n); cout<<"]\n"
#define DAR(a,n,s) cout<<#a<<"["<<s<<"-"<<s+n-1<<"]=["; printarray(a,n,s); cout<<"]\n"
#else
#define D(x) 
#define DN(x)
#define DA(a,n) 
#define DAR(a,n,s)
#endif

#ifdef DEBUG
#define DPR(fmt, ...) \
	do { printf(fmt, ## __VA_ARGS__); } while (0)
#else
#define DPR(fmt, ...) \
	do { } while (0)
#endif

#define PR(fmt, ...) \
	do { printf(fmt, ## __VA_ARGS__); } while (0)

#define SC(fmt, ...) \
	do { scanf(fmt, ## __VA_ARGS__); } while (0)

# define mod 1000000007
# define PI 3.14159265f


#define tri pair< int,pii >
#define trl pair< long long,pll >
#define Ft first
#define St second.first
#define Tt second.second
#define mkt(a,b,c) mp(a,mp(b,c))






// Useful constants
#define INF                         (int)1e9
#define EPS		(int)1e-9

//STL containers
#define sz(a)                       ((int)(a.size()))

//fill char arrays
#define fill(a,v)                    memset(a, v, sizeof (a))

#define checkbit(n,b)                ( (n >> b) & 1)
#define DREP(a)                      sort(all(a)); a.erase(unique(all(a)),a.end())
#define INDEX(arr,ind)               (lower_bound(all(arr),ind)-arr.begin())

#define exchange(t,a,b) typeof(a) t =a; a=b; b=t
//STL output ********************************
template <typename T1, typename T2>
inline std::ostream& operator << (std::ostream& os, const std::pair<T1, T2>& p)
{
	return os << "(" << p.first << ", " << p.second << ")";
}

template<typename T>
inline std::ostream &operator << (std::ostream & os,const std::vector<T>& v)
{
	bool first = true;
	os << "[";
	for(unsigned int i = 0; i < v.size(); i++)
	{
		if(!first)
			os << ", ";
		os << v[i];
		first = false;
	}
	return os << "]";
}


	
template<typename T1, typename T2>
inline std::ostream &operator << (std::ostream & os,const std::map<T1, T2>& v)
{
	bool first = true;
	os << "[";
	for (typename std::map<T1, T2>::const_iterator ii = v.begin(); ii != v.end(); ++ii)
	{
		if(!first)
			os << ", ";
		os << *ii ;
		first = false;
	}
	return os << "]";
}
//*****************************************
//printing array
template<typename T,typename T2>
void printarray(T  a[],T2 sz,T2 beg=0)
{
	for(T2 i=beg;i<beg+sz;i++) cout<<a[i]<<" ";
}
//*********************************8

	char board[5][5];
bool iswin(char w)
{
	int i,j;
	for (i = 0; i < 4; i++) {
		for (j = 0; j < 4; j++) {
			if(board[i][j]!=w && board[i][j]!='T') break;
		}
		if (j==4) {
			return 1;
		}
	}
	for (i = 0; i < 4; i++) {
		for (j = 0; j < 4; j++) {
			if(board[j][i]!=w && board[j][i]!='T') break;
		}
		if (j==4) {
			return 1;
		}
	}

	for (i = 0; i < 4; i++) {
			if(board[i][i]!=w && board[i][i]!='T') break;
	}
		if (i==4) {
			return 1;
		}


	for (i = 0; i < 4; i++) {
			if(board[i][4-i-1]!=w && board[i][4-i-1]!='T') break;
	}
		if (i==4) {
			return 1;
		}
		return 0;
}

bool isdraw()
{
	int i,j;
	for (i = 0; i < 4; i++) {
		for (j = 0; j < 4; j++) {
			if (board[i][j]=='.') {
				return 0;
			}
		}
	}
	return 1;
}

int main()
{
	int t;
	int i,j,casen=0;
	int n,m;
	scanf("%d",&t);
	string ans;
	while(++casen<=t)
	{
		//START
		for (i = 0; i < 4; i++) {
			scanf("%s",board[i]);
			
		}
		if (iswin('X')) {
			ans="X won";
		}
		else if (iswin('O')) {
			ans= "O won";
		}
		else if (isdraw()) {
			ans= "Draw";
		}
		else {
			ans="Game has not completed";
		}

		printf("Case #%d: ",casen);
		cout<<ans;
		printf("\n");
			
	}
	return 0;
}	


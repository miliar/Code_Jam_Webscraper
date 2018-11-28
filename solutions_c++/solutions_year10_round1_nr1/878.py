#include<iostream>
#include<cstdio>
#include<queue>
#include<cstring>
#include<map>
#include<algorithm>
#include<cmath>
#include<set>
#include<sstream>
#include<map>
#include<utility>
#include<cmath>

#define S(n) scanf("%d",&n)
#define SL(n) scanf("%lld",&n)
#define SF(n) scanf("%Lf",&n)

#define REP(i,n) for(i=0; i<n; i++)
#define REPA(i,a,n) for(i=a; i<n; i++)
#define SOR(x) sort(x.begin(), x.end())
#define REV(x) reverse(x.begin(), x.end())
#define FOREACH(iter,var) for(__typeof((var).begin()) iter=(var).begin(); iter!=(var).end(); iter++)
#define PB push_back
#define VI vector<int>
#define SZ size()
#define VS vector<string>

#define MP make_pair
#define VVI vector< vector<int> >
#define INF 2000000000

#define CLR(var,val) memset(var,val,sizeof((var)))
#define S(n) scanf("%d",&n)
#define LL long long
#define LD long double
#define triple pair<int, pair<int,int> >
#define OFF 0
#define MOD
#define ISBITSET(n,i) ((n&(1<<i))>>i)
#define TOGGLEBIT(n,i) (n^(1<<i))
#define SETBIT(n,i) (n|(1<<i))
#define CLRBIT(n,i) (n & (n^(1<<i)))
#define FIN freopen("inp.in","r",stdin)
#define FOUT freopen("out.out", "w",stdout)
using namespace std;

int v[51][51];
int N, K;

bool check( string s, string k )
{
	string::size_type loc = s.find( k, 0 );
	if( loc != string::npos )
		return true;
	return false;
}

int main()
{
	FIN;
	FOUT;
	int i, j, k, T;
	bool ansR = false, ansB = false;
	cin >> T;
	VS b;	
	int caseN = 1;
	while( T-- )
	{
		ansR = ansB = false;
		b.clear();
		VI last;
		cin >> N >> K;
		REP( i, N )	{	string t;	cin >> t;	b.PB(t);	}
		last.resize(N);
		REP( i, N ) 
		{
			last[i] = 0;
			for( j = N-1; j >= 0; j-- )	if( b[i][j] == '.' )	
			{	last[i] = j;	break;	}
		}
		REP( i, N )
			for( j = last[i]-1; j >= 0; j-- )	
				if( b[i][j] != '.' )
				{	
					swap(b[i][last[i]], b[i][j]);
					last[i]--;
					j++;
				}
		
		/*cout << endl;
		REP( i, N )	cout << b[i] << endl;
		cout << endl;*/
		
		CLR( v, false );
		string checkR = "", checkB = "";
		REP( i, K ){	checkR += 'R';	checkB += 'B';	}
		REP( i, N )	
		{
			if( !ansR )	ansR = check( b[i], checkR );
			if( !ansB )	ansB = check( b[i], checkB );
			string col = "";
			REP( j, N )
				col += b[j][i];
			if( !ansR )	ansR = check( col, checkR );
			if( !ansB )	ansB = check( col, checkB );
			string diag = "";
			int c = i;
			for( j = 0; j < N - i; j++ )
				diag += b[j][c++];
			if( !ansR )	ansR = check( diag, checkR );
			if( !ansB )	ansB = check( diag, checkB );
			diag = "";	c = 0;
			for( j = i; j < N; j++ )
				diag += b[j][c++];
			if( !ansR )	ansR = check( diag, checkR );
			if( !ansB )	ansB = check( diag, checkB );
			
			diag = "";	c = i;
			for( j = 0; j < i + 1; j++ )
				diag += b[j][c--];
			if( !ansR )	ansR = check( diag, checkR );
			if( !ansB )	ansB = check( diag, checkB );
			diag = "";	c = N-1;
			for( j = i; j < N; j++ )
				diag += b[j][c--];
			if( !ansR )	ansR = check( diag, checkR );
			if( !ansB )	ansB = check( diag, checkB );
		}
		cout << "Case #" << caseN << ": "; 
		caseN++;
		if( ansR && ansB )	cout << "Both";
		else if( ansR )		cout << "Red";
		else if( ansB )		cout << "Blue";
		else 				cout << "Neither";
		cout << endl;
	}
	
}

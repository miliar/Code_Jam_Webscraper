#include <cstdio>
#include <set>
#include <cstring>
#include <string>
#include <algorithm>
using namespace std;

#define FOR(i,a,b)  for(int i=(a),_n=(b);i<=_n;i++)
#define FORD(i,a,b) for(int i=(a),_n=(b);i>=_n;i--)
#define REP(i,n) FOR(i,0,n-1)
typedef long long int64;
#define two(X) (1<<(X))
#define two64(X) (((int64)1)<<(X))
#define contain(S,x) (((S)&two(x))>0)

struct T {
	double prob;
	string fea;
	int c[2];
	int nc;
};

T tr[10005];

int ntr;
int L,A, len=0;
char str[1805];
char buf[105];
int ii;

void constructTree( int now ) {
	int nn=0;

	while ( ii<len && str[ii] != '(' ) ii++;

	tr[now].prob = 0.0;
	while ( ii<len && (str[ii]<'0' || str[ii]>'9') )
		ii++;
	int tmp=(str[ii]-'0'), p=1;

	while ( ii<len && str[ii]!='.' ) ii++;
	ii++;
	
	while ( ii<len && str[ii]>='0' && str[ii]<='9' ) {
		tmp = tmp*10 + (str[ii]-'0');
		p*=10;
		if ( p>=1000000000 ) {
			while ( ii<len && str[ii]>='0' && str[ii]<='9' ) ii++;
			break;
		}
		ii++;
	}
	
	tr[now].prob = (double)tmp/p;
	tr[now].fea = "";

	while ( ii<len ) {
		if ( str[ii]=='(' ) break;
		if ( str[ii]==')' ) break;
		if ( str[ii]>='a' && str[ii]<='z' ) {
			while ( ii<len && str[ii]>='a' && str[ii]<='z' )
				tr[now].fea += str[ii], ii++;
			break;
		}
		ii++;
	}


	while ( ii<len && str[ii]!=')' ) {
		while ( ii<len && str[ii]!=')' && str[ii]!='(' ) ii++;
		if ( str[ii]=='(' ) {
			ntr++;
			tr[now].c[tr[now].nc++]=ntr;
			constructTree(ntr);
		}
		if ( str[ii]==')' ) {
			ii++;
			break;
		}
	}
	if ( str[ii]==')' ) ii++;
}

double trav( int now, set<string> &tfea ) {
	if ( tr[now].nc==0 ) return tr[now].prob;
	if ( tfea.find(tr[now].fea)!=tfea.end() ) 
		return tr[now].prob*trav( tr[now].c[0], tfea );
	else if ( tr[now].c[1] > 0 ) 
		return tr[now].prob*trav( tr[now].c[1], tfea );
	return 1.0;
}

int main() {
	freopen( "A.in", "r", stdin );
	freopen( "A.out", "w", stdout );

	int ntc;
	scanf( "%d",&ntc );
	getchar();
	REP(tc,ntc) {
		scanf( "%d", &L );
		getchar();
		
		len = 0;
		strcpy(str,"");
		REP(i,L) {
			gets(buf);
			len += strlen(buf); 
			strcat( str, buf );
		}
		str[len]='\0';
		
		ii=0;
		ntr=1;
		REP(i,10000) {
			tr[i].nc=0;
			tr[i].c[0] = tr[i].c[1] = 0;
			tr[i].prob=1.0;
		}

		constructTree(1);

		//FOR(i,1,ntr) printf( "%lf %s %d\n", tr[i].prob, tr[i].fea.c_str(), tr[i].nc );
		//printf( "selesai\n" );
		
		printf( "Case #%d:\n", tc+1 );
		scanf( "%d", &A );
		REP(i,A) {
			char buf[15];
			scanf( "%s", buf );

			int nn;
			scanf( "%d", &nn );

			set<string> tfea;

			REP(j,nn) {
				char buf2[15];
				scanf( "%s", buf2 );
				tfea.insert( buf2 );
			}
			
			printf( "%lf\n", trav(1,tfea) );
		}
	}
	return 0;
}

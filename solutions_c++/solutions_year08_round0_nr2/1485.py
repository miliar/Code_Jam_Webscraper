// Jacek Migdal 2008-07-17
#include <cstdio>
#include <utility>
#include <queue>
#include <algorithm>
using namespace std;

int readTime() {
	static char tmp[128];
	scanf("%s", tmp);
	return ((tmp[0]-'0')*10 + (tmp[1]-'0'))*60 +
		(tmp[3]-'0')*10+(tmp[4]-'0');
}

void doIt() {
	int nA, nB;
	int turnover;

	const int MAX = 128;
	static pair<int,int> A[MAX], B[MAX];

	int resultA = 0, resultB = 0;
	scanf("%d", &turnover );
	scanf("%d %d", &nA, &nB);

	for( int i = 0 ; i<nA ; i++ ) {
		int depart = readTime();
		int arrive = readTime();
		A[i] = make_pair( depart, arrive );
	}
	
	for( int i = 0 ; i<nB ; i++ ) {
		int depart = readTime();
		int arrive = readTime();
		B[i] = make_pair( depart, arrive );
	}

	sort( A, A+nA );
	sort( B, B+nB );

	priority_queue<int, vector<int>, greater<int> > qA, qB;

	for( int itA = 0, itB = 0 ; itA<nA || itB<nB ; ) {
		bool moveA;

		if( itA>=nA ) {
			moveA = false;
		} else if( itB>=nB ) {
			moveA = true;
		} else {
			if( A[itA].first<=B[itB].first ) {
				moveA = true;
			} else {
				moveA = false;
			}
		}

		if( moveA ) {
			int now = A[itA].first;
		//	printf("moveA: now %d A[iT]=%d,%d qA: %d\n", now, A[itA].first, A[itA].second, (qA.empty()?0:qA.top()));
			if( !qA.empty() && qA.top()<=now ) {
				qA.pop();
			} else {
				resultA++;
			}
			qB.push( A[itA].second+turnover );
			itA++;
		} else {
			int now = B[itB].first;
		//	printf("moveB: now %d B[iT]=%d,%d qB: %d\n", now, B[itB].first, B[itB].second, (qB.empty()?0:qB.top()));
			if( !qB.empty() && qB.top()<=now ) {
				qB.pop();
			} else {
				resultB++;
			}
			qA.push( B[itB].second+turnover );
			itB++;
		}
	}

	
	printf( "%d %d", resultA, resultB );
}

int main() {
	int nTests;
	scanf( "%d", &nTests );
	for( int i = 1 ; i<=nTests ; i++ ) {
		printf("Case #%d: ", i );
		doIt();
		printf("\n");
	}
	return 0;
}

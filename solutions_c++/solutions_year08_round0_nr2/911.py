#include <iostream>
#include <vector>
using namespace std;
const int mn = 26 * 60;
const int mt = 23 * 60 + 59;
int na , nb , timeA[mn] , timeB[mn] , reqdA[mn] , reqdB[mn] , turn;

int main () {
	int t;
	scanf ( "%d" , &t );
	for ( int kase = 1; kase <= t; kase ++ ) {
		for ( int i=0;i<mn;i++ ) {
			timeA[i] = 0 ;timeB[i] = 0 ; reqdA[i] = 0 ; reqdB[i] = 0;
		}
		scanf ( "%d" , &turn );
		scanf ( "%d %d" , &na , &nb );
		int thr , tmin;
		for ( int i=0;i<na;i++ ) {
			scanf ( "%d:%d" , &thr , &tmin );
			reqdA[thr*60 + tmin] ++;
			scanf ( "%d:%d" , &thr , &tmin );
			timeB[ thr*60  + tmin + turn ] ++;
		}
		for ( int i=0;i<nb;i++ ) {
			scanf ( "%d:%d" , &thr , &tmin );
			reqdB[thr*60 + tmin] ++;
			scanf ( "%d:%d" , &thr , &tmin );
			timeA[thr*60  + tmin + turn ] ++;		
		}
		int cnta , cntb ;
		int resa , resb;
		cnta = 0 ; cntb = 0 ; resa = 0 ; resb = 0;
		for ( int tim = 0 ; tim <= mt ; tim ++ ) {
			cnta += timeA[tim];
			cntb += timeB[tim];	
			if ( reqdA[tim] ) {
				if ( cnta >= reqdA[tim] ) cnta -= reqdA[tim];
				else {
					resa += reqdA[tim] - cnta;
					cnta = 0;					
				}
			}
			if ( reqdB[tim] ) {
				if ( cntb >= reqdB[tim] ) cntb -= reqdB[tim];
				else {
					resb += reqdB[tim] - cntb;
					cntb = 0;					
				}
			}
		}
		cout << "Case #" << kase <<": " << resa <<" " << resb << endl;
	}
	return 0;
}

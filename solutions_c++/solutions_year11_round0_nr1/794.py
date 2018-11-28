#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;
	
int findDest(char b, int start, char *bot, int *but, int N, 
	     int &p, int &d, int &v) 
{
    int i;
    for (i = start; i<N; ++i) {
	if (bot[i] == b) {
	    d = but[i];
	    break;
	}
    }
    if (i == N) {
	v = 0;
	d = -1;
    	return -1;
    }
    if (p < d) {
	v = 1;
    } else if (p > d) {
	v = -1;
    } else v = 0;
    return d;
}

int main (void) {
    int T = 0;
    cin >> T;

    for (int c = 1; c<=T; ++c) {
	int N;
	cin >> N;
	char bot[128];
	int but[128];
	for (int i = 0; i<N; ++i) 
	    cin >> bot[i] >> but[i];
	
	int Op = 1, Ov = 0, Od = 0, Bp = 1, Bv = 0, Bd = 0;
	
	findDest('O',0,bot,but,N, Op, Od, Ov);

	findDest('B',0,bot,but,N, Bp, Bd, Bv);
	
	int time = 0;
	for (int b = 0; b<N; ++b) {
//	    cout<<"Button "<<b<<": bot "<<bot[b]<<", "<<but[b]<<endl;
//	    cout<<"  time "<<time<<": O "<<Op<<","<<Ov<<"->"<<Od
//				 <<": B "<<Bp<<","<<Bv<<"->"<<Bd<<endl;
	    if (bot[b] == 'O') {
		int t = 1;
		if (Op != but[b]) {
		    t += abs(Op-but[b]);
		    Op = but[b];
		}
		if (Bd != -1) {
		    if (t < abs(Bp-Bd)) {
			Bp += Bv*t;
		    } else {
			Bp = Bd;
			Bv = 0;
		    }
		}
		time += t;
		findDest('O',b+1,bot,but,N, Op, Od, Ov);
	    } else {
		int t = 1;
		if (Bp != but[b]) {
		    t += abs(Bp-but[b]);
		    Bp = but[b];
		}
		if (Od != -1) {
		    if (t < abs(Op-Od)) {
		        Op += Ov*t;
		    } else {
		        Op = Od;
		        Ov = 0;
		    }
		}
		time += t;
		findDest('B',b+1,bot,but,N, Bp, Bd, Bv);
	    }
	}
	cout<<"Case #"<<c<<": "<<time<<endl;
    }

    return 0;
}

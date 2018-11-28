/*
	http://code.google.com/codejam/contest/1460488/dashboard#s=p1
*/
#include <iostream>

#define min(a, b) ((a>b)?b:a)
	
using namespace std;

int main()
{
	int T, N, S, p;
	int *t;
	
	cin >> T;
	
	for (int i = 0; i < T; i++) {
		int boundary;
		int nUpper = 0;
		int nStar = 0;
		
		cin >> N;	// # of googlers
		cin >> S;	// # of surprising triplets of scores
		cin >> p;
		
		t = new int[N];
		boundary = (p - 1) * 3;
				
		for (int j = 0; j < N; j++) {
			cin >> t[j];
			
			if (t[j] > boundary)
				nUpper++;
			else if (t[j] >= boundary -1) {
				if (t[j] >= 2)	
					nStar++;
			}
		}
		
		//cout << "nUpper: " << nUpper << " nStar: " << nStar << endl;
		
		cout << "Case #" << (i+1) << ": " << nUpper + min(nStar, S) << endl;
		
		
		delete t;
	}
	
	return 0;	
}

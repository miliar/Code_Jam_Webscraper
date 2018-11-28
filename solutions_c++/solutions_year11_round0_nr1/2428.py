#include <iostream>

using namespace std;

int main(){
	int n, ni, c, l, i, p, j;
	int p1, p2, q1, q2;
	char t;
	
	cin >> n;

	for (ni = 1; ni <= n; ni++){
		cin >> c;
		p1 = 1; p2 = 1;
		q1 = 0; q2 = 0;
		
		for (i = 0; i < c; i++){
			cin >> t;
			cin >> l;
			if (t == 'B'){
				int d = p1 - l;
				d = (d>0) ? d : -d;
				q1 += d+1;
				if (q1 <= q2) q1 = q2+1;
				p1 = l;
			}else if (t == 'O'){
				int d = p2 - l;
				d = (d>0) ? d : -d;
				q2 += d+1;
				if (q2 <= q1) q2 = q1+1;
				p2 = l;
			}
		}
		cout << "Case #" << ni << ": " << (q2 > q1 ? q2 : q1) << endl;
	}
}

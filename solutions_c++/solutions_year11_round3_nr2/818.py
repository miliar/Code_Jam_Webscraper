#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main (int argc, char * const argv[]) {
    //ifstream in("..//..//sample.in.txt");
	ifstream in("..//..//B-small-attempt0.in.txt");
	if (!in)
	{
		cout << "Input file cannot be opened";
		return 1;
	}
	
	ofstream out("output.txt");
	if (!out) {
		cout << "Output file cannot be opened";
		in.close();
		return 1;
	}
	
	int T;
	in >> T;
	
	for (int tt = 0; tt < T; tt++) {
		long L, t, N, C;
		in >> L >> t >> N >> C;
		
		long a[C];
		long s[N];
		for (int c = 0; c < C; c++) {
			in >> a[c];
			s[c] = 0;
		}
		
		long totalTime = 0;
		int n = 0;
		for (int c = 0; n < N; c++) {
			if (c == C)
				c = 0;
			
			if ((totalTime + a[c] * 2) > t) {
				if (totalTime < t)
				{
					s[n] = (a[c] * 2 - (t - totalTime)) / 2;	
				}
				else {
					// time saving is possible
					s[n] = a[c];	
				}
			}
			
			totalTime += a[c] * 2;
			n++;
		}
		
		vector<int> savings(s, s + N);
		sort(savings.begin(), savings.end());
		reverse(savings.begin(), savings.end());
//		for (int i = 0; i < N; i++) {
//			cout << savings[i] << " ";
//		}
//		cout << endl;
		
		for (int l = 0; l < L && l < N; l++) {
			totalTime -= savings[l];
		}
		
		out << "Case #" << (tt + 1) << ": " << totalTime << endl;
	}
	
	in.close();
	out.close();
	
    return 0;
}

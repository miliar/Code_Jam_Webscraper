#include <iostream>

using namespace std;

/*
3
4 6 4
1 4 2 1
100 10 1
1
5 5 10
2 4 2 3 4 2 1 2 1 3
*/
//#define __TEST

/*
long long bf(int R, int K, int N, int *g) {
	int num = 0;
	long long sum = 0;
	long long ret = 0;
	int idx = 0;
	int end = 0;
	
	//cout << "R: " << R << " K: " << K << " N: " << N << endl;
	//for (int i = 0; i < N; i++) 
	//	cout << "g[" << i << "]: " << g[i] << endl;
	
	while(end < R) {		
		if (num >= N || (sum + g[idx]) > K) {
		//	cout << "sum: " << sum << endl;
			ret += sum;
			sum = 0;
			num = 0;
			end++;
		} else {
			sum += g[idx];
			idx = (idx + 1) % N;
			num++;
		}
	}

	return ret;
}

void testset() {
	int T = 50;
	int R = 100000000;
	int K = rand() % 1000000000;
	int N = 1000;
	
	cout << T << endl;
	for (int i = 0; i < T; i++) {
		cout <<	R << " " << K << " " << N << endl;
		for (int j = 0; j < N; j++) {
			cout << rand() % 10000000 << " ";
		}
		cout << endl;
	}
}
*/


int main() {
	
//	testset();
/*
	int *ss, **ssp;
	ss = new int[1000];
	ssp = new int*[1000];
	for (int i = 0; i < 1000; i++) {
		ssp[i] = new int[1000];	
	}
	
	for (int i = 0; i < 1000; i++) {
		ss[i] += rand() % 100000000;		
	}

	for (int i = 0; i < 1000; i++) {
		for (int j = 0; j < 1000; j++) {
			if (i == j) {
				ssp[i][j] = (i > 0) ? ss[i] - ss[i-1] : ss[i];
			} else if (i > j) {
				ssp[i][j] = (i > 0) ? ss[j] - ss[i-1] : ss[j];
			} else {
				ssp[i][j] = (i-1>=j+1) ? ss[999] - ssp[i-1][j+1] : ss[999];
			}
		}
	}
	
	delete[] ss;
	for (int i = 0; i < 1000; i++) {
		delete ssp[i];
	}
	delete[] ssp;
*/	


	//return 0;
	
	long long  T, R, K, N;
	long long  *g, *e;
	long long *s;

	cin >> T;
	
	//cout << "T: " << T << endl;
	
	for (int i = 0; i < T; i++) {
		cin >> R;	// # of rounds
		cin >> K;	// capacity of roller coster
		cin >> N; // # of groups

#ifdef __TEST
		cout << "R: " << R << " K: " << K << " N: " << N << endl;
#endif
		
		g = new long long [N];
		e = new long long [N];
		s = new long long[N];

		
#ifdef __TEST
		cout << "Group:: ";
#endif
		for (int j = 0; j < N; j++) {
			cin >> g[j];
#ifdef __TEST	
			cout << g[j] << " ";
#endif
			e[j] = -1;
			s[j] = 0;
		}
#ifdef __TEST
		cout << endl;
#endif
		
		long long sum = 0;	// subsum
		long long  idx = 0;	// index
		long long  eidx = 0; 	// index for e
		
		e[0] = 0;	// eidx
		
		long long  first = -1;
		long long  gap;
		long long  start = 0;
		
		long long  num = 0;
		while (true) {
			if (num >= N || sum + g[idx] > K) {	// store current subset
				s[eidx] = (eidx >= 1) ? sum + s[eidx-1] : sum;

#ifdef __TEST
				cout << "s[" << eidx << "]: " << s[eidx] << " sum: " << sum << " next idx: " << idx << " eidx: " << eidx << endl;
#endif			

				sum = 0;
				num = 0;	
				if (e[idx] >= 0) {	// already exists
			//		cout << "NOW DUPLICATE idx: " << idx << " e[idx]: " << e[idx] << endl;
					first = e[idx];
					gap = eidx - first;

#ifdef __TEST
					cout << "first: " << first << " gap: " << gap << endl;
#endif

					break;
				} else {
					e[start] = eidx;
				}
				eidx++;
				start = idx;
			} else {
				sum += g[idx];
				num++;
				idx = (idx + 1) % N;
			}
		}

#ifdef __TEST		
		cout << "s: ";
		for (int j = 0; j < N; j++) {
			cout << s[j] << " ";
		}
		cout << endl;
		cout << "first: " << first << " gap: " << gap << endl;
#endif
		
		long long ret;
		if (R-1 < first)
			ret = s[R-1];
		else {
			if (gap == 0)
				ret = s[first] * (long long)R;
			else {
				long long tominus = 0;
				long long total = s[eidx];
				
				if (first >= 1)
					tominus = s[first-1];
			/*
				if (first == -1) {
					int tmp = (int)(R - 1);
					ret = ((int)tmp / (int)gap) * (s[eidx]) + s[(tmp % gap)];
				} else {
			*/
					long long tmp = (long long)(R - first);	// items in loop
#ifdef __TEST
					cout << "tominus: " << tominus << endl;
					cout << " tmp: " << tmp;
					cout << " tmp/(gap+1): " << (long long)tmp / ((long long)gap+1) << endl;
					cout << " total - tominus: " << total - tominus;
					cout << " (tmp % (gap+1)): " << (tmp % (gap + 1)) << " s[(tmp % (gap+1))+first]: " << s[(tmp % (gap + 1))];
					cout << " gap: " << gap << endl;
#endif
					ret = tominus;
					ret += ((long long)tmp / (long long)(gap+1)) * ((long long)total - (long long)tominus);
					if (tmp % (gap+1) != 0)
						ret += s[(tmp % (gap+1))+first-1] - tominus;
			}
			cout.flush();			
		}
		
		//int bff = bf(R, K, N, g);
		//int bff = 0;
		//cout << "Case #" << (i+1) << ": " << bff << endl;
		
		cout << "Case #" << (i+1) << ": " << ret << endl; // " bff: " << bff << endl;
		/*
		if (bff != ret)
			cout << "up BREAK!!!!!!!!!!" << endl;
		*/
		
		delete[] g;
		delete[] e;
		delete[] s;
	}
	return 0;
}

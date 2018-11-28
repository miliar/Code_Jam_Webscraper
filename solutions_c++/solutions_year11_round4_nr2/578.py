#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>

using namespace std;

typedef long long int datum;

datum get(vector<vector<datum> >& data, int row, int col) {
	if(row<0 || col<0) { return 0; }
	return data[row][col];
}

datum gott(vector<vector<datum> >& data, int row, int col, int rrow, int ccol) {
	return get(data, rrow, ccol) - get(data, rrow, col-1) - get(data, row-1, ccol) + get(data, row-1, col-1);
}

int main(void) {
	int Kase;
	cin >> Kase;
	for(int kase = 0; kase < Kase; ++kase) {
		datum R, C, D;
		cin >> R >> C >> D;
		
		vector<string> data;
		for(int r = 0; r < R; ++r) {
			string s; cin >> s;
			data.push_back(s);
		}
		vector<vector<datum> > master;
		vector<vector<datum> > master_r;
		vector<vector<datum> > master_c;
		for(int r = 0; r < R; ++r) {
			datum sum = 0;
			datum sum_r = 0;
			datum sum_c = 0;
			vector<datum> hap;
			vector<datum> hap_r;
			vector<datum> hap_c;

			for(int c = 0; c < C; ++c) {
				int value = data[r][c];
				sum += value;
				sum_r += value * (r+1);
				sum_c += value * (c+1);
				hap.push_back(sum + get(master, r-1, c));
				hap_r.push_back(sum_r + get(master_r, r-1, c));
				hap_c.push_back(sum_c + get(master_c, r-1, c));
			}
			master.push_back(hap);
			master_r.push_back(hap_r);
			master_c.push_back(hap_c);
		}
		if(false) {
			for(int r = 0; r < R; ++r) {
				for(int c = 0; c < C; ++c) {
					cerr << master[r][c] << " ";
				}
				cerr << endl;
			}
			cerr << endl;
		}
		int soln = 0;
		for(datum k = min(R, C); k >= 3; --k) {
			for(datum r = 0; r+k-1 < R; ++r) {
				for(datum c = 0; c+k-1 < C; ++c) {
					datum sum = gott(master, r, c, r+k-1, c+k-1);
					datum sum_r = gott(master_r, r, c, r+k-1, c+k-1);
					datum sum_c = gott(master_c, r, c, r+k-1, c+k-1);
					datum got = ((datum)data[r][c] + (datum)data[r][c+k-1] + (datum)data[r+k-1][c] + (datum)data[r+k-1][c+k-1]);
					datum got_r = ((datum)data[r][c]*(r+1) + (datum)data[r][c+k-1]*(r+1) + (datum)data[r+k-1][c]*(r+k) + (datum)data[r+k-1][c+k-1]*(r+k));
					datum got_c = ((datum)data[r][c]*(c+1) + (datum)data[r][c+k-1]*(c+k) + (datum)data[r+k-1][c]*(c+1) + (datum)data[r+k-1][c+k-1]*(c+k));

					sum -= got;
					sum_r -= got_r;
					sum_c -= got_c;

					sum_r *= 2;
					sum_c *= 2;
					datum so_r = ((r+1) + (r+k)) * sum;
					datum so_c = ((c+1) + (c+k)) * sum;
					if(false && k == 3) {
						cerr << r << " " << c << " " << sum_r << " " << so_r << " " << sum_c << " " << so_c << endl;
					}
					if(sum_r == so_r && sum_c == so_c) {
						soln = k;
						break;
					}
				}
				if(soln) { break; }
			}
			if(soln) { break; }
		}
		cout << "Case #" << (kase + 1) << ": ";
		if(!soln) {
			cout << "IMPOSSIBLE";
		}
		else {
			cout << soln;
		}
		cout << endl;
	}
	return 0;
}

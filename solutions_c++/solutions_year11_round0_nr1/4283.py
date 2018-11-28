#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

struct seq_element {
	string robot;
	int pos;
};

int main() {
	ios_base::sync_with_stdio(false);
	int case_nr, T;

	cin >> T;

	for (case_nr=1; case_nr<=T; case_nr++) {
		cout << "Case #" << case_nr << ": ";

		int N, O=1, B=1, time=0, b_ptr=0, o_ptr=0;
		string robot;

		cin >> N;

		vector<seq_element> sequence(N);
		vector<int> b_seq, o_seq;

		for (int i=0; i<N; i++) {
			cin >> sequence[i].robot >> sequence[i].pos;
			if (sequence[i].robot[0]=='O')
				o_seq.push_back(sequence[i].pos);
			else
				b_seq.push_back(sequence[i].pos);
		}
		o_seq.push_back(-1);
		b_seq.push_back(-1);

		for (int i=0; i<N; i++) {
			int pos;

			if (sequence[i].robot[0]=='O') {
				int step=abs(sequence[i].pos-O)+1;
				O=sequence[i].pos;
				o_ptr++;
				if (B-b_seq[b_ptr] > 0) {
					B-=min(abs(B-b_seq[b_ptr]), step);
				} else {
					B+=min(abs(B-b_seq[b_ptr]), step);
				}
				time+=step;
			} else {
				int step=abs(sequence[i].pos-B)+1;
				B=sequence[i].pos;
				b_ptr++;
				if (O-o_seq[o_ptr] > 0) {
					O-=min(abs(O-o_seq[o_ptr]), step);
				} else {
					O+=min(abs(O-o_seq[o_ptr]), step);
				}
				time+=step;
			}
		}

		cout << time << endl;
	}
}

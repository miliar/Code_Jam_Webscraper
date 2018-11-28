#include <iostream>
#include <vector>
using namespace std;

int func(int x, vector <int> &v) {
	for (int i=0;i<v.size();i++) if (v[i] >= x) return i;
	return INT_MAX;
}

int main(void) {
	int N,T,NA,NB,acnt,bcnt;
	string D,A;
	cin >> N;
	for (int testcase=0;testcase<N;testcase++) {
		cin >> T >> NA >> NB;
		vector <int> ad,bd,aa,ba;
		for (int aaa=0;aaa<NA;aaa++) {
			cin >> D >> A;
			ad.push_back((D[0]-'0')*600+(D[1]-'0')*60+(D[3]-'0')*10+D[4]-'0');
			ba.push_back((A[0]-'0')*600+(A[1]-'0')*60+(A[3]-'0')*10+A[4]-'0');
		}
		for (int bbb=0;bbb<NB;bbb++) {
			cin >> D >> A;
			bd.push_back((D[0]-'0')*600+(D[1]-'0')*60+(D[3]-'0')*10+D[4]-'0');
			aa.push_back((A[0]-'0')*600+(A[1]-'0')*60+(A[3]-'0')*10+A[4]-'0');
		}
		
		sort(ad.begin(),ad.end());
		sort(bd.begin(),bd.end());
		sort(aa.begin(),aa.end());
		sort(ba.begin(),ba.end());
		
		vector <int> achk(ad.size(),0), bchk(bd.size(),0);
		
		for (int i=0;i<aa.size();i++) {
			for (int p=func(aa[i]+T,ad);p<ad.size();p++) {
				if (!achk[p]) {
					achk[p] = 1;
					break;
				}
			}
		}
		for (int i=0;i<ba.size();i++) {
			for (int p=func(ba[i]+T,bd);p<bd.size();p++) {
				if (!bchk[p]) {
					bchk[p] = 1;
					break;
				}
			}
		}
		
		acnt = bcnt = 0;
		for (int i=0;i<achk.size();i++) if (!achk[i]) acnt++;
		for (int i=0;i<bchk.size();i++) if (!bchk[i]) bcnt++;
		cout << "Case #" << testcase+1 << ": " << acnt << " " << bcnt << endl;
	}
}

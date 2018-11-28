#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

#define REP(a,b) for (int a=0; a<b; ++a)

int m[128][300];
int D, I, M;
int num[128];

int go(int pos, int val) 
{
	if (pos == 0) {
		return min(abs(val-num[pos]),D);
	} else {
		if (m[pos][val] < 0) {
			m[pos][val] = 1<<30;
			//REP(i,256) m[pos][val] = min(m[pos][val], D + go(pos-1, i));
			m[pos][val] = D + go(pos-1,val);
			REP(i,256) {
				if (M != 0) 
					m[pos][val] = min(m[pos][val], go(pos-1,i)+abs(val-num[pos])+I*(max(0,(abs(val-i)-1))/M));
				else {
					if (val != i) continue;
					m[pos][val] = min(m[pos][val], go(pos-1,i)+abs(val-num[pos]));
				}
			}
		}
		return m[pos][val];
	}

}

int main() 
{
	ifstream fin("b.in");
	ofstream fout("b.out");

	int tc, n;
	
	fin >> tc;

	REP(t,tc) {
		fin >> D >> I >> M >> n;
		REP(i,n) fin >> num[i];

		memset(m, -1, sizeof(m));
		int res = 1<<30;

		REP(i,256) {
			res = min(res,go(n-1,i));
			//cout << i << " " << res << endl;
		}

		fout << "Case #" << t+1 << ": " << res << endl;
	}



	fout.close();

	return 0;
}
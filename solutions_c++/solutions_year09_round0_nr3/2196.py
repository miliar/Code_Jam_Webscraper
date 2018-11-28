#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <stack>
#include <queue>
#include <complex>
#include <set>
#include <list>
#include <iomanip>



using namespace std;
#define FOR(i,n) for(int i=0;i<(int)n;++i)
#define FORI(p, x) for (int i = p; i < (int)(x); ++i)
#define FORJ(p, x) for (int j = p; j < (int)(x); ++j)
#define FORK(p, x) for (int k = p; k < (int)(x); ++k)

#define MOD 1000000000

// BEGIN CUT HERE
int main() {
//	ifstream cin("in.txt");
//	ifstream cin("C-small-attempt0.in");
	fstream cin("C-large.in");
	ofstream cout("out.txt");
	
	int N;
	cin>>N;cin.ignore();
	
	FORI(0,N){
		string s;
		//cin>>s;
		getline(cin,s);
		vector<int> cnt(19);
		FORJ(0,s.size()){
			char cur=s[j];
			switch(cur){
				case 'w':
					cnt[0]++;
					break;
				case 'e':
					cnt[1]+=cnt[0];cnt[1]%=MOD;
					cnt[6]+=cnt[5];cnt[6]%=MOD;
					cnt[14]+=cnt[13];cnt[14]%=MOD;
					break;
				case 'l':
					cnt[2]+=cnt[1];cnt[2]%=MOD;
					break;
				case 'c':
					cnt[3]+=cnt[2];cnt[3]%=MOD;
					cnt[11]+=cnt[10];cnt[11]%=MOD;
					break;
				case 'o':
					cnt[4]+=cnt[3];cnt[4]%=MOD;
					cnt[9]+=cnt[8];cnt[9]%=MOD;
					cnt[12]+=cnt[11];cnt[12]%=MOD;
					break;
				case 'm':
					cnt[5]+=cnt[4];cnt[5]%=MOD;
					cnt[18]+=cnt[17];cnt[18]%=MOD;
					break;
				case ' ':
					cnt[7]+=cnt[6];cnt[7]%=MOD;
					cnt[10]+=cnt[9];cnt[10]%=MOD;
					cnt[15]+=cnt[14];cnt[15]%=MOD;
					break;
				case 't':
					cnt[8]+=cnt[7];cnt[8]%=MOD;
					break;
				case 'd':
					cnt[13]+=cnt[12];cnt[13]%=MOD;
					break;
				case 'j':
					cnt[16]+=cnt[15];cnt[16]%=MOD;
					break;
				case 'a':
					cnt[17]+=cnt[16];cnt[17]%=MOD;
					break;
			}

		}
		char ans[36];
		cnt[18]=cnt[18]%10000;
		sprintf(ans,"%04d", cnt[18]);
		cout << "Case #" << i+1 <<": " << ans << endl;


	}
	
		
	
	return 0;
}
// END CUT HERE

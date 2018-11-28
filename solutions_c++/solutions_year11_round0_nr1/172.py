// C++0x (GCC 4.6.1 20110325 (prerelease), -std=c++0x option)
#include <iostream>
#include <iomanip>
#include <vector>
#include <array>
#include <unordered_map>
#include <unordered_set>
#include <tuple>
#include <functional>
#include <cassert>

using namespace std;

int main() {
	int T; cin >> T;
	for(int K=1;K<=T;K++) {
		int N; cin >> N;
		vector<char> who(N);
		vector<int> blue,orange;
		for(int i=0;i<N;i++) {
			int id;
			cin >> who[i] >> id;
			if(who[i]=='B')
				blue.push_back(id);
			else
				orange.push_back(id);
		}
		blue.push_back(1);
		orange.push_back(1);
		int bPos=1,oPos=1;
		int bBtn=0,oBtn=0,btn=0;
		int t=0;
		while(btn<who.size()) {
			int btn2=btn;
			if(who[btn]=='B' && bPos==blue[bBtn]) {
				bBtn++;
				btn2++;
			} else if(bPos<blue[bBtn])
				bPos++;
			else if(bPos>blue[bBtn])
				bPos--;
			if(who[btn]=='O' && oPos==orange[oBtn]) {
				oBtn++;
				btn2++;
			} else if(oPos<orange[oBtn])
				oPos++;
			else if(oPos>orange[oBtn])
				oPos--;
			btn=btn2;
			t++;
		}
		cout << "Case #" << K << ": " << t << endl;
		cout.flush();
	}
	
	return 0;
}
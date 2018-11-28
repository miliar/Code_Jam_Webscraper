//#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>
using namespace std;
ifstream cin("A-large.in");
ofstream cout("A-large.out");
int main(){
int T;
cin >> T;
for (int i=1; i<=T; i++) {
int N;
cin >> N;
vector<pair<int,int> > steps;
vector<int> steps0;
vector<int > steps1; 
int turn = 0;
for (int j=0; j<N; j++) {
	char R;
	int P;
	cin >> R >> P;
	if (R=='O') { steps.push_back(make_pair(0,P)); steps0.push_back(P); } else { steps.push_back(make_pair(1,P)); steps1.push_back(P); }
}
int isat0 = 1;
int isat1 = 1;
int bg0 = 0;
int bg1= 0;
int res = 0;
int curres = 0;
for (int j=0; j<steps.size(); j++) {
	if (steps[j].first == 0) {
		curres = abs(steps[j].second-isat0)+1;
		res += curres;
		isat0 = steps[j].second;
		bg0++;
		if (bg1 < steps1.size()) { if (abs(steps1[bg1]-isat1)<=curres) isat1 = steps1[bg1]; else if (steps1[bg1] > isat1) isat1 +=curres; else isat1-=curres; }
	} else {
		curres = abs(steps[j].second-isat1)+1;
                res += curres;
                isat1 = steps[j].second;
                bg1++;
                if (bg0 < steps0.size()) { if (abs(steps0[bg0]-isat0)<=curres) isat0 = steps0[bg0]; else if (steps0[bg0] > isat0) isat0 +=curres; else isat0-=curres; }
	}
}
cout << "Case #"<<i<<": "<<res<<endl;
}
return 0;
}

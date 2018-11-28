
#include <cstdio>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <queue>
#include <set>
#include <cstring>
#include <sstream>
#include <cassert>
#include <map>
#include <stack>

#define FOR(I,A,B) for(int I=(A);I<(B);I++)
#define REP(I,N) FOR(I,0,N)
#define ALL(A) (A).begin(),(A).end()

#define SQR(x) ((x)*(x))
#define PB(x) push_back(x)

#define PI (acos(-1.0))

using namespace std;

typedef vector<int> VI;
typedef vector< vector<int> > VVI;

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int testcase;
	cin >> testcase;
	for(int tc=1;tc<=testcase;tc++) {
		int C,D,N;
		vector<string> combines;
		vector<string> opposed;
		cin >> C;
		REP(i,C) {
			string temp;
			cin >> temp;
			combines.PB(temp);
			reverse(temp.begin(),temp.begin()+2);
			combines.PB(temp);
		}
		cin >>D;
		REP(i,D) {
			string temp;
			cin >> temp;
			opposed.PB(temp);
			reverse(ALL(temp));
			opposed.PB(temp);
		}
		cin >>N;
		
		string base;
		cin >> base;
		string element;
		REP(i,N) {
			element += base[i];
			REP(j,combines.size()) {
				if(element.length() < 2) continue;
				if(element.substr(element.length()-2,2)==combines[j].substr(0,2)) {
					element = element.substr(0,element.length()-2) + combines[j][2];
					break;
				}
			}
			REP(j,opposed.size()) {
				if(element.length() < 2) continue;
				if(element[element.length()-1] == opposed[j][0])
				if(element.find(opposed[j][1]) != string::npos) {
					element = "";
					break;
				}
			}
		}
		string result;
		result += "[";
		REP(i,element.length()) {
			result += element[i];
			if(i==element.length()-1) break;
			result += ", ";
		}
		result += "]";
		printf("Case #%d: %s\n",tc,result.c_str());
	}
}

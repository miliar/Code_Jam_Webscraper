#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>

using namespace std;

int main(void) {
	int T;
	int W;
	int NA, NB;
	int ar, de;
	int resa;
	int resb;
	int dir;
	int C = 1;
	vector< pair<int,int> > A;
	vector< pair<int,int> > B;
	priority_queue<int, vector<int>, greater<int> > TA;
	priority_queue<int, vector<int>, greater<int> > TB;
	scanf("%d", &T);
	string str;
	while(T--) {
		resa = 0;
		resb = 0;
		A.clear();
		B.clear();
		while(!TA.empty()) TA.pop();
		while(!TB.empty()) TB.pop();
		scanf("%d", &W);
		scanf("%d", &NA);
		scanf("%d\n", &NB);
		for(int i = 0; i < NA; ++i) {
			getline(cin, str);		
			de = (str[0]-'0') * 600 + (str[1]-'0') * 60 + (str[3]-'0') * 10 + (str[4]-'0');
			ar = (str[6]-'0') * 600 + (str[7]-'0') * 60 + (str[9]-'0') * 10 + (str[10]-'0') + W;
			A.push_back(make_pair(de,ar));
		}
		sort(A.begin(), A.end());
		reverse(A.begin(), A.end());
		for(int i = 0; i < NB; ++i) {
			getline(cin, str);		
			de = (str[0]-'0') * 600 + (str[1]-'0') * 60 + (str[3]-'0') * 10 + (str[4]-'0');
			ar = (str[6]-'0') * 600 + (str[7]-'0') * 60 + (str[9]-'0') * 10 + (str[10]-'0') + W;
			B.push_back(make_pair(de,ar));
		}		
		sort(B.begin(), B.end());
		reverse(B.begin(), B.end());
		while(!A.empty() || !B.empty()) {
			if(A.empty()) {
				de = B.back().first;
				ar = B.back().second;
				dir = -1;
			}
			else if(B.empty()) {
				de = A.back().first;
				ar = A.back().second;
				dir = 1;
			}
			else if(A.back() > B.back()) {
				de = B.back().first;
				ar = B.back().second;
				dir = -1;
			}
			else {
				de = A.back().first;
				ar = A.back().second;
				dir = 1;
			}
			if(dir == -1) {
				B.pop_back();
				if(!TB.empty() && TB.top() <= de) {
					TB.pop();
				}
				else {
					resb++;
				}
				//printf("pushing %d in TA\n", ar);
				TA.push(ar);
			}
			else {
				A.pop_back();
				if(!TA.empty() && TA.top() <= de) {
					TA.pop();
				}
				else {
					resa++;
				}
				//printf("pushing %d in TB\n", ar);
				TB.push(ar);
			}
		}
		printf("Case #%d: %d %d\n", C, resa, resb);
		C++;
	}
	return 0;
}

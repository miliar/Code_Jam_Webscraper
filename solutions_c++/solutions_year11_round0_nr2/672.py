#include <iostream>
#include <vector>
#include <deque>
using namespace std;

vector<pair<pair<char, char>, char> > com;
vector<pair<char, char> > opp;
vector<char> s;
deque<char> ans;

char findCom(char a, char b){
	for (int i = 0; i < com.size(); i++)
		if ((com[i].first.first == a && com[i].first.second == b) ||
			(com[i].first.second == a && com[i].first.first == b))
				return com[i].second;
	return '#';
}

bool findOpp(char a, char b){
	for (int i = 0; i < opp.size(); i++)
		if ((opp[i].first == a && opp[i].second == b) ||
			(opp[i].first == b && opp[i].second == a))
				return true;
	return false;
}

int main(){
	int T, n, c, d;
	cin >> T;
	char a, b, m;
	string S = "QWERASDF";
	
	for (int C = 1; C <= T; C++){
		com.clear(), opp.clear(), s.clear(), ans.clear();
		
		cin >> c;
		for (int i = 0; i < c; i++){
			cin >> a >> b >> m;
			com.push_back(make_pair(make_pair(a, b), m));			
		}
		
		cin >> d;
		for (int i = 0; i < d; i++){
			cin >> a >> b;
			opp.push_back(make_pair(a, b));
		}
		
		cin >> n;
		for (int i = 0; i < n; i++){
			cin >> a;
			s.push_back(a);
		}
		
		int t = 0;
		char tC;
		while (t != s.size()){
			ans.push_back(s[t]);
			if (ans.size() >= 2){
				if ((tC = findCom(ans[ans.size() - 1], ans[ans.size() - 2])) != '#'){
					ans.pop_back();
					ans.pop_back();
					ans.push_back(tC);
				}
				
				for (int i = ans.size() - 2; i >= 0; i--)
					if (S.find(ans[i]) != string::npos){
						if (findOpp(ans[i], ans[ans.size() - 1])){
							ans.clear();
							break;
						}
					}
			}
			/*for (int i = 0; i < ans.size(); i++){
				printf("%c", ans[i]);
			}
			cout << endl;*/
			t++;
		}
		printf("Case #%d: [", C);
		for (int i = 0; i < ans.size(); i++){
			if (i)
				printf(", ");
			printf("%c", ans[i]);
		}
		printf("]\n");
	}
	return 0;
}

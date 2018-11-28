#include <iostream>
#include <string>
#define REP(i,n) for(int i = 0; i < n; i++)
using namespace std;

string s = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjvz";
string p = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveupq";

int mp[500];
int main() {
	memset(mp, -1, sizeof(mp));
	REP(i,s.size()) {
		mp[s[i]] = p[i];
	}
	mp[' '] = ' ';
	string line;

	int n;
	cin >> n;
	getline(cin, line);
	REP(i,n) {
		getline(cin, line);
		REP(j,line.size()) {
        	if(mp[line[j]] != -1) {
				line[j] = mp[line[j]];
			}
			else line[j] = '_';
		}
		cout << "Case #" << i+1 << ": " << line << endl;
	}
}
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>

using namespace std;
#define FOR(i,a,n) for(int i = a; i < n; i++)
#define REP(i,n) FOR(i,0,n)
#define pb push_back


int main() {
	int n;
	cin >> n;
	REP(i,n) {
		int opp[26][26], like[26][26];
		REP(j,26) REP(k,26) opp[k][j] = like[k][j] = 0;
		int m;
		cin >> m;
		REP(j,m) {
			char buf[3];
			scanf("%s", buf);
			like[buf[0]-'A'][buf[1]-'A'] = buf[2]-'A';
			like[buf[1]-'A'][buf[0]-'A'] = buf[2]-'A';	
		}
		
		cin >> m;
		REP(j,m) {
			char buf[2];
			scanf("%s", buf);
			opp[buf[0]-'A'][buf[1]-'A'] = opp[buf[1]-'A'][buf[0]-'A'] = 1;		
		}
		
		cin >> m;
		int st[101], cnt=0;
		REP(j,m) {
			char c;
			cin >> c;

			int val = c-'A';
			st[cnt++] = val;
			while(1) {
				if(cnt-2 >= 0 && like[st[cnt-1]][st[cnt-2]]) {			
					st[cnt-2] = like[st[cnt-1]][st[cnt-2]];
					cnt--;
				}
				else {
					break;
				}
			}			
			
			for(int k = cnt-2; k >= 0; k--) {
				if(opp[st[k]][st[cnt-1]]) {
					cnt = 0;
					break;
				}
			}
	//		REP(k,cnt) cout << (char)('A'+st[k]) <<" "; cout << endl;
			
			
		}
	
		cout << "Case #" << i+1 <<": [";
		REP(j,cnt) {
			cout << (char)('A'+st[j]);
			if(j < cnt-1) cout << ", ";
		}
		cout << "]\n";
		
	}
}			

		
		


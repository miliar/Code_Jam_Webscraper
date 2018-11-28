#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int n, m;
int h[1000], w[1000];
int qh[1000], qw[1000];
bool b[1000];

void input() {
	cin >> n;
	for(int i=0;i<n;i++) {
		cin >> h[i] >> w[i];
		//cout << h[i] << endl;
		string tc;
		cin >> tc;
		//cout << tc << endl;
		b[i] = (tc == "BIRD");
		if(tc == "NOT")
			cin >> tc;
	}
	cin >> m;
	for(int i=0;i<m;i++)
		cin >> qh[i] >> qw[i];		
}

int ahn;
int ah[1000];
int awn;
int aw[1000];

int r[1000];

int main() {
	freopen("Input.txt","r",stdin);
	int casen;
	cin >> casen;
	for(int casei=1;casei<=casen;casei++) {
		input();
		
		
		
		ahn = 0;
		awn = 0;
		for(int i=0;i<n;i++) {
			if(b[i]) {
				ah[ahn++] = h[i];
				aw[awn++] = w[i];
			} else {
				ah[ahn++] = h[i]-1;
				aw[awn++] = w[i]-1;
				ah[ahn++] = h[i]+1;
				aw[awn++] = w[i]+1;
			}
		}
		ah[ahn++] = 0;
		ah[ahn++] = 10000000;
		aw[awn++] = 0;
		aw[awn++] = 10000000;
		sort(ah, ah + ahn);
		sort(aw, aw+ awn);
		ahn = unique(ah, ah+ahn) - ah;
		awn = unique(aw, aw+awn) - aw;
		
		cout << "Case #" << casei << ": " << endl;

		//cout << m << endl;
		for(int i=0;i<m;i++) {
			int scnt = 0;
			int fcnt = 0;
			for(int j=0;j<ahn;j++)
				for(int k=j;k<ahn;k++)
					for(int q=0;q<awn;q++)
						for(int r=q;r<awn;r++) {
							bool suc = true;
							for(int s=0;s<n;s++) {
								bool f1 = ah[j] <= h[s] && h[s] <= ah[k];				
								bool f2 = aw[q] <= w[s] && w[s] <= aw[r];
								if(b[s] && !(f1&& f2))
									suc = false;
								if(!b[s] && (f1 && f2))
									suc = false;
							}
							//if(suc)
								//cout << ah[j] << " " << ah[k] << " , " << aw[q] << " " << aw[r] << " : " << suc << endl;
							//cout << "S" << suc << endl;
							if(suc) {
								if(ah[j] <= qh[i] && qh[i] <= ah[k] && aw[q] <= qw[i] && qw[i] <= aw[r])
									scnt ++;
								else
									fcnt ++;
							}
						}
			//cout << scnt << " " << fcnt << endl;
			if(scnt > 0 && fcnt == 0)
				cout << "BIRD" << endl;
			else if(fcnt > 0 && scnt == 0)
				cout << "NOT BIRD" << endl;
			else
				cout << "UNKNOWN" << endl;
			
		}	
		
	}
	return 0;
}

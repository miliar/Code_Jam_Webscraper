#include <fstream>
#include <vector>
using namespace std;

int main() {
  ifstream cin("input.txt");
  ofstream cout("output.txt");
  int t,n,k;
  cin >> t;
  for(int tc=1; tc<=t; tc++) {
    cin >> n >> k;
	vector<vector<char> > a(n, vector<char>(n));
	for(int i=0; i<n; i++)
	  for(int j=0; j<n; j++)
	    cin >> a[j][n-i-1];

	for(int i=n-2; i>=0; i--) {
	  for(int j=0; j<n; j++) {
		if(a[i][j]!='.') {
		  int p = i;
		  while(p+1<n && a[p+1][j]=='.') p++;
		  if(p!=i) {
		    a[p][j]=a[i][j];
		    a[i][j]='.';
		  }
		}
	  }
	}

    int bc=0, rc=0;
	for(int i=0; i<n; i++) {
      for(int j=0; j<n; j++) {
	    if(a[i][j]=='.') continue;
	    int cnt = 0, ti,tj;
		tj=j; ti=i; cnt=1;
		while(tj+1<n && a[ti][tj+1]==a[ti][tj]) {
		  cnt++; tj++;
		}
		if(a[i][j]=='B' && cnt==k) bc=1;
		if(a[i][j]=='R' && cnt==k) rc=1;
		tj=j; ti=i; cnt=1;
		while(ti+1<n && a[ti+1][tj]==a[ti][tj]) {
		  cnt++; ti++;
		}
		if(a[i][j]=='B' && cnt==k) bc=1;
		if(a[i][j]=='R' && cnt==k) rc=1;
		tj=j; ti=i; cnt=1;
		while(tj-1>=0 && ti+1<n && a[ti+1][tj-1]==a[ti][tj]) {
		  cnt++; ti++; tj--;
		}
		if(a[i][j]=='B' && cnt==k) bc=1;
		if(a[i][j]=='R' && cnt==k) rc=1;
		tj=j; ti=i; cnt=1;
		while(tj+1<n && ti+1<n && a[ti+1][tj+1]==a[ti][tj]) {
		  cnt++; tj++; ti++;
		}
		if(a[i][j]=='B' && cnt==k) bc=1;
		if(a[i][j]=='R' && cnt==k) rc=1;
	  }
	}
	if(bc && rc) cout << "Case #" << tc << ": Both" << endl; else
	if(bc) cout << "Case #" << tc << ": Blue" << endl; else
	if(rc) cout << "Case #" << tc << ": Red" << endl; else
    cout << "Case #" << tc << ": Neither" << endl;
  }
  return 0;
}
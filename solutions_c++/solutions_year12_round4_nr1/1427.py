#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
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
#include <cctype> 
#include <string> 
#include <cstring> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <ctime> 

using namespace std; 


#define PI acos(-1)
#define CLEAR(A) memset(A,0,sizeof(A))
#define SETMAX(A) memset(A,0x7f,sizeof(A))
#define SETM1(A) memset(A,-1,sizeof(A))
#define SQ(A) (A)*(A)


int T;
int N;
int d[10002];
int l[10002];
int D;
map<pair<int,int>, bool> m;

bool isok(int pos, int swing) {
	if(m.find(make_pair(pos,swing)) != m.end()) return m[make_pair(pos,swing)];
	if(pos + 2*swing >= D) return true;
	bool ret = false;
	for(int i=0;i<N;i++) {
		if(d[i] > pos+swing && d[i]<=pos+2*swing) {
			int newpos = max(pos+swing,d[i]-l[i]);
			int newsw = min(d[i]-pos-swing, l[i]);
			if(isok(newpos,newsw)) {
				ret = true;
				goto out;
			}
		}
	}
out: ;
	m[make_pair(pos,swing)] = ret;
	return ret;
}

int main()
{
	cout << setprecision(9) ;
	cin >> T;
	for(int i=1;i<=T;i++) {
		m.clear();
		cin >> N;
		for(int j=0;j<N;j++) {
			cin >> d[j] >> l[j];
		}
		cin >> D;
		if(isok(0,d[0])) cout << "Case #" << i<< ": YES" << endl;
	       	else cout << "Case #" << i<< ": NO" << endl;	
	}
	return 0;
}



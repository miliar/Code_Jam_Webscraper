#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;
#define fu(i,m,n) for(int i=m; i<n; i++)
#define fr(i,m,n) for(typeof(m) i=m; i!=n; i++)
#define fa(i,c) fr(i,c.begin(),c.end())

int main(void) {
	int T;
	cin >> T;
	fu(tc,1,T+1) {
		int C;
		cin >> C;
		map<int,int> street;
		fu(c,0,C) {
			int P,V;
			cin >> P >> V;
			street[P] = V;
		}
		int ret=0;
		bool done = false;
		while(!done)  {
			done = true;
			fa(i,street) {
				int p = i->first;
				int v = i->second;
				if(i->second > 1) {
					done = false;
					int w = v/2;
					street[p]-=2*w;
					//fu(i,1,w+1) street[p-i]++;
					//fu(i,1,w+1) street[p+i]++;
					street[p-1]+=w;
					street[p+1]+=w;
					ret += w;
					break;
				}
			}
		}
		cout << "Case #" << tc << ": " << ret << endl;
	}
}

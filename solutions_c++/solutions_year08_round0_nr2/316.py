#include <iostream>
#include <map>
#include <vector>
using namespace std;
#define fu(i,m,n) for(int i=m; i<n; i++)

int read_time(istream& is) {
	int h,m; char c;
	is >> h >> c >> m;
	return 60*h+m;
}

int main(void) {
	int N;
	cin >> N;
	fu(ts,1,N+1) {
		vector<pair<int,pair<int,int> > > trips;
		cout << "Case #" << ts << ": ";
		int T;
		cin >> T;
		int NA, NB;
		cin >> NA >> NB;
		fu(i,0,NA) {
			int a=read_time(cin);
			int b=read_time(cin);
			trips.push_back(make_pair(b+T, make_pair(-1,1)));
			trips.push_back(make_pair(a, make_pair(1,0)));
		}
		fu(i,0,NB) {
			int a=read_time(cin);
			int b=read_time(cin);
			trips.push_back(make_pair(b+T, make_pair(-1,0)));
			trips.push_back(make_pair(a, make_pair(1,1)));
		}
		sort(trips.begin(),trips.end());
		int cnt[2]={0,0};
		int ret[2]={0,0};
		fu(i,0,trips.size()) {
			int w = trips[i].second.second;
			cnt[w] -= trips[i].second.first;
			while(cnt[w]<0) ret[w]++, cnt[w]++;
		}
		cout << ret[0] << " " << ret[1] << endl;
	}
}

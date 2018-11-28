#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <set>
#include <cmath>
#include <cassert>

using namespace std;

typedef vector<int> VI;
typedef long long LL;
typedef pair<int,int> PI;
#define MP make_pair
#define REP(x,n) for(int x=0; x<(int)(n); ++x)
#define REB(b,x,n) for(int x=b; x<(int)(n); ++x)
#define REPD(x,n) for(int x=(n)-1; x>=0; --x)
#define PB push_back
#define ST first
#define ND second
const int INF = 1000000001;
const double EPS = 10e-9;

//timebegin,timeend, begin from A/B
typedef pair<pair<int,int>,bool> Schedule;

int main()
{
	ios_base::sync_with_stdio(0);
	int N;
	cin>>N;
	REP(ncase,N) {
		multiset<Schedule> alls;

		int T,NA,NB;
		cin>>T>>NA>>NB;
		REP(i,NA+NB) {
			string clock;
			cin>>clock;
			assert(clock.size()==5);
			assert(clock[2]==':');
			int timebegin = ((clock[0]-'0')*10+(clock[1]-'0'))*60 + (clock[3]-'0')*10+(clock[4]-'0');
			assert(timebegin<24*60);
			assert(timebegin>=0);
			cin>>clock;
			assert(clock.size()==5);
			assert(clock[2]==':');
			int timeend = ((clock[0]-'0')*10+(clock[1]-'0'))*60 + (clock[3]-'0')*10+(clock[4]-'0');
			assert(timeend<24*60);
			assert(timeend>=0);
			alls.insert(MP(MP(timebegin,timeend),(bool)(i>=NA)));
			//cout<<"ins "<<(bool)(i>=NA)<<" "<<timebegin<<" "<<timeend<<endl;
		}

		int result[2] = {0,0};
		multiset<int> avail[2];

		//greedy!
		while(!alls.empty()) {
			//pop first uhandled schedule
			Schedule cur = *(alls.begin());
			alls.erase(alls.begin());
			//check first available train on appropriate station A/B.
			set<int>::iterator cand = avail[cur.ND].begin();
			//if no available train can handle the shedule
			if(cand == avail[cur.ND].end() || *cand > cur.ST.ST) {
				//create new train
				result[cur.ND]++;
				avail[1-cur.ND].insert(cur.ST.ND + T);
				//cout<<"add "<<cur.ST.ST<<" "<<cur.ST.ND<<endl;
			} else {
				//use and move the train
				avail[cur.ND].erase(cand);
				avail[1-cur.ND].insert(cur.ST.ND + T);
			}
		}

		cout<<"Case #"<<ncase+1<<": "<<result[0]<<" "<<result[1]<<"\n";
	}
	cout<<flush;

  return 0;
}

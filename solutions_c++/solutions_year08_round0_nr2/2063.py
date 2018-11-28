#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>

#define tr(c,x) for(typeof((c).begin() x = (c).begin(); x != (c).end(); x++) 


using namespace std;

int starta,startb;
int tt;
typedef pair<int,bool> st;
vector<st> da,db,aa,ab;

void solve(){
	for(vector<st>::iterator ita = da.begin(); ita!=da.end(); ita++){
		bool empty = true;
		for(vector<st>::iterator itb = ab.begin(); itb!=ab.end(); itb++){
			if ((*itb).second == true) continue;
			empty = false;
			if ((*itb).first+tt > (*ita).first) { starta++; break; }
			if ((*itb).first+tt <= (*ita).first) { (*itb).second = true; break; }
		}
		if (empty == true) starta++;
	}
	
	for(vector<st>::iterator ita = db.begin(); ita!=db.end(); ita++){
		bool empty = true;
		for(vector<st>::iterator itb = aa.begin(); itb!=aa.end(); itb++){
			if ((*itb).second == true) continue;
			empty = false;
			if ((*itb).first+tt > (*ita).first) { startb++; break; }
			if ((*itb).first+tt <= (*ita).first) { (*itb).second = true; break; }
		}
		if (empty == true) startb++;
	}

}

int main(){
	int cases;
	int h1,m1,h2,m2;
	int time1,time2;
	int na,nb;
	scanf("%d",&cases);
	for(int i=1;i<=cases;i++){
		starta=startb=0;
		da.clear();
		db.clear();
		aa.clear();
		ab.clear();
		scanf("%d",&tt);
		scanf("%d %d",&na,&nb);
		if (na>0 && nb==0) starta = na;
		else if (nb>0 && na==0) startb = nb;
		else {
			while(na--){
				scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
				time1 = h1*60+m1;
				time2 = h2*60+m2;
				da.push_back(make_pair(time1,false));
				aa.push_back(make_pair(time2,false));
			}
			sort(da.begin(),da.end());
			sort(aa.begin(),aa.end());
			while(nb--){
				scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
				time1 = h1*60+m1;
				time2 = h2*60+m2;
				db.push_back(make_pair(time1,false));
				ab.push_back(make_pair(time2,false));
			}
			sort(db.begin(),db.end());
			sort(ab.begin(),ab.end());
		}
		solve();
		
		printf("Case #%d: %d %d\n",i,starta,startb);
	}
	return 0;
}

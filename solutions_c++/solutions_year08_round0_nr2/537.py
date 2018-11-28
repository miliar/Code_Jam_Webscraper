
#include <iostream>
#include <map>
#include <set>
using namespace std;

int main(){
	int nn;
	cin>>nn;
	for(int npr=1;npr<=nn;npr++){
		int time;
		int na,nb;
		cin>>time>>na>>nb;
		multimap<int, pair<int, int> > mp;
		for(int i=0;i<na;i++){
			int h,m;
			char c;
			cin>>h>>c>>m;
			int sta=h*60+m;
			cin>>h>>c>>m;
			int arr=h*60+m;
			mp.insert(make_pair(sta, make_pair(arr,0)));
		}
		for(int i=0;i<nb;i++){
			int h,m;
			char c;
			cin>>h>>c>>m;
			int sta=h*60+m;
			cin>>h>>c>>m;
			int arr=h*60+m;
			mp.insert(make_pair(sta, make_pair(arr,1)));
		}

		multiset<int> a,b;
		int ansA=0,ansB=0;
		for(__typeof(mp.begin()) it=mp.begin();it!=mp.end();it++){
			int sta=it->first;
			int end=it->second.first;
			int from=it->second.second;
				
			if(from==0){	//AtoB
				if(a.size() && *a.begin()<=sta)a.erase(a.begin());
				else ansA++;
				b.insert(end+time);
			}else{
				if(b.size() && *b.begin()<=sta)b.erase(b.begin());
				else ansB++;
				a.insert(end+time);
			}
		}
		cout<<"Case #"<<npr<<": "<<ansA<<" "<<ansB<<endl;
	}

	return 0;
}

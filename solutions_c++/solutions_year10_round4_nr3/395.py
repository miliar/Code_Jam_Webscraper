#include<iostream>
#include<vector>
#include<set>
using namespace std;

vector<pair<int,int> > ar[2];
set<pair<int,int> > ada;
set<pair<int,int> >::const_iterator pos;
int T,t,R,i,j,k,x1,x2,y1,y2,ans;
pair<int,int> crnt,neks;

int main() {
	cin>>T;
	for(t=1;t<=T;t++) {
		cin>>R;
		ada.clear();
		for(i=0;i<R;i++) {
			cin>>x1>>y1>>x2>>y2;
			for(j=y1;j<=y2;j++) {
				for(k=x1;k<=x2;k++) {
					if(ada.find(make_pair(j,k))!=ada.end()) continue;
					ada.insert(make_pair(j,k));
				}
			}
		}
		ans=0;
		while(ada.size()>0) {
			ans++;
			ar[0].clear();
			for(pos=ada.begin();pos!=ada.end();pos++) {
				crnt=*pos;
				if(ada.find(make_pair(crnt.first-1,crnt.second))!=ada.end()||ada.find(make_pair(crnt.first,crnt.second-1))!=ada.end()) continue;
				ar[0].push_back(crnt);
			}
			ar[1].clear();
			for(pos=ada.begin();pos!=ada.end();pos++) {
				crnt=*pos;
				neks=crnt;
				neks.first--; neks.second++;
				if(ada.find(neks)!=ada.end()) ar[1].push_back(make_pair(crnt.first,neks.second));
				neks=crnt;
				neks.first++; neks.second--;
				if(ada.find(neks)!=ada.end()) ar[1].push_back(make_pair(neks.first,crnt.second));
			}
			for(i=0;i<ar[0].size();i++) ada.erase(ar[0][i]);
			for(i=0;i<ar[1].size();i++) {
				if(ada.find(ar[1][i])!=ada.end()) continue;
				ada.insert(ar[1][i]);
			}
		}
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
}

#include<iostream>
#include<vector>
using namespace std;

int T,X,tc,N,a,b,c,posNow;
double S,R,t,ans,speed,timeTaken,dist;
vector<pair<double,pair<int,int> > > newAr;
vector<pair<pair<int,int>, double> > ar;

int main() {
	cin>>T;
	for(int tc=1;tc<=T;tc++) {
		cin>>X>>S>>R>>t>>N;
		ar.clear();
		for(int i=0;i<N;i++) {
			cin>>a>>b>>c;
			ar.push_back(make_pair(make_pair(a,b),c));
		}
		sort(ar.begin(),ar.end());
		posNow=0;
		ans=0.00;
		newAr.clear();
		for(int i=0;i<N;i++) {
			if(posNow<ar[i].first.first) {
				newAr.push_back(make_pair(0.00,make_pair(posNow,ar[i].first.first)));
			}
			newAr.push_back(make_pair(ar[i].second,make_pair(ar[i].first.first,ar[i].first.second)));
			posNow=ar[i].first.second;
		}
		if(posNow<X) {
			newAr.push_back(make_pair(0.00,make_pair(posNow,X)));
		}
		sort(newAr.begin(),newAr.end());
		posNow=0;
		for(int i=0;i<newAr.size();i++) {
			//cout<<"jalanan "<<i<<": "<<newAr[i].first<<" "<<newAr[i].second.first<<" "<<newAr[i].second.second<<endl;
			dist=newAr[i].second.second-newAr[i].second.first;
			speed=newAr[i].first;
			//kalo bisa lari full
			if((speed+R)*t>=dist) {
				//cout<<"lari full"<<endl;
				timeTaken=dist/(speed+R);
				//cout<<"time taken: "<<timeTaken<<endl;
				t-=(dist/(speed+R));
				//cout<<"sisa waktu: "<<t<<endl;
			}
			//kalo ga bisa lari full
			else {
				//cout<<"lari setengah"<<endl;
				timeTaken=t+(dist-(speed+R)*t)/(speed+S);
				//cout<<"time taken: "<<timeTaken<<endl;
				//cout<<"dist lari: "<<(speed+R)*t<<endl;
				t=0.00;
				//cout<<"sisa waktu: "<<t<<endl;
			}
			ans+=timeTaken;			
		}
		cout<<"Case #"<<tc<<": ";
		printf("%.9lf\n",ans);
	}
}

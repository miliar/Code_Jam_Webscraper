#include <vector>
#include <string>
#include <iostream>
#include <utility>

using namespace std;

int n,na,nb;
int ta,tb;
int turnAround;
vector<pair<int,int> > tableA(0),tableB(0);
vector<pair<int,int> > freeTrain(0);

int init(){
	ta=0;
	tb=0;
	tableA.resize(0);
	tableB.resize(0);
	freeTrain.clear();
	freeTrain.resize(24*60+100);
	cin>>turnAround;
	cin>>na>>nb;
	int tmpH,tmpM;
	char tmpC;
	for(int i=0;i<na;++i){
		pair<int,int> element;
		cin>>tmpH>>tmpC>>tmpM;
		element.first=tmpH*60+tmpM;
		cin>>tmpH>>tmpC>>tmpM;
		element.second=tmpH*60+tmpM;
		tableA.push_back(element);
	}
	for(int i=0;i<nb;++i){
		pair<int,int> element;
		cin>>tmpH>>tmpC>>tmpM;
		element.first=tmpH*60+tmpM;
		cin>>tmpH>>tmpC>>tmpM;
		element.second=tmpH*60+tmpM;
		tableB.push_back(element);
	}
	for(int i=0;i<24*60;++i){
		freeTrain[i].first=0;
		freeTrain[i].second=0;
	}
	return 0;
}

int solve(){
	for(int time=0;time<24*60;++time){
		for(int i=0;i<na;++i){
			if(tableA[i].first==time){
				if(freeTrain[time].first==0){
					++ta;
					freeTrain[time].first=1;
				}
				--freeTrain[time].first;
				++freeTrain[tableA[i].second+turnAround].second;
			}
		}
		for(int i=0;i<nb;++i){
			if(tableB[i].first==time){
				if(freeTrain[time].second==0){
					++tb;
					freeTrain[time].second=1;
				}
				--freeTrain[time].second;
				++freeTrain[tableB[i].second+turnAround].first;
			}
		}
		freeTrain[time+1].first+=freeTrain[time].first;
		freeTrain[time+1].second+=freeTrain[time].second;
	}
	return 0;
}

int show(int n){
	cout<<"Case #"<<n<<": "<<ta<<' '<<tb<<endl;
	return 0;
}

int main(){
	freopen("B-large.in","r",stdin);
	freopen("test.out","w",stdout);
	cin>>n;
	for(int i=0;i<n;++i){
		init();
		solve();
		show(i+1);
	}
	return 0;
}
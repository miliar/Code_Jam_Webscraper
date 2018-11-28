#include<iostream>
#include<string>
#include<cmath>
#include<algorithm>
#include<vector>
using namespace std;

struct trip{
	pair<int,int> s;
	pair<int,int> t;
	char c;
	bool operator <(const trip& tr)const{
		if(s == tr.s && t == tr.t)return c<tr.c;
		if(s == tr.s) return t<tr.t; 
		return s < tr.s;
	}
};

struct train{
	pair<int,int> dept;
	char c;
	char l;
};

vector<trip> trips;
vector<train> trains;

int main(){
	freopen("sample.in","rt",stdin);
	freopen("sample.out","w",stdout);
	
	int n,na,nb;
	int t,h,m;
	char c;
	cin>>n;
	trip tr;
	for(int i=0;i<n;i++){
		cin>>t;
		cin>>na>>nb;
		
		for(int j=0;j<na;j++){
			cin>>h>>c>>m;
			tr.s = make_pair(h,m);
			cin>>h>>c>>m;
			tr.t = make_pair(h,m);
			tr.t.second += t;
			if(tr.t.second >= 60)
			{
				tr.t.second -= 60;
				tr.t.first ++;
			}
			tr.c = 'A';
			trips.push_back(tr);
		}
		for(int j=0;j<nb;j++){
			cin>>h>>c>>m;
			tr.s = make_pair(h,m);
			cin>>h>>c>>m;
			tr.t = make_pair(h,m);
			tr.t.second += t;
			if(tr.t.second >= 60)
			{
				tr.t.second -= 60;
				tr.t.first ++;
			}
			tr.c = 'B';
			trips.push_back(tr);
		}
		
		sort(trips.begin(),trips.end());
		
		for(int j=0;j<(int)trips.size();j++){
			int k;
			for(k=0;k<(int)trains.size();k++){
				if(trains[k].dept <= trips[j].s && trains[k].l != trips[j].c){
					trains[k].dept = trips[j].t;
					trains[k].l = trips[j].c;
					break;
				}
			}
			if(k == (int)trains.size()){
				train tn;
				tn.dept = trips[j].t;
				tn.c = trips[j].c;
				tn.l = trips[j].c;
				trains.push_back(tn);
			}
		}
		
		int a = 0;
		int b = 0;
		for(int j=0;j<trains.size();j++){
			if(trains[j].c == 'A' )a++;
			else b++;
		}
		cout<<"Case #"<<(i+1)<<": "<<a << " " << b<<endl;
		trips.clear();
		trains.clear();
	}
	
	return 0;
}

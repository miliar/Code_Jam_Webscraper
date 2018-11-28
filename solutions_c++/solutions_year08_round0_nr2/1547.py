#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int convert(string data){
	return 60*(data[0]*10+data[1])+data[3]*10+data[4];
}
struct node{
	int time;
	int going;
	int station;
};
bool con(const node &a,const node &b){
	if(a.time!=b.time)
		return a.time<b.time;
	else
		return a.going<b.going;
}
int main(){
	int h;
	cin>>h;
	for(int i=0;i<h;++i){
		int t,m,n;
		cin>>t>>m>>n;
		vector<node>data;
		for(int j=0;j<m;++j){
			node temp;
			temp.going=1;
			temp.station=0;
			string s;
			cin>>s;
			temp.time=convert(s);
			data.push_back(temp);
			cin>>s;
			temp.going=0;
			temp.station=1;
			temp.time=convert(s)+t;
			data.push_back(temp);
		}
		for(int j=0;j<n;++j){
			node temp;
			temp.going=1;
			temp.station=1;
			string s;
			cin>>s;
			temp.time=convert(s);
			data.push_back(temp);
			cin>>s;
			temp.going=0;
			temp.station=0;
			temp.time=convert(s)+t;
			data.push_back(temp);
		}
		sort(data.begin(),data.end(),con);
		int ret0=0,ret1=0,ab=0,ba=0;
		for(int j=0;j<data.size();++j){
			//cout<<data[j].time<<" "<<data[j].going<<" "<<data[j].station<<endl;
			if(data[j].going){
				if(data[j].station){	
					if(ba==0) ++ret1; else ba--;
				}
				else{
					if(ab==0) ++ret0; else ab--;
				}
			}
			else{
				if(data[j].station){
					ba++;
				}
				else{
					ab++;
				}
			}
		}
		cout<<"Case #"<<i+1<<": "<<ret0<<" "<<ret1<<endl;
	}
	return 0;
}

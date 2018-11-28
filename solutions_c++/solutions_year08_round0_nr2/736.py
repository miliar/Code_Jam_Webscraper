#include <iostream>
#include <vector>
#include <string>
using namespace std;

typedef pair<int,int> PII;

int solve(vector<PII> &v){
	sort(v.begin(), v.end());
	int res=0;
	int train=0;
	for(int i=0; i<v.size(); i++){
		if(v[i].second==0){
			train++;
		}else{
			if(train==0) res++;
			else train--;
		}
	}
	return res;
}

int get_m(string s){
	return (s[0]-'0')*600
		+(s[1]-'0')*60
		+(s[3]-'0')*10
		+(s[4]-'0');
}

int main(){
	int N;
	cin>>N;
	for(int k=1; k<=N; k++){
		int NA,NB,T;
		cin>>T>>NA>>NB;
		vector<PII> a,b;
		for(int i=0; i<NA; i++){
			string str;
			cin>>str;
			int t1=get_m(str);
			cin>>str;
			int t2=get_m(str);
			a.push_back(make_pair(t1,1));
			b.push_back(make_pair(t2+T,0));
		}
		for(int i=0; i<NB; i++){
			string str;
			cin>>str;
			int t1=get_m(str);
			cin>>str;
			int t2=get_m(str);
			b.push_back(make_pair(t1,1));
			a.push_back(make_pair(t2+T,0));
		}
		cout<<"Case #"<<k<<": "<<solve(a)<<" "<<solve(b)<<endl;
	}
	return 0;
}

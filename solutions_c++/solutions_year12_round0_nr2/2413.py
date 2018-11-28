#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

int n,s,p;
vector<int> v;
void solve(){
	int cnt=0;
	sort(v.begin(),v.end(),greater<int>());
//	cout<<"n:"<<n<<" s:"<<s<<" p:"<<p<<endl;
	for(int i=0;i<v.size();i++){
		int num=v[i];
		int d=num%3;
		int b=num/3;
//		cout<<num<<":"<<d<<":"<<b<<":(c:"<<cnt;
		if(d==0){
			if(b>=p)cnt++;
			else if(b+1==p&&s>0&&num!=0){
				s--;
				cnt++;
			}
		}
		else if(d==1&&b+1>=p)cnt++;
		else if(d==2){
			if(b+1>=p)cnt++;
			else if(b+2==p&&s>0){
				s--;
				cnt++;
			}
		}
//		cout<<":"<<cnt<<")"<<endl;
	}
	cout<<cnt<<endl;
}
int main(){
	int t;
	cin >> t;
	for( int i = 0; i < t; i++){
		cin >> n >> s>> p;
		v.clear();
		for( int  j = 0; j < n; j++){
			int score;
			cin >> score;
			v.push_back(score);
		}
		printf("Case #%d: ",i+1);
		solve();

	}

	return 0;
}
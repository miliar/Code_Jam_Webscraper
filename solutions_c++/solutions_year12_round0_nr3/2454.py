#include <iostream>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <algorithm>
#include <utility>
#include <sstream>

using namespace std;
int a,b;
void solve(){
	int cnt=0;
	stringstream ss;
	ss << a;
	string _a=ss.str() + ss.str();
	ss.str("");
    ss.clear(stringstream::goodbit);
	ss << b;
	string _b=ss.str()+ss.str();
	ss.str("");
    ss.clear(stringstream::goodbit);
//	cout<<"_a:"<<_a<<" _b:"<<_b<<endl;
	for(int i = a; i <= b; i++){
		if(i<10)continue;
		ss << i;
		string n=ss.str()+ss.str();
		map<string,int> v;

		for(int j=1;j<n.size()/2;j++){
			string m=n.substr(j,n.size()/2);
			if(m!=n.substr(0,n.size()/2)&&n.substr(0,n.size()/2)<m&&m<=_b&&v[m]!=1){
				cnt++;
//				cout<<"    n:"<<n<<endl;
//				cout<<"        s:"<<m<<endl;
//				cout<<"        cnt"<<endl;
//				cout<<"        "<<v[m]<<endl;
				v[m]++;
			}
			
		}
		
		ss.str("");
   		ss.clear(stringstream::goodbit);
	}
	cout<<cnt<<endl;
}
int main(){
	int t;
	cin >> t;
	for( int i = 0; i < t; i++){
		cin >> a >> b;
		printf("Case #%d: ",i + 1);
		solve();
	}


	return 0;
}
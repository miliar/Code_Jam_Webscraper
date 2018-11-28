#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <fstream>
using namespace std;
static const double EPS = 1e-5;
typedef long long ll;


int main(){
	ifstream ifs("data.txt");
	int cases;ifs >> cases;
	for(int i=0;i<cases;++i){
		ll result=0;	
		string A,B;
		ifs >> A >> B;
		ll dig=1;
		for(ll j=0;j<A.length()-1;++j)dig*=10;
		ll A_int=atoi(A.c_str());
		ll B_int=atoi(B.c_str());
		
		for(ll j=A_int; j<B_int;++j){
			ll k=10;
			vector <ll> dup;
			while(j/k!=0){
				ll back=j%k;
				ll tmp=j/k;
				tmp+= back*(dig/k)*10;
				if(tmp<=B_int&&tmp>j&&find(dup.begin(),dup.end(),tmp)==dup.end()){
				//	cout<<j<<";"<<tmp<<endl;
					dup.push_back(tmp);
					++result;
				}
				k*=10;
			}

		}
		
		cout<<"Case #"<<i+1<<": "<<result<<endl;
	};
	

};


#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
#define all(v) v.begin(),v.end()
typedef long long ll;

vector<ll> cambia_base(ll n,int base){
    vector<ll> res;
    
    while(n!=0){
	res.push_back(n%base);
	n/=base;
    }
    reverse(all(res));
    return res;
}

bool funca(ll n,int base){
  set<ll> visited;
  visited.insert(n);
  while(true){
    vector<ll> num=cambia_base(n,base);
    ll suma=0;
    for(int i=0;i<num.size();i++) suma+=num[i]*num[i];
    if(suma==1) return true;
    n=suma;
    if(visited.find(n)!=visited.end()) return false;
    visited.insert(n);
  }
  return false;
}

int main(){
    int t;
    string aux;
    getline(cin,aux);
    sscanf(aux.c_str(),"%d",&t);
    //cout<<t<<endl;
    for(int tt=1;tt<=t;tt++){
	getline(cin,aux);
	istringstream is(aux);
	vector<int> bas;int ss;
	while(is>>ss) bas.push_back(ss);
	
	for(int i=2;;i++){
	    bool cumple=true;
	    for(int j=0;j<bas.size();j++) if(!funca(i,bas[j])){cumple=false;break;}
	    if(cumple){
		cout<<"Case #"<<tt<<": "<<i<<endl;
		break;
	    }
	}
	
    }
}
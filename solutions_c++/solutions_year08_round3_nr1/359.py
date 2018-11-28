#include <vector>
#include <list>
#include <ctime>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define ll  long long
#define pb push_back
#define mp make_pair
#define size(v) (int)(v.size())
#define loop(i,n) for(i=0;i<n;i++)
#define all(v) v.begin(), v.end()
#define tr(container, it)  for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define vi vector<int>


using namespace std;

int main() {

    int i,j,k;
    int t;
    cin>>t;
    for(int numt=0;numt<t;numt++){
    	int p,k,l;
    	cin>>p>>k>>l;
    	vector<ll> freq;
    	ll a;
    	int cnt=0;
    	for(i=0;i<l;i++){
    		cin>>a;
    		if(a==0) cnt++;
    		freq.pb(a);
    	}
    	if(p*k<l-cnt){
    		cout<<"Case #"<<numt+1<<": "<<"Impossible"<<endl;
    		continue;
    	}
    	sort(all(freq));
    	ll sum=0;
    	cnt=0;int kp=1;
    	bool done=true;
    	for(i=size(freq)-1;i>=0;i--){
    		sum+=freq[i]*kp;
    		cnt++;
    		if(cnt==k) {kp++;cnt=0;}
    		//if(kp>p){done=false;}
    	}
    	//if(!done)cout<<"Case #"<<numt+1<<": "<<"Impossible"<<endl;

    	 cout<<"Case #"<<numt+1<<": "<<sum<<endl;
    }

    return 0;
}

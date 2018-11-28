#include <vector>
#include <list>
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
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>

using namespace std;
long long l, t, n, nc, ocyc, tdist;
long long c[1005], cnt[1005];

void doit(){
	long long tn, tmod,tcnt,ret=0;
	long long dcov, tk,drem;
	int inx=0;
	vector <pair<long long,long long> > vp;
	memset(c,0,sizeof(c));
	memset(cnt,0,sizeof(cnt));
	ocyc=0;tdist=0;
	cin>>l>>t>>n>>nc;
	dcov=t/2;
	tmod=n%nc;tcnt=n/nc;
	for(int i=0;i<nc;i++){
		cin>>c[i];
		ocyc+=c[i];
		cnt[i]=tcnt;
		if(tmod>i)cnt[i]++;
		tdist+=(cnt[i]*c[i]);
	}
	if(tdist<=dcov){
		cout<<tdist*2<<endl;
		return;
	}
	tk=dcov/ocyc;
	if(tk){
		for(int i=0;i<nc;i++)cnt[i]-=tk;
	}
	drem=dcov-(ocyc*tk);
	while(c[inx]<=drem){
		drem-=c[inx];
		cnt[inx]--;
		inx++;
	}
	if(drem){
		vp.push_back(make_pair(c[inx]-drem,1)); 
		cnt[inx]--;
	}
	for(int i=0;i<nc;i++)
	if(cnt[i]){
		vp.push_back(make_pair(c[i],cnt[i])); 
	}
	sort(vp.begin(),vp.end());
	ret=t;
	for(int i=vp.size()-1;i>=0;i--){
		if(l>=vp[i].second){
			l-=vp[i].second;
			ret+=(vp[i].first*vp[i].second);
		}
		else{
			ret+=(vp[i].first*l);
			ret+=(vp[i].first*(vp[i].second-l)*2);
			l=0;
		}
	}
	cout<<ret<<endl;
	return;
}

int main(){
    int tc;
    cin>>tc;
    for(int i=1;i<=tc;i++){
        cout<<"Case #"<<i<<": ";
        doit();
    }
    return 0;
}


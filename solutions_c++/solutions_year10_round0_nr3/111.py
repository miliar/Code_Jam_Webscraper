#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

pair<pair<int,int>,long long> simulate(const vector<int>& g,int nstep,int k,int start,bool stop = true){
    if(nstep == 0){
	return make_pair(make_pair(0,0),0);
    }
    vector<bool> mrk(g.size(),false);
    int ind = start;
    int step = 0;
    long long ret = 0;
    do{
	mrk[ind] = true;
	int cap = k;
	int sind = ind;
	do{
	    cap -= g[ind];
	    ret += g[ind];
	    ++ind;
	    if(ind == g.size()){
		ind = 0;
	    }
	} while(cap >= g[ind] && ind != sind);
	++step;
    } while((!stop || !mrk[ind]) && step < nstep);
    
    return make_pair(make_pair(step,ind),ret);
}

int main(){
    int t;
    cin >> t;
    for(int lp=1;lp<=t;++lp){
	cout << "Case #" << lp << ": ";
	int r,k,n;
	cin >> r >> k >> n;
	vector<int> g(n);
	for(int i=0;i<n;++i){
	    cin >> g[i];
	}
	
	long long ret;
	
	if(r < n){
	    ret = simulate(g,r,k,0,false).second;
	}
	else{
	    pair<pair<int,int>,long long> p = simulate(g,n,k,0);
	    ret = p.second;
	    
	    r -= p.first.first;
	    int start = p.first.second;
	    
	    p = simulate(g,n,k,start);
	    int nc = p.first.first;
	    
	    ret += (r/nc) * p.second;
	    
	    ret += simulate(g,r%nc,k,start).second;
	}
	
	cout << ret << "\n";
    }
    return 0;
}
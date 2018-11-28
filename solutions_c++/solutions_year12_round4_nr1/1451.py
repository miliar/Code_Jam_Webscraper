#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cfloat>
#include <complex>
using namespace std;

vector<long long int> D;
vector<long long int> L;
long long int dist;

bool check(long long int cur,long long int pos,long long int len) {
    if(pos + len >= dist)
        return true;
    for(int i=cur + 1; i<D.size(); i++) {
        if(D[i] > pos+len)
            break;
        if(check(i, D[i], min(D[i]-pos, L[i])))
            return true;
        }
    return false;
}

int main(){
	
	freopen("input.txt","rt",stdin);
    //freopen("out.txt","wt",stdout);
    
    string temp;
    long long int i,j,k,l;
    int t, N;
    long long int a,b;
    bool flag = true;
	cin>>t;

	for ( k=1; k<=t; k++){
        flag = true;
        cin>>N;
        D.clear();
        L.clear();

        for (i = 0; i < N; ++i) {
            cin>>a>>b;
            D.push_back(a);
            L.push_back(b);
        }
        cin>>dist;

        flag = check(0,D[0],D[0]);


        if(flag)
            cout<<"Case #"<<k<<": YES"<<endl;
        else
            cout<<"Case #"<<k<<": NO"<<endl;

    }
	
	return 0;
	
}
		
			
			
			
			
			
			

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

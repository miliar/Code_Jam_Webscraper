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
#include <complex>
using namespace std;



//6 6 8 min suprisigin = 20
//7 7 8 min non suprising = 22

//  p-2 + p -2 +p = 3p-4
//  p-1 + p -1 +P = 3p-2

vector<int> v;

int main(){
	
	freopen("input.txt","rt",stdin);
    freopen("out.txt","wt",stdout);
    
    int temp;
	int i,j,k,l;
    int t,n,s,p,ti;
	cin>>t;

    for ( k=1; k<=t; k++){
        v.clear();
        int c = 0;
        cin>>n;
        cin>>s;
        cin>>p;

        int minS = (3*p)-4;
        int minNS = (3*p)-2;

        for(i=0; i<n; i++) {
            cin>>temp;
            v.push_back(temp);
        }

        sort(v.begin(), v.end(), std::greater<int>());

        for(i=0; i<n; i++) {
            if(v[i] >= minNS) {
                c++;
            }
            else if(v[i]>=minS && s>0 && p!=1) {
                c++;
                s--;
            }
        }
        if(p == 0)
            cout<<"Case #"<<k<<": "<<n<<endl;
        else
            cout<<"Case #"<<k<<": "<<c<<endl;


	}
	
	return 0;
	
}
		
			
			
			
			
			
			

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

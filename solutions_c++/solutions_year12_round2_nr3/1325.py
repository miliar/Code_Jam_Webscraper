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
#define EPSILON 0.000001

struct hede {
    hede(){ sum = 0; };
    vector<long long int> elem;
    double sum;
};



vector<hede> V;

int main(){
	
	freopen("input.txt","rt",stdin);
    freopen("out.txt","wt",stdout);
    
	int i,j,k,l;
    long long int t,N, temp, size, sum;
	int flag=0;
	cin>>t;

    for ( k=1; k<=t; k++) {
        V.clear();
        cin>>N;
        for( i = 0; i < N; i++) {
            cin>>temp;
            if(i==0) {
                hede h;
                h.elem.push_back(temp);
                h.sum+=temp;
                V.push_back(h);
            }
            else {
                size = V.size();
                for(j = 0; j<size; j++) {
                    hede h = V[j];
                    h.elem.push_back(temp);
                    h.sum+=temp;
                    V.push_back(h);
                }
                hede h;
                h.elem.push_back(temp);
                h.sum+=temp;
                V.push_back(h);
            }
        }

        cout<<"Case #"<<k<<":"<<endl;
        for(i = 0; i < V.size(); i++)
            for(j=0; j< V.size(); j++)
                if(abs(V[i].sum - V[j].sum) < 0.000001 && i != j) {
                    for(l = 0; l<V[i].elem.size(); l++)
                        cout<<V[i].elem[l]<<" ";
                    cout<<endl;
                    for(l = 0; l<V[j].elem.size(); l++)
                        cout<<V[j].elem[l]<<" ";
                    cout<<endl;
                    goto asd;
                    }
        asd:sum = 0;

    }
	
	return 0;
	
}
		
			
			
			
			
			
			

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

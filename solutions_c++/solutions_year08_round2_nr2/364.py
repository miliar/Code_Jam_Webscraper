#include <iostream>
#include <set>
#include <vector>

using namespace std;
main(){
        int z;
        cin >> z;
        
        int Prime[1001] = {0};
        
        for(int i=2; i<=1000; i++){
        	int ok=1;
        	for(int j=2; j*j <= i; j++){
        		if(i%j == 0) ok=0;
        	}
        	Prime[i]=ok;
        } 
        set<int> SS;
        for(int l=1; l<=z; l++){
        	int a, b, p;
        	
        	cin >> a >> b >> p;
        	
        	set<int> s[1001];
        	
        	for(int i=a; i<=b; i++){
        		s[i].insert(i);
        	}
        	
        	
        	for(int i=p; i<=b; i++){
        		if(Prime[i] == 0 ) continue;
        		
        		int last = -1;
        		for(int j=a; j<=b; j++){
        			int ok = 0;
        			
        			for(set<int>::iterator it = s[j].begin(); it!=s[j].end(); it++){
        				//cout << *it << " " << i << endl;
        				if(*it % i == 0){
        					ok = 1;
        					break;
        				}        			
        			}
        			
        			if(ok){
        				if(last == -1) last = j;
        				else{
        					for(set<int>::iterator it = s[j].begin(); it!=s[j].end(); it++){
        						s[last].insert(*it);
						}
        					s[j].clear();
					}
        			}
        		}        		
        	}
        	
        	int res=0;
        	for(int i=a; i<=b; i++){
        		if(! s[i].empty()) res++;
        		
        	}
        		
        	cout << "Case #" << l << ": " << res << endl;  
        }  

}

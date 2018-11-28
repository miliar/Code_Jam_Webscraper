#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <ctime>
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define pv(v)  tr((v),i) cout << *i << " "; cout << endl
#define pr(i) cout << #i << "=" << (i) << endl
#define pr2(i,j) cout << #i << "=" << (i) << " " << #j << "=" << (j) << endl
#define pr3(i,j,k) cout << #i << "=" << (i) << " " << #j << "=" << (j) << endl << " " << #k << "=" << (k) << endl
using namespace std;

int main() {
    int t;
    vector<int> index(26,-1);
    index['Q'-'A'] = 0;
    index['W'-'A'] = 1;
	index['E'-'A'] = 2;
    index['R'-'A'] = 3;
    index['A'-'A'] = 4;     
    index['S'-'A'] = 5;     
    index['D'-'A'] = 6;     
    index['F'-'A'] = 7;
    string keypad = "QWERASDF";

    
              
    cin>>t;
    
    for(int kases = 1; kases <= t; kases ++) {
    	int c,d,n;
		cin>>c;
		string s;
		vector<vector<char> > combine(8, vector<char> (8, 0));
	    vector<vector<bool> > oppose(8, vector<bool> (8, false));
	    
		for(int i = 0; i < c; i++) {
			cin >> s;
			combine[index[s[0]-'A']][index[s[1]-'A']] = s[2]; 	
			combine[index[s[1]-'A']][index[s[0]-'A']] = s[2]; 			
		}
 		cin>>d;
		for(int i = 0; i < d; i++) {
			cin >> s;
			oppose[index[s[0]-'A']][index[s[1]-'A']] = true; 			
			oppose[index[s[1]-'A']][index[s[0]-'A']] = true; 						
		}

		cin>>n;
		cin >> s;
		vector<char> list(n,-1);
		int start = 0, end = -1;
        
		for(int i = 0; i < n; i++) {
			int ind = index[s[i]-'A'];
			if(ind == -1) {
				list[++end] = s[i];
            }       
			if(end >= start) {
				//non-empty;
				if(combine[ind][index[list[end]-'A']] != 0) {
					list[end] = combine[ind][index[list[end]-'A']];
				} else {
					bool found = false;				
					for(int j = start; j <= end; j++) {
						if(oppose[ind][index[list[j]-'A']]) {
							start = end + 1;
							found = true;
							break;
						}
					}
					if(!found) {
						//couldn't combine and couldn't oppose
						list[++end] = s[i];
					}
				} 
			} else {
				//empty
				list[++end] = s[i]; 
			}
		}
    	cout << "Case #" << kases << ": ";
    	string ans = "[";
    	if(end >= start) {
			for(int i = start; i < end; i++) {
				ans += list[i];
                ans += ", ";
			}
			ans += list[end];
		}
    	
    	ans += "]";
    	cout << ans << endl;
    	
    }
    
    return 0;
}








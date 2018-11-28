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
    cin>>t;
    for(int kases = 1; kases <= t; kases ++) {
    	int n;
    	cin >> n;
    	vector<int> orange, blue;
    	string seq;
        char color;
    	int last_blue = 1, last_orange = 1, button;
    	for(int j = 0; j < n; j++) {
			cin >> color >> button;
			if(color == 'B') {
				blue.push_back(abs(last_blue-button)+1);
				last_blue = button;
			} else  {
				orange.push_back(abs(last_orange-button)+1);
				last_orange = button;
			}
			seq += color;
			
    	}
    	//pr(seq);
    	//pv(orange);
    	//pv(blue);
    	int cur_blue = 0, cur_orange = 0;
    	int num_but = seq.length(), num_orange = orange.size(), num_blue = blue.size();
    	int ans = 0;
    	for(int j = 0; j<num_but; j++) {
    		if(seq[j] == 'B') {
    			ans += blue[cur_blue];
				if(cur_orange < num_orange && orange[cur_orange] > 1) {
					if(orange[cur_orange] > blue[cur_blue]) {
						orange[cur_orange] -= blue[cur_blue];
					} else {
						orange[cur_orange] = 1;
					} 
					
				}    			
    			cur_blue++;
    		} else {
    			ans += orange[cur_orange];
    			if(cur_blue < num_blue && blue[cur_blue] > 1) {
					if(blue[cur_blue] > orange[cur_orange]) {
						blue[cur_blue] -= orange[cur_orange];
					} else {
						blue[cur_blue] = 1;
					} 
					
				}
    			cur_orange++;
    		}
    		
    	}
    	cout << "Case #" << kases << ": " << ans << endl;
    }
    //cin >> t;
    return 0;
}








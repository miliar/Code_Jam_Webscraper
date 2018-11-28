#include <string>
#include <vector>
#include <map>
#include <set>
#include <iostream>
#include <cstdio>
#include <queue>
#include <deque>

using namespace std;

int main()	
{
	freopen("output.txt","w",stdout);
	int tests;
    cin >> tests;
    for(int tt=0;tt<tests;++tt){
        map< char ,map<char,char> > good;
        map< char, map<char, bool> > huy;
        int n;
        cin >> n;
        string s;
        for(int i=0;i<n;++i){
            cin >> s;
            good[ s[0] ][ s[1] ] = s[2];
            good[ s[1] ][ s[0] ] = s[2];
        }
        cin >> n;
        for(int i=0;i<n;++i){
            cin >> s;
            huy[ s[0] ][ s[1] ] = true ;
            huy[ s[1] ][ s[0] ] = true ;
        }
        cin >> n;  
		cin >> s;   
		deque<char> ebatgusey;
		for (int i=0; i<n; i++) {
			ebatgusey.push_back(s[i]);
		}
		deque<char> pizdakommunizmy;
		while (ebatgusey.size()) {
			char c = ebatgusey.front(); ebatgusey.pop_front();
			char last = pizdakommunizmy.size()?pizdakommunizmy.back():0;
			if (last && good.count(last) && (good[pizdakommunizmy.back()].count(c))) {
				pizdakommunizmy.pop_back(); 
				ebatgusey.push_front(good[last][c]);
				continue;
			}
			bool flajog = false;
			for (deque<char>::iterator it = pizdakommunizmy.begin(); it != pizdakommunizmy.end(); it++) {
				if (huy[c][*it]) {
					flajog = true;
					break;
				}
			}
			if (flajog) { 
				pizdakommunizmy.clear();
				continue;
			}
			pizdakommunizmy.push_back(c);			
		}	
		cout << "Case #"<<tt+1<<": [";
		if (pizdakommunizmy.size()) {
			cout << pizdakommunizmy.front(); 
			pizdakommunizmy.pop_front();	
		}
		for(;pizdakommunizmy.size();){
			cout << ", ";
			cout << pizdakommunizmy.front(); pizdakommunizmy.pop_front();
		}
		cout << "]" <<endl;
    }
    return 0;
}
#include <list>
#include <deque>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <utility>
#include <string>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <sstream>

using namespace std;

int exist[128];
bool bas[128];
char combs[3*36];
char opos[2*28];
char mg[100];

int main() {
	for(int i=0;i<128;i++)
		bas[i]=false;
	bas['Q']=true;
	bas['W']=true;
	bas['E']=true;
	bas['R']=true;
	bas['A']=true;
	bas['S']=true;
	bas['D']=true;
	bas['F']=true;
	int NC;
	char c;
	string s;
	cin >> NC;
	
	for(int cs=1;cs<=NC;cs++) {
		for(int i=0;i<128;i++)
			exist[i]=0;
		int C,D,N,num=0;
		cin >> C;
		for(int i=0;i<C;i++) {
			cin >> s;
			combs[3*i]=s[0];
			combs[3*i+1]=s[1];
			combs[3*i+2]=s[2];
		}
		cin >> D;
		for(int i=0;i<D;i++) {
			cin >> s;
			opos[2*i]=s[0];
			opos[2*i+1]=s[1];
		}
		cin >> N;
		if(N==0) {
			cout << "Case #" << cs << ": []"  << endl;
			continue;
		}
		if(N==1) {
			cin >> c;
			cout << "Case #" << cs << ": [" << c << "]" << endl;
			continue;
		}
		for(int i=0;i<N;i++) {
			cin >> c;
			if(num==0) {
				mg[0]=c;
				exist[c]++;
				num++;
				continue;
			}
			bool cmb=false;
			if(bas[mg[num-1]]) {
				for(int j=0;j<C;j++) {
					if((mg[num-1]==combs[3*j] && c==combs[3*j+1]) || (mg[num-1]==combs[3*j+1] && c==combs[3*j])) {
						cmb=true;
						exist[mg[num-1]]--;
						mg[num-1] = combs[3*j+2];
						break;
					}
				}
			}
			
			if(cmb)
				continue;
				
			num++;
			mg[num-1]=c;
			
			for(int j=0;j<D;j++) {
				if((c==opos[2*j] && exist[opos[2*j+1]]) || (c==opos[2*j+1] && exist[opos[2*j]])) {
					for(int k=0;k<128;k++)
						exist[k]=0;
					num=0;
				    break;
				}
			}
			if(num!=0)
				exist[c]++;
		}	
	
	
		cout << "Case #" << cs << ": [";
		if(num>0)
			cout << mg[0];
		for(int i=1;i<num;i++) 
			cout << ", " << mg[i];
		cout << "]" << endl;
	}
	
	return 0;
}

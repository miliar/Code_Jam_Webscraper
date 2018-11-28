#include <stdio.h>
#include <algorithm>
#include <memory.h>
#include <queue>
#include <math.h>
#include <vector>
#include <map>
#include <stack>
#include <string.h>
#include <string>
#include <iostream>
#include <deque>
#include <stdlib.h>
#include <stack>
using namespace std;
int _T;
typedef pair<char,char> pcc;

char C[255][255];
bool D[255][255];

int main() {
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	
	scanf("%d",&_T);
	for (int _t=1;_t<=_T;_t++) {
		vector<char> ans;
		memset(C,0,sizeof(C)); 
		memset(D,0,sizeof(D));
		int c,d,n; 
		char t[111];
		
		cin >> c;
		while (c--) {
			cin >> t;
			C[t[0]][t[1]] = C[t[1]][t[0]] = t[2];
		}
		
		cin >> d;
		while (d--) {
			cin >> t;
			D[t[0]][t[1]] = D[t[1]][t[0]] = 1;
		}
		
		cin >> n;
		cin >> t;
		
		for (int i=0;i<n;i++) {
			if (ans.size() == 0) {
				ans.push_back(t[i]);
				continue;
			}
			
			if (C[ans[ans.size()-1]][t[i]] != 0) {
				char need = C[ans[ans.size()-1]][t[i]];
				ans.pop_back();
				//cout <<  C[ans[ans.size()-1]][t[i]] << endl;
				ans.push_back( need );
				continue;
			}
			
			bool cool = 0;
			for (int j=0;j<ans.size();j++)
				if (D[ans[j]][t[i]]) {
					cool = 1;
					break;
				}
			if (cool) {
				ans.clear();
				continue;
			}
			
			ans.push_back(t[i]);
		}
		
		printf("Case #%d: ",_t);
		putchar('[');
		for (int i=0;i+1<ans.size();i++) printf("%c, ",ans[i]);
		if (ans.size() > 0) putchar(ans[ ans.size() - 1 ]);
		puts("]");
	}
	
	return 0;
}

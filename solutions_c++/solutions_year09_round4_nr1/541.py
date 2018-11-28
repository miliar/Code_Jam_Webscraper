#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

string s[100];
bool use[100];

int main() {
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int t; cin>>t;
	for (int o=0; o<t; o++) {
		int n = 0, res =0;
		cin>>n; 
		getline(cin,s[0]);
		for (int i=0; i<n; i++)
			getline(cin,s[i]);
		memset(use,false,sizeof use);
		for (int i=0; i<n; i++) {
			int t = 0;
			for (int j=0; j<n; j++) 
				if (!use[j]) {
					bool f = true;
					for (int k=i+1; k<n && f; k++)
						if (s[j][k]=='1')
							f = false;
					if (!f) {t++;continue;}
					use[j] = true; break;
				}
			res+=t;
		}
		cout<<"Case #"<<o+1<<": "<<res<<endl;
	}
	return 0;
}
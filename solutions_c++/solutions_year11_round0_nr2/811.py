#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <cmath>
#include <vector>
#include <iostream>
#include <cctype>
#include <algorithm>
using namespace std;
char res[1<<8][1<<8];
vector<int> cnt;
vector<vector<char> > opp;
string s;
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test;
	cin>>test;
	for (int t=1;t<=test;t++){
		printf("Case #%d: ",t);
		int n;
		memset(res,0,sizeof(res));
		opp.assign(1<<8,vector<char>());
		cnt.assign(1<<8,0);
		cin>>n;
		for (int i=0;i<n;i++){
			cin>>s;
			res[s[0]][s[1]]=res[s[1]][s[0]]=s[2];
		}
		cin>>n;
		for (int i=0;i<n;i++){
			cin>>s;
			opp[s[0]].push_back(s[1]);
			opp[s[1]].push_back(s[0]);
		}
		cin>>n>>s;
		string cur;
		for (int i=0;i<n;i++){
			cur.push_back(s[i]);
			cnt[s[i]]++;
			if (cur.size()<2)
				continue;
			char last=cur[cur.size()-1];
			char prev=cur[cur.size()-2];
			if (res[prev][last]){
				cnt[last]--;
				cnt[prev]--;
				cur.pop_back();
				cur.pop_back();
				cur.push_back(res[prev][last]);
				cnt[res[prev][last]]++;
			}else{
				for (int j=0;j<opp[last].size();j++){
					if (cnt[opp[last][j]]>0){
						cnt.assign(1<<8,0);
						cur.clear();
					}
				}
			}
		}
		cout<<"[";
		for (int i=0;i<cur.size();i++){
			if (i==0)
				cout<<cur[i];
			else
				cout<<", "<<cur[i];
		}
		cout<<"]\n";
	}
	return 0;
}
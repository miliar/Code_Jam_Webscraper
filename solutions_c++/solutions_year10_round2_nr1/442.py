#include <cstdio>
#include <ctime>
#include <cstring>
#include <assert.h>
#include <iostream>
#include <cmath>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int main()
{

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	int n,m;
	set<string>dict;
	cin>>T;
	for(int t=1;t<=T;++t){
		dict.clear();

		cin>>n>>m;
		int count=0;
		string str;
		for(int i=0;i<n;++i){
			cin>>str;
			int j=1;
			while(j<str.length()){
				for(;j<str.length()&&str[j]!='/';++j) {}
				if(dict.find(str.substr(0,j)) == dict.end()){
					dict.insert(str.substr(0,j));
				}
				++j;
			}
		}
		for(int i=0;i<m;++i){
			cin>>str;
			int j=1;
			while(j<str.length()){
				for(;j<str.length()&&str[j]!='/';++j) {}
				if(dict.find(str.substr(0,j)) == dict.end()){
					dict.insert(str.substr(0,j));
					++count;
				}
				++j;
			}
		}
		printf("Case #%d: %d\n",t,count);
	}
	return 0;
}
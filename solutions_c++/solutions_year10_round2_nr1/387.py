#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
#include <string>

using namespace std;
set <string> dir;
int createset(string str){
	int n,ret=0;
	n=str.size();
	for(int i=1;i<n;i++){
		if(str[i]=='/' && dir.count(str.substr(0,i))==0){
			ret++;
			dir.insert(str.substr(0,i));
		}
	}
	if(dir.count(str)==0){
		ret++;
		dir.insert(str);
	}
	return ret;
}
void doit(){
	int n,m,ret=0;
	string str;
	dir.clear();
	cin>>n>>m;
	for(int i=0;i<n;i++){
		cin>>str;
		createset(str);
	}
	for(int i=0;i<m;i++){
		cin>>str;
		ret+=createset(str);
	}
	cout<<ret<<endl;
}
int main(){
    int tc;
    cin>>tc;
    for(int i=1;i<=tc;i++){
        cout<<"Case #"<<i<<": ";
        doit();
    }
    return 0;
}


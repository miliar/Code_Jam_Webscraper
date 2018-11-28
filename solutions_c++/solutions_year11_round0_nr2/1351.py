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

void doit(){
	char res[200], opp[200][2];
	int resi=0, oppi=0;
	int n;
	string s, ts="  ";
	map <string,char> mp;
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>s;
		ts[0]=s[0];ts[1]=s[1];
		mp[ts]=s[2];
		ts[0]=s[1];ts[1]=s[0];
		mp[ts]=s[2];
	}
	cin>>oppi;
	for(int i=0;i<oppi;i++){
		cin>>s;
		opp[i][0]=s[0];
		opp[i][1]=s[1];
	}
	cin>>n>>s;
	for(int i=0;i<n;i++){
		res[resi++]=s[i]; 
		if(resi<2) continue;
		//chk for combine
		ts[0]=res[resi-2];ts[1]=res[resi-1];
		if(mp.count(ts)>0){
			resi-=2;
			res[resi++]=mp[ts];
		}
		//chk for oppose
		for(int i=0;i<resi;i++)
		for(int j=0;j<resi;j++)
		if(i!=j){
			for(int k=0;k<oppi && resi>0;k++){
				if(opp[k][0]==res[i] && opp[k][1]==res[j])
					resi=0;
			}
		}
	}
	cout<<"[";
	for(int i=0;i<resi;i++){
		if(i)cout<<", ";
		cout<<res[i];
	}
	cout<<"]"<<endl;
	return;
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

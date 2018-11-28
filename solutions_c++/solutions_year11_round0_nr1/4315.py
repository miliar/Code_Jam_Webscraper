#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <cstring>

using namespace std;
int main(){
	
	int Test;int cnt=1;
	cin>>Test;
	char c[115];
	int val[115];
	while(Test--){
		int n;
		cin>>n;
		for(int i=0;i<n;i++){
			cin>>c[i]>>val[i];	
		}
		int poso=1,posb=1,chances=0,res=0;
		char who='X';
		for(int i=0;i<n;i++){
			if(c[i]=='O'){
				int t=abs(val[i]-poso);
				poso=val[i];
				//cout<<"hereO"<<res<<"t"<<t<<"CH"<<chances<<endl;
				if(who!='O'&&chances<t)
					res+=(t-chances);
				res+=1;
				if(who=='O'){
					res+=t;
					chances+=(t+1);
					////cout<<"here2"<<res;
				}else
					{
					if(t>chances)
					chances=(t-chances+1);else
					chances=1;
					who='O';}
			}else{
				int t=abs(val[i]-posb);
				posb=val[i];
				//cout<<"hereB"<<res<<"t"<<t<<"CH"<<chances<<endl;
				if(who!='B'&&chances<t)
					res+=(t-chances);
				res+=1;
				if(who=='B'){
					res+=t;
					chances+=(t+1);
					////cout<<"here2"<<res;
				}else
					{
					if(t>chances)
					chances=(t-chances+1);else
					chances=1;
					who='B';}		
			}
			//cout<<res<<endl;
		}
		cout<<"Case #"<<cnt++<<": "<<res<<endl;
	}
	return 0;
}
		

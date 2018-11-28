/*
LANG: C++
TASK: C
*/

#include <stdio.h>
#include <iostream>
#include <string.h>
#include <math.h>
#include <vector>
#include <set>
#include <queue>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <iomanip>

using namespace std;

int T,A,B;
int cnt;
string smallest,largest;

string itos(int x){
    string ret="";
    string temp;
    while(x!=0){
        temp=ret;
        ret=char('0'+x%10);
        ret+=temp;
        x/=10;
    }
    return ret;
}

int stoi(string s){
    int ret=0;
    int temp;
    for(int i=0; i<s.size(); i++){
        ret=(s[i]-'0')+ret*10;
    }
    return ret;
}

pair<int,int> power(int x){
    pair<int,int> ret=make_pair(0,1);
    while(x/10!=0){
        ret.second*=10;
        ret.first++;
        x/=10;
    }
    return ret;
}

int main(){
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	scanf("%d",&T);
	for(int i=1; i<=T; i++){
	    cnt=0;
	    scanf("%d %d",&A,&B);
	    smallest=itos(A);
	    largest=itos(B);
	    for(int j=A; j<=B; j++){
	        map<int,bool> mp;
	        pair<int,int> num=power(j);
	        int at=j;
	        //112 -> 211 -> 121
	        for(int k=0; k<num.first; k++){
	            int curr=(at%10)*num.second+at/10;
	            at=curr;
	            if(mp.find(curr)!=mp.end())
                    continue;
                else{
                    if(j<curr && curr<=B){
                        cnt++;
                        //cout<<j<<" "<<curr<<endl;
                        mp[curr]=true;
                    }
                }
	        }
	    }
		cout<<"Case #"<<i<<": "<<cnt<<endl;
	}
	return 0;
}

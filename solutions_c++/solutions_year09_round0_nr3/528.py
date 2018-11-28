#include<vector>
#include<list>
#include<map>
#include<set>
#include<queue>
#include<algorithm>
#include<sstream>
#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
using namespace std;

string target = "welcome to code jam";
string s;
int l;

int memo[500][19];

int go(int sindex, int tindex){

    if(tindex==19) return 1;
    if(sindex==l) return 0;

    int &m=memo[sindex][tindex];
    if(m!=-1) return m;

    int res=0;
    for(int i=sindex;i<l;i++)
	if(s[i]==target[tindex])
	    res=(res+go(i+1,tindex+1))%10000;

    return m=res;
}

main(){

    int T; scanf("%d\n",&T);
    for(int test=1;test<=T;test++){

        getline(cin,s);
	l=s.length();

	for(int i=0;i<l;i++)
	    for(int j=0;j<19;j++)
		memo[i][j]=-1;

	int x=go(0,0);
	string res="0000";
	for(int i=3;i>=0;i--){
	    res[i]+=x%10;
	    x/=10;
	}

	printf("Case #%d: %s\n",test,res.c_str());

    }
}

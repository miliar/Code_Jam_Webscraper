#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <queue>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <bitset>
#include <set>

#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,b) FOR(i,0,b)
#define sqr(a) ((a)*(a))

const double EPS=1e-5;
#define eq(a,b) (abs((a)-(b))<=EPS)

using namespace std;

char fin[]="a.in",fout[]="a.out";
int n,s,q,res;
map< string,int > xuj;
vector< bool > is;

int main(){
	freopen(fin,"r",stdin);
	freopen(fout,"w",stdout);
	scanf("%d",&n);
	string t;
	int top=0;
	map< string,int>::iterator it;
	REP(z,n){
		res=top=0;
		xuj.clear();
		scanf("%d\n",&s);
		is=vector< bool >(s,false);
		REP(i,s){
			getline(cin,t);
			xuj[t]=top++;
		}
		top=0;
		scanf("%d\n",&q);
		REP(i,q){
			getline(cin,t);
			it=xuj.find(t);
			if(it!=xuj.end())
				if(!is[xuj[t]]){
					is[xuj[t]]=true;
					top++;
					if(top==s){
						res++;
						is=vector< bool >(s,false);
						is[xuj[t]]=true;
						top=1;
					}
				}
		}
		printf("Case #%d: %d\n",z+1,res);
	}
	exit(0);
}

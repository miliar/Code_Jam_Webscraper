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

using namespace std;

#define FOR(i,a,b) for (int i(a); i < (b); i++) 
#define REP(i,n) FOR(i,0,n) 
#define SORT(v) sort((v).begin(),(v).end())
#define UN(v) sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define CL(a,b) memset(a,b,sizeof(a))
#define pb push_back

char rep[1000], dis[1000], s[1000];
vector<char> v;
int main(){
	int tc, c, d, n;
	cin >> tc;
	REP(t,tc){
		v.clear();
		rep[0]=dis[0]=s[0]='\0';
		cin >> c;
		if(c!=0)cin >> rep;
		cin >> d;
		if(d!=0)cin >> dis;
		cin >> n >> s;
		REP(i,n){
			bool flag=false;
			if(v.size()){
				for(int j=0;j<strlen(rep);j+=3){
					if((rep[j]==v.back()&&rep[j+1]==s[i])||(rep[j+1]==v.back()&&rep[j]==s[i])){
						v.pop_back();
						v.push_back(rep[j+2]);
						flag=true;
						break;
					}
				}
				int cnt=v.size();
				if(!flag){
					REP(j,v.size()){
						for(int k=0;k<strlen(dis);k+=2){
							if((dis[k]==v[j]&&dis[k+1]==s[i])||(dis[k+1]==v[j]&&dis[k]==s[i])){
								//for(int p=0;p<cnt;p++)v.pop_back();
								v.clear();
								flag=true;
								break;
							}
						}
						cnt--;
						if(flag)break;
					}
				}
			}
			if(!flag)v.push_back(s[i]);			
		}
		printf("Case #%d: [",t+1);
		REP(i,v.size()){
			printf("%c",v[i]);
			if(i!=v.size()-1)printf(", ");
		}
		puts("]");
	}
	return 0;
}

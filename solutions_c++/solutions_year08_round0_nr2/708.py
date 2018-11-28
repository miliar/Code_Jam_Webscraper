#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <map>
#include <set>
#include <list>
#include <deque>
#include <queue>
#include <numeric>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#define F(i,a,b) for(int i=(a);i<(b);++i)
#define Fe(it,v)for(__typeof__((v).begin()) it=(v).begin();it!=(v).end();++it)
#define all(x) (x).begin(),(x).end()
using namespace std;
int main(){
	int t[100000];
	int n,test=1;
	cin>>n;
	while(n--){
		int na,nb,T;
		cin>>T>>na>>nb;
		int ca=0,cb=0;
		int ra[2000]={},rb[2000]={};
		int ava[2000]={},avb[2000]={};
		//int eva[2000],evb[2000];
		vector<int> eva[2000];
		vector<int> evb[2000];
		F(i,0,na){
			string a,b;
			cin>>a>>b;
			int t1=((a[0]-'0')*10+(a[1]-'0'))*60+((a[3]-'0')*10+(a[4]-'0'));
			int t2=((b[0]-'0')*10+(b[1]-'0'))*60+((b[3]-'0')*10+(b[4]-'0'));
			ra[t1]++;
			eva[t1].push_back(t2+T);
			//avb[t2+T]++;
		}
		F(i,0,nb){
			string a,b;
			cin>>a>>b;
			int t1=((a[0]-'0')*10+(a[1]-'0'))*60+((a[3]-'0')*10+(a[4]-'0'));
			int t2=((b[0]-'0')*10+(b[1]-'0'))*60+((b[3]-'0')*10+(b[4]-'0'));
			rb[t1]++;
			evb[t1].push_back(t2+T);
			//ava[t2+T]++;
		}
		int reta=0,retb=0;
		priority_queue<int,vector<int>,greater<int> > Qa,Qb;
		F(i,0,60*24){
			F(j,0,ra[i]){
				Qb.push(eva[i][j]);
				if(Qa.empty()||Qa.top()>i){
					reta++;
				}
				else{
					Qa.pop();
				}
			}
			F(j,0,rb[i]){
				Qa.push(evb[i][j]);
				if(Qb.empty()||Qb.top()>i){
					retb++;
				}
				else{
					Qb.pop();
				}
			}
		}
		cout<<"Case #"<<test++<<": "<<reta<<" "<<retb<<endl;
	}
}

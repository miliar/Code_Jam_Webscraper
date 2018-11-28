#include<vector>
#include<cmath>
#include<map>
#include<cstdlib>
#include<iostream>
#include<sstream>
#include<string>
#include<algorithm>
#include<cstring>
#include<cstdio>
#include<set>
#include<stack>
#include<bitset>
#include<functional>
#include<cstdlib>
#include<ctime>
#include<queue>
#include<deque>
using namespace std;
#define pb push_back
typedef long long lint;
#define mp make_pair
#define fi first
#define se second
typedef pair<int,int> pint;
lint calc(lint a,lint b,lint n,vector <lint> c){
	lint sa=0;int i;
	vector <lint> ch;
	for(i=0;i<1010;i++) ch.pb(-1);
	for(i=0;i<n;i++) sa+=c[i];if(sa<=b) return a*sa;
	vector <lint> ke,ind;ke.pb(0);ind.pb(0);
	while(1){
		lint kei=0;
		for(i=0;i<n;i++){
			if(kei+c[((ind[ind.size()-1])+i)%n]>b){
				ind.pb(((ind[ind.size()-1])+i)%n);ke.pb(ke[ke.size()-1]+kei);break;
			}
			kei+=c[((ind[ind.size()-1])+i)%n];
		}
//		cout<<i<<endl;
		if(ch[ind[ind.size()-1]]>-1){
			i=ch[ind[ind.size()-1]];
			lint out=ke[i]+(a-i)/(ind.size()-1-i)*(ke[ke.size()-1]-ke[i]);
			out+=(ke[(a-i)%(ind.size()-1-i)+i]-ke[i]);
			return out;
		}
		else ch[ind[ind.size()-1]]=ind.size()-1;
//		cout<<ind[ind.size()-1]<<endl;
/*		for(i=0;i<ind.size()-1;i++){
			if(ind[i]==ind[ind.size()-1]){
				lint out=ke[i]+(a-i)/(ind.size()-1-i)*(ke[ke.size()-1]-ke[i]);
				out+=(ke[(a-i)%(ind.size()-1-i)+i]-ke[i]);
				return out;
			}
		}
*/		if(ke.size()>a) return ke[a];
	}
}
int main()
{
	vector <lint> out;
	int t,i,j,s;
	cin>>t;
	for(i=0;i<t;i++){
		lint a,b,n;vector <lint> c;
		cin>>a>>b>>n;
		for(j=0;j<n;j++){
			cin>>s;c.pb(s);
		}
		out.pb(calc(a,b,n,c));
	}
	for(i=0;i<t;i++){
		cout<<"Case #"<<i+1<<": "<<out[i]<<endl;
	}
	return 0;
}

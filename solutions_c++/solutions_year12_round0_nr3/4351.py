#include<deque>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<vector>
#include<algorithm>
#include<string>
#include<iostream>
#include<sstream>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std;
int main(){
	int h,i,j;
	freopen("i","r",stdin);
	freopen("o","w",stdout);
	int b[]={1,10,100,1000,10000,100000,1000000,10000000};
	int t;
	cin>>t;	
	for(h=1;h<=t;++h){
		int p,q;
		cin>>p>>q;
		set<pair<int,int> > a;
		for(i=p;i<q;++i){
			int ln;
			for(ln=1;i%b[ln]!=i;++ln);
			for(j=1;j<ln;++j){
				int r=i/b[ln-j]+i%b[ln-j]*b[j];
				if(r>i&&r<=q)
					a.insert(make_pair(i,r));
			}
		}
		cout<<"Case #"<<h<<": "<<a.size()<<endl;
	}
}
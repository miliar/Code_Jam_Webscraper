#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <utility>
#include <algorithm>
#include <iomanip>
#include <cmath>
using namespace std;

struct train{
	int d,a,f;
};

bool cmp(struct train a,struct train b) {
	if(a.a!=b.a) return a.a<b.a;
	return a.d<b.d;
}

int main() {
	ifstream cin ("B-large.in");
    ofstream cout ("B-large.out");
	int i,j,k,n,A,B,t,p,q,x,res;
	char ch;
	int c;
	struct train temp;
	vector<struct train> v;
	int s[200];
	string str;
	for(cin>>n,c=1;c<=n;c++) {
		v.resize(0);
		memset(s,0,sizeof(s));
		cin>>t>>A>>B;
		for(i=0;i<A+B;i++) {
			cin>>str;
			istringstream in1(str);
			in1>>j>>ch>>k;
			temp.d=60*j+k;
			cin>>str;
			istringstream in2(str);
			in2>>j>>ch>>k;
			temp.a=60*j+k;
			temp.f=(i<A?0:1);
			v.push_back(temp);
		}
		sort(v.begin(),v.end(),cmp);
		for(i=0;i<v.size();i++) {
			if(s[i]==1) continue;
			s[i]=1;
			k=i,p=v[i].f;
			while(1) {
				q=10000;
				for(j=0;j<v.size();j++) {
					if(s[j]==0&&v[j].f!=p&&v[k].a+t<=v[j].d) {
						if(v[j].d<q) q=v[j].d,x=j;
						//break;
					}
				}
				if(q==10000) break;
				else p^=1,k=x,s[k]=1,(v[k].f==0?A:B)--;
				//if(j==v.size()) break;
			}
		}
		cout<<"Case #"<<c<<": "<<A<<" "<<B<<endl;
	}
}
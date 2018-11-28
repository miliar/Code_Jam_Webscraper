#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <algorithm>

using namespace std;

int n,A[500],B[500],S[500],res,mm=0;
bool use[500];
struct qqQ {
	int a,b;
} Q[500];
int F[500];
const int inf =1000000000;

void can() {
	int L=0;
	for (int i=0; i<n; i++)
		if (use[S[i]]) {
			Q[L].a=A[i];
			Q[L].b=B[i];
			L++;
		}
	int cc=inf;
	for (int i=0; i<L; i++) {
		F[i]=inf;
		if (Q[i].a<=1) F[i]=1;
		else { 
			for (int j=0; j<i; j++)
				if (Q[j].b+1>=Q[i].a && F[i]>F[j]+1)
					F[i]=F[j]+1;
		}
		if (Q[i].b>=10000 && cc>F[i])
			cc=F[i];
	}
	if (cc<res)
		res=cc;
}

void gen(int p, int t, int st) {
	if (t>3) return;
	can();
	for (int i=st; i<=mm; i++)
		if (!use[i]) {
			use[i]=true;
			gen(0,t+1,i+1);
			use[i]=false;
		}
}

int main() {
	ifstream cin("B-large.in");
	ofstream cout("B-large.out");
	int T; cin>>T;
	for (int o=1; o<=T; o++) {
		map<string, int> SS;
		cin>>n; mm=-1;
		for (int i=0; i<n; i++) {
			string s;
			cin>>s>>A[i]>>B[i];
			if (SS.count(s)==0)
				S[i]=SS[s]=++mm;
			else
				S[i]=SS[s];
		}
		for (int j=0; j<n; j++)
			for (int i=0; i<n-1; i++)
				if (B[i]>B[i+1] || (B[i]==B[i+1] && A[i]<A[i+1])) {
					int tmp=A[i]; A[i]=A[i+1]; A[i+1]=tmp;
					tmp=B[i]; B[i]=B[i+1]; B[i+1]=tmp;
					tmp=S[i]; S[i]=S[i+1]; S[i+1]=tmp;
				}
		res=inf;
		memset(use,false,sizeof use);
		gen(0,0,0);
		if (res==inf)
			cout<<"Case #"<<o<<": "<<"IMPOSSIBLE"<<endl;
		else
			cout<<"Case #"<<o<<": "<<res<<endl;
	}
	return 0;
}
#include<iostream>
#include<vector>
using namespace std;
void computeinstance(int thiscase) {
    int n,pi;
    char ci;
    vector<char> c;
    vector<int> p;
    int po,to,pb,tb;
    po=1;
    pb=1;
    to=0;
    tb=0;
    cin>>n;
    for(int i=0;i<n;i++) {
	cin>>ci>>pi;
	c.push_back(ci);
	p.push_back(pi);
    }
    for(int i=0;i<n;i++) {
	if(c[i]=='O') {
	    to=max(tb,to+abs(po-p[i]))+1;
	    po=p[i];
	}
	else {
	    tb=max(to,tb+abs(pb-p[i]))+1;
	    pb=p[i];
	}
    }
    cout<<"Case #"<<thiscase<<": "<<max(to,tb)<<endl;
}
int main(void) {
    int t;
    cin>>t;
    for(int i=0;i<t;i++) {
	computeinstance(i+1);
    }
}

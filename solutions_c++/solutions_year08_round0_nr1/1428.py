#include <vector>
#include <string>
#include <iostream>
#include <stdio.h>


using namespace std;

int N,Q,S,i,j,curpos,maxp,p,res,switch_c;
	vector<string> e, q;
	char tmp[102];

	int findmatch(int startpos, string s) {
		for(int k=startpos;k<Q;k++) {
			if(s == q[k]) return k;
		}
		return -1;
	}


int main() {
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	cin >> N;
	for(i=0;i<N;i++) {
		cin >> S;
		gets(tmp);
		e.clear();
		q.clear();
		for(j=0;j<S;j++) {
			gets(tmp);
			e.push_back(tmp);
		}
		cin >> Q;
		gets(tmp);
		for(j=0;j<Q;j++) {
			gets(tmp);
			q.push_back(tmp);
		}
		curpos=0;
		switch_c=-1;
		while(true) {
			maxp=0;
			res=-1;
			switch_c++;
			for(j=0;j<S;j++) {
				p=findmatch(curpos, e[j]);
				if(p == -1) {
					// ok
					res=switch_c;
					break;
				}
				else if(p>maxp) {
					maxp=p;
				}
			}
			if(res>-1) {
				break;
			}
			curpos = maxp;
		}
		cout<< "Case #"<<(i+1)<<": "<<res<<endl;
	}
	return 0;
}

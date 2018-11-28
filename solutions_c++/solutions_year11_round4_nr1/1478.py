#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <iomanip>
using namespace std;

#define FILENAME "A-large"

struct cor {
	int b,e,w;
	bool operator<(const cor c2) const {
		return b<c2.b;
	}
};

struct st {
	int l,v;
	st() {}
	st(int al, int av) {
		v=av; l=al;
	}
	bool operator<(const st s2) const {
		return v<s2.v;
	}
};

int main(int argc, char *argv[]) {
	
	ifstream fin(FILENAME".in");
	ofstream fout(FILENAME".out");
	
	int C;
	cor cr[1001];
	fin>>C;
	for (int c=0;c<C;c++) {
		int x,n,s,r,t;
		fin>>x>>s>>r>>t>>n;
		for (int i=0;i<n;i++) {
			fin>>cr[i].b>>cr[i].e>>cr[i].w;
		}
		sort(cr,cr+n);
		vector<st> v;
		int p=0, ic=0;
		while (p<x) {
			while (ic<n && (p>cr[ic].b)) ic++;
			if (ic>=n) {
				v.push_back(st(x-p,s));
				break;
			} else {
				if (cr[ic].b!=p) {
					v.push_back(st(cr[ic].b-p,s));
					p=cr[ic].b;
				}
				v.push_back(st(cr[ic].e-cr[ic].b,cr[ic].w+s));
				p=cr[ic].e;
			}
		}
		sort(v.begin(),v.end());
		double f=0, tt=t,m;
		int vl=v.size();
		for (int i=0;i<vl;i++) {
			if (tt<=0) {
				f+=double(v[i].l)/v[i].v;
			} else {
				m=tt*(v[i].v-s+r);
				if (m>=v[i].l) {
					f+=double(v[i].l)/(v[i].v-s+r);
					tt-=double(v[i].l)/(v[i].v-s+r);
				} else {
					f+=tt; tt=0;
					f+=double(v[i].l-m)/(v[i].v);
				}
			}
		}
		
		fout<<"Case #"<<c+1<<": "<<setprecision(20)<<fixed<<f<<endl;
	}
	
	fin.close();
	fout.close();
	return 0;
	
}


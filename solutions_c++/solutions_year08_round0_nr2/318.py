#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <list>
#include <algorithm>
using namespace std;

ifstream fin("in.txt");
ofstream fout("out.txt");

struct H {
	int h,m;
};

bool operator<(const H& h1, const H& h2) {
	if(h1.h<h2.h)return true;
	if(h1.h>h2.h)return false;
	if(h1.m<h2.m)return true;
	return false;
}

struct S {
	H a,d;
	bool b; // if b then from A to B
};

bool operator<(const S& s1, const S& s2) {
	if(s1.d<s2.d)return true;
	if(s2.d<s1.d)return false;
	if(s1.a<s2.a)return true;
	return false;
}

vector<S> vec;
vector<H> veca;
vector<H> vecb;
int reta,retb;

int main() {
	int n;
	fin>>n;
	int t,T,na,nb;
	int i;
	S tmp;
	string s;bool bo;
	vector<H>::iterator it;
	H th;
	for(t=1;t<=n;t++) {
		reta=0;retb=0;
		fin>>T;
		fin>>na>>nb;
		vec.clear();
		veca.clear();
		vecb.clear();
		for(i=0;i<na;i++) {
			tmp.b=true;
			fin>>s;
			tmp.d.h = (s[0]-'0')*10 + (s[1]-'0');
			tmp.d.m = (s[3]-'0')*10 + (s[4]-'0');
			fin>>s;
			tmp.a.h = (s[0]-'0')*10 + (s[1]-'0');
			tmp.a.m = (s[3]-'0')*10 + (s[4]-'0');
			vec.push_back(tmp);
		}
		for(i=0;i<nb;i++) {
			tmp.b=false;
			fin>>s;
			tmp.d.h = (s[0]-'0')*10 + (s[1]-'0');
			tmp.d.m = (s[3]-'0')*10 + (s[4]-'0');
			fin>>s;
			tmp.a.h = (s[0]-'0')*10 + (s[1]-'0');
			tmp.a.m = (s[3]-'0')*10 + (s[4]-'0');
			vec.push_back(tmp);
		}
		sort(vec.begin(),vec.end());
		//for(i=0;i<vec.size();i++) {
			//if(vec[i].b)cout<<"A->B"<<endl;
			//else cout<<"B->A"<<endl;
			//cout<<"departure "<<vec[i].d.h<<":"<<vec[i].d.m<<endl;
			//cout<<"arrive "<<vec[i].a.h<<":"<<vec[i].a.m<<endl;
		//}
		for(i=0;i<vec.size();i++) {
			bo=false;
			if(vec[i].b) {
				// from A
				bo=false;
				for(it=veca.begin();it!=veca.end();it++) {
					if(vec[i].d<(*it))continue;
					bo=true;
					veca.erase(it);
					break;
				}
				if(!bo)reta++;
				th = vec[i].a;
				th.m+=T;
				if(th.m>=60) {
					th.m-=60;
					th.h++;
				}
				vecb.push_back(th);
			}
			else {
				// from B
				bo=false;
				for(it=vecb.begin();it!=vecb.end();it++) {
					if(vec[i].d<(*it))continue;
					bo=true;
					vecb.erase(it);
					break;
				}
				if(!bo)retb++;
				th = vec[i].a;
				th.m+=T;
				if(th.m>=60) {
					th.m-=60;
					th.h++;
				}
				veca.push_back(th);
			}
		}
		fout<<"Case #"<<t<<": "<<reta<<" "<<retb<<endl;
		//cout<<"----------"<<endl;
	}
	return 0;
}
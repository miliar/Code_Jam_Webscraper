#include <algorithm>  
#include <iostream>  
#include <sstream>  
#include <string>  
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <list>  
using namespace std;
// for size length iterator begin end push_back int char string vector stringstream
#define foreach(it,v) for( typeof((v).begin()) it = (v).begin(); it!= (v).end();++it)
#define present(c,x) ( (c).find((x)) != (c).end() )
#define all(v) (v).begin(), (v).end() 
template <class T> void dump(T& v) { foreach(it,v) cout<< *it<<' '; cout << endl;}
#define FOR(i,m,n) for(int i=(m);i<=(int)(n);i++)
#define rep(i,n) FOR(i,0,(n)-1)

using namespace std;

string readln() {
    string s="";
    char buf[10000];
    cin.getline(buf,10000);
    s=buf;
    return s;
}

vector<int> readIntLines(int num) {
	vector<int> retval;
	rep(i,num) {
		int s;
		scanf("%d\n",&s);
		retval.push_back(s);
	}
	return retval;
}

vector<string> readStringLines(int num) {
	vector<string> retval;
	rep(i,num) {
		retval.push_back(readln());
	}
	return retval;
}

string inttos(int a) {
    char buf[100];
    sprintf(buf,"%d",a);
    return buf;
}


void printv(vector<string> v) {
	rep(i,v.size()) {
		rep(j,v.size()) {
			cout << v[i][j];
		}
		cout <<"\n";
	}
}
string cons(int num) {
	string s="";
	rep(i,num) {
		s+=".";
	}
	return s;
}
vector<string> rotate(vector<string> v) {
	vector<string> ret;
	int n=v.size();
	rep(i,v.size()) {
		string s="";
		rep(j,v[i].size()) {
			if(v[i][j] != '.') {
				s=s+v[i][j];
			}
		}
		s=cons(n-s.size())+s;
		ret.push_back(s);
	}
	return ret;
}

bool hasit(vector<string> v, char c, int k) {
	rep(i,v.size()) {
		rep(j,v.size()) {

			int hasit=true;
			for(int x=0;x<k;x++) {
				if(j+x>=v.size() || v[i][j+x] != c) {
					hasit=false;
					break;
				}
			}
			if(hasit) return true;

			hasit=true;
			for(int x=0;x<k;x++) {
				if(i+x>=v.size() || v[i+x][j] != c) {
					hasit=false;
					break;
				}
			}
			if(hasit) return true;

			hasit=true;
			for(int x=0;x<k;x++) {
				if(j+x>=v.size() || i+x>=v.size() || v[i+x][j+x] != c) {
					hasit=false;
					break;
				}
			}
			if(hasit) return true;
			hasit=true;

			for(int x=0;x<k;x++) {
				if(j-x <0 || i+x>=v.size() || v[i+x][j-x] != c) {
					hasit=false;
					break;
				}
			}
			if(hasit) return true;
		}
	}
	return false;
}

map<string,bool> emap;

void e(string s) {
	emap[s]=true;
	for(int i=s.size()-1;i>0;i--) {
		if(s[i]=='/') {
			emap[s.substr(0,i)]=true;
		}
	}
}

int c(string s) {
	if(present(emap,s)) {
		return 0;
	}
	int cc=0;
	for(int i=s.size()-1;i>0;i--) {
		if(s[i]=='/') {
			cc++;
			if(present(emap,s.substr(0,i))) {
				e(s);
				return cc;
			}
		}
	}
	e(s);
	return cc+1;

}

string main_fn(vector<string> exist,vector<string> create)
{
	emap.clear();
    string retval="";
	int ret=0;
	rep(i,exist.size()) {
		e(exist[i]);
	}
	rep(i,create.size()) {
		ret+=c(create[i]);
	}


    return inttos(ret);
}

int main()
{
	vector<string> answers;
	int T;
	scanf("%d\n",&T);
    rep(i,T)
    {
		cerr << i+1<<" .... ";
		int N=0,M=0;
		scanf("%d %d\n",&N,&M);
		vector<string> exist;
		vector<string> create;
		for(int j=0;j<N;j++) {
			exist.push_back(readln());
		}
		for(int j=0;j<M;j++) {
			create.push_back(readln());
		}


		answers.push_back(main_fn(exist,create));
		cerr << "done\n";
    }
    rep(i,T) {
        cout << "Case #"<<i+1<<": "<<answers[i]<<"\n";
	}
} 

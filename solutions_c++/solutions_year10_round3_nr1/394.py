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

string main_fn(int n, vector<int> a, vector<int> b)
{
    string retval="";
	int ret=0;
	rep(i,n) {
		for(int j=i+1;j<n;j++) {
			if( (a[i] < a[j] && b[i] > b[j]) ||
					(a[i] > a[j] && b[i] < b[j])) {
				ret++;
			}
		}
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
		int N=0;
		scanf("%d\n",&N);
		vector<int> a,b;
		for(int i=0;i<N;i++) {
			int ai,bi;
			scanf("%d %d\n",&ai,&bi);
			a.push_back(ai);
			b.push_back(bi);
		}

		answers.push_back(main_fn(N,a,b));
		cerr << "done\n";
    }
    rep(i,T) {
        cout << "Case #"<<i+1<<": "<<answers[i]<<"\n";
	}
} 

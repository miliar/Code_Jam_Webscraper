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
    char buf[1000];
    cin.getline(buf,1000);
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

string main_fn(int n, int k)
{
	for(int i=0;i<n;i++) {
		if(!((1 << i) & k)) return "OFF";
	}
    return "ON";
}

int main()
{
	vector<string> answers;
	int T;
	scanf("%d\n",&T);
    rep(i,T)
    {
		int N,K;
		scanf("%d %d\n",&N,&K);
		answers.push_back(main_fn(N,K));
    }
    rep(i,T) {
        cout << "Case #"<<i+1<<": "<<answers[i]<<"\n";
	}
} 

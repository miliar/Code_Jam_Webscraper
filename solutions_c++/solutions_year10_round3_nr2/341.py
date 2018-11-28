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

double lgbas(double x, double base) {
	return log(x)/log(base);
}
int doit(int l,int p,int c) {
	if( (double)p/c <=l ) return 0;
	if( (double)l*c >=p ) return 0;
	int r = ceil(ceil(lgbas( (double) p/l , c))/2) ;

	int m1=l*pow(c,r);
	int m2=ceil(p/pow(c,r));


	if( (double)p/c <= m1 && (double)m1/c<=l) return 1;
	if( (double)p/c <= m2 && (double)m2/c<=l) return 1;

	int a1=doit(l,m1,c)+1;
	int a2=doit(m1,p,c)+1;

	int ax=a1>a2? a1:a2;

	int b1=doit(l,m2,c)+1;
	int b2=doit(m2,p,c)+1;

	int bx=b1>b2?b1:b2;



	return  ax<bx?ax:bx;
}


string main_fn(int l, int p, int c)
{
    string retval="";
	int ret=doit(l,p,c);
	
	//int ret = ceil(ceil(lgbas( (double) p/l , c))/2) ;
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
		int l,p,c;
		scanf("%d %d %d\n",&l,&p,&c);

		answers.push_back(main_fn(l,p,c));
		cerr << "done\n";
    }
    rep(i,T) {
        cout << "Case #"<<i+1<<": "<<answers[i]<<"\n";
	}
} 

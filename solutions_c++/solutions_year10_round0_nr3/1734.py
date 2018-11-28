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
// for size length iterator begin end push_back long char string vector stringstream
#define foreach(it,v) for( typeof((v).begin()) it = (v).begin(); it!= (v).end();++it)
#define present(c,x) ( (c).find((x)) != (c).end() )
#define all(v) (v).begin(), (v).end() 
template <class T> void dump(T& v) { foreach(it,v) cout<< *it<<' '; cout << endl;}
#define FOR(i,m,n) for(long i=(m);i<=(long)(n);i++)
#define rep(i,n) FOR(i,0,(n)-1)

using namespace std;

string readln() {
    string s="";
    char buf[10000];
    cin.getline(buf,10000);
    s=buf;
    return s;
}

/**
 * assumes newline after last long by default
 */
vector<long> readIntLines(long num,bool newlineAfterEveryInt=false) {
	vector<long> retval;
	string scanpattern="%d";
	if(newlineAfterEveryInt) scanpattern+="\n";
	rep(i,num) {
		long s;
		scanf(scanpattern.c_str(),&s);
		retval.push_back(s);
	}
	if(!newlineAfterEveryInt) scanf("\n");
	return retval;
}

vector<string> readStringLines(long num) {
	vector<string> retval;
	rep(i,num) {
		retval.push_back(readln());
	}
	return retval;
}

string longtos(long a) {
    char buf[100];
    sprintf(buf,"%ld",a);
    return buf;
}

long getRotated(long i, long r, long max) {
	return (i+r) % max;
}

string main_fn(long R, long k, long N, vector<long> g,int c)
{
    string retval="";
	long r=0;
	map<long,long> rtoi;
	map<long,long> itol;
	vector<long> rs;

	long i=0;

	while(!present(rtoi,r) ) {
		rs.push_back(r);
		rtoi[r]=i;
		long l=0;
		long j=0;
		while(j<g.size()) {
			long lt=l+g[getRotated(j,r,g.size())];
			if(lt<=k) {
				l=lt;
				j++;
			} else 
				break;
		}
		itol[i++]=l;
		r=getRotated(j,r,g.size());
	}

	long long retlong=0;
	if( R <= rs.size()) {
		for(long k=0;k<R;k++) {
			retlong+=itol[k];
		}
	}else {
		int numrep=(rs.size()-rtoi[r]);
		for(int k=0;k<rtoi[r];k++) {
			retlong+=itol[k];
			R--;
		}
		for(int k=0;k<R % numrep;k++) {
			retlong+=itol[rtoi[r]+k];
		}
		long long x=0;
		for(int k=0;k<rs.size();k++) {
			x+=itol[rtoi[r]+k];
		}
		retlong+=(x* ((long)( R / numrep )));
	}

		cout << "Case #"<<c<<": "<<retlong<<"\n";;


    return longtos(retlong);

}

int main()
{
	vector<string> answers;
	int T;
	scanf("%d\n",&T);
    rep(i,T)
    {
		int R,k,N;
		scanf("%d %d %d\n",&R,&k,&N);
		answers.push_back(main_fn(R,k,N,readIntLines(N),i+1));
    }
    rep(i,T) {
        //cout << "Case #"<<i+1<<": "<<answers[i]<<"\n";
	}
} 

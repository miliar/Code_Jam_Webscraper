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

vector<int> readAllIntsOnLine(string line) {
	vector<int> retval;
	stringstream ss(line);
	int i;
	while(ss>>i) {
		retval.push_back(i);
	}
	return retval;
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


void sort(vector<double> a, vector<int> index) {
	rep(i,a.size()) {
		for(int j=i+1;j<a.size();j++) {
			if(a[i] < a[j]) {
				double t=a[i];
				a[i]=a[j];
				a[j]=t;

				int tt=index[i];
				index[i]=index[j];
				index[j]=tt;
			}
		}
	}
}

string main_fn(int n,int k,int b,int t,vector<int> x,vector<int> v)
{
	if(k==0) return "0";
    string retval="";
	vector<double> a;
	rep(i,x.size()) {
		a.push_back( ((double)b-x[i])/v[i] );
	}
	vector<int> in;
	rep(i,x.size()) {
		in.push_back(i);
	}
	sort(a,in);
	set<int> arr;
	rep(i,n) {
		if(a[i]<=t) {
			arr.insert(in[i]);
		}
	}
	if(arr.size() < k  ) return "IMPOSSIBLE";
	vector<int> oz;
	rep(i,n) {
		if(present(arr,i)) {
			oz.push_back(1);
		} else {
			oz.push_back(0);
		}
	}

	int fi=n-1;
	int c=0;
	int swaps=0;
	for(int i=fi;i>=0;i--) {
		if(c == k ) break;
		if(oz[i] == 1) {c++;continue;}
		else swaps+=(k-c);
	}



    return inttos(swaps);
}

int main()
{
	vector<string> answers;
	int C;
	scanf("%d\n",&C);
    rep(i,C)
    {
		int n,k,b,t;
		cerr << i+1<<" .... ";
		scanf("%d %d %d %d\n",&n,&k,&b,&t);
		vector<int> x=readAllIntsOnLine(readln());
		vector<int> v=readAllIntsOnLine(readln());
		answers.push_back(main_fn(n,k,b,t,x,v));
		cerr << "done\n";
    }
    rep(i,C) {
        cout << "Case #"<<i+1<<": "<<answers[i]<<"\n";
	}
} 

#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <functional>
#include <cmath>
#include <sstream>
#include <memory.h>
     
#define forn(i,n) for (int i = 0; i < (int)(n); i++)
#define forv(i, a) for(int i=0; i<(int)a.size(); i++)
#define all(a) a.begin(),a.end()
#define mp make_pair
#define pb push_back
#define sz size()
#define VI vector< int >
#define VS vector< string >
#define PII pair< int,int >
#define PDD pair< double,double >
#define PIS pair< int, string >
#define sqr(a) ((a)*(a))
#define cube(a) ((a)*(a)*(a))
#define pi 3.1415926535897932384626433832795
const int inf=500*1000*1000;
#define eps 1e-6
#define ll long long
using namespace std;

int cnt[28];
int opposed[28];
int a[28][28];
int seq[200];
int t;

void clear(){
	t=0;
	forn(i, 28) cnt[i]=0;
}

void go(){
	if(t<2) return;

	if(a[seq[t-1]][seq[t-2]]!=-1){
		cnt[seq[t-1]]--;
		cnt[seq[t-2]]--;
		
		int z=a[seq[t-1]][seq[t-2]];
		seq[t-2]=z;
		t--;
		cnt[z]++;
		go();
	}
	else{
		if(opposed[seq[t-1]]!=-1 && cnt[opposed[seq[t-1]]]>0) clear();
	}

}


int main(){
    freopen("B-small.in", "r", stdin);
    freopen("B-small.out", "w", stdout);

	int T, n, d, c;
	char trans[5];
	string str;

	cin>>T;

	forn(q, T){
		t=0;
		forn(i, 28){
			cnt[i]=0;
			opposed[i]=-1;
			forn(j, 28) a[i][j]=-1;
		}

		cin>>c;

		forn(i, c){
			cin>>trans;
			forn(j, 3) trans[j]-='A';

			a[trans[0]][trans[1]]=trans[2];
			a[trans[1]][trans[0]]=trans[2];
		}

		cin>>d;

		forn(i, d){
			cin>>trans;
			forn(j, 2) trans[j]-='A';

			opposed[trans[0]]=trans[1];
			opposed[trans[1]]=trans[0];
		}

		cin>>n;
		cin>>str;

		forn(i, n){
			seq[t++]=str[i]-'A';
			cnt[str[i]-'A']++;

			go();
		}

		cout<<"Case #"<<q+1<<": [";
		forn(i, t){
			cout<<(char)(seq[i]+'A');
			if(i!=t-1) cout<<", ";
		}
		cout<<"]"<<endl;
	}

	return 0;
}
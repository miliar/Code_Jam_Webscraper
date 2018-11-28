#include<iostream>
#include<fstream>
#include<sstream>
#include<string>
#include<vector>
#include<cmath>
#include<ctime>
#include<algorithm>
#include <map>

using namespace std;
#define SZ(v) ((int)v.size())
#define FOR(i,b,e) for(int i = b;i < e; ++i)
#define REP(i,v) FOR(i,0,SZ(v))
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef vector<char> VC;
typedef long long int64;
typedef unsigned long long uint64;
const double pi=acos(-1.0);
const double eps=1e-11;
#define zero(x) memset(&x, 0, sizeof x);
//int toInt(string s){istringstream si(s);int i;si>>i;return i;}
//string toString(int i){ostringstream so;so<<i;return so.str();}
VS words;	
int L,D,N;
int ts,l;
char ch[10000];

bool check(string s,int ll){
	int ben=0,end=D-1;
	bool f=false;
	while(ben<end-1){
		int mid=(ben+end)/2;
		if (words[mid].substr(0,ll)>s) end=mid;
		else if (words[mid].substr(0,ll)<s) ben=mid;
		else {f=true;break;}
	}
	if (f==false){
		if (words[ben].substr(0,ll)==s) f=true;
		if (words[end].substr(0,ll)==s) f=true;
	}
	return f;

}
int go(string s,int n,int len){
	int be=0;
	if (n==l)
	{
		if (check(s,len)) ++ts;

	
	}else{
		
		if (len>0&&check(s,len)==false) return 0; 



		if (ch[n]!='(') {
			go(s+ch[n],n+1,len+1);
		}
		else{
			++n;be=n;
			while(ch[n]!=')')  {++n;}
			++n;

			FOR(i,be,n-1)
			go(s+ch[i],n,len+1);
		
		}
	
	}
	return 0;
}

int main(){

	freopen("A-small-attempt1.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>L>>D>>N;

	FOR(i,0,D){
		cin>>ch;
		words.push_back(ch);
	}
	sort(words.begin(),words.end());

	FOR(i,0,N){
		ts=0;
		cin>>ch;
		l=strlen(ch);
		go("",0,0);
		cout<<"Case #"<<i+1<<": "<<ts<<endl;
	}


	return 0;

}
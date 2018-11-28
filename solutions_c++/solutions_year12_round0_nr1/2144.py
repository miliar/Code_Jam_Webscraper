//#pragma comment(linker, "/STACK:100000000")
#include <iostream>   
#include <sstream>   
#include <cstdio>   
#include <cstdlib>   
#include <cmath>   
#include <memory>   
#include <cctype>   
#include <string>   
#include <vector>   
#include <list>   
#include <queue>   
#include <deque>   
#include <stack>   
#include <map>   
#include <set>   
#include <algorithm>   
using namespace std;  
   
#define FOR(i,a,b) for(int (i) = (a); (i) < (b); ++(i))  
#define RFOR(i,a,b) for(int (i) = (a)-1; (i) >= (b); --(i))  
#define CLEAR(a) memset((a),0,sizeof(a))  
#define INF 1000000000  
#define PB push_back  
#define ALL(c) (c).begin(), (c).end()  
#define pi 2*acos(0.0)  
#define SQR(a) (a)*(a)  
#define MP make_pair  
#define CONST 1000
#define MAX 2300
#define mod 1000000007
#define X                       first
#define Y                       second.first
#define Z                       second.second
   
typedef long long LL; 
typedef long long i64; 
typedef pair<LL,LL>           PII;
typedef vector<LL>             VI;

int pr[300];
int main()
{
	freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
	string s1,d1;
	FOR(i,0,300)
		pr[i]=i;
	pr['q']='z';
	pr['z']=char('a'+16);
	s1="ejp mysljylc kd kxveddknmc re jsicpdrysi";
	d1="our language is impossible to understand";
	//swap(s1,d1);
	FOR(i,0,s1.size())
		pr[s1[i]]=d1[i];
	s1="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	d1="there are twenty six factorial possibilities";
	//swap(s1,d1);
	FOR(i,0,s1.size())
		pr[s1[i]]=d1[i];
	s1="de kr kd eoya kw aej tysr re ujdr lkgc jv";
	d1="so it is okay if you want to just give up";
	//swap(s1,d1);
	FOR(i,0,s1.size())
		pr[s1[i]]=d1[i];

	int n;
	cin>>n;
	getline(cin,s1);
	FOR(t,1,n+1){
		string s;
		getline(cin,s);
		cout<<"Case #"<<t<<": ";
		FOR(i,0,s.size())
			cout<<char(pr[s[i]]);
		cout<<endl;
	}

	
    return 0;
}
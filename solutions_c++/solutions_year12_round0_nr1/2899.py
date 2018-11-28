/*************************************************************
 ********                    Vikash Gupta             ********
 ********                     IIT2009088              ********
 ********                   IIIT Allahabad            ********
 ***************************************************************/


/************Header Files****************/
#include<iostream>
#include<cstdio>
#include<cmath>
#include<vector>
#include<cstdlib>
#include<climits>
#include<map>
#include<utility>
#include<stack>
#include<queue>
#include<cstring>
#include<string>
#include<algorithm>
#include<numeric>

using namespace std;

/*************** Prototypes ****************/
#define MAX 1e9
#define MIN 1e-9
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define FORR(i,a,b) for(int i=b-1;i>=a;i--) 
#define REPR(i,n) FORR(i,0,n)
#define sz size()
#define all(c) c.begin(),c.end()
#define mp make_pair
#define fill(ar,val) memset(ar,val,sizeof ar)
#define FORE(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define S(n) scanf("%d",&n)
#define SL(n) scanf("%ld",&n)
#define SC(c) scanf("%c",c)
#define SCS(s) scanf("%s",s)
#define SS(s) scanf("%s",s.c_str())
#define SD(d) scanf("%lf",&d)
#define acc(s,n) accumulate(s,s+n,0)
#define pb push_back

typedef long long ll;
typedef vector<int> VI;
typedef vector<string> VS;
typedef map<int,int> MII;
typedef map<int,string> MIS;
typedef map<string,int> MSI;
typedef pair<int,int> PII;
typedef pair<string,string> PSS;
typedef pair<int,string> PIS;
typedef pair<string,int> PSI;

/**************** execution function main is being begin *********************/

int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("output.txt","w",stdout);

	int a[200];
	fill(a,0);

	string s1="abcdefghijklmnopqrstuvwxyz";
	string s2="yhesocvxduiglbkrztnwjpfmaq";

	REP(i,26) a[s1[i]]=s2[i];

	int t;
	string t1;
	getline(cin,t1);
	t=atoi(t1.c_str());

	REP(j,t) {
		string s;
		getline(cin,s);
		int l=s.length();

		cout<<"Case #"<<j+1<<": ";

		REP(i,l) {
			if(s[i]==' ') cout<<s[i];
			else {
				char c=a[s[i]];
				cout<<c;
			}
		}

		cout<<endl;
	}
}

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
	//freopen("input.txt","r",stdin);
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	int t;
	cin>>t;

	REP(j,t) {
		int n,s,p;
		S(n),S(s),S(p);
		//cin>>n>>s>>p;

		int t[n],a[n],ch[n];
		fill(ch,0);

		cout<<"Case #"<<j+1<<": ";

		REP(i,n) S(t[i]);

		sort(t,t+n);

		int ans=0;

		if(s==0) {
			REP(i,n) {
				if(t[i]==0) a[i]=t[i];
				else if(t[i]%3==0) a[i]=t[i]/3; 
				else if(t[i]%3==1) a[i]=t[i]/3+1;
				else if(t[i]%3==2) a[i]=t[i]/3+1;
			}

			REP(i,n) if(a[i]>=p) ans++;
			cout<<ans<<endl;
		}
		else {
			REPR(i,n) {
				if(t[i]==0) a[i]=t[i];
				else if(t[i]%3==1) a[i]=t[i]/3+1;
				else if(t[i]%3==2) {
				       if(t[i]/3+1<p && s) {a[i]=t[i]/3+2;s--;}
				       else a[i]=t[i]/3+1;
				}
				else if(t[i]%3==0) {
					if(t[i]/3<p && s) {a[i]=t[i]/3+1;s--;}
					else a[i]=t[i]/3;
				}
			
			}

			REP(i,n) if(a[i]>=p) ans++;
			cout<<ans<<endl;

		}
	}

}

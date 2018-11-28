#include<vector>
#include<iostream>
#include<sstream>
#include<iomanip>
#include<set>
#include<string.h>
#include<map>
#include<algorithm>
#include<cassert>
#include<cstdio>
#include<cstdlib>
#include<queue>
#include<stack>
#include<ctype.h>
#include<cmath>
#include<locale>
using namespace std;

#define all(c) (c).begin(), (c).end()
#define iter(c) __typeof((c).begin())
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define tr(c, i) for (iter(c) i = (c).begin(); i != (c).end(); ++i)
#define pb push_back
#define mp make_pair
#define fia(i,a,b) for(int i=(int)(a);i<(int)(b);i++)
#define fib(i,a,b) for(int i=(int)(b);i>(int)(a);i--)
#define ipow(a,b) (int)pow((double)a,(double)b)
#define fill(a,b) memset(a,b,sizeof(a))
#define inp(n) scanf("%d",&n)
#define MOD 1000000007
typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<string> vs;
typedef vector<vi> vvi;
typedef  unsigned long long ull;
int main()
{
	
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int n,a,b;
	cin>>n;
	
	rep(i,n)
	{
		cin>>a>>b;
		int cnt= 0;
		set<pair<string,string> > set1;	
		for(int j = a; j<=b ; j++){
			for(int k = j+1; k <=b ;k++){
				std::string s1;
				std::stringstream out1;
				out1 << j;
				s1 = out1.str();
				std::string s2;
				std::stringstream out2;
				out2 << k;
				s2 = out2.str();
				string s3 = s1, s4 = s2;
				sort(all(s1));
				sort(all(s2));
				if(s1==s2){
					bool boo = false;
					for(int l = 0; l < s4.size(); l++){
						string temp=  s4.substr(l,s4.size()-l) + s4.substr(0,l);
						//cout<<s3<<" "<<temp<<endl;
						if(temp== s3){
							boo = true;
						}
					}
					for(int l = 0; l < s3.size(); l++){
						string temp=  s3.substr(l,s3.size()-l) +s3.substr(0,l);
						//cout<<s4<<" "<<temp<<endl;
						if(temp== s4){
							boo = true;
						}
					}
					if(boo)
					cnt++;
				}	
				
				
			}
		}
				
		cout<<"Case #"<<i+1<<": "<<cnt<<endl;
	}	
	return 0;
}	
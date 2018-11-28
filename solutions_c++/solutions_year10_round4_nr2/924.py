#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <set>
#include <map>

using namespace std;

#define pb push_back
#define sz size
#define all(a)  a.begin(),a.end()
#define SZ(v) ((int)(v).size())

typedef long long  LL;
typedef vector<int> VI;
typedef vector< vector<int> > VVI;
typedef vector<string> VS;
typedef pair< int, int > PII;

vector< int > mat;
int p;

int main()
{
	int t;
	cin>>t;
	for(int test=1;test<=t;test++){
		cout << "Case #" << (test) << ": ";
		int a,ans=0;
		cin>>p;mat.clear();
		for(int i=0;i< (1<<p) ;i++){
			scanf("%d",&a);
			mat.pb(a);
		}
		
		for(int i=0;i<p;i++)
		for(int j=0;j< (1<<(p-i-1)); j++)
			scanf("%d",&a);
		
		for(int level=1;level<=p;level++){
			int start=1,end=start+ (1<< (level)) -1 ;
			for(int match=1;match<= (1<< (p-level) ); match++){
				int flag=0;
				for(int k=start;k<=end;k++)	if(mat[k-1]<level)	{flag=1;break;}
				if(flag)	ans++;
				start=end+1;
				end=start+ (1<< (level)) -1 ;
			}		
		}		
		cout<<ans<<endl;	
	}	
	return 0;
}	



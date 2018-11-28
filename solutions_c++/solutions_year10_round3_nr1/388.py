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

int main()
{
	int t;
	cin>>t;
	for(int test=1;test<=t;test++){
		cout << "Case #" << (test) << ": ";							
		int n,ans=0;
		scanf("%d",&n);
		VI a(n),b(n);
		for(int i=0;i<n;i++)	scanf("%d %d",&a[i],&b[i]);
		for(int i=0;i<n;i++)
		for(int j=i+1;j<n;j++)
			if((a[i]<a[j] && b[i]>b[j]) || (a[i]>a[j] && b[i]<b[j]))	ans++;			 
		cout<<ans<<endl;		
	}		
	return 0;
}	

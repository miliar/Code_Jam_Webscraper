#include<vector>
#include<iostream>
#include<iomanip>
#include<set>
#include<string>
#include<map>
#include<algorithm>
#include<cassert>
#include<cstdio>
#include<cstdlib>
using namespace std;
#define all(c) (c).begin(), (c).end()
#define iter(c) __typeof((c).begin())
#define present(c, e) ((c).find((e)) != (c).end())
#define cpresent(c, e) (find(all(c), (e)) != (c).end())
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define tr(c, i) for (iter(c) i = (c).begin(); i != (c).end(); ++i)
#define pb push_back
#define mp make_pair
int main()
{	
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	long long n,k,a,r;
	
	cin>>t;
	for(int i=1;i<=t;i++){
		cin>>r>>k>>n;
		vector<long long> v;
		
		rep(j,n){
			cin>>a;
			v.pb(a);
		}
		long long start=0,end=0;
		long long ret=0;
		int l=0;
		while(r--){
		long long sum=0;
		long long thi=l;
		
			while(1){
				
				if(sum<k)
				{sum+=v[l%n];
				l++;
				
				}
				if(sum==k)
				{	
					break;
				}
				if(sum>k)
				{
				l--;
				sum-=v[l%n];
				break;
				}
				if(l-thi>=n)
				break;
				}
			//cout<<sum<<endl;	
			ret+=sum;
		}			
				
		cout<<"Case #"<<i<<": "<<ret<<endl;
	}
//	system("pause");
	return 0;
}	
	
			
		

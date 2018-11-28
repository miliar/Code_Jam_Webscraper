#include<iostream>
#include<vector>
#include<string>
#include<queue>
#include<sstream>
#include<map>
#include<stack>
#include<set>
#include<cmath>
using namespace std;
#define PB push_back
#define vi vector<int>
#define vvi vector<vi>
#define LL long long
#define all(v) v.begin(),v.end()
#define pii pair<int,int>
#define MP make_pair
#define INF 200000000
inline int gcd(int m,int n){int tmp;while(n!=0){tmp=m%n;m=n;n=tmp;}return m;}  
LL s2i(string s){LL n;stringstream ss;ss<<s;ss>>n;return n;}
string i2s(LL n){stringstream ss;ss<<n;return ss.str();}
int p[10000],rank[10000];
void create_set(int x)
{
	p[x]=x;
	rank[x]=0;
}
int find_set(int x)
{
	if(p[x]!=x) p[x]=find_set(p[x]);
	return p[x];
}
void merge_set(int x,int y)
{
	int px=find_set(x);
	int py=find_set(y);
	if(rank[px]>rank[py])
		p[py]=px;
	else if(rank[px]<rank[py])
		p[px]=py;
	else if(px!=py)
	{
		p[py]=px;
		rank[px]++;
	}
}
int G[1001][1001];
int main()
{
	int t;
	cin>>t;
	for(int kase=1;kase<=t;kase++)
	{
		int a,b,pp;
		cin>>a>>b>>pp;
		vi primes;
		for(int i=pp;i<1000;i++){
		bool ok=1;
		for(int j=2;j<=sqrt(i);j++)
			if(i%j==0){
				ok=0;
				break;
			}
			if(ok) primes.PB(i);
		}
		for(int i=a;i<=b;i++)
			for(int j=a;j<=b;j++)
				G[i][j]=gcd(i,j);
		memset(p,0,sizeof(p)); memset(rank,0,sizeof(rank));
		for(int i=a;i<=b;i++)
			create_set(i);
		while(1)
		{	
			bool ok=0;
			for(int i=a;i<=b;i++){
				for(int j=i+1;j<=b;j++)
				{
					if(find_set(i)==find_set(j)) continue;
					int g=gcd(i,j);
					for(int k=0;k<primes.size();k++){
						if(primes[k]>=pp && g%primes[k]==0){
							merge_set(i,j);
							//cout<<i<<" "<<j<<endl;
							ok=1;
							break;
						}	
					}
					//if(ok) break;
				}
				//if(ok) break;
			}	
			if(!ok) break;
		}		
		set<int> s;
		for(int i=a;i<=b;i++)
			s.insert(find_set(i));
		cout<<"Case #"<<kase<<": "<<s.size()<<endl;	
	}
}	
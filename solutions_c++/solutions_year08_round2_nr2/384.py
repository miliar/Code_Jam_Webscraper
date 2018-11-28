#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<algorithm>
#include<iterator>
#include<map>
#include<vector>
#include<list>
#include<set>
#include<queue>
#include<cassert>
#include<deque>
#include<stack>
#include<bitset>
#include<functional>
#include<numeric>
#include<utility>
#include<sstream>
#include<iomanip>
#include<string>
#include<cmath>
#include<ctime>
using namespace std;
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii;
bool seive[2000];
int parent[2000];
void init()
{
	memset(seive,true,sizeof(seive));
	for(int i=2;i<=2000;i++)
		if(seive[i])
			for(int j=2*i;j<=2000;j+=i)
				seive[j]=false;
	return;
}
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define debug 1
int par(int i)
{
	if(parent[i]==-1)
		return i;
	int n=par(parent[i]);
	parent[i]=n;
	return n;
}
void setpar(int i,int paren)
{
//	cout << "In setpar " << paren << " " << parent[i]<< "\n";
	int p=par(i);
//	cout << i << " parent " << p  << endl;
	if(p!=paren)
		parent[p]=paren;
	p=par(i);
//	cout << p << endl;
	return;
}
int main()
{
	init();
	int N,a,b,p;
	scanf("%d",&N);
	for(int test=0;test<N;test++)
	{
		scanf("%d %d %d",&a,&b,&p);
		for(int i=a;i<=b;i++)
			parent[i]=-1;
		for(int i=p;i<=b;i++)
			if(seive[i])
			{
//				cout << "PRIME " << i << endl;
				int first,temp;
				if(a%i==0)
					first = a;
				else
					first = ((a/i)+1)*i;
//				cout << "FIRST " << first << endl;
				for(temp=first+i;temp<=b;temp+=i)
				{
//					cout << temp << endl;
					setpar(temp,par(first));
				}
			}
//		cout << "Stage 2\n";
		int cnt=0;
		for(int i=a;i<=b;i++)
			if(parent[i]==-1)
				cnt++;
		printf("Case #%d: %d\n",test+1,cnt);
	}
	return 0;
}

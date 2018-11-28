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
priority_queue<ii,vector<ii>, greater<ii> > Q; //ascending order
priority_queue<ii> QQ;//normal descending order
#define mp make_pair
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define debug 0
#define FOR(i,j,k) for(int i=j;i<k;++i)	
#define RREP(i,n) for(int i=n;i>=0;--i)		
#define REP(i,n) for(int i=0;i<n;i++)
int array[100];
string ss;
int ugly(long long int n)
{
	if(n==0)return 1;
	if(n%3==0)return 1;
	if(n%5==0)return 1;
	if(n%7==0)return 1;
	if(n%2==0)return 1;
	return 0;
}
int l,ans;
void back(int cnt)
{
//cout<<cnt<<" "<<l-1<<endl;
	if(cnt==l-1)
	{
//REP(i,l-1)cout<<array[i]<<" ";
//cout<<endl;
		long long int sign=1;
		long long int num=0,ind=0,start=0,final=0;
		for(int i=0;i<l-1;)
		{
num=0;
			while(i<l-1&&!array[i])i++;
			for(int j=start;j<=i;++j)num=num*10+ss[j]-'0';
			num*=sign;
			final+=num;
			if(array[i]==2)sign=-1;
			else sign=1;
			start=i+1;
                        ++i;
		//	cout<<num<<" ";
		}
if(l==1)final=ss[l-1]-'0';
else

if(array[l-2]!=0)final+=sign*(ss[l-1]-'0');
//,cout<<sign*(ss[l-1]-'0')<<endl;
//cout<<endl;
//getchar();
//getchar();
//cout<<"("<<final<<")"<<" "<<endl;
		if(ugly(final))ans++;
		return ;
	}
	for(int i=0;i<3;++i)
	{
		array[cnt]=i;
		back(cnt+1);
	}

}
int main()
{
	int _;
	scanf("%d",&_);
	for(int ppp=0;ppp<_;++ppp)
	{
		cin>>ss;
		l=ss.length();
                
		memset(array,0,sizeof(array));
		ans=0;
		back(0);
cout<<"Case #"<<ppp+1<<": "<<ans<<endl;
	}
	return 0;
}


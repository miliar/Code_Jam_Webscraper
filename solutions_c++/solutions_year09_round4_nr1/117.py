#include  <cstdio> 
#include  <cstdlib> 
#include  <cstring> 
#include  <string> 
#include  <vector> 
#include  <cmath> 
#include  <algorithm> 
#include  <cassert> 
#include  <set> 
#include  <map> 
#include  <queue> 
#include  <iostream> 
#include <fstream> 
using namespace std; 
#define pb push_back 
#define REP(i,n) for(int i=0;i<(n);i++ )  

typedef long long LL; 
typedef pair<int,int> pii; 

string s[50];

int valid(string& s, int n)
{
	for (int i = n+1; i<s.size();i++)
		if (s[i]=='1')
			return false;
		return true;
}

int main()
{
	int cases;
	scanf("%d", &cases);
	REP(caseIndex, cases)
	{
		int res = 0;
		int N;
		cin>>N;
		//cout<<N<<endl;
		//return 0;
		REP(i,N)
			cin>>s[i];
		REP(i,N)
		{
			int r = 0;
			for (int j = i;j<N;j++)
				if (valid(s[j],i))
				{
					r = j;
					break;
				}
			//cout<<r<<endl;
			res +=r-i;
			for (int j = r;j>i;j--)
				s[j] = s[j-1];
		}
		printf("Case #%d: %d\n", caseIndex + 1,res);
	}
}

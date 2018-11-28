#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <functional>
#include <map>
#include <set>
#include <cassert>
#include <list>
#include <deque>
#include <iomanip>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <cctype>
#include <queue>
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b)) 
#define SETF(x) memset(x,0xff,sizeof(x))
#define SET0(x) memset(x,0,sizeof(x))
#define ALL(x) x.begin(),x.end()
#define PB(x) push_back(x)
#define VI vector <int> 
#define VVI vector < vector <int> > 
#define VS vector <string>
 
using namespace std;

string lst[5001];
string S;
bool find(int index, char c)
{
	int i;
	for(i=index;S[i]!=')';i++)
		if(S[i]==c)
			return true;
	return false;
}
int getnext(int index)
{
	int i;
	for(i=index;S[i]!=')';i++){}
	return (i);
}
bool chk(string str)
{
	int i;
	int st=0;
	int cnt=0;
	for(i=0;i<S.size();i++)
	{
		//cout<<str<<endl;
		if(S[i]=='(' && !find(i+1,str[cnt]))
		{
			//cout<<"here"<<endl;
			return false;
		}
		if(S[i]=='(' && find(i+1,str[cnt]))
		{
			i=getnext(i);
			cnt++;
			continue;
		}
		if(S[i]!=str[cnt] && S[i]!='(')
			return false;
		if(S[i]!='(' && S[i]==str[cnt])
			cnt++;
	}
	return true;
}
int main()
{
	int L,D,N;
	cin>>L>>D>>N;
	int i;
	int cas=1;
	for(i=0;i<D;i++)
		cin>>lst[i];
	while(N--)
	{
		int ret=0;
		cin>>S;
		for(i=0;i<D;i++)
			if(chk(lst[i]))
				ret++;
		cout<<"Case #"<<cas<<": "<<ret<<endl;
		cas++;
	}
	return 0;
}

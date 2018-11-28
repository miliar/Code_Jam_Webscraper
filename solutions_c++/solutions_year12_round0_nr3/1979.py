// This works!!
//Data-structures includes
#include<vector>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<string>


//Other Includes
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<cstdio>
#include<cmath>

using namespace std;

#define pb		push_back
#define mp	 	make_pair
#define fill(a,v) 	memset(a, v, sizeof(a))
#define sz		size()
#define all(x)		x.begin(), x.end()
#define INDEX(arr,ind)	(lower_bound(all(arr),ind)-arr.begin())
#define FF		first
#define SS		second
#define T(t)            int t;scanf ("%d",&t);while (t--)

typedef vector<int> VI;
typedef vector<vector<int> > VVI;
typedef long long int LL;
typedef vector<long long> VLL;
typedef pair<int,int> PII;
typedef vector<pair<int,int> > VPII;
typedef pair<double,double> pdd;

string convertInt(int number)
{
	if (number == 0)
		return "0";
	string temp="";
	string returnvalue="";
	while (number>0)
	{
		temp+=number%10+48;
		number/=10;
	}
	for (int i=0;i<temp.length();i++)
		returnvalue+=temp[temp.length()-i-1];
	return returnvalue;
}

set<pair<int,int> > ss;
int main()
{
	int gg=1;
	T(t)
	{
	int a,b;
	string s;
	scanf ("%d%d",&a,&b);
	int i,len,num=0,j,k,temp=0;
	for (i=a;i<=b;i++)
	{
		s=convertInt(i);
		len=s.length();
		for (k=1;k<len;k++)
		{
			if (s[k]!='0' && s[k]>=s[0])
			{
				int g=len-1,num=0;
				for (j=0;j<len;j++)
				{
					num+=(s[(k+j)%len]-'0')*pow(10,g--);
				}
				if (num <=b && num>i){
					ss.insert(mp(i,num));
				}
			}
		}

	}
	printf ("Case #%d: %lld\n",gg++,(LL)ss.size());
	ss.clear();
	}
	return 0;
}

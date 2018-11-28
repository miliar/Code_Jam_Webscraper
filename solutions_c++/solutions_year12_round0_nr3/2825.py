
//#include<stdlib.h>
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<set>
#include<map>
#include<stack>
#include<list>
#include<queue>
#include<deque>
#include<cctype>
#include<string>
#include<vector>
#include<sstream>
#include<iterator>
#include<numeric>
#include<cmath>
#include<cstring>
#include<complex>
#include<cstdlib>
#include<climits>
#include<bitset>
using namespace std;
#define RFOR(i,a,b) for(int i=a; i > b; i--)
#define FOR(i,a,b) for(int i=a; i < b;i++)
#define PB push_back
#define BN begin()
#define ED end()
#define RN rbegin()
#define RD rend()
#define PF push_front
#define BP pop_back
#define FP pop_front
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define IT(X) __typeof((X).BN) 
#define RIT(X) __typeof((X).RN) 
#define REF(X) __typeof(__typeof(X)::reference) 
#define FORIT(it, X) for(IT(X) it = (X).BN; it != (X).ED; ++it) 
#define FORITR(it, X) for(RIT(X) it = (X).RN; it != (X).RD; ++it)
#define VV(X) vector< vector< X > > 
#define PIB(X) pair<IT(X),bool>
#define SQ ((x)*(x))
#define El() cout<<endl;

typedef long long LL;
typedef unsigned long long ULL;
typedef istringstream ISS;
typedef stringstream SS;
typedef vector<int> VI;
typedef pair <int,int> PII;
typedef vector< PII > VPII;

using namespace std;
int main()
{
        int cas,n=1;
	cin >> cas;
	while(n<=cas)
	{int l=0,a,b;
	int count=0;
	cin >> a >> b;
	int num=a;//string numstr,remnum;SS buf;
	set<int> s;
        while(num > 0){
        num/=10;
        l++;
        }
	FOR(i,a,b+1)
	{num=i;
//	cout<<num<<endl;
	/*int num=i;string numstr,remnum;SS buf;
	while(num > 0){
	num/=10;
	l++;
	}num=i;*/
/*	FOR(j,1,l)
	{cout<<l<<endl;
                                 //numstr =  (num % 10);
			k=num%10;
			buf << (k);
			numstr = buf.str();
				 num /=10; 
			k=num;
			buf << k;
			remnum=buf.str();
			numstr += remnum; 
			num = strtol( numstr.c_str() ); 
			//buf(numstr);
			numstr.erase();
			//buf >> num;
			if(num > i) 
			count++;
	}
	}VI v;int d;
	while(num > 0)
	{d=num%10;
	num/=10;
	v.PB(d);
	}
	rotate(v.PB,v.PB + (l-1),v.ED);*/
	FOR(j,1,l)
	{
	num=(num/10)+(num%10)*pow(10,l-1);
	//cout << num<<endl;
	if((a<=i)&&(i<num)&&(num<=b))
	//count++;
{	//cout<<num<<endl;
	s.insert(num);
	}}
		
	count+=s.size();	
	//set<int>::iterator it,it1;
/*	for(it=s.BN;it!=s.ED;it++)
		{for(it1=it++;it1!=s.ED;it1++)
		{if((a<*it)&&(*it1<b))
		count++;
	}}*/
	s.clear();	}
	cout<<"Case #"<<n<<": "<<count<<endl;
	n++;
	}
	return 0;
}

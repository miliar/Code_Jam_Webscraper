#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <climits>
#include <cmath>
#include <cstring>
#define FOR(x,y,z) for(int (x)=(y);(x)<(z);(x)++)
#define FORD(x,y,z) for(int (x)=(y);(x)>=(z);(x)--)
#define PB push_back
#define F first
#define S second
#define MP make_pair
using namespace std;
struct ltstr
{
  bool operator()(const char* s1, const char* s2) const
  {
	return (strcmp(s1,s2) <0);
  }
};
struct zomgf
{
  bool operator()(const string s1, const string s2) const
  {
	return s1.compare(s2)<0;
  }
};

unsigned long long hasz(const char* x)
{
	unsigned long long int r=0;
	unsigned long long int mn=1;
	FOR(i,0,strlen(x))
	{
		r+=(x[i]-'a')*mn;
		mn*=10;
	}
	return r;
}
class wezel
{
public:
	map<string,wezel*,zomgf> dzieci;
};
wezel* root;
//void wypisz(wezel* x)
//{
//	for(map<unsigned long long,wezel*>::iterator i=x->dzieci.begin();i!=x->dzieci.end();i++)
//	{
//		printf("%llu\n",i->first);
//		wypisz(i->second);
//	}
//}
int main()
{
	int Z;
	scanf("%d",&Z);
	root = new wezel();
	FOR(h,1,Z+1)
	{
		//delete root;
		root= new wezel();
		int n,m;
		scanf("%d%d",&n,&m);
		char s[500010];
		FOR(i,0,n)
		{
			scanf("%s",&s);
			string szit;
			szit=s;
			//int b=1;
			wezel* ak = root;
			FOR(b,1,szit.size())
			{
				string temp;
				while(szit[b]!='/'&&b<szit.size())
				{
					temp.PB(szit[b]);b++;
				}
				if(ak->dzieci.find(temp)!=ak->dzieci.end())
				{
					ak=ak->dzieci[temp];
				}
				else {
					ak->dzieci[temp]=new wezel();
					ak=ak->dzieci[temp];
				}
				//wypisz(root);
			}
			
			//putchar('\n');
		}
		//wypisz(root);
		int wynik=0;
		FOR(i,0,m)
		{
			scanf("%s",&s);
			string szit;
			szit=s;
			//int b=1;
			wezel* ak = root;
			FOR(b,1,szit.size())
			{
				string temp;
				while(szit[b]!='/'&&b<szit.size())
				{
					temp.PB(szit[b]);b++;
				}
				if(ak->dzieci.find(temp)!=ak->dzieci.end())
				{
					ak=ak->dzieci[temp];
				}
				else {
					ak->dzieci[temp]=new wezel();
					ak=ak->dzieci[temp];
					wynik++;
				}
				//wypisz(root);
			}
			
			//putchar('\n');
		}

		printf("Case #%d: %d\n",h,wynik);
	}
	return 0;
}
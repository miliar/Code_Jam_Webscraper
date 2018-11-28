#include<cstdio>
#include<cstring>
#include<map>
#include<set>
#include<vector>
using namespace std;

struct mydata
{
	char a , b;
	mydata(char _a = 0 , char _b = 0) : a(_a) , b(_b) {}
	bool operator<(const mydata &r) const
	{
		if(a == r.a) return b < r.b;
		else return a < r.a;
	}
};

int main()
{
//	freopen("1.txt" , "r" , stdin);
//	freopen("2.txt" , "w" , stdout);
	int t;
	scanf("%d" , &t);
	int ii = 0;
	while(t--)
	{
		map<mydata , char> mymap;
		set<char> myset[26];
		int n;
		scanf("%d" , &n);
		int i;
		while(n--)
		{
			char c[6];
			scanf("%s" , &c);
			mymap[mydata(c[0] , c[1])] = c[2];
			mymap[mydata(c[1] , c[0])] = c[2];
		}
		scanf("%d" , &n);
		while(n--)
		{
			char c[6];
			scanf("%s" , &c);
			myset[c[0] - 'A'].insert(c[1]);
			myset[c[1] - 'A'].insert(c[0]);
		}
		char c[200];
		scanf("%d%s" , &n , &c);
		vector<int> ret;
		for(i = 0;i < n;i++)
		{
			if(!ret.empty() && mymap.find(mydata(c[i] , ret[ret.size() - 1])) != mymap.end())
			{
				char temp = mymap[mydata(c[i] , ret[ret.size() - 1])];
				ret.pop_back();
				ret.push_back(temp);
			}
			else
			{
				int j;
				for(j = 0;j < ret.size();j++)
				{
					if(myset[c[i] - 'A'].find(ret[j]) != myset[c[i] - 'A'].end())
						break;
				}
				if(j < ret.size())
				{
					ret.clear();
				}
				else
				{
					ret.push_back(c[i]);
				}
			}
		}
		printf("Case #%d: " , ++ii);
		printf("[");
		for(i = 0;i < ret.size();i++)
		{
			if(i != ret.size() - 1)
			{
				printf("%c, " , ret[i]);
			}
			else
			{
				printf("%c" , ret[i]);
			}
		}
		printf("]\n");
	}
	return 0;
}
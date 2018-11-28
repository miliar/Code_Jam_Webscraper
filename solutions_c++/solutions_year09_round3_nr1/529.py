#include <iostream>
#include <fstream>
#include <string>
#include <map>
using namespace std;

ifstream fin("a.txt");
#define cin fin

ofstream fout("out.txt");
#define cout fout

long long F(long long n, long long i, long long b)
{
	long long j = 1;
	long long ret = 0;
	while(i--)
	{
		j *= b;
	}
	ret += n * j;
	return ret;
}

int main()
{
	long long i, j, k, n, mx;
	cin>>n;
	for(i=0; i<n; i++)
	{
		string s;
		cin>>s;
		map<char, long long>mp;
		k = 0;
		mx = 2;
		mp[s[0]] = 1;
		for(j=1; j<s.size(); j++)
		{
			if(mp.find(s[j]) == mp.end())
			{
				if(k == 1)
					k++;
				mp[s[j]] = k;
				k++;
				mx = max(k, mx);
			}
		}
		long long res = 0;
		for(j=s.size()-1; j>=0; j--)
		{
			res += F(mp[s[j]], s.size() - j - 1, mx);
		}
		cout<<"Case #"<<i+1<<": ";
		cout<<res<<endl;
	}
	return 0;
}
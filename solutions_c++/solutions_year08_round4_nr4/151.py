#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int N,k;
	string s;
	string t;
	int tests;
	cin>>N;
	int rez;
	int i;
	for (tests=1; tests<=N; tests++)
	{
		cin>>k>>s;
		vector<int> v(k);
		for (i=0; i<k; i++)
			v[i]=i;
		rez=s.size();
		do
		{
			t=s;
			for (i=0; i<s.size(); i++)
			{
				t[i]=s[i-i%k+v[i%k]];
			}
			int l=0;
			for (i=0; i<t.size(); i++)
			{
				if (i==0 || t[i]!=t[i-1])
					l++;
			}
			if (l<rez)
				rez=l;
		} while (next_permutation(v.begin(), v.end()));
		cout<<"Case #"<<tests<<": "<<rez<<endl;
	}
	return 0;
}

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

ifstream fin("The Next Number.txt");
#define cin fin

ofstream fout("out.txt");
#define cout fout

int main()
{
	int n, i, j;
	cin>>n;
	for(i=0; i<n; i++)
	{
		string s;
		cin>>s;
		vector<char>v(s.size());
		for(j=0; j<v.size(); j++)
		{
			v[j] = s[j];
		}
		cout<<"Case #"<<i+1<<": ";
		if(next_permutation(v.begin(), v.end()))
		{
			for(j=0; j<v.size(); j++)
			{
				cout<<v[j];
			}
			cout<<endl;
		}
		else
		{
			sort(v.begin(), v.end());
			j = 0;
			char ch;
			while(v[j] == '0')
				j++;
			ch = v[j];
			v[j] = '0';
			sort(v.begin(), v.end());
			cout<<ch;
			for(j=0; j<v.size(); j++)
			{
				cout<<v[j];
			}
			cout<<endl;
		}
	}
	return 0;
}

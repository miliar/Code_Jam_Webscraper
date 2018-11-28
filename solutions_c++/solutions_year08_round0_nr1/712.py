#include <iostream>
#include <fstream>
#include <string>
#include <map>
using namespace std;

ifstream fin("universe.txt");
#define cin fin

ofstream fout("output.txt");
#define cout fout

int query[1100];
bool present[110];
int s, q;

void Init()
{
	int i;
	for(i=0; i<s; i++)
	{
		present[i] = 0;
	}
}

int main()
{
	int n, i, j, k;
	cin>>n;
	for(i=0; i<n; i++)
	{
		cin>>s;
		map<string, int>mp;

		char ch[110];
		string str;
		int x = 0, sw = 0;

		cin.getline(ch, 100);
		for(j=0; j<s; j++)
		{
			cin.getline(ch, 100);
			str = ch;
			mp[str] = j;
		}
		cin>>q;

		cin.getline(ch, 100);
		for(j=0; j<q; j++)
		{
			cin.getline(ch, 100);
			str = ch;
			x = mp[str];
			query[j] = x;
		}
		Init();
		int p = 0;
		for(j=0; j<q; j++)
		{
		//	cout<<query[j]<<endl;
			if(!present[query[j]])
			{
				present[query[j]] = 1;
				p++;
			}
			if(p == s)
			{
				Init();
				j--;
				p = 0;
				sw++;
			}
		}

		cout<<"Case #"<<i+1<<": "<<sw<<endl;
	}
	return 0;
}
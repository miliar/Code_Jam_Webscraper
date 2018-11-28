///Welcome to Code Jam
#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
using namespace std;

ifstream fin("Welcome to Code Jam.txt");
#define cin fin

ofstream fout("Welcome to Code Jam out.txt");
#define cout fout

int e[600][50];
int a[600][50];
int b[600][50];

void Display(int arr[600][50], int x, int y)
{
	int i, j;
	for(i=0; i<x; i++)
	{
		for(j=0; j<y; j++)
		{
			cout<<arr[i][j]<<" ";
		}
		cout<<endl;
	}
	cout<<"---"<<endl;
}

int Solve(string s, string t)
{
	int i, j, k, ret = 0;
	for(i=0; i<t.size(); i++)
	{
		for(j=0; j<s.size(); j++)
		{
			e[i][j] = (t[i] == s[j]);
			a[i][j] = 0;
		}
	}
	for(i=0; i<t.size(); i++)
	{
		if(e[i][s.size() - 1])
			a[i][s.size() - 1] = 1;
	}
	for(j=s.size() - 1; j>=0; j--)
	{
		for(i=t.size() - 1; i>=0; i--)
		{
			if(e[i][j])
			{
				for(k=0; k<i; k++)
				{
					if(e[k][j-1])
					{
						a[k][j-1] += a[i][j];
					}
				}
			}
		}
	}
	//Display(e, t.size(), s.size());
	//Display(a, t.size(), s.size());
	for(i=0; i<t.size(); i++)
	{
		ret += a[i][0];
		ret %= 10000;
	}
	return ret;
}

int main()
{
	int i, n;
	char ch[1000];
	string s, t;
	s = "welcome to code jam";
	//s = "gcj";
	cin>>n;
	cin.getline(ch, 1000);
	for(i=0; i<n; i++)
	{
		cin.getline(ch, 1000);
		t = ch;
		int ret = Solve(s, t);
		cout<<"Case #"<<i+1<<": "<<setfill('0')<<setw(4)<<ret<<endl;
	}
	return 0;
}
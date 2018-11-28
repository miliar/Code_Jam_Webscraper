#include<iostream>
#include<string>
using namespace std;

void solve(int num)
{
	int n, m, z;
	cin >> n;
	string nt[100], mt[100], s;
	for(int i = 0; i < n; i++)
	{
		cin >> nt[i];
	}
	cin >> m;
	for(int i = 0; i< m; i++)
	{
		cin >> mt[i];
	}
	cin >> z;
	for(int i = 0; i < z; i++)
	{
		char zn;
		cin >> zn;
		s+= zn;
//		cout << s << endl;
//		s+='&';
		for(int u = 0; u < s.size()-1; u++)
		{
			for(int j = 0; j < n; j++)
			{
				if(nt[j][0] == s[u])
				{
					if(s[u+1] == nt[j][1])
					{
//						s+='&';
						string lol;
						lol=nt[j][2];
						s.insert(u,lol);
						s.erase(u+1,u+2);
//						s.resize(s.size()-1);
					}
				}
				if(nt[j][1] == s[u])
				{
					if(s[u+1] == nt[j][0])
					{
//						s+='&';
						string lol;
						lol=nt[j][2];
						s.insert(u, lol);
						s.erase(u+1,u+2);
//						s.resize(s.size()-1);
					}
				}
			}
		}
		for(int u = 0; u < s.size(); u++)
		{
			for(int j = 0; j < m; j++)
			{
				if(mt[j][0]== s[u])
				{
					for(int k = 0; k < s.size(); k++)
					{
						if(mt[j][1] == s[k] && k != u)
						{
							s.clear();
							continue;
						}
					}
				}
				if(mt[j][1]== s[u])
				{
					for(int k = 0; k < s.size(); k++)
					{
						if(mt[j][0] == s[k] && k != u)
						{
							s.clear();
							continue;
						}
					}
				}
			}
		}
	}
	cout << "Case #" << num << ": [";
	for(int i = 0 ; i< s.size(); i++)
	{

		if(i!=s.size()-1)cout << s[i] << ", ";
		if(i == s.size()-1)cout << s[i];
	}
	cout << "]\n";
}

int main()
{
	int n;
	cin >> n;
	for(int i = 1;i <= n; i++)solve(i);
}

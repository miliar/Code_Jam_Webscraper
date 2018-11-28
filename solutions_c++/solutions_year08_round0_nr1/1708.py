#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;

const int N = 1000;

int n;
vector<string> S;
char tmp[N];
bool used[N];
int lft;

inline void nul()
{ for (int i=0; i<n; i++) used[i]=0; lft=n; }

void funk(int x)
{
	cin.getline(tmp,1000);
	n = atoi(tmp);
	S.resize(n);
	for (int i=0; i<n; i++)
	{
		cin.getline(tmp,1000);
		S[i]=string(tmp);
//		cout << "S[] = " << i << " " << S[i] << endl;
		
	}
//	cout << "n = " << n << endl;
	nul();
	int m;
	int c = 0;
	cin.getline(tmp,1000);
	m = atoi(tmp);
//	cout << "m = " << m << endl;
	while (m--)
	{
		string s;
		cin.getline(tmp,1000);
		s=string(tmp);
		int j=0;
		while (S[j]!=s) j++;
		if (used[j]) continue;
		used[j]=1;
		if (lft<=1)
		{
			nul();
			used[j]=1;
			lft--;
			c++;
		}
		else lft--;
	}
	cout << "Case #" << x << ": " << c << endl;
	return;
}

int main()
{
	int j;
	cin.getline(tmp,1000);
	j = atoi(tmp);
	for (int i=0; i<j; i++) funk(i+1);
	return 0;
}






#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>

using namespace std;

int main()
{
	freopen("inn.in", "rt", stdin);
	freopen("out.out", "wt", stdout);
	
	char m[200];
	m[97]='y';	
	m[98]='h';	
	m[99]='e';	
	m[100]='s';	
	m[101]='o';	
	m[102]='c';	
	m[103]='v';	
	m[104]='x';	
	m[105]='d';	
	m[106]='u';	
	m[107]='i';	
	m[108]='g';	
	m[109]='l';	
	m[110]='b';	
	m[111]='k';	
	m[112]='r';	
	m[113]='z';	
	m[114]='t';	
	m[115]='n';	
	m[116]='w';	
	m[117]='j';	
	m[118]='p';	
	m[119]='f';	
	m[120]='m';	
	m[121]='a';	
	m[122]='q';	
	m[32]=' ';

	int n;
	cin >> n;

	int s1[33][110];
	int u[33];

	for (int i=0; i<=n; i++)
	{
		char s[110];
		cin.getline(s, 105);

		int j=0;
		while (s[j])
		{
		    	s1[i][j]=(int)m[(int)s[j]];
			j++;	
		}
		u[i]=j;
	}


	for(int t=1; t<=n; t++)
	{
		cout << "Case #" << t << ": ";

		for(int i=0; i<u[t]; i++)
		{
			cout << (char)s1[t][i];
		}
		cout << endl;
	}
	return 0;
}

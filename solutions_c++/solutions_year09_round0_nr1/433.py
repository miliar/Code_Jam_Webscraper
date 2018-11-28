#include<iostream>
#include<string>
#include<vector>

using namespace std;


int N;


int L,D;

string dic[5000];

bool b[20][26];

int main()
{
   cin >> L >> D >> N;
for (int i = 0;i<D;i++) cin >> dic[i];
for (int i = 0;i<N;i++)
{
	string p;
	cin >> p;
	memset(b,0,sizeof(b));
	int l = -1;
	bool multiple = false;
	for (int j = 0;j < p.size();j++)
		if (p[j] == '(') { multiple = true; l++;}
		else if (p[j] == ')') { multiple = false;}
		else
		{
			if (!multiple) l++;
			b[l][p[j]-'a'] = true;
		}
	int cnt = 0;
	for (int di=0;di<D;di++)
	{
		bool flag = true;
		for (int li = 0;li < L;li++)
			if (b[li][  dic[di][li] -'a' ] == false) { flag = false; break;}
			if (flag) cnt++;
	}
	printf("Case #%d: %d\n", i+1, cnt); 
}
}
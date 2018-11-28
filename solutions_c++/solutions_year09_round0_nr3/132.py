#include <iostream>
#include <cstdio>
#include <vector>
#include <string>

using namespace std;

const int mod = 10000;
const string cc = "welcome to code jam";
vector<int> aa;

void process(void)
{
	aa = vector<int>(cc.size(),0);
	string line;

	getline(cin, line);

	for(int i=0;i<(int)line.size();i++)
	{
		for(int j=(int)cc.size()-1;j>0;j--)
		{
			if(line[i] != cc[j]) continue;
			aa[j] = (aa[j] + aa[j-1]) % mod;
		}
		if(line[i] == cc[0]) aa[0] = (aa[0] + 1) % mod;
	}
	printf("%04d\n",aa[cc.size()-1]);
}

int main(void)
{
	int N;
	cin >> N;
	string str;
	getline(cin,str);
	for(int i=0;i<N;i++)
	{
		cout << "Case #" << i+1 << ": ";
		process();
	}
}

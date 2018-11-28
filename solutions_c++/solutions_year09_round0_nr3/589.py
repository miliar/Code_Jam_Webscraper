
#define _CRT_SECURE_NO_DEPRECATE
#include <iostream> 
#include <string>
#include <vector>
#include <sstream>
#include <queue>
#include <algorithm>
#include <iomanip>
#include <map>
#include <set>
#include <math.h>
#include <stack>
#include <deque>
#include <numeric>
#define all(x) x.begin(),x.end()
#define mpair make_pair
using namespace std;
typedef long long ll;
typedef long double ld;
const ld epsylon = 1e-9;
const int mod = 10000;
int mem[512][32];
const string target = "welcome to code jam";
inline int get_code(char c)
{
	if(c>= 'a' && c <='z')
		return c - 'a';
	else
		return 26;
}
inline char decode(int cd)
{
	if(cd < 26)
		return cd + 'a';
	return ' ';
}
string input;
int solve(int pos,int idx)
{
	if(input[pos] != target[idx])
	{
		return mem[pos][idx] = 0;
	}
	if(idx == (int)target.size() - 1)
		return mem[pos][idx] = 1;
	int res = 0;
	for(int j = pos + 1;j < input.size();j++)
	{
		if(input[j] == target[idx+1])
		{
			int temp = 0;
			if(mem[j][idx+1] == -1)
				temp = solve(j,idx+1);
			else
				temp = mem[j][idx+1];
			res = (res + temp)%mod;
		}
	}
	return mem[pos][idx] = res;
}
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int nt;
	cin>>nt;
	getline(cin,input);
	for(int it=1;it<=nt;it++)
	{
		memset(mem,-1,sizeof(mem));
		getline(cin,input);
		for(int i=0;i<input.size();i++)
			solve(i,0);
		int res = 0;
		for(int i=0;i<input.size();i++)
			res = (res + mem[i][0])%mod;
		printf("Case #%d: %.4d\n",it,res);
		//cout<<"Case #"<<it<<": "<<endl;
	}
	return 0;
}

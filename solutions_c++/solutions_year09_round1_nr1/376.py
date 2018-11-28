#include <iostream>
#include <sstream>
#include <string>

using std::istringstream;
using std::string;
using std::cin;
using std::cout;

const int max_v = 10000;
const int min_base = 2;
const int max_base = 10;
const int base_num = max_base - min_base + 1;
const int base_add = 2;

bool happies[base_num][max_v];
bool visited[base_num][max_v];

void init()
{
	for(int i = 0;i < base_num; ++i)
	{
		for(int k = 0;k < max_v; ++k)
		{
			happies[i][k] = false;
			visited[i][k] = false;
		}
		happies[i][0] = true;
		visited[i][0] = true;
	}
}

int squar_sum(int b,int v)
{
	int ret = 0;
	for(;v > 0;v /= b)
	{
		int t = v%b;t *= t;
		ret += t;
	}
	return ret;
}

bool pre_do_h(int b,int v)
{
	int p = b - base_add;
	int q = v - 1;
	if(visited[p][q])
	{
		return happies[p][q];
	}
	visited[p][q] = true;
	happies[p][q] = pre_do_h(b,squar_sum(b,v));
	return happies[p][q];
}

void pre_do()
{
	init();
	for(int i = 0;i < base_num; ++i)
	{
		for(int k = 0;k < max_v; ++k)
		{
			pre_do_h(i + base_add,k + 1);
		}
	}
}

int main()
{
	pre_do();
	int nCases = 0;
	cin >> nCases;
	string s;
	getline(cin,s);
	int bases[9];
	for(int iCases = 1;iCases <= nCases;iCases++)
	{
		getline(cin,s);
		istringstream in(s);
		int base_cnt = 0;
		for(;in >> bases[base_cnt];++base_cnt);
		unsigned long ret = 2;
		for(;; ++ ret)
		{
			int i = 0;
			for(;i < base_cnt; ++i)
			{
				int k = ret;
				int b = bases[i];
				for(;k > max_v;k = squar_sum(b,k));
				if(!happies[b-base_add][k-1]) break;
			}
			if(i == base_cnt) { break; }
		}
		cout << "Case #" << iCases << ": " << ret << std::endl;
	}
	return 0;
}
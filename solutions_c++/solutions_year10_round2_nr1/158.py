#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define rep(i,n) for(int i=0;i<n;i++)

using namespace std;

long long N, M, T;
long long re;
vector< string > p1;
vector< string > p2;


int main()
{
    fstream fin("A-large.in",fstream::in);
    fstream fout("A-large.out",fstream::out);
    fin >> T;
	long long per = 0;
	string tmp;
    for(int j=1;j<=T;j++)
    {
		p1.resize(0);
		p2.resize(0);
		re = 0;
		fin >> N >> M;
		rep(i, N)
		{
			fin >> tmp;
			p1.push_back(tmp);
		}
		rep(i, M)
		{
			fin >> tmp;
			p2.resize(0);
			while (tmp.size()>0)
			{
				if (find(p1.begin(), p1.end(), tmp)!=p1.end())
				{
					break;
				}
				p2.push_back(tmp);
				while (tmp[tmp.size()-1]!='/') tmp.erase(tmp.begin() + tmp.size() - 1);
				tmp.erase(tmp.begin() + tmp.size() - 1);
			}
			re += p2.size();
			rep(i, p2.size()) p1.push_back(p2[i]);
		}
		fout << "Case #" << j << ": " << re << "\n";
    }
    fin.close();
	fin.clear();
    fout.close();
	fout.clear();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC;
    system("PAUSE");
    return 0;
}

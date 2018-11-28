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

int T;
string t;
vector<int> num,n1;

int main()
{
    fstream fin("B-large.in",ifstream::in);
    fstream fout("B-large.out",ofstream::out);
    fin >> T;
    for(int j=1;j<=T;j++)
    {
		num.resize(0);
		fin >> t;
		rep(i,t.length()) num.push_back(t[i]-'0');
		n1 = num;
		fout << "Case #" << j << ": " ;
		if (next_permutation(num.begin(),num.end()))
		{
			rep(i,num.size()) fout << num[i];
			fout << "\n";
		}
		else
		{
			sort(n1.begin(),n1.end());
			int k=0;
			while(n1[k]==0) k++;
			swap(n1[k],n1[0]);
			n1.insert(n1.begin()+1,0);
			rep(i,n1.size()) fout << n1[i];
			fout << "\n";
		}
    }
    fin.close();
    fout.close();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC;
    system("PAUSE");
    return 0;
}

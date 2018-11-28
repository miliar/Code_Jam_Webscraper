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

int C;
int N;

bool cmp(vector<int> a, vector<int> b)
{
	if (a.size()<b.size()) return 0;
	if (a.size()>b.size()) return 1;
	rep(i, a.size())
	{
		if (a[i]<b[i]) return 0;
		if (a[i]>b[i]) return 1;
	}
	return 0;
}

vector<int> add(vector<int> a, vector<int> b)
{
	if (a.size()<b.size()) swap(a,b);
	vector<int> ret(a.size());
	int carry = 0, tmp = 0, k1, k2;
	carry = 0;
	rep(i, a.size())
	{
		k2 = b.size() - i - 1;
		k1 = a.size() - i - 1;
		ret[k1] = 0;
		if (k2>=0) tmp = a[k1] + b[k2] + carry;
		else tmp = a[k1] + carry;
		if (tmp>9)
		{
			carry = 1;
			tmp = tmp%10;
		}
		else carry = 0;
		ret[k1] += tmp;
	}
	if (carry>0) ret.insert(ret.begin(), carry);
	return ret;
}

vector<int> sub(vector<int> a, vector<int> b)
{
	vector<int> ret(a.size());
	int carry = 0, tmp = 0, k1, k2;
	carry = 0;
	rep(i, a.size())
	{
		k2 = b.size() - i - 1;
		k1 = a.size() - i - 1;
		ret[k1] = 0;
		if (k2>=0) tmp = a[k1] - b[k2] - carry;
		else tmp = a[k1] - carry;
		if (tmp<0)
		{
			carry = 1;
			tmp += 10;
		}
		else carry = 0;
		ret[k1] += tmp;
	}
	while (ret[0]==0 && ret.size()>1) ret.erase(ret.begin());
	return ret;
}

vector<int> mod(vector<int> a, vector<int> b)
{
	vector<int> tmp(0), tmp2;
	tmp.push_back(0);
	while(1)
	{
		tmp2 = b;
		if (cmp(add(tmp, b), a)) break;
		while (!cmp(add(tmp, tmp2), a))
		{
			tmp2.push_back(0);
		}
		tmp2.erase(tmp2.end()-1);
		tmp = add(tmp, tmp2);
	}
	return sub(a, tmp);
}

vector<int> gcd(vector<int> a, vector<int> b)
{
	while (!(a.size()==1 && a[0]==0) && !(b.size()==1 && b[0]==0))
	{
		if (!cmp(a,b)) swap(a, b);
		a = mod(a, b);
		swap(a, b);
	}
	if (!cmp(a,b)) swap(a, b);
	return a;
}

vector< vector<int> > t;
vector< vector<int> > diff;

int main()
{
    fstream fin("B-large.in",ifstream::in);
    fstream fout("B-large.out",ofstream::out);
    fin >> C;
	string temp;
    for(int j=1;j<=C;j++)
    {
        fin >> N;
		t.resize(0);
		rep(i, N)
		{
			fin >> temp;
			vector<int> temp2(temp.size());
			rep(i, temp.size()) temp2[i] = temp[i] - '0';
			t.push_back(temp2);
		}
		sort(t.begin(), t.end(), cmp);
		diff.resize(t.size()-1);
		rep(i, t.size()-1) diff[i] = sub(t[i], t[i+1]);
		vector<int> gc;
		gc = diff[0];
		rep(i,diff.size()-1)
			gc = gcd(gc, diff[i+1]);
		vector<int> zz(1);
		zz[0] = 0;
		vector<int> re = sub(gc,mod(t[0], gc));
		if (mod(t[0], gc)==zz) re = zz;
        fout << "Case #" << j << ": ";
		rep(i, re.size()) fout << re[i];
		fout << "\n";
    }
    fin.close();
    fout.close();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC;
    system("PAUSE");
    return 0;
}

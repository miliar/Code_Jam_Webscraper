#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <functional>
using namespace std;
ifstream in;
ofstream out;


void solve(int test)
{
	string str;
	getline(in, str);
	vector<int> v(str.size());
	bool ok = false;
	int i,j,k,m,n = str.size();
	for(i=0;i<str.size();++i)
		v[n - i - 1] = str[i] - '0';
	reverse(v.begin(), v.end());
	next_permutation(v.begin(), v.end());
	vector<int> v2 = v;
	sort(v2.begin(), v2.end());
	if(v2!=v)
	{
		out << "Case #" << test << ": ";
		for(i=0;i<n;++i)
			out << v[i];
		out << endl;
	}
	else
	{
		out << "Case #" << test << ": ";
		reverse(v.begin(), v.end());
		v.push_back(0);
		k = n;
		while(v[k]==0) --k;
		swap(v[k], v[n]);
		for(i=n;i>=0;--i)
			out << v[i];
		out << endl;
		
	}
}
	/*for(i=n-2;i>=0;--i)
		if(v[i] > v[i+1])
		{
			ok = true;
			break;
		}
	if(!ok)
	{
		sort(v.begin(), v.end());
		out << "Case #" << test << ": ";
		int k = 0;
		while(v[k]==0) ++k;
		out << v[k] << 0;
		for(i=0;i<n;++i)
			if(i!=k)
			out << v[i];
		out << endl;
	}
	else
	{
		bool finish = false;
		int temp = 10, ind = -1;
		for(i=1;i<n;++i)
		{
			for(j=i-1;j>=0;--j)
			{
				if(v[i] < v[j])
				{
					if(v[j] < temp)
					{
						temp = v[j];
						ind = j;
					}
				}/*
				if(v[i] < v[j])
				{
					swap(v[i], v[j]);
					sort(v.begin(), v.begin() + i);
					out << "Case #" << test << ": ";
					for(i=n-1;i>=0;--i)
						out << v[i];
					out << endl;
					finish = true;
					break;
				} */
			//}
		/*	if(ind!=-1)
			{
				swap(v[i], v[ind]);
				sort(v.begin(), v.begin() + i, greater<int>());
				out << "Case #" << test << ": ";
				for(i=n-1;i>=0;--i)
					out << v[i];
				out << endl;
				break;
			}
		}
	}*/


int main()
{
	in.open("B-small.in");
	out.open("B-small.out");
	int kol, n;
	in >> kol;
	getline(in, string());
	for(n=1;n<=kol;++n)
		solve(n);
	in.close();
	out.close();
}
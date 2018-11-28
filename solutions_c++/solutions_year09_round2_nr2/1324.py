#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	ifstream f;
	ofstream o;
	f.open("Bsmall2.txt");
	o.open("Bout.txt");
	int N;
	f >> N;
	for(int i = 0; i < N; i++)
	{
		__int64 m,k;
		f >> m;
		vector<__int64> v;
		k = m;
		while(m > 0)
		{
			v.insert(v.begin(), m % 10);
			m /= 10;
		}
		next_permutation(v.begin(), v.end());
		__int64 a = 0;
		__int64 d = 1;
		for(int j = v.size() - 1; j >= 0; j--)
		{
			a += v[j]*d;
			d *= 10;
		}
		if(a <= k)
		{
			v.insert(v.begin(), 0);
			int q = 0;
			while(v[q] == 0)
				q++;
			swap(v[0],v[q]);
			a = 0;
			d = 1;
			for(int j = v.size() - 1; j >= 0; j--)
			{
				a += v[j]*d;
				d *= 10;
			}
		}
		o << "Case #" << (i+1) << ": " << a << endl;
	}
	o.close();
	f.close();
}

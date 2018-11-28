#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
//---------------------------------------------------------------------------
using namespace std;
//---------------------------------------------------------------------------
class Case
{
	friend std::istream& operator >> (std::istream&,Case&);
public:
	int Calc()
	{
		int result = 0;

		if(P*K < L)
			result = -1;
		else
		{
			sort(freqs.rbegin(), freqs.rend());
			for(int i = 0, cp = 1; i < L && cp <= P; ++i)
			{
				if(i > 0 && i%K == 0)
					++cp;
				result += freqs[i]*cp;
			}
		}

		return result;
	}
private:
	int P, K, L;
	vector<int> freqs;
};
//---------------------------------------------------------------------------
std::istream& operator >> (std::istream& is, Case& c)
{
	is >> c.P >> c.K >> c.L;
	for(int i = 0; i < c.L; ++i)
	{
		int x = 0;
		is >> x;
		c.freqs.push_back(x);
	}
	return is;
}
//---------------------------------------------------------------------------
int main()
{
	int N = 0;
	cin >> N;
	for(int i = 0; i < N; ++i)
	{
		Case c;
		cin >> c;

		cout << "Case #" << i+1 << ": " << c.Calc() << std::endl;
	}
	return 0;
}
//---------------------------------------------------------------------------

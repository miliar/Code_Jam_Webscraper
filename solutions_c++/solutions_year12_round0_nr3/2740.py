#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <functional>
#include <cmath>

using namespace std;


class CaseInfo
{
public:
	int a;
	int b;
	int how_many;

	friend istream & operator>>(istream & is, CaseInfo & info)
	{
		return is >> info.a >> info.b;
	}

	friend ostream & operator<<(ostream & os, const CaseInfo & info)
	{
		return os << info.how_many;
	}

	bool IsRecycledPair(int n, int m)
	{
		char s[10]; 
		sprintf(s, "%d", n); 
		int n_width = strlen(s);     
		sprintf(s, "%d", n); 
		int m_width = strlen(s);     
		int width = max(n_width, m_width);

		for (size_t i=0; i<width - 1; i++)
		{
			n = (n % 10) * pow(10.0, width - 1) + n / 10;

			if (n == m)
				return true;
		}

		return false;
	}

	void ProcessCase()
	{
		how_many = 0;

		for (int i=a; i<b+1; i++)
			for (int j=i+1; j<b+1; j++)
				if (IsRecycledPair(i, j))
					how_many++;
	}
};


int main()
{
	ifstream ifs("C-small-attempt0.in");
	ofstream ofs("C-small-attempt0.out");

	string line;
	getline(ifs, line);

	int number = 1;
	CaseInfo case_info;
	while (ifs >> case_info)
	{
		case_info.ProcessCase();

		ofs << "Case #" << number++ << ": " << case_info << "\n";
	}

	return 0;
}

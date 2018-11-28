#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;


class CaseInfo
{
public:
	int googlers_count;
	int surprising_count;
	int best_result_standard;
	vector<int> total_points;
	int how_many;

	friend istream & operator>>(istream & is, CaseInfo & info)
	{
		string line;
		getline(is, line);
		stringstream ss(line);
		ss >> info.googlers_count >> info.surprising_count >> info.best_result_standard;
		info.total_points.clear();
		copy(istream_iterator<int>(ss), istream_iterator<int>(), back_inserter(info.total_points));
		return is;
	}

	friend ostream & operator<<(ostream & os, const CaseInfo & info)
	{
		return os << info.how_many;
	}

	void ProcessCase()
	{
		how_many = 0;

		if (best_result_standard == 0)
		{
			how_many = googlers_count;
			return;
		}

		if (best_result_standard == 1)
		{
			how_many = count_if(total_points.begin(), total_points.end(), bind2nd(greater<int>(), 1));
			return;
		}

		for (vector<int>::iterator it=total_points.begin(); it!=total_points.end(); ++it)
		{
			if (*it >= 3 * best_result_standard - 2)
			{
				how_many++;
				continue;
			}

			if ((*it >= 3 * best_result_standard - 4) && (surprising_count > 0))
			{
				how_many++;
				surprising_count--;
			}
		}
	}
};


int main()
{
	ifstream ifs("B-small-attempt0.in");
	ofstream ofs("B-small-attempt0.out");

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

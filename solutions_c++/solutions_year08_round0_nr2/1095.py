#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdlib>
using namespace std;

inline int cnv_time (string time_str)
{
	return atoi (time_str.substr(0,2).c_str()) * 60 + atoi(time_str.substr(3,2).c_str());
}

// Time vs. arrival/dept.
typedef pair<int, bool> Train;

int cmp_trains (const Train& t1, const Train& t2)
{
	if (t1.first == t2.first)
		return t1.second > t2.second;
	else
		return t1.first < t2.first;
}


int main ()
{
	int i_cases;

	cin >> i_cases;

	for (int i = 0; i < i_cases ; i++)
	{
		int turn, i_a, i_b, a_cnt=0, b_cnt=0;
		cin >> turn;
//		turn - 1; // To resolve cases where A = B;
		cin >> i_a >> i_b;
		vector<Train> A, B;
		cin.ignore();
		string time_str;
		for (int j = 0; j < i_a; j++)
		{
			getline (cin, time_str);

		//	cout << cnv_time (time_str.substr(0, 5)) << " | " << (cnv_time (time_str.substr(6, 5)) + turn) << endl;
			A.push_back (Train(cnv_time (time_str.substr(0, 5)), false));
			B.push_back (Train(cnv_time (time_str.substr(6, 5)) + turn, true));
		}

		for (int j = 0; j < i_b; j++)
		{
			getline (cin, time_str);

		//	cout << cnv_time (time_str.substr(0, 5)) << " | " << (cnv_time (time_str.substr(6, 5)) + turn) << endl;
			B.push_back (Train(cnv_time (time_str.substr(0, 5)), false));
			A.push_back (Train(cnv_time (time_str.substr(6, 5)) +turn, true));
		}

		sort (A.begin(), A.end(), cmp_trains);
		sort (B.begin(), B.end(), cmp_trains);

		i_a = 0;
		for (vector<Train>::iterator ii = A.begin(); 
						ii != A.end(); ++ii)
		{
		//	cout << ii->first << ": " << ii->second << " : " << i_a << endl;
			if (ii->second) i_a++;
			else i_a--;
			if (i_a < 0)
			{
				i_a = 0;
				a_cnt++;
			}
		}

		i_b = 0;
		for (vector<Train>::iterator ii = B.begin(); 
						ii != B.end(); ++ii)
		{
		//	cout << ii->first << ": " << ii->second << " : " << i_b << endl;
			if (ii->second) i_b++;
			else i_b--;
			if (i_b < 0)
			{
				i_b = 0;
				b_cnt++;
			}
		}
		cout << "Case #" << i+1 << ": " << a_cnt << " " << b_cnt << endl;
	}

}


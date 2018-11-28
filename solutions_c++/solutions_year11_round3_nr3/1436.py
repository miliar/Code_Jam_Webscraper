

#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
#include <utility>
#include <list>
#include <set>

#define FOR(a,b,c) for(int a = (b); a < (c); ++a)
#define FORI(a,b) for((a)::iterator b = (a).begin(); b < (a).end(); ++b)
#define REP(a,b) for(int a = 0; a < (b); ++a)

using std::cin;
using std::cout;
using std::endl;

using std::vector;
using std::string;
using std::pair;
using std::list;
using std::set;

using std::make_pair;

class doesnt_divide
{
public:
	doesnt_divide(long long x) : i(x) {}
	bool operator()(long long x) { 
		//if (i % x && x % i)
		//	cout << "not divisible: " << i << " " << x << endl;
		return i % x && x % i;
	}
	long long i;
};

//bool is_multiple(long long x, set<long long> &div)
//{
//	if (div.size() == 0)
//		return false;
//	long long r = std::sqrt((long double)x);
//	long long j = *div.begin();
//	for (set<long long>::iterator i = div.begin(); i != div.end(); i++)
//	{
//		if (r < *i)
//			return false;
//		if (x % *i == 0)
//			return true;
//	}
//	return false;
//}

void test_case(int case_num)
{
	int note_count;
	long long low, high, note, min_note = 0x7fffffffffffffff, mid_note = 0, min_start;
	cin >> note_count >> low >> high;
	vector<long long> notes;
	REP(i,note_count)
	{
		cin >> note;
		if (note > 3 && note < 100000)
			mid_note = std::max(mid_note, note);
		min_note = std::min(min_note, note);
		notes.push_back(note);
	}

	if (low == 1)
	{
		cout << "Case #" << case_num + 1 << ": 1" << endl;
			return;
	}

	//if (mid_note != 0)
	//	min_note = mid_note;

	//min_start = (low / min_note + 1) * min_note;
	//

	//vector<long long> divisors;
	//for (long long i = low; i <= min_note; i++)
	//{
	//	if (min_note % i == 0)
	//		divisors.push_back(i);
	//}
	//for (long long i = min_start; i < high; i += min_note)
	//{
	//	divisors.push_back(i);
	//}
	//divisors.push_back(high);

	//REP(i,note_count)
	//{
	//	divisors.erase(std::remove_if(divisors.begin(), divisors.end(), doesnt_divide(notes[i])),divisors.end());

	//	if (divisors.size() == 0)
	//	{
	//		cout << "Case #" << case_num + 1 << ": NO" << endl;
	//		return;
	//	}
	//}

	vector<long long> divisors;
	for (long long i = low; i <= high; i++)
	{
		divisors.push_back(i);
	}
	REP(i,note_count)
	{
		divisors.erase(std::remove_if(divisors.begin(), divisors.end(), doesnt_divide(notes[i])),divisors.end());

		if (divisors.size() == 0)
		{
			cout << "Case #" << case_num + 1 << ": NO" << endl;
			return;
		}
	}

	//for (vector<long long>::iterator i = divisors.begin(); i != divisors.end(); i++) cout << *i << " ";
	cout << "Case #" << case_num + 1 << ": " << *divisors.begin() << endl;
}


int main(int argc, char* argv[])
{
	int t; cin >> t;
	REP(i,t) test_case(i);
}

#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

struct letr
{
	int index, count;
};

bool lessltr(const letr &l1, const letr &l2)
{
	return l1.count>l2.count;
}

int main(int argc, char* argv[])
{
	int scount, qcount, count;
	int i, j, t;

	int p, k, l;

	vector<letr> letters;
	letr ll;

	cin >> count;
	for(i=0;i<count;i++)
	{
	cin >> p >> k >> l;

	letters.clear();
	for(j=0;j<l;j++)
	{
		ll.index = j;
		cin >> ll.count;
		letters.push_back(ll);
	}

	sort(letters.begin(), letters.end(), lessltr);

	/*for(j=0;j<l;j++)
		cout << letters[j].index << "-" << letters[j].count << endl;
*/
	long long int r = 0;
	for(j=0;j<l;j++)
		r += letters[j].count*(j/k + 1);

	//result
		cout << "Case #" << i+1 << ": ";
		cout << r;
		cout << endl;
	}


	return 0;
}


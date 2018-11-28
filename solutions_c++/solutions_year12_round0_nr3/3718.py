#include <iostream>
#include <string>
#include <set>

using namespace std;

std::set< pair<int, int>> s;

int get_length(int t)
{
	int r = 0;
	while (t)
	{
		r++;
		t /= 10;
	}
	return r;
}

int count (int A, int B)
{
	int i, j, l = get_length(A), val;
	int pow10 = 1;
	
	for (j = 1; j <= l; ++j)
	{
		pow10 *= 10;
	}
	
	int pow10_inv;
	int pow10_rev;

	for (i = A; i <= B; ++i)
	{
		pow10_inv = 1;
		pow10_rev = pow10;

		for (j = 1; j <= l; ++j)
		{
			pow10_inv *= 10;
			pow10_rev /= 10;

			val = (i % pow10_inv) * pow10_rev + i / pow10_inv;
			if ((val >= A) && (val <= B) && (val > i))
			{
				s.insert(pair<int,int>(val, i));
			}
		}
	}
	int res = s.size();
	s.clear();
	return res;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t;
	cin >> t;
	int i, A, B;
	for (i = 1; i <= t; ++i)
	{
		cin >> A >> B;
		cout << "Case #" << i << ": " << count(A,B) << "\n";
	}
	return 0;
}
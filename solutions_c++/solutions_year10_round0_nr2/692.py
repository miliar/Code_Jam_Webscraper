#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

class Long
{
public:
	vector<int> data;

	Long()
	{
		
	}

	Long(string str)
	{
		for (int i = (int)str.length() - 1; i >= 0; i--)
			data.push_back((int)str[i] - (int)'0');
	}

	bool operator < (const Long &value) const
	{
		if ((int)data.size() < value.data.size())
			return true;

		if ((int)data.size() > value.data.size())
			return false;

		for (int i = (int)data.size() - 1; i >= 0; i--)
		{
			if (data[i] != value.data[i])
				return (data[i] < value.data[i]);
		}

		return false;
	}

	bool operator == (const Long &value) const
	{
		if ((int)data.size() < value.data.size())
			return false;

		if ((int)data.size() > value.data.size())
			return false;

		for (int i = (int)data.size() - 1; i >= 0; i--)
		{
			if (data[i] != value.data[i])
				return false;
		}

		return true;
	}

	Long operator * (const int value) const
	{
		Long rez;

		int tmp = 0;

		for (int i = 0; i < (int)data.size(); i++)
		{
			rez.data.push_back((data[i] * value + tmp) % 10);
			tmp = (data[i] * value + tmp) / 10;
		}

		if (tmp > 0)
			rez.data.push_back(tmp);

		return rez;
	}

	Long operator / (const Long &value) const
	{
		Long rez, tmp;

		for (int i = (int)data.size() - 1; i >= 0; i--)
		{
			tmp.data.push_back(data[i]);
			reverse(tmp.data.begin(), tmp.data.end());
			if (value < tmp || value == tmp)
			{
				for (int j = 1; j <= 10; j++)
				{
					if (tmp == value * j)
					{
						rez.data.push_back(j);
						tmp.data.clear();
						break;
					}
					else if (tmp < value * j)
					{
						rez.data.push_back(j - 1);
						tmp = tmp - value * (j - 1);
						break;
					}
				}
			}
			else
				rez.data.push_back(0);

			reverse(tmp.data.begin(), tmp.data.end());
		}

		reverse(rez.data.begin(), rez.data.end());

		rez.Trim();

		return rez;
	}

	Long operator % (const Long &value) const
	{
		Long rez, tmp;

		for (int i = (int)data.size() - 1; i >= 0; i--)
		{
			tmp.data.push_back(data[i]);
			reverse(tmp.data.begin(), tmp.data.end());
			if (value < tmp || value == tmp)
			{
				for (int j = 1; j <= 10; j++)
				{
					if (tmp == value * j)
					{
						rez.data.push_back(j);
						tmp.data.clear();
						break;
					}
					else if (tmp < value * j)
					{
						rez.data.push_back(j - 1);
						tmp = tmp - value * (j - 1);
						break;
					}
				}
			}
			else
				rez.data.push_back(0);

			reverse(tmp.data.begin(), tmp.data.end());
		}

		reverse(rez.data.begin(), rez.data.end());

		reverse(tmp.data.begin(), tmp.data.end());

		rez.Trim();

		tmp.Trim();

		return tmp;
	}

	void Trim()
	{
		while (data.size() > 1 && data[(int)data.size() - 1] == 0)
			data.erase(--data.end());
	}

	bool IsNull()
	{
		if (data.empty())
			return true;

		return ((int)data.size() == 1 && data[0] == 0);
	}

	Long operator - (const Long &value) const
	{
		Long rez;
		int mem = 0;
		int plus = 0;
		int c = 0;

		for (int i = 0; i < (int)data.size(); i++)
		{
			if (i >= value.data.size())
				c = 0;
			else
				c = value.data[i];

			if (plus > 0 && data[i] > 0)
				mem = -1;

			if (data[i] + mem >= c && (data[i] != 0 || plus == 0))
			{
				rez.data.push_back(data[i] - c + mem);

				if (plus > 0)
				{
					plus = 0;
					mem = 0;
				}
			}
			else
			{
				if (plus == 0)
					plus = 10;

				rez.data.push_back(plus + data[i] - c);
				
				if (plus == 10)
					plus = 9;
			}
		}

		rez.Trim();

		return rez;
	}
};

Long GCD(Long a, Long b)
{
	while ( !(a.IsNull()) && !(b.IsNull()) )
	{
		if (a < b)
			b = b % a;
		else
			a = a % b;
	}

	if (a < b)
		return b;
	return a;
}

int c, n;
string temp;
vector<Long> nums, rezults;
Long rez;

int main()
{
	freopen("B-small.in", "r", stdin);
	freopen("B-small.out", "w", stdout);

	cin >> c;

	for (int i = 0; i < c; i++)
	{
		cin >> n;

		nums.clear();
		rezults.clear();
		nums.resize(n);

		for (int j = 0; j < n; j++)
		{
			cin >> temp;
			nums[j] = Long(temp);
		}

		for (int j = 0; j < n; j++)
			for (int u = 0; u < n; u++)
			{	
				if (j == u || nums[j] == nums[u])
					continue;

				if (nums[j] < nums[u])
					rezults.push_back(nums[u] - nums[j]);
				else
					rezults.push_back(nums[j] - nums[u]);
			}

		//sort(rezults.begin(), rezults.end());

		Long tmp2 = Long("999999999999999999999999999999999999999999999999999999999999999999999999999");

		for (int j = 0; j < (int)nums.size(); j++)
			if (nums[j] < tmp2)
				tmp2 = nums[j];

		//sort(nums.begin(), nums.end());
		Long tmp1 = rezults[0];

		for (int j = 1; j < (int)rezults.size(); j++)
			tmp1 = GCD(tmp1, rezults[j]);


		//while (tmp1 < tmp2 && !(tmp1 == tmp2))
		tmp2 = tmp2 % tmp1;

		if (tmp2.IsNull())
			rez = Long("0");
		else
			rez = tmp1 - tmp2;

		cout << "Case #" << i + 1 << ": ";

		for (int j = (int)rez.data.size() - 1; j >= 0; j--)
			cout << rez.data[j];

		cout << endl;
	}
	return 0;
}
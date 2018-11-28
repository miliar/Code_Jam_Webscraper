#include <iostream>
#include <vector>

using namespace std;

struct Triplet
{
	bool amaze;
	int a, b, c;
	Triplet()
	{}
	Triplet(int aa, int ab, int ac, bool interest)
		:a(aa), b(ab), c(ac), amaze(interest)
	{}
};

int main ()
{
	vector< vector<Triplet> > v(31);
	for(int n = 0; n < 31; n++)
	{
		for (int i = 0; i < 11; i++)
		{
			for (int j = 0; j < 3; j++)
			{
				for (int k = j; k < 3; k++)
				{
					if (i + (i + j) + (i + k) == n)
					{
						bool amaze = false;
						if (j == 2 && k == 2 || j == 1 && 2 == k || j == 0 && k == 2)
						{
							amaze = true;
						}
						v[n].push_back(Triplet(i, i + j, i + k, amaze));
					}
				}
			}
		}
	}
	
	int t;
	cin >> t;

	vector<int> res(t);
	for (int i = 0; i < t; i++)
	{
		int n, s, p, counter = 0;
		cin >> n >> s >> p;
		vector<int> ans;
		for (int j = 0; j < n; j++)
		{
			int temp;
			cin >> temp;
			if (temp != 0 && temp != 1 && (v[temp][1].a >= p || v[temp][1].b >= p || v[temp][1].c >= p) && 
				(v[temp][0].a >= p || v[temp][0].b >= p || v[temp][0].c >= p))
			{
				counter++;
			}
			else
			{
				ans.push_back(temp);
			}
		}

		for(int j = 0; j < (int)ans.size(); j++)
		{
			if(ans[j] == 0 || ans[j] == 1)
			{
				if(v[ans[j]][0].a >= p || v[ans[j]][0].b >= p || v[ans[j]][0].c >= p)
				{
					counter++;
				}
			}
			if(s > 0 && ans[j] != 0 && ans[j] != 1 && (v[ans[j]][0].a >= p || v[ans[j]][0].b >= p || v[ans[j]][0].c >= p))
			{
				counter++;
				s--;
			}
			else if(ans[j] != 0 && ans[j] != 1 && (v[ans[j]][1].a >= p || v[ans[j]][1].b >= p || v[ans[j]][1].c >= p))
			{
				counter++;
			}
		}
		res[i] = counter;
	}
	for (int i = 0; i < t; i++)
	{
		cout << "Case #" << i + 1 << ": " << res[i] << endl;
	}
	
}
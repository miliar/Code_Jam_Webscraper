#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <fstream>
#include <algorithm>
#include <memory.h>

using namespace std;

vector<int> vi;


int main()
{
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("bSout1.txt", "w", stdout);
	int cas;
	cin >> cas;
	for(int ca=1; ca<=cas; ca++)
	{
		vi.clear();
		cout << "Case #" << ca <<": ";
		int l, n, c;
		long long t;
		int i, j;
		cin >> l >> t >> n >> c;
		for(i=0; i<c; i++)
		{
			int tmp;
			cin >> tmp;
			vi.push_back(tmp * 2);
		}
		vector<int> need;
		for(i=0;i<n;i++)
			need.push_back(vi[i%c]);
		long long sum = 0;
		for(i=0;i<n;i++)
			if(sum + need[i] >= t)
				break;
			else
				sum += need[i];
		if(i != n)
		{
			if(sum + need[i] == t)
				i++;
			if(sum + need[i] >  t)
			{
				int tmp = need[i];
				need[i] = t - sum;
				need.push_back(tmp - need[i]);
				i++;
			}
			sort(need.begin()+i, need.end(), greater<int>());
			while(l--)
				need[i++] /= 2;
		}
		sum = 0;
		for(int i = 0; i<need.size(); i++)
			sum += need[i];
		cout << sum << endl;
	}
	return 0;
}

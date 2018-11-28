/*#include <iostream>
#include <cstring>
#include <fstream>
#include <sstream>
using namespace std;
int repeat(int n)
{
	int sum = 0;
	int t = 0;
	while(n>0)
	{
		t = n%10;
		t *= t;
		sum += t;
		n /= 10;
	}
	return sum;
}
const int maxloop = 100;
int change(int num, int b)
{
	if(num == 0)
		return 0;

	int m = 1;
	while(num>=m)
	{
		m *= b;
	}
	m /= b;

	int res = 0;
	while(m > 0)
	{
		res += num / m;
		res *= 10;
		num %= m;
		m /= b;
	} 
	return res/10;
}
bool ishappy(int num, int b)
{
	int count = 0;
	while(count++ <maxloop)
	{
		
			if(num == 1)
				return true;
				
		num = repeat(num);
		num = change(num, b);
	}
	return false;
}
const int maxlen = 21;
const int maxnum = 100000;
bool happy[11][maxnum];
void init()
{
	memset(happy , 0, sizeof(bool)*11*maxnum);

	int num, i, j;
	for(i=2; i<maxnum; ++i)
	{
		happy[10][i] = ishappy(i, 10);
		for(j=2; j<10; j++)
		{
			int t = change(i, j);
			happy[j][i] = ishappy(t, j);
		}
	}
}
int main()
{
	init();

	int t, i, c=1, j;
	cin >> t;
	char str[maxlen];
	int bases[maxlen];

	ofstream out("result.txt");
	getchar();
	while(c <= t)
	{
		int count = 0;
		cin.getline(str, maxlen);
		istringstream ss(str);
		while(ss >> bases[count])
		{
			count++;
		}
	

		bool mins = true;
		for(i=2; i<maxnum; i++)
		{
			mins = true;
			for(j=0; j<count; j++)
			{
				mins = mins && happy[bases[j]][i];
				if(!mins)
					break;
			}
			if(mins)
			{
				out << "Case #" << c <<": " << i << endl;
				break;
			}

		}
		if(!mins)
		{
			for(i=maxnum; i<20000000; i++)
			{
				mins = true;
				for(j=count-1; j>=0; j--)
				{
					if(bases[j] == 10)
					{
						mins = mins && ishappy(i, bases[j]);						
					}
					else
						mins = mins && ishappy(change(i,bases[j]), bases[j]);
					if(!mins)
						break;
				}
				if(mins)
				{
					out << "Case #" << c <<": " << i << endl;
					break;
				}
			}
		}
		c++;
	}

	out.close();
}*/
/*
#include <iostream>
#include <cstring>
#include <fstream>
#include <sstream>
using namespace std;
struct Node
{
	int s, w, t;
};
Node road[21][21];
int time[42][42];
int GetSouthToNorth(int i, int j, int t)
{
	int sum = road[i][j].s + road[i][j].w;

	if(t > road[i][j].t)
	{
		t = (t-road[i][j].t) % sum;
		if(t>=0 && t < road[i][j].s)
			return 0;
		else 
			return sum-t;
	}
	else
	{
		t = (road[i][j].t-t) % sum;
		if(t>0 && t<=road[i][j].w)
			return t;
		else 
			return 0;
	}
	return 0;
}

int GetWestToEast(int i, int j, int t)
{
	int sum = road[i][j].s + road[i][j].w;

	if(t > road[i][j].t)
	{
		t = (t-road[i][j].t) % sum;
		if(t>=0 && t<road[i][j].s)
			return road[i][j].s-t;
		else
			return 0;
	}
	else
	{
		t = (road[i][j].t-t) % sum;
		if(t>0 && t<=road[i][j].w)
		{
			return 0;
		}
		else if(t == 0)
		{
			return road[i][j].s;
		}
		return t-road[i][j].w;
	}
}
int dir[4][2] = {{0, 1},{0,-1},{1,0},{-1,0}};
bool inbound(int n, int m, int i, int j)
{
	return i<n&& i>= 0 && j<m && j>=0;
}

int main()
{
	int c, ts=0, n, m, i, j;
	cin >> c;

	ofstream out("res.txt");
	while(ts++<c)
	{
		cin >> n >> m;
		for(i=0; i<n; i++)
		{
			for(j=0; j<m; j++)
			{
				cin >> road[i][j].s >> road[i][j].w >> road[i][j].t;
			}
		}
		memset(time , 0, sizeof(int)*42*42);

		for(j=1; j<2*m; ++j)
		{
			if(j%2 == 1)
			{
				time[2*n-1][j] = time[2*n-1][j-1] + GetWestToEast(n-1, j/2, time[2*n-1][j-1]) + 1;
			}
			else
			{
				time[2*n-1][j] = time[2*n-1][j-1] + 2;
			}
		}
		for(i=2*n-2; i>=0; --i)
		{
			if(i%2 == 0)
			{
				time[i][0] = time[i+1][0] + GetSouthToNorth(i/2, 0, time[i+1][0]) + 1;
			}
			else
			{
				time[i][0] = time[i+1][0] + 2;
			}
		}

		for(i=2*n-2; i>=0; --i)
		{
			for(j=1; j<2*m; ++j)
			{
				int west_t, south_t;
				if(j%2 == 1)
				{
					west_t = time[i][j-1] + GetWestToEast(i/2, (j-1)/2, time[i][j-1]) + 1;
				}
				else
				{
					west_t = time[i][j-1] + 2;
				}

				if(i%2 == 0)
				{
					south_t = time[i+1][j] + GetSouthToNorth((i+1)/2, j/2, time[i+1][j]) + 1;
				}
				else
				{
					south_t = time[i+1][j] + 2;
				}

				time[i][j] = min(west_t, south_t);
			}
		}

		out << "Case #" << ts << ": " << time[0][2*m-1] << endl;
		

	}
	out.close();
	return 0;
}*/
/*
#include <iostream>
#include <cstring>
#include <fstream>
#include <sstream>
#include <set>
#include <map>
using namespace std;
const int MAXLEN= 65;
int main()
{
	char str[MAXLEN];
	int t, cs=0, i;
	cin >> t;
	ofstream out("res.txt");
	while(cs++ < t)
	{
		cin >> str;
		int len = strlen(str);
		set<char> kinds;
		map<char, int> maps;
		int num = 1;
		for(i=0; i<len; i++)
		{
			if(kinds.find(str[i]) == kinds.end())
			{
				kinds.insert(str[i]);
				maps.insert(make_pair(str[i], num));
				if(num == 1)
					num = 0;
				else if(num == 0)
					num = 2;
				else
					num++;
			}
		}
		int count = kinds.size();
		if(count < 2)
			count = 2;
		
		long long res = 0;
		for(i=0; i<len; i++)
		{
			res *= count;
			res += maps[str[i]];
		}
		cout << "Case #" << cs << ": " << res << endl;
		out << "Case #" << cs << ": " << res << endl;
	}
	return 0;
}*/
/*
#include <iostream>
#include <cstring>
#include <fstream>
#include <sstream>
#include <cmath>
#include <set>
#include <map>
using namespace std;
void findmid(int s, int e, int nums[], int a, int b, int &res)
{
	int mins = 100000000;
	int mini = 0;
	int sum = (s+e);
	for(int i=a; i<b; i++)
	{
		int temp = abs(sum-2*nums[i]);
		if(temp < mins)
		{
			mins = temp;
			mini = i;
		}
	}
	res += e-s;
	if(a < mini)
	{
		findmid(s, nums[mini]-1, nums, a, mini, res);
	}
	if(mini+1 < b)
	{
		findmid(nums[mini]+1, e, nums, mini+1, b, res);
	}
}
int nums[10001];
int main()
{
	int p, q, i;
	int n, cs = 0;
	cin >> n;
	ofstream out("res.txt");
	while(cs++ < n)
	{
		cin >> p >> q;
		for(i=0; i<q; i++)
		{
			cin >> nums[i]; 
		}
		int res = 0;
		findmid(1, p, nums, 0, q, res);
		cout << "Case #" << cs << ": " << res << endl;
		out << "Case #" << cs << ": " << res << endl;
	}
	return 0;
}*/
#include <iostream>
#include <cstring>
#include <fstream>
#include <sstream>
#include <cmath>
#include <algorithm>
using namespace std;
int Bribe(int p, int q, int nums[])
{
	int i, j;
	int res = 0;
	bool state[101];
	memset(state, 0, sizeof(bool)*101);
	for(i=0; i<q; i++)
	{
		state[nums[i]] = true;
		for(j=nums[i]+1; j<=p && !state[j]; j++)
		{
			res++;
		}
		for(j=nums[i]-1; j>0 && !state[j]; j--)
		{
			res++;
		}
	}
	return res;
}
int main()
{
	int p, q, i;
	int n, cs = 0;
	cin >> n;
	ofstream out("res.txt");
	int nums[101];
	while(cs++ < n)
	{
		cin >> p >> q;
		for(i=0; i<q; i++)
		{
			cin >> nums[i]; 
		}
		int res = 10000000;
		do
		{
			int tempres = Bribe(p, q, nums);
			if(res > tempres)
			{
				res = tempres;
			}
		}
		while(next_permutation(nums, nums+q));


		cout << "Case #" << cs << ": " << res << endl;
		out << "Case #" << cs << ": " << res << endl;
	}
	out.close();
	return 0;
}
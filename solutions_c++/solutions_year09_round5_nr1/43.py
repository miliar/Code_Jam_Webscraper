#include <iostream>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <deque>

using namespace std;

const int	maxNM = 150;
const int	maxS = 1000000;

typedef vector<int> state_t;

pair<state_t,int>	queue[maxS];
int			n, m, answer, op, cl;
string		board;
state_t		final;
set<state_t> hash;

bool empty(state_t &s, int p)
{
	if (board[p] == '#') return false;
	for (int i = 0; i < s.size(); ++i) if (s[i] == p) return 0;
	return true;
}

bool is_connect(state_t &s)
{
	static int queue[10];
	static bool used[10];
	memset(used, 0, s.size() * sizeof(used[0]));
	int op = 0, cl = 1;
	queue[0] = s[0];
	used[0] = true;
	while (op < cl)
	{
		int u = queue[op++];
		for (int i = 0; i < s.size(); ++i) if (!used[i])
			if (abs(u - s[i]) == m || u % m > 0 && u == s[i] + 1 || u % m != m - 1 && u == s[i] - 1)
			{
				used[i] = true;
				queue[cl++] = s[i];
			}
	}
	return cl == s.size();
}

void push(state_t &s, int depth)
{
	queue[cl++] = make_pair(s, depth);
	hash.insert(s);
}

pair<state_t, int>& pop()
{
	++op;
	return queue[op - 1];
}

bool try_push(state_t &s, bool flag)
{
	sort(s.begin(), s.end());
//	printf("s = (%d %d %d), flag = %d, is_connect = %d\n", s[0], s[1], s[2], (int)flag, (int) is_connect(s));
	if (!flag && !is_connect(s)) return false;
	if (hash.count(s)) return false;
//	cout << "compile" << ' ' << s[0] << ' ' << s[1] << ' ' << final[0] << ' ' << final[1] << ' ' << (s == final) << endl;
	if (s == final) return true;
	push(s, answer);
	return false;
}

bool move_ud(state_t s, int k, bool flag)
{
	//k + m >= n * m || board[k + m] == '#' || find(s, k + m)
//		|| k < m || board[k + m] == '#' || find(s, k + m))
	if (s[k] - m < 0 || s[k] + m >= n * m) return false;
	if (!empty(s, s[k] + m) || !empty(s, s[k] - m)) return false;

	state_t temp = s;
	temp[k] += m;
	if (try_push(temp, flag)) return true;

	temp = s;
	temp[k] -= m;
	if (try_push(temp, flag)) return true;
	return false;
}

bool move_lr(state_t s, int k, bool flag)
{
	if (s[k] % m == 0 || s[k] % m == m - 1) return false;
	if (!empty(s, s[k] + 1) || !empty(s, s[k] - 1)) return false;

	state_t temp = s;
	temp[k] += 1;
	if (try_push(temp, flag)) return true;

	temp = s;
	temp[k] -= 1;
	try_push(temp, flag);
	if (try_push(temp, flag)) return true;
	return false;
}

int	main()
{
	int task;
	cin >> task;
	for (int now_case = 0; now_case < task; ++now_case)
	{
		cin >> n >> m;
		board = "";
		string line;
		hash.clear();
		for (int i = 0; i < n; ++i) 
		{
			cin >> line;
			board += line;
		}

		state_t s;
		state_t t;
		for (int i = 0; i < board.size(); ++i)
		{
			if (board[i] == 'o' || board[i] == 'w') s.push_back(i);
			if (board[i] == 'x' || board[i] == 'w') t.push_back(i);
		}

		if (s == t)
		{
			printf("Case #%d: %d\n", now_case + 1, 0);
			continue;
		}

		final = t;

		op = cl = 0;
		push(s, 0);

		bool no_solution = true;

		while (op < cl)
		{
			pair<state_t, int> head = pop();
			state_t &x = head.first;
			int depth = head.second;
			bool flag = is_connect(x);
			answer = depth + 1;
//			cout << x[0] << ' ' << x[1] << ' ' << x[2] << ' ' << flag << endl;
			
			bool found = false;
			for (int i = 0; i < x.size(); ++i)
			{
				if (move_ud(x, i, flag)) found = true;
				if (move_lr(x, i, flag)) found = true;
			}

//			cout << "op, cl, found = " << op << ' ' << cl << ' ' << found << endl;

			if (found) 
			{
				no_solution = false;
				break;
			}
		}
		printf("Case #%d: %d\n", now_case + 1, no_solution ? -1 : answer);
	}
	return 0;
}

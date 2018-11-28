#include <iostream>
#include <vector>

using namespace std;

typedef struct {
	char name;
	int cur;
	int nxt;
	bool pushing;
}Bot_t;

class BotTrust {
public:
	BotTrust::BotTrust() {
		int t;
		cin >> t;
		for (int i = 0; i < t; i++)
			solveCase(i);
	}

	void solveCase(int cn) {
		int n;
		cout << "Case #" << (cn + 1) << ": ";
		cin >> n;
		runCase(n);
		//cout << n << endl;
	}

	void runCase(int n)
	{
		int b;
		char c = 'n';
		vector<char> q;
		vector<int> blu;
		vector<int> org;
		for (int i = 0; i < n; i++)	{
			cin >> c;
			cin >> b;
			if ('B' == c)
				blu.push_back(b);
			else
				org.push_back(b);
			q.push_back(c);
		}
		cout << solve(q, blu, org) << endl;
	}

	void run_robot(Bot_t &rob, char pushRob, int &i0, int &i1)
	{
		if (rob.pushing)
		{
			rob.pushing = false;
//			i1++;
		}
//		else
//		{
			if (rob.nxt == rob.cur)
			{
				if (pushRob == rob.name)
				{
					rob.pushing = true;
					i0++;
					i1++;
				}
			}
			else {
				if (rob.nxt < rob.cur)
					rob.cur--;
				else
					rob.cur++;
			}
//		}
	}

	void print_rob_state(Bot_t &r, char pushRob)
	{
		cout << r.name << (pushRob == r.name ? "*":"-") << ":" << (r.pushing ? "P" : ".");
		if (r.cur == r.nxt)
			cout << "(" << r.cur << ")  ";
		else
			cout << "(" << r.cur << "-->" << r.nxt << ")  ";
	}

	int solve(vector<char> q, vector<int> b, vector<int> o)
	{
		int ib = 0;
		int io = 0;
		int t = 0;
		Bot_t blu = {'B', 1, (b.size() > 0) ? b[0] : 1, false};
		Bot_t org = {'O', 1, (o.size() > 0) ? o[0] : 1, false};

		int i = 0;
		while (i < q.size())
		{
			char pushRob = q[i];
//			cout << "T"<<t << " ";
//			print_rob_state(blu, pushRob);
//			print_rob_state(org, pushRob);
//			cout << endl;
			run_robot(blu, pushRob, i, ib);
			run_robot(org, pushRob, i, io);
			if (ib < b.size())
				blu.nxt = b[ib];
			if (io < o.size())
				org.nxt = o[io];
			t++;
		}
		//cout << "FINAL STATE"<< endl;
		//print_rob_state(blu, 'g');
		//print_rob_state(org, 'g');
		//cout << endl;
		return t;
				
//		cout << q.size() << "," << b.size() << "," << o.size() << endl;
/*
		for (int i = 0; i < q.size(); i++) {
			int c = ('B' == q[i] ? b[ib++] : o[io++]);
			cout << q[i] << c << " ";
		}
		cout << endl;
		return 0;
		*/
	}
};

int main()
{
	BotTrust* bt = new BotTrust();
	delete bt;
}

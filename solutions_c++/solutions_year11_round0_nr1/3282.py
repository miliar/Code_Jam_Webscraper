#include <iostream>
#include <utility>
#include <vector>

using namespace std;

void move(int& position, const vector <int>& steps)
{
	if (!steps.size())
		return;
	if (steps[0] > position)
		++position;
	if (steps[0] < position)
		--position;
}

int main(int argc, char** argv)
{
	int tests;
	cin >> tests;
	for (int i = 0; i < tests; ++i)
	{
		int n;
		cin >> n;
		vector <int> o, b;
		vector <pair <char, int> > buttons;
		for (int j = 0; j < n; ++j)
		{
			char c;
			int button;
			cin >> c >> button;
			buttons.push_back(make_pair(c, button));
			if (c == 'O')
				o.push_back(button);
			else
				b.push_back(button);
		}
		int po = 1, pb = 1, time;
		for (time = 0; buttons.size(); ++time)
		{
			if (buttons[0].first == 'O' && buttons[0].second == po)
			{
				buttons.erase(buttons.begin());
				o.erase(o.begin());
				move(pb, b);
			}
			else if(buttons[0].first == 'B' && buttons[0].second == pb)
			{
				buttons.erase(buttons.begin());
				b.erase(b.begin());
				move(po, o);
			}
			else
			{
				move(pb, b);
				move(po, o);
			}
		}
		cout << "Case #" << (i + 1) << ": " << time << endl;
	}
	return 0;
}

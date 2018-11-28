#include <iostream>
#include <queue>

using namespace std;

int main()
{
	int t;
	
	cin >> t;
	
	for (int i = 0; i < t; i++)
	{
		int n;
		
		int o_pos = 1;
		int b_pos = 1;
		
		queue<int> o_buttons;
		queue<int> b_buttons;
		queue<char> bot_sequence;
		
		cin >> n;
		
		for (int j = 0; j < n; j++)
		{
			char r;
			int p;
			
			cin >> r >> p;
			
			bot_sequence.push(r);
			
			if (r == 'O')
			{
				o_buttons.push(p);
			}
			else if (r == 'B')
			{
				b_buttons.push(p);
			}
		}
		
		int y = 0;
		
		while (!bot_sequence.empty())
		{
			bool pushed = false;
			if (!o_buttons.empty())
			{
				if (o_pos == o_buttons.front())
				{
					if (bot_sequence.front() == 'O')
					{
						o_buttons.pop();
						pushed = true;
					}
				}
				else if (o_pos < o_buttons.front())
				{
					o_pos++; 
				}
				else
				{
					o_pos--;
				}
			}
			
			if (!b_buttons.empty())
			{
				if (b_pos == b_buttons.front())
				{
					if (bot_sequence.front() == 'B')
					{
						b_buttons.pop();
						pushed = true;
					}
				}
				else if (b_pos < b_buttons.front())
				{
					b_pos++;
				}
				else
				{
					b_pos--;
				}
			}
			
			if (pushed)
			{
				bot_sequence.pop();
			}
			
			y++;
		}
		
		cout << "Case #" << (i + 1) << ": " << y << "\n";
	}
}

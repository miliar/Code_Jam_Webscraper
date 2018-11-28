#include <iostream>
#include <sstream>

using namespace std;

struct seqType
{
	char bot;
	int button;
	int next;
};

struct bot
{
	int loc;
	int target;
};

int oneCase();
bool act(bot* b);

int main()
{
	int t;
	cin >> t;

	for (int i = 0; i < t; i++)
	{
		cout << "Case #" << i+1 << ": " << oneCase() << endl;
	}

	return 0;
}

int oneCase()
{
	int count;
	cin >> count;

	bot O;
	bot B;
	O.loc = B.loc = 1;
	O.target = B.target = -1;

	seqType seq[100];
	int lastO = -1;
	int lastB = -1;
	for (int i = 0; i < count; i++)
	{
		seq[i].next = -1;
		cin >> seq[i].bot >> seq[i].button;
		if (seq[i].bot == 'O')
		{
			if (O.target == -1) O.target = seq[i].button;
			if (lastO != -1) seq[lastO].next = seq[i].button;
			lastO = i;
		}
		else
		{
			if (B.target == -1) B.target = seq[i].button;
			if (lastB != -1) seq[lastB].next = seq[i].button;
			lastB = i;
		}
	}

	int time = 0;
	int curr = 0;
	while (curr < count)
	{
		time++;
		
		if (seq[curr].bot == 'O')
		{
			if (act(&O))
			{
				O.target = seq[curr].next;
				curr++;
			}
			act(&B);
		}
		else
		{
			if (act(&B))
			{
				B.target = seq[curr].next;
				curr++;
			}
			act(&O);
		}
	}

	return time;
}

bool act(bot* b)
{
	if (b->target == -1)
	{
		return false;
	}
	
	int diff = b->loc - b->target;
	if (diff == 0)
	{
		return true;
	}
	else if (diff < 0)
	{
		b->loc++;
	}
	else
	{
		b->loc--;
	}

	return false;
}
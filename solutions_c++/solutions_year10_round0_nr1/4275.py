#include <iostream>

using std::cin;
using std::cout;
using std::cerr;
using std::endl;

struct snappers
{
	bool on;
	snappers *next;
};

int main()
{
	unsigned long count;
	cin >> count;
	if(!cin)
	{
		cerr << "not a number..." << endl;
		return -1;
	}
	for(unsigned long i = 0 ; i < count ; i++)
	{
		long N, K;
		cin >> N >> K;
		if(!cin)
		{
			cerr << "not a number..." << endl;
			return -1;
		}
		// will it be on or off???
		if(N == 0)
		{
			cout << "Case #" << (i+1) << ": ON" << endl;
			break;
		}

		// we build a row of N snappers.
		snappers first = {false, 0};
		snappers *next = &first;
		for(long k = 1 ; k < N ; k++)
		{
			snappers *tmp = new snappers;
			tmp->on = false;
			tmp->next = 0;
			next->next = tmp;
			next = tmp;
		}

		// snap K times
		for(long k = 0 ; k < K ; k++)
		{
			snappers *next = &first;
			while(next != 0 && next->on)
			{
				next->on = false;
				next = next->next;
			}
			if(next != 0)
				next->on = true;
		}
		// all snappers on?
		next = &first;
		bool on = true;
		while(next != 0)
		{
			if(!next->on)
			{
				on = false;
				break;
			}
			next = next->next;
		}
		cout << "Case #" << (i+1) << ": " << (on ? "ON" : "OFF") << endl;
	}
}
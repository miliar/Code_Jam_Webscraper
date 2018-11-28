#include <iostream>

#define LIMIT 100
#define START 1
#define ORANGE 'O'
#define BLUE 'B'

using namespace std;

int abs(int n)
{
	if (n > 0)
		return n;
	return -1 * n;
}

void compensate(int & curr, int value, int ret)
{
	if (abs(value - curr) <= ret)
			curr = value;
	else
		if (value > curr)
			curr += ret;
		else
			curr -= ret;
}

int move(int & curr_o, int *& ptr_begin_o, int * ptr_end_o, int & curr_b, int *& ptr_begin_b, int * ptr_end_b, int *& ptr_begin, char turn)
{
	int ret = * ptr_begin;
	if (turn == BLUE)
	{
		ret = abs(ret - curr_b) + 1;
		curr_b = * ptr_begin;
		if (ptr_begin_o != ptr_end_o)
			compensate(curr_o, * ptr_begin_o, ret);
		/*cout << "B vai para " << curr_b << endl;
		cout << "O vai para " << curr_o << endl;*/
		++ ptr_begin_b;
	}
	else
	{
		ret = abs(ret - curr_o) + 1;
		curr_o = * ptr_begin;
		if (ptr_begin_b != ptr_end_b)
			compensate(curr_b, * ptr_begin_b, ret);
		/*cout << "O vai para " << curr_o << endl;
		cout << "B vai para " << curr_b << endl;*/
		++ ptr_begin_o;
	}
	++ ptr_begin;
	return ret;
}

int main()
{
	char robot;
	char sequence[LIMIT];
	int n, t, time;
	int curr_o, curr_b, diff_o, diff_b;
	int * ptr_begin, * ptr_end, * ptr_begin_o, * ptr_end_o, * ptr_begin_b, * ptr_end_b;
	int buttons[LIMIT], buttons_o[LIMIT], buttons_b[LIMIT];
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		time = 0;
		curr_o = START;
		curr_b = START;
		ptr_begin = buttons;
		ptr_end = buttons;
		ptr_begin_o = buttons_o;
		ptr_begin_b = buttons_b;
		ptr_end_o = buttons_o;
		ptr_end_b = buttons_b;
		cin >> n;
		for (int j = 0; j < n; j++)
		{
			cin >> robot;
			sequence[j] = robot;
			if (robot == ORANGE)
			{
				cin >> * ptr_end_o;
				* ptr_end = * ptr_end_o;
				++ ptr_end_o;
			}
			else
			{
				cin >> * ptr_end_b;
				* ptr_end = * ptr_end_b;
				++ ptr_end_b;
			}
			++ ptr_end;
		}
		for (int j = 0; j < n; j++)
			time += move(curr_o, ptr_begin_o, ptr_end_o, curr_b, ptr_begin_b, ptr_end_b, ptr_begin, sequence[j]);
		cout << "Case #" << i + 1 << ": " << time << endl;
	}
	return 0;
}

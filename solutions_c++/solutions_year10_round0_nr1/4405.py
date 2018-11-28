#include <iostream>
using namespace std;

struct Snapper {
	bool power;
	bool snap_on;
};


void clear(Snapper s[], int n)
{
	for (int i = 0; i < n; i++)
	{
		s[i].power = false;
		s[i].snap_on = false;
	}
	s[0].power = true;
}

void print(Snapper s[], int n)
{
	cout << "Status:" << endl;
	for (int i = 0; i < n; i++)
		cout << s[i].power << " " << s[i].snap_on << endl;
	cout << endl;
}

bool hasPower(Snapper s[], int n, int k)
{
	clear(s, n);
	//cout << "Entering ";
	//print(s, n);
	int hwp = 0;
	for (int i = 0; i < k; i++)
	{
		//cout << "Begin loop ";
		//print(s,n);
		for (int j = hwp; j >= 0; j--)
			s[j].snap_on = !s[j].snap_on;
		//cout << "Do Switch ";
		//print(s,n);
		//cout << "hwp ";
		for (int j = 0; j < n; j++)
		{
			hwp = j;
			if (s[j].snap_on && j < n -1)
				s[j+1].power = true;
			else
				break;
		//	cout << hwp << "\t";
		}
		//cout << endl;
		//cout << "Highest with Power: " << hwp << endl;
		//cout << "Turn on ones with power/snap_on ";
		//print(s, n);
		for (int j = hwp + 1; j < n; j++)
			s[j].power = false;
		//cout << "Turn off rest ";
		//print(s,n);
	}
	//cout << "Leaving ";
	//print(s,n);
	return s[n - 1].power && s[n - 1].snap_on;
}

int main()
{
	int snappers_size = 30;
	Snapper snappers[snappers_size];
	int tests;
	cin >> tests;
	for (int i = 0; i < tests; i++)
		{
			int n,k;
			cin >> n >> k;
			cout << "Case #" << i + 1 << ": " << (hasPower(snappers, n, k)? "ON"
			: "OFF") << endl;
		}
}

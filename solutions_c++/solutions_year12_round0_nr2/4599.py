#include <iostream>
#include <set>
#include <vector>
#include <map>
#include <fstream>
using namespace std;

int main(int argc, char **argv)
{
	ifstream ifstr;
	ifstr.open("input.txt", ios::in);
	int N;
	ifstr >> N;
	ofstream ofstr;
	ofstr.open("output.txt", ios::out);
	
	for (int i = 0; i < N; i++)
	{
		int n, s, p;
		ifstr >> n >> s >> p;
		// int *iArr = new int(n);
		int max = -1, maxind = -1, min = 31, minind = -1;
		int cnt = 0, sur = 0, norm = 0, onlynorm = 0;

		for (int j = 0; j < n; j++)
		{
			int num;
			ifstr >> num;
			if (num == 0 || num == 1)
			{
				if (num >= p)
					onlynorm++;
				// cout << norm << " " << sur << " " << onlynorm << " " << cnt << endl;
				continue;
			}
			int c[3] = {0,0,0};
			if (num%3 == 0)
			{
				if (num/3 >= p)
				{
					cnt++;
					norm++;
				}
				else if ((num/3)+1 >= p)
				{
					cnt++;
					sur++;
				}
			}
			else
			{
				int tmp = num-(3*(num/3));
				if (tmp == 1)
				{
					if ((num/3)+1 >= p)
					{
						cnt++;
						// sur++;
						norm++;
					}
				}
				else if (tmp == 2)
				{
					if ((num/3)+1 >= p)
					{
						cnt++;
						norm++;
					}
					else if ((num/3)+2 >= p)
					{
						cnt++;
						sur++;
					}
				}
			}
			// cout << norm << " " << sur << " " << onlynorm << " " << cnt << endl;
		}
		ofstr << "Case #" << i+1 << ": ";
		if ( sur > s) sur = s;
		ofstr << norm+sur+onlynorm << endl;

	}
	ofstr.close();
	ifstr.close();
	return 0;
}

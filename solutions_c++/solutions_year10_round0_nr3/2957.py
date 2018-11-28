#include <algorithm>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <deque>

using namespace std;

int main(int argc, char *argv[], char *envp[])
{
	int T = 0;
	int r = 0;
	int R = 0;
	int k = 0;
	int K = 0;
	int N = 0;
	int g = 0;
	int G = 0;
	int P = 0;
	deque<int> LineQueue;
	deque<int> TempQueue;
	ifstream file_in;
	ofstream file_out;

	file_in.open("input.txt", ios::in);
	file_out.open("output.txt", ios::out);

	file_in >> T;

	if (T > 0)
	{
		for (int i = 1; i <= T; i++)
		{
			R = 0;
			file_in >> R;
			if (R > 0)
			{
				K = 0;
				file_in >> K;
				if (K > 0)
				{
					N = 0;
					file_in >> N;
					if (N > 0)
					{
						LineQueue.clear();
						for (int j = 1; j <= N; j++)
						{
							G = 0;
							file_in >> G;
							if (G > 0)
							{
								LineQueue.push_back(G);
							}
							else
							{
								cout << "Invalid G in test case " << i << " index " << j << endl;
							}
						}

						P = 0;

						for (r = 0; r < R; r++)
						{
							k = 0;
							TempQueue.clear();
							for (auto lqIter = LineQueue.begin(); lqIter != LineQueue.end(); lqIter++)
							{
								if ((k + *lqIter <= K))
								{
									k += *lqIter;
								}
								else
								{
									TempQueue.assign(LineQueue.begin(), lqIter);
									LineQueue.erase(LineQueue.begin(), lqIter);
									LineQueue.insert(LineQueue.end(), TempQueue.begin(), TempQueue.end());
									break;
								}
							}
							P += k;
						}

						file_out << "Case #" << i << ": " << P << endl;
					}
					else
					{
						cout << "Invalid N in test case " << i << endl;
					}
				}
				else
				{
					cout << "Invalid K in test case " << i << endl;
				}
			}
			else
			{
				cout << "Invalid R in test case " << i << endl;
			}
		}
	}
	else
	{
		cout << "Invalid T" << endl;
	}

	file_in.close();
	file_out.close();
	cin >> T;
}
#include <vector>
#include <list>
#include <algorithm>
#include <cmath>
#include <functional>
#include <cstdlib>
#include <iostream>
#include <string>

using namespace std;

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int cases, N, M, count;
	scanf("%d", &cases);

	list<string> paths;
	list<string>::iterator iter;
	string path;
	bool exist;

	for (int i = 1; i <= cases; i++)
	{
		scanf("%d %d", &N, &M);
		count = 0;
		paths.clear();

		for (int n = 0; n < N; n++)
		{
			cin >> path;
			paths.push_back(path);
		}

		for (int m = 0; m < M; m++)
		{
			cin >> path;

			while (strcmp(path.c_str(), "") != 0)
			{
				exist = false;
				for (iter = paths.begin(); iter != paths.end(); iter++)
				{
					if (strcmp(((string)*iter).c_str(), path.c_str()) == 0)
					{
						exist = true;
						break;
					}
				}

				if (!exist)
				{
					paths.push_back(path);
					count++;
				}

				path.erase(path.begin() + path.find_last_of("/"), path.end());
			}
		}

		cout << "Case #" << i << ": " << count << endl;
	}

	return 0;
}
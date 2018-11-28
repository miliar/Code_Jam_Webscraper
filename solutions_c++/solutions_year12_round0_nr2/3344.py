#include <iostream>

using namespace std;

int main()
{
	int t, i, n, s, p, j, num;
	int data[110][3];

	cin >> t;
	for(i = 1; i <= t; i++)
	{
		cin >> n >> s >> p;
		num = 0;
		for(j = 0; j < n; j++)
		{
			cin >> data[j][0];
			if(data[j][0] % 3 == 0)
			{
				data[j][1] = data[j][0] / 3;
				data[j][2] = data[j][0] / 3 + 1;
			}else if(data[j][0] % 3 == 1)
			{
				data[j][1] = (data[j][0] - 1) / 3 + 1;
				data[j][2] = (data[j][0] - 1) / 3 + 1;
			}else
			{
				data[j][1] = (data[j][0] + 1) / 3;
				data[j][2] = (data[j][0] + 1) / 3 + 1;
			}

			if(data[j][1] >= p)num ++;
			else if(data[j][2] >= p && data[j][2] >= 2 && s > 0)
			{
				s--;
				num++;
			}
		}
		cout << "Case #" << i << ": " << num << endl;
	}
	return 0;
}

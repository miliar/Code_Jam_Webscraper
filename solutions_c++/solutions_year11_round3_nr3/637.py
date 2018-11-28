#include <iostream>
#include <fstream>


using namespace std;

int cas, index=1;
ifstream fin("C-small-attempt0.in");
ofstream fout("C-small-attempt0.out");

int n, l, h;
const int SIZE = 100;
int arr[SIZE];

void read()
{
	fin >> n >> l >> h;

	for (int i=0; i < n; i ++)
	{
		fin >> arr[i];
	}
}

int cal()
{
	bool flag = false;
	for (int i=l; i <= h; i ++)
	{
		bool flag = true;	
		for (int j=0; j < n; j ++)
		{
			if (i > arr[j] && i % arr[j] == 0)
			{
				continue;
			}
			if (i <= arr[j] && arr[j] % i == 0)
			{
				continue;
			}
			flag = false;
			break;
		}
		if (flag)
		{
			return i;
		}
	}

	return -1;
};

int main()
{
	fin >> cas;

	while (index <= cas)
	{
		read();
		int result = cal();

		if (result == -1)
		{
			fout <<"Case #"<<index<<": NO" << endl;
		}
		else
		{
			fout << "Case #"<<index <<": "<<result << endl;
		}

		index ++;
	}

	return 0;
}

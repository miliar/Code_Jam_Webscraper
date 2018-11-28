#include<iostream>
#include<string>
#include<map>
using namespace std;

int arr[1000][1000];
int conn[1000][1000];
int M, N;

void prepare()
{
	for(int i = 0; i < N; i++)
	{
		int r1 = 0, r2;
		while(r1 < M)
		{
			if (arr[r1][i] == 2)
			{
				conn[r1][i] = 0;
				r1++;
			}
			else
			{
				r2 = r1 + 1;
				while(arr[r2][i] != 2 && arr[r2][i] != arr[r2 - 1][i]) r2++;
				while(r1 < r2)
				{
					conn[r1][i] = r2 - r1;
					r1++;
				}
			}
		}
	}
}

int cut(int size, bool remove = true)
{
	int ans = 0;
	for(int i = 0; i < M - size + 1; i++)
	{
		int j = 0;
		int row = i, col;
		while(j < N - size + 1)
		{
			col = j; 
			if(conn[i][j] < size)
			{
				j++;
				continue;
			}

			j++;
			int fnd = 1;
			while(conn[i][j] >= size && arr[i][j] != arr[i][j-1] && fnd < size && j < N)
			{
				j++;
				fnd++;
			}
			if(fnd >= size)
			{
				if (!remove)
				{
					return 1;
				}
				for(int ii = row; ii < row + size; ii++)
				{
					for(int jj = col; jj < col + size; jj++)
					{
						arr[ii][jj] = 2;
						conn[ii][jj] = 0;
					}
				}
				ans++;
			}
		}
	}
	return ans;
}

int main()
{
	int CAS;
	cin >> CAS;
	for(int cas=1; cas <= CAS; cas++)
	{
		cin >> M >>N;
		for(int i = 0; i < M; i++)
		{
			string str;
			cin>> str;
			for(int j = 0; j < str.size(); j++)
			{
				int val;
				if(str[j] >= '0' && str[j] <= '9')
					val = str[j] - '0';
				else
					val = toupper(str[j]) - 'A' + 10;
				for(int k = 0; k < 4; k++)
				{
					arr[i][j * 4 + 3 - k] = val % 2;
					val /= 2;
				}
			}
		}

		pair<int, int> ans[1000];
		int found = 0;
		int size = (M < N? M : N) + 1;

		do {
			prepare();
			int lb = 1, ub = size;
			do {
				size = (lb + ub) / 2;
				if (cut(size, false))
					lb = size;
				else
					ub = size;
			} while (ub - lb > 1);
			size = lb;
			if (size < ub)
				ans[found++] = make_pair(size, cut(size));
		} while(size > 1);
		
		cout << "Case #" << cas << ": " << found << endl;
		for(int i =0; i < found; i++)
			cout << ans[i].first << " " << ans[i].second << endl;
	}
	return 0;

}

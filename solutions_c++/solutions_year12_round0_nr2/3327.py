#include <iostream>
#include <vector>
using namespace std;

//#define MYDEBUG

int N, S, P;
vector<int> points;

int matrix[102][102];

int bestSurprising(int sum)
{
	if (sum-4>=0 && (sum-4)%3 == 0)
		return (sum-4)/3 + 2;
	if (sum-3>=0 && (sum-3)%3 == 0)
		return (sum-3)/3 + 2;
	if (sum-2>=0 && (sum-2)%3 == 0)
		return (sum-2)/3 + 2;
	return -1;
}

int bestUnsurprising(int sum)
{
	if (sum-2>=0 && (sum-2)%3 == 0)
		return (sum-2)/3 + 1;
	if (sum-1>=0 && (sum-1)%3 == 0)
		return (sum-1)/3 + 1;
	if (sum%3 == 0)
		return sum/3;
	return -1;
	
}

void set(int& lf, int rt)
{
	lf = max(lf,rt);
}
int calc()
{
	matrix[0][0] = 0;
	for(int x = 1; x<= N; x++)
	{
		matrix[x][0] = 0;
		int res = points[x];
		int bS = bestSurprising(res);
		int bU = bestUnsurprising(res);
#ifdef MYDEBUG

		cout << "Sum = " << res << ", bS = "<< bS << ", bU = " << bU << endl;
#endif
		
		for(int y=0; y<=S && y<=x; y++)
		{
			if (bS != -1 && bS >= P )
			{
				if (y-1 >= 0 && matrix[x-1][y-1] != -1) {
					set(matrix[x][y], matrix[x-1][y-1]+1);
#ifdef MYDEBUG

								cout << "Setting matrix[" << x << "][" << y << "] = "
									<< matrix[x][y] << endl;
#endif
				}
			} else if(bS != -1)
			{
				if (y-1>= 0 && matrix[x-1][y-1] != -1) {
					set (matrix[x][y], matrix[x-1][y-1]);
				}
			} else
				set(matrix[x][y],matrix[x-1][y]);
			if (bU != -1 and bU >= P)
			{
				if (matrix[x-1][y] != -1) {
					set(matrix[x][y], matrix[x-1][y]+1);
#ifdef MYDEBUG
					cout << "Setting matrix[" << x << "][" << y << "] = "
					<< matrix[x][y] << endl;
#endif
				}
			} else
				set(matrix[x][y], matrix[x-1][y]);
		}
	}
#ifdef MYDEBUG
	for(int j=0; j<=S; j++) {
		for(int i=0; i<=N; i++)
				cout << matrix[i][j] << " ";
	cout << endl;
	}
#endif
	return max(matrix[N][S],0);
}

int process()
{
	points.clear();
	memset(matrix, -1, sizeof(matrix));
	
	cin >> N >> S >> P;
	points.push_back(0);
	for(int i=0; i<N;i++)
	{
		int tmp;
		cin >> tmp;
		points.push_back(tmp);
	}
	
	return calc();
}
int main (int argc, char * const argv[]) {
    int T;
	cin >> T;
	for(int i=0; i<T;i++)
	{
		int res = process();
		cout << "Case #" << i+1 << ": " << res << endl;
	}
	return 0;
}

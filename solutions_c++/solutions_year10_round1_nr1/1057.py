#include <iostream>
#include <vector>
#include <string>
using namespace std;
#define ONLINE

vector<string> Map, T;
int N, K;
int B, R;

void Rotate_Fall(vector<string>& M, vector<string>& T)
{
	string Blank = "";
	T.clear();
	for(int i = 0; i < M.size(); i++) Blank += ".";
	for(int i = 0; i < M.size(); i++) T.push_back(Blank);

	for(int i = 0; i < M.size(); i++)
	{
		for(int j = 0; j < M.size(); j++)
		{
			T[j][M.size() - 1 - i] = M[i][j];
		}
	}

	//for(int i = 0; i < T.size(); i++) cout << T[i] << endl;

	for(int i = 0; i < T.size(); i++)
	{
		for(int j = T.size() - 1; j >= 0; j--)
		{
			if(T[j][i] == '.')
			{
				for(int k = j - 1; k >= 0; k--)
				{
					if(T[k][i] != '.') 
					{
						T[j][i] = T[k][i];
						T[k][i] = '.';
						break;
					}
					
				}
			}
		}
	}
}

void ProcessDiagnal(int Sx, int Sy, int Ix, int Iy, int K, vector<string>& T)
{
	int cnt = K;
	int count = 0;
	int x = Sx, y = Sy;
	while(cnt > 0)
	{
		if(x < 0 || y < 0 || x >= T.size() || y >= T.size()) break;
		if(T[x][y] == 'B') count++;
		if(T[x][y] == 'R') count--;
		x += Ix, y += Iy;
		cnt--;
	}
	if(count == K) {B = 1; return;}
	if(count == -K) {R = 1; return;}

	while(true)
	{
		if(x < 0 || y < 0 || x >= T.size() || y >= T.size()) break;
		if(T[x][y] == 'B') count++;
		if(T[x - Ix * K][y - Iy * K] == 'B')count--;

		if(T[x][y] == 'R') count--;
		if(T[x - Ix * K][y - Iy * K] == 'R') count++;

		if(count == K) {B = 1; return;}
		if(count == -K) {R = 1; return;}
		x += Ix;
		y += Iy;
	}
}
void Count(vector<string>& T, int K)
{
	B = 0, R = 0;

	for(int i = 0; i < T.size(); i++)
	{
		ProcessDiagnal(i, 0, 0, 1, K, T);
	}

	for(int i = 0; i < T.size(); i++)
	{
		ProcessDiagnal(0, i, 1, 0, K, T);
	}
	for(int i = K - 1; i < T.size(); i++)
	{
		ProcessDiagnal(0, i, 1, -1, K, T);
	}

	for(int i = T.size() - K; i >= 0; i--)
	{
		ProcessDiagnal(0, i, 1, 1, K, T);
	}

	for(int i = T.size() - K; i >= 0; i--)
	{
		ProcessDiagnal(i, 0, 1, 1, K, T);
	}

	for(int i = T.size() - K; i >= 0; i--)
	{
		ProcessDiagnal(i, T.size() - 1, 1, -1, K, T);
	}
}
int main()
{
#ifdef ONLINE
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif

	int iCaseTimes;
	cin >> iCaseTimes;

	for(int kk = 0; kk < iCaseTimes; kk++)
	{
		cin >> N >> K;
		Map.clear();
		for(int i = 0; i < N; i++)
		{
			string Line;
			cin >> Line;
			Map.push_back(Line);
		}

		T.clear();
		Rotate_Fall(Map, T);
		//cout << endl;
		//for(int i = 0; i < T.size(); i++) cout << T[i] << endl;
		Count(T, K);

		printf("Case #%d: ", kk + 1);
		if(R == 1 && B == 1) printf("Both\n");
		else if(R == 1) printf("Red\n");
		else if(B == 1) printf("Blue\n");
		else printf("Neither\n");
	}
	return 0;
}
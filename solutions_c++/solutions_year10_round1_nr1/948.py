#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>

using namespace std;
const int MAXN = 60;
int arr[MAXN][MAXN];

int main()
{
	//const char* iFileName = "A-small-attempt1.in";
	const char* iFileName = "A-large.in";
	const char* oFileName = "out.txt";

	ifstream iFile(iFileName);
	ofstream oFile(oFileName);
	int Cases;
	iFile >> Cases;
	for(int caseNum=1; caseNum<=Cases; ++caseNum)
	{
		memset(arr, 0, sizeof(arr));
		int n, k;
		iFile >> n >> k;
		int maxR = -1;
		for(int i=0; i<n; ++i)
		{
			string tmp;
			if(i==0)
				getline(iFile, tmp); //eat;
			getline(iFile, tmp);
			for(int p=0; p<tmp.size(); ++p)
			{
				if(tmp[p] == '.')
					arr[i][p] = 0;
				else if(tmp[p] == 'R')
				{
					arr[i][p] = 1;
					if(p > maxR)
						maxR = p;
				}
				else // 'B'
				{
					arr[i][p] = 2;
					if(p > maxR)
						maxR = p;
				}
			}
		}

		for(int i=0; i<n; ++i)
		{
			int pos = maxR;
			while(arr[i][pos] != 0)
				--pos;
			while(pos>=0 && arr[i][pos] == 0)
				--pos;
			for(int j=maxR; j>=0&&pos>=0; --j)
			{
				if(arr[i][j] != 0)
					continue;
				arr[i][j] = arr[i][pos];
				arr[i][pos] = 0;
				while(pos>=0 && arr[i][pos] == 0)
					--pos;
			}
		}

		int win[3] = {0, 0, 0}; // dummy, red, blue
		for(int i=0; i<n; ++i)
		{
			for(int j=0; j<n; ++j)
			{
				int item = arr[i][j];
				if(item == 0 || win[item] == 1)
					continue;
				int cnt = 1;
				//right
				for(int y=j+1; y<n; ++y)
				{
					if(arr[i][y] != item)
						break;
					++cnt;
					if(cnt >= k)
					{
						win[item] = 1;
						break;
					}
				}

				if(win[item] == 1)
					continue;
				cnt = 1;
				//down
				for(int x=i+1; x<n; ++x)
				{
					if(arr[x][j] != item)
						break;
					++cnt;
					if(cnt >= k)
					{
						win[item] = 1;
						break;
					}
				}

				if(win[item] == 1)
					continue;
				cnt = 1;
				//down-right
				for(int x=i+1,y=j+1; x<n&&y<n; ++x,++y)
				{
					if(arr[x][y] != item)
						break;
					++cnt;
					if(cnt >= k)
					{
						win[item] = 1;
						break;
					}
				}

				if(win[item] == 1)
					continue;
				cnt = 1;
				//left-down
				for(int x=i+1,y=j-1; x<n&&y<n; ++x,--y)
				{
					if(arr[x][y] != item)
						break;
					++cnt;
					if(cnt >= k)
					{
						win[item] = 1;
						break;
					}
				}
			}
		}

		string ans;
		if(win[1] == 1 && win[2] == 1)
			ans = "Both";
		else if(win[1] == 0 && win[2] == 0)
			ans = "Neither";
		else if(win[1] == 1)
			ans = "Red";
		else
			ans = "Blue";
		oFile << "Case #" << caseNum << ": ";
		oFile << ans << endl;
	}
	return 0;
}
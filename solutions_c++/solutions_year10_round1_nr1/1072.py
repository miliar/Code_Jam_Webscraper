#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;

typedef signed int int32;
typedef unsigned int uint32;
typedef signed __int64 int64;
typedef unsigned __int64 uint64;

void Tokenize(const string& str,
			  vector<string>& tokens,
			  const string& delimiters = " ")
{
	// 맨 첫 글자가 구분자인 경우 무시
	string::size_type lastPos = str.find_first_not_of(delimiters, 0);
	// 구분자가 아닌 첫 글자를 찾는다
	string::size_type pos     = str.find_first_of(delimiters, lastPos);

	while (string::npos != pos || string::npos != lastPos)
	{
		// token을 찾았으니 vector에 추가한다
		tokens.push_back(str.substr(lastPos, pos - lastPos));
		// 구분자를 뛰어넘는다.  "not_of"에 주의하라
		lastPos = str.find_first_not_of(delimiters, pos);
		// 다음 구분자가 아닌 글자를 찾는다
		pos = str.find_first_of(delimiters, lastPos);
	}
}

template <typename NodeName>
void ClearVec(vector<NodeName*>& nList)
{
	vector<NodeName*>::iterator iter = nList.begin();
	while(iter != nList.end())
	{
		delete *iter;
		++iter;
	}
	nList.clear();
}

char table[64][64];

void rotate(int N)
{
	char temp[64];

	for (int i=0; i<N; ++i)
	{
		int index = N-1;
		memset(temp, '.', sizeof(temp));
		for (int j=N-1; j>=0; --j)
		{
			if (table[i][j] != '.')
			{
				temp[index] = table[i][j];
				--index;
			}
		}

		memcpy(table[i], temp, sizeof(temp));
	}
}

bool find1(char piece, int N, int K)
{
	char temp[64];

	for (int i=0; i<N; ++i)
	{
		for (int j=0; j<N; ++j)
		{
			if (table[i][j] == piece)
			{
				int count = 0;
				for (;j<N; ++j)
				{
					if (table[i][j] == piece)
					{
						++count;
					}
					else
					{
						break;
					}
				}
				if (count >= K)
				{
					return true;
				}
			}
		}
	}
	return false;
}

bool find2(char piece, int N, int K)
{
	char temp[64];

	for (int i=0; i<N; ++i)
	{
		for (int j=0; j<N; ++j)
		{
			if (table[j][i] == piece)
			{
				int count = 0;
				for (;j<N; ++j)
				{
					if (table[j][i] == piece)
					{
						++count;
					}
					else
					{
						break;
					}
				}
				if (count >= K)
				{
					return true;
				}
			}
		}
	}
	return false;
}

bool find3(char piece, int N, int K)
{
	char temp[64];

	for (int i=0; i<N; ++i)
	{
		for (int j=0; j<N; ++j)
		{
			if (i+j >= N)
				break;
			//printf("(%d, %d)\n", i+j, j);

			if (table[i+j][j] == piece)
			{
				int count = 0;
				for (;j<N; ++j)
				{
					if (i+j >= N)
						break;

					if (table[i+j][j] == piece)
					{
						++count;
					}
					else
					{
						break;
					}
				}
				if (count >= K)
				{
					return true;
				}
			}
		}
	}

	for (int i=0; i<N; ++i)
	{
		for (int j=0; j<N; ++j)
		{
			if (i+j >= N)
				break;
			//printf("(%d, %d)\n", j, j+i);

			if (table[j][i+j] == piece)
			{
				int count = 0;
				for (;j<N; ++j)
				{
					if (i+j >= N)
						break;

					if (table[j][i+j] == piece)
					{
						++count;
					}
					else
					{
						break;
					}
				}
				if (count >= K)
				{
					return true;
				}
			}
		}
	}

	return false;
}

bool find4(char piece, int N, int K)
{

	char temp[64];

	for (int i=0; i<N; ++i)	// row
	{
		for (int j=0; j<N; ++j)	// col
		{
			if (i-j < 0)
				break;

			//printf("(%d, %d)\n", i-j, j);

			if (table[i-j][j] == piece)
			{
				int count = 0;
				for (;j<N; ++j)
				{
					if (i-j < 0)
						break;

					if (table[i-j][j] == piece)
					{
						++count;
					}
					else
					{
						break;
					}
				}
				if (count >= K)
				{
					return true;
				}
			}
		}
	}

	for (int i=0; i<N; ++i) // col
	{
		for (int j=N-1; j>=0; --j)	// row
		{
			if ((N-1)-j+i >= N)
				break;

			//printf("(%d, %d)\n", j, (N-1)-j+i);

			if (table[j][(N-1)-j+i] == piece)
			{
				int count = 0;
				for (; j>=0; --j)	// row
				{
					if ((N-1)-j+i >= N)
						break;

					if (table[j][(N-1)-j+i] == piece)
					{
						++count;
					}
					else
					{
						break;
					}
				}
				if (count >= K)
				{
					return true;
				}
			}
		}
	}

	return false;
}

bool find(char piece, int N, int K)
{
	if (find1(piece, N, K))
	{
		return true;
	}
	if (find2(piece, N, K))
	{
		return true;
	}
	if (find3(piece, N, K))
	{
		return true;
	}
	if (find4(piece, N, K))
	{
		return true;
	}
	return false;
}

int main()
{
	//freopen("A-small-attempt0.in","r",stdin);
	//freopen("A-small-attempt0.out","w",stdout);
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int start = time(NULL);

	int testCase = 0;
	scanf("%d",&testCase);
	for (int testId=1; testId <= testCase; ++testId)
	{
		int N, K;
		scanf("%d %d", &N, &K);

		memset(table, 0, sizeof(table));

		for (int i=0; i<N; ++i)
		{
			scanf("%s", table[i]);
		}

		rotate(N);

		bool isRed = find('R', N, K);
		bool isBlue = find('B', N, K);

		//uint64 result = 0;
		//double fResult = 0;

		char* sResult = "Neither";
		if (isBlue && isRed)
		{
			sResult = "Both";
		}
		else if (isRed)
		{
			sResult = "Red";
		}
		else if (isBlue)
		{
			sResult = "Blue";
		}

		printf("Case #%d: %s\n", testId, sResult);
		//printf("Case #%d: %I64u\n", testId, result);
		//printf("Case #%d: %f\n", testId, fResult);		

	}

	//printf("Time : %d\n", time(NULL) - start);
	return 0;
}


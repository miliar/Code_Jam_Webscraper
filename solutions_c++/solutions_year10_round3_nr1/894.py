#define _CRT_SECURE_NO_WARNINGS
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

int N;
int a[1000];
int b[1000];

bool isConnected(int i, int j)
{
	if ((a[i] - a[j]) * (b[i] - b[j]) > 0)
	{
		return false;
	}
	else
		return true;
}

int Solve()
{
	int count = 0;
	for (int i=0; i<N; ++i)
	{
		for (int j=i; j<N; ++j)
		{
			if (i == j)
			{
				continue;
			}
			if (isConnected(i, j))
			{
				++count;
			}
		}
	}
	return count;
}

int main()
{
	//freopen("A-small-practice.in","r",stdin);
	//freopen("A-small-practice.out","w",stdout);
	//freopen("A-small-attempt0.in","r",stdin);
	//freopen("A-small-attempt0.out","w",stdout);
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	time_t start = time(NULL);

	int testCase = 0;
	scanf("%d",&testCase);
	for (int testId=1; testId <= testCase; ++testId)
	{
		scanf("%d", &N);
		for (int i=0; i<N; ++i)
		{
			scanf("%d %d", &a[i], &b[i]);
		}

		uint64 result = Solve();
		double fResult = 0;

		printf("Case #%d: %I64u\n", testId, result);
		//printf("Case #%d: %f\n", testId, fResult);		

	}

	//printf("Time : %d\n", time(NULL) - start);
	return 0;
}


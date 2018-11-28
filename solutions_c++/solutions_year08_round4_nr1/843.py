
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>

using namespace std;

const int MAX = 2*10000 + 128;

int M;
int value[MAX];
int isOr[MAX];
int isLeaf[MAX];
int changeable[MAX];

inline int Apply(int op, int left, int right)
{
	if (op)
		return (left || right);

	return (left && right);
}

inline int GetLeft(int node)
{
	return (node * 2);
}

inline int GetRight(int node)
{
	return (node * 2) + 1;
}

int CalcValue(int node)
{
	if (isLeaf[node])
		return value[node];

	value[node] = Apply(isOr[node], CalcValue(GetLeft(node)), CalcValue(GetRight(node)));
}

int ChangesNeed(int node, int toValue)
{
	if (value[node] == toValue)
		return 0;

	if (isLeaf[node] && value[node] != toValue)
		return -1;

	int oldLeft = value[GetLeft(node)];
	int oldRight = value[GetRight(node)];
	int oldOp = isOr[node];

	int changesLeft = ChangesNeed(GetLeft(node), !oldLeft);
	int changesRight = ChangesNeed(GetRight(node), !oldRight);

	int newLeft = (changesLeft < 0)? oldLeft : !oldLeft;
	int newRight = (changesRight < 0)? oldRight : !oldRight;
	int newOp = !isOr[node];

	if (changeable[node] && Apply(newOp, oldLeft, oldRight) == toValue)
		return 1;

	int changesMin = -1;
	
	if (changesLeft > 0 && (changesLeft < changesRight || changesMin < 0))
	{
		if (Apply(oldOp, newLeft, oldRight) == toValue)
			changesMin = changesLeft;

		if (changeable[node] &&  Apply(newOp, newLeft, oldRight) == toValue)
			changesMin = changesLeft + 1;
	}

	if (changesRight > 0 && (changesRight < changesLeft || changesMin < 0))
	{
		if (Apply(oldOp, oldLeft, newRight) == toValue)
			changesMin = changesRight;

		if (changeable[node] &&  Apply(newOp, oldLeft, newRight) == toValue)
			changesMin = changesRight + 1;
	}

	if (changesMin >= 0)
		return changesMin;

	if (changesLeft > 0 && changesRight > 0)
	{
		if (Apply(oldOp, newLeft, newRight) == toValue)
			return changesLeft + changesRight;

		if (changeable[node] &&  Apply(newOp, newLeft, newRight) == toValue)
			return changesLeft + changesRight + 1;
	}

	return -1;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int caseCount;
	cin >> caseCount;
	for (int caseNum=1; caseNum<=caseCount; caseNum++)
	{
		int v;
		cin >> M >> v;

		memset(isOr, 0, sizeof isOr);
		memset(changeable, 0, sizeof changeable);
		memset(value, 0, sizeof value);
		memset(isLeaf, 0, sizeof isLeaf);

		for (int i=0; i<(M-1)/2; i++)
		{
			int isAnd;
			cin >> isAnd >> changeable[1+i];
			isOr[1+i] = !isAnd;
		}

		for (int i=0; i<(M+1)/2; i++)
		{
			int curVal, node;
			cin >> curVal;
			node = 1 + i + (M-1)/2;
			value[node] = curVal;
			isLeaf[node] = 1;
		}

		CalcValue(1);

		int res = 0;
		
		if (value[1] != v)
			res = ChangesNeed(1, v);

		cout << "Case #" << caseNum << ": ";

		if (res < 0)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << res << endl;
	}

	return 0;
}



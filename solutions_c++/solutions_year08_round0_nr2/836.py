
#include <iostream>
#include <queue>
#include <functional>
#include <string>
#include <cstdio>

using namespace std;

typedef pair<int,int> PII;

int gettime(const string& s)
{
	int h, m;
	sscanf(s.c_str(), "%d:%d", &h, &m);
	return 60*h + m;
}

int main()
{
	int n;
	cin >> n;
	for (int kase=1; kase<=n; kase++)
	{
		int turn, na, nb;
		string dep, arr;
		cin >> turn >> na >> nb;
		priority_queue<PII, vector<PII>, greater<PII> > depA, depB;
		priority_queue<int, vector<int>, greater<int> > arrA, arrB;
		for (int i=0; i<na; i++)
		{
			cin >> dep >> arr;
			depA.push(PII(gettime(dep), gettime(arr)+turn));
		}
		for (int i=0; i<nb; i++)
		{
			cin >> dep >> arr;
			depB.push(PII(gettime(dep), gettime(arr)+turn));
		}
		int solA = 0, solB = 0;
		int numA = 0, numB = 0;
		for (int t=0; t<24*60; t++)
		{
			while (!arrA.empty() && arrA.top() == t)
			{
				numA++;
				arrA.pop();
			}
			while (!arrB.empty() && arrB.top() == t)
			{
				numB++;
				arrB.pop();
			}
			while (!depA.empty() && depA.top().first == t)
			{
				PII p = depA.top();
				depA.pop();
				arrB.push(p.second);
				if (numA > 0)
					numA--;
				else
					solA++;
			}
			while (!depB.empty() && depB.top().first == t)
			{
				PII p = depB.top();
				depB.pop();
				arrA.push(p.second);
				if (numB > 0)
					numB--;
				else
					solB++;
			}
		}
		cout << "Case #" << kase << ": " << solA << " " << solB << endl;
	}
	return 0;
}

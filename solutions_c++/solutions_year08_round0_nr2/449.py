#include <iostream>
#include <list>

using namespace std;

int main()
{
	string line;
	list<int> departureA, arrivalB, departureB, arrivalA;
	int a, numCases, turnaround, numAtoB, numBtoA;
	int h1, m1, h2, m2;
	list<int>::iterator p, q;
	
	cin >> numCases;
	for (int curCase = 1; curCase <= numCases; curCase++)
	{
		cin >> turnaround;
		cin >> numAtoB;
		cin >> numBtoA;
		getline(cin, line);
		for (a = 0; a < numAtoB; a++)
		{
			scanf("%d:%d %d:%d\n", &h1, &m1, &h2, &m2);
			departureA.push_back(60 * h1 + m1);
			arrivalB.push_back(60 * h2 + m2 + turnaround);
		}
		for (a = 0; a < numBtoA; a++)
		{
			scanf("%d:%d %d:%d\n", &h1, &m1, &h2, &m2);
			departureB.push_back(60 * h1 + m1);
			arrivalA.push_back(60 * h2 + m2 + turnaround);
		}
		departureA.sort();
		arrivalB.sort();
		departureB.sort();
		arrivalA.sort();
		
		p = departureA.begin();
		q = arrivalA.begin();
		while (p != departureA.end() && q != arrivalA.end())
		{
			while (p != departureA.end() && *q > *p)
			{
				++p;
			}
			if (p != departureA.end())
			{
				p = departureA.erase(p);
				q = arrivalA.erase(q);
			}
		}
		p = departureB.begin();
		q = arrivalB.begin();
		while (p != departureB.end() && q != arrivalB.end())
		{
			while (p != departureB.end() && *q > *p)
			{
				++p;
			}
			if (p != departureB.end())
			{
				p = departureB.erase(p);
				q = arrivalB.erase(q);
			}
		}
		cout << "Case #" << curCase << ": " << departureA.size() << " " << departureB.size() << endl;
		departureA.clear();
		arrivalB.clear();
		departureB.clear();
		arrivalA.clear();
	}
	return 0;
}

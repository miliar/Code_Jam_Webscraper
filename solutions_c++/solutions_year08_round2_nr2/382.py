#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
#include <set>

using namespace std;

/*
 nput

One line containing an integer C, the number of test cases in the input file.

For each test case, there will be one line containing three single-space-separated
integers A, B, and P. A and B are the first and last integers in the interval, and
P is the number as described above.
 */

vector <bool> IsPrime;


vector <int> Parent;	// Parents. Each element is initialized to self
int GetParent(int Node)
{
	if (Parent[Node] == Node)
		return Node;
	return Parent[Node] = GetParent(Parent[Node]);
}


int Num(unsigned long long A, unsigned long long B, unsigned long long P)
{
	Parent.clear();
	Parent.resize(B+10);

	for (int i=A; i <= B; ++i)
	{
		Parent[i] = i;
	}

	int Count = 0;
	for (int i=A; i <= B; ++i)
	{
		for (int j=A; j <= B; ++j)
		{
			if (i == j)
				continue;
			if (GetParent(i) != GetParent(j))
			{
				for (int Prime = P; Prime <= min(i, j); ++Prime)
				{
					if (IsPrime[Prime])
					{
						if (i % Prime == 0 && (j%Prime == 0))
						{
						//	cout << i << " and " << j << " share " << Prime<<endl;
							// Group
							if (i < j)
							{
								Parent[GetParent(i)] = GetParent(j);
							}
							else
							{
								Parent[GetParent(j)] = GetParent(i);
							}
							//Count++;
							break;
						}
					}
				}
			}
		}
	}

	set <int> DistinctParents;	// To find out if it was possible to connect the whole graph
	 for (int i=A; i <= B; ++i)
	 		DistinctParents.insert(GetParent(i));

	return DistinctParents.size();
}
/*
Eratosthenes(n) {
  a[1] := 0
  for i := 2 to n do a[i] := 1
  p := 2
  while p2  <  n do {
    j := p2
    while (j  <  n) do {
      a[j] := 0
      j := j+p
    }
    repeat p := p+1 until a[p] = 1
  }
  return(a)
}
*/
int main()
{
	int C;
	ifstream cin ("B.in");
	ofstream cout ("B.out");
	cin >> C;

	IsPrime.resize(2000, true);
	//IsPrime[1] = false;

	for (int i=2; i < IsPrime.size(); ++i)
	{
		for (int j=i*i; j < IsPrime.size(); j += i)
		{
			IsPrime[j] = false;
		}
	}

/*	for (int i=1; i < 100; i++ )
	{
		if (IsPrime[i])
		cout << i << endl;
	}
*/
	for (int iCase = 1; iCase <= C; ++iCase)
	{
		unsigned long long A, B, P;
		cin >> A >> B >> P;

		cout << "Case #"<<iCase<<": "<< Num(A, B, P)<<endl;
	}
	return 0;
}

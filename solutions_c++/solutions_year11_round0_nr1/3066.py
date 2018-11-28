#include <fstream>
#include <queue>
#include <string>

using namespace std;
ifstream cin("A.in");
ofstream cout("out.out");

struct pos
{
	int k,x;
};

pos CPos(int k, int x)
{
	pos a;
	a.k = k;
	a.x = x;
	return a;
}

int Calc(queue<pos> O, queue<pos> B)
{
	int t1 = 1, t2 = 1, t = 0;
	pos A,C;
	while(!O.empty() || !B.empty())
	{
		if(O.empty())
		{
			C = B.front(); B.pop();
			int r = abs(C.k - t2);
			t += r+1;
			t2 = C.k;
			continue;
		}
		if(B.empty())
		{
			A = O.front(); O.pop();
			int r = abs(A.k - t1);
			t += r+1;
			t1 = A.k;
			continue;
		}
		A = O.front(); C = B.front();
		if(A.x > C.x)
		{
			B.pop();
			int r = abs(C.k - t2), r1 = abs(A.k - t1);
			t += r+1;
			t2 = C.k;
			if(r+1 >= r1)t1 = A.k;else
			{
				if(A.k > t1)t1 += r+1;else
				if(A.k < t1)t1 -= r+1;
			}
		}else
		{
			O.pop();
			int r = abs(A.k - t1), r1 = abs(C.k - t2);
			t += r+1;
			t1 = A.k;
			if(r+1 >= r1)t2 = C.k;else
			{
				if(C.k > t2)t2 += r+1;else
				if(C.k < t2)t2 -= r+1;
			}
		}
	}
	return t;
}

int main()
{
	int n;
	cin >> n;
	for(int i=0;i<n;i++)
	{
		int m,k;
		queue<pos> O,B;
		string s;
		cin >> m;
		for(int j=0;j<m;j++)
		{
			cin >> s >> k;
			if(s=="O")O.push(CPos(k,j+1));else B.push(CPos(k,j+1));
		}
		cout << "Case #" << i+1 << ": " << Calc(O,B) << endl;
	}
	return 0;
}
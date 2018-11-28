#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <sstream>
#include <algorithm>
using namespace std;

struct Train
{
	int s, e;
	int dir;

	bool operator<(const Train& a) const
	{
		return s < a.s;
	}
};

int parse(string s)
{
	s[2] = ' ';
	stringstream s1(s);
	int a, b;
	s1 >> a >> b;
	return a*60 + b;
}

int main()
{

int N;
// this is fun!
fstream In("B-large.in", ios::in);
fstream Out("B-large.out", ios::out);

int i, j;

In >> N;

for(int h=1; h<=N; h++)
{
int T, NA, NB;

In >> T >> NA >> NB;

priority_queue<pair<int, Train> > q;

for(i=0; i<NA; i++)
{
	string a, b;
	In >> a >> b;
	Train t;
	t.s = parse(a);
	t.e = parse(b);
	t.dir = 0;
	q.push(make_pair(-1*t.s, t));

}


for(i=0; i<NB; i++)
{
	string a, b;
	In >> a >> b;
	Train t;
	t.s = parse(a);
	t.e = parse(b);
	t.dir = 1;
	q.push(make_pair(-1*t.s, t));

}

int a = 0, b = 0;

priority_queue<int> A, B;

while(!q.empty() )
{
	Train t;
	t = q.top().second;
	q.pop();

	if(t.dir==0)
	{
		if(A.empty() )
		{
			B.push(-1*(t.e+T) );
			a++;
		}
		else if(A.top()*-1 <= t.s)
		{
			A.pop();
			B.push(-1*(t.e+T) );
		}
		else
		{
			a++;
			B.push(-1*(t.e+T) );
		}
	}
	
	else
	{
		if(B.empty() )
		{
			A.push(-1*(t.e+T) );
			b++;
		}
		else if(B.top()*-1 <= t.s)
		{
			B.pop();
			A.push(-1*(t.e+T) );
		}
		else
		{
			b++;
			A.push(-1*(t.e+T) );
		}
	}

}

Out << "Case #" << h << ": " << a << " " << b << endl;

}

In.close();
Out.close();

return 0;

}
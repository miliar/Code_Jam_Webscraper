#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#include <cmath>
#include <bitset>
#include <cctype>
#include <complex>
using namespace std;

#define X		real()
#define Y		imag()

typedef complex<double> point, Vector;

const double dx[4] = {  0.0, + 1.0,   0.0, - 1.0};
const double dy[4] = {+ 1.0,   0.0, - 1.0,   0.0};
const point INF = point(150912385019358051398.1923851, 103275132905710575323.1359712359);

int L, ans;
bool a[220][220];
vector<point> v;

void Read()
{
int dir = 0;
point now(0, 0);
string s;
	
	cin >> L;
	
	ans = 0;
	v.clear();
	v.push_back(now);
	memset(a, false, sizeof(a));
//	cout << now << "\n";
	
	for(int i = 0, t; i < L; i ++)
	{
		cin >> s >> t;
		
		for(int iter = 1; iter <= t; iter ++)
		{
			for(int j = 0; j < s.size(); j ++)
			{
				switch(s[j])
				{
					case 'F':
						now.X += dx[dir];
						now.Y += dy[dir];
						break;
					
					case 'R':
						if(!(i + 1 == L && iter == t && j + 1 == s.size()))
						{
//							cout << now << "\n";
							v.push_back(now);
						}
						dir = (dir + 1) % 4;
						break;
					
					case 'L':
						if(!(i + 1 == L && iter == t && j + 1 == s.size()))
						{
//							cout << now << "\n";
							v.push_back(now);
						}
						dir = (4 + dir - 1) % 4;
						break;
				}
			}
		}
	}
	
	v.push_back(now);
	
//	system("pause");
}

double cross(const Vector &a, const Vector &b)
{
       return imag(conj(a) * b);
}

double area2(const point &a, const point &b, const point &c)
{
       return cross(b - a, c - a);
}

bool intersects_segments(const point &a, const point &b, const point &p, const point &q)
{
	if( area2(a, b, p) * area2(a, b, q) >= 0.0 ) return false;
	 
	if( area2(p, q, a) * area2(p, q, b) >= 0.0 ) return false;
	
	return true;
}

bool inside(const point & p)
{
int ret = 0;
	
	for(int i = 0, n = int(v.size()) - 1; i < n; i ++)
	{
		if(intersects_segments(v[i], v[i + 1], p, INF))
		{
			ret ++;
		}
	}
	
	return (ret & 1);
}

void Solve()
{

	for(int i = 0; i < v.size(); i ++)
	{
		v[i] += point(105.0, 105.0);
//		cerr << v[i] << "  ";
	}
//	cerr << "\n";
//	system("pause");

	
	for(double i = 0.5; i < 210.0; i += 1.0)
	{
		for(double j = 0.5; j < 210.0; j += 1.0)
		{
			if(inside(point(i, j)))
			{
				a[int(i)][int(j)] = true;
			}
//			cout << a[int(i)][int(j)];
		}
//		cout << "\n";
	}
//	system("pause");
	
	for(int i = 0; i < 210; i ++)
	{
		for(int j = 0; j < 210; j ++)
		{
			if(a[i][j]) continue;
			
			bool up = false, left = false, down = false, right = false;
			
			for(int k = 0; k < 210; k ++)
			{
				if(a[k][j])
				{
					if(k < i) down = true;
					else up = true;
				}
				
				if(a[i][k])
				{
					if(k < j) left = true;
					else right = true;
				}
			}
			
			ans += bool((up && down) || (left && right));
		}
	}
}

void Write(const int test_case)
{
	printf("Case #%d: ", test_case);
	
	printf("%d\n", ans);
}

int main()
{
int TESTS;
	
	scanf("%d", & TESTS);
	
	for(int i = 1; i <= TESTS; i ++)
	{
		Read();
		
		Solve();
		
		Write(i);
	}
	
//	system("pause");
	
	return 0;
}

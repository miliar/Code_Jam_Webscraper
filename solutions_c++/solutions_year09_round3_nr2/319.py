/*#include <stdlib.h>
#include <stdio.h>
#include <algorithm>
int comp(const void *p, const void *q)
{
    return (*(int *)p - *(int *)q);
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, i, j, x, y, t, a, b, c;
	char ch[100];
	scanf("%d ", &T);
	for (i = 0; i < T; i++)
	{
		for (j = 0; scanf("%c", &ch[j]) != -1; j++)
		{
			if (ch[j] <'0' || ch[j] > '9')
				break;
		}
		for (t = -1, x = j-1; x > 0; x--)
		{
			for (y = x-1; y>= 0; y--)
			{
				if (ch[x] > ch[y])
				{	
					t = ch[x];
					break;
				}
			}
			if (t > 0)
				break;
		}
		if (t > 0)
		{
			while (y < x)
			{
				ch[x] = ch[x-1];
				x--;
			}
			ch[x] = t;
		}
		else
		{
			ch[j++] = '0';
			ch[j] = 0;
			std::sort(ch, ch+j);
		}
		ch[j] = 0;
		printf("Case #%d: %s\n", i, ch);
	}
	return 0;
}*/
/*
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

template <class A, class B> void convert(A& x, B& y) {stringstream s; s<<x; s>>y;}

int main() {
	ifstream cin("in.txt");
	//ifstream cin("A-small.in");
	//ifstream cin("A-large.in");
	ofstream cout("out.txt");
	int T, Case;
	int i, j, k;
	string s;
	for (cin>>T, Case=1; T; T--,Case++) {
		cin>>s;
		s = string(21-s.length(),'0') + s;
		next_permutation(s.begin(), s.end());
		cout<<"Case #"<<Case<<": ";
		for (i=0; i<s.size(); i++) {
			if (s[i]!='0') break;
		}
		for (; i<s.size(); i++) {
			cout<<s[i];
		}
		cout<<endl;
	}
}*/
/*#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

template <class A, class B> void convert(A& x, B& y) {stringstream s; s<<x; s>>y;}

int main() {
	ifstream cin("in.txt");
	//ifstream cin("A-small.in");
	//ifstream cin("A-large.in");
	ofstream cout("out.txt");
	int T, Case;
	int i, j, k, t, v[61];
	__int64 sum = 0, temp = 0;
	map<int, int> m;
	string s;
	for (cin>>T, Case=1; T; T--,Case++) {
		cin>>s;
		m.clear();
		m[s[0]] = 1;
		for (i = 0, k = j = 1; i < s.size(); i++)
		{
			if (m.find(s[i]) != m.end())
			{
				v[i] = m[s[i]];
			}
			else if (k == 1)
			{
				m[s[i]] = v[i] = 0;
				k++;
			}
			else
			{
				m[s[i]] = v[i] = ++j;
				k++;
			}
		}
		if (k == 1) k = 2;
		sum = 0, temp = 1;
		for (i = s.size()-1; i>=0; i--)
		{
			sum += v[i]*temp;
			temp *= k;
		}
		cout<<"Case #"<<Case<<": "<<sum<<endl;
	}
}*/

#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;


int main() {
	ifstream cin("in.txt");
	freopen("out.txt", "w", stdout);
	int N, T, Case;
	int i, j, k;
	int x, y, z, vx, vy, vz;
	__int64 sx, sy, sz, svx, svy, svz;

 	double dm, dt;
	for (cin>>T, Case=1; T; T--,Case++) 
	{
		sx = sy = sz = svx = svy = svz = 0;
		for (cin>>N, i = 0; i < N; i++)
		{
			cin>>x>>y>>z>>vx>>vy>>vz;
			sx += x, sy += y, sz += z, svx += vx, svy += vy, svz += vz;
		}
		__int64 ab = -2*(sx*svx+sy*svy+sz*svz);
		__int64 AB = 2*(svx*svx+svy*svy+svz*svz);

		if ((ab < 0) || (AB == 0))
		{
			dt=0;
			dm = sqrt(1.0*sx*sx+sy*sy+sz*sz)/N;
		}
		else 
		{
			dt = 1.0 * ab/AB;
			dm = (sx+svx*dt)*(sx+svx*dt)+(sy+svy*dt)*(sy+svy*dt)+(sz+svz*dt)*(sz+svz*dt);
			dm = sqrt(dm) / N;
		}
		printf("Case #%d: %.8lf %.8lf\n", Case, dm, dt);
	}
}


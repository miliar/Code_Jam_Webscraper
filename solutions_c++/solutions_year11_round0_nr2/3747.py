#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <stack>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;

#define _CRT_SECURE_NO_WARNINGS
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()
#define C2N(c) (c)-'A'

template<typename T, typename S> T cast(S s) {
	stringstream ss;
	ss << s;
	T res;
	ss >> res;
	return res;
}

template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline int Size(const T& c) { return (int)c.size(); }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }

const double pi = 2*acos(0.0);

int main() 
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int t;
	int nc, no, ne;
	char aux, elements[4], element, last = 0, penultimate = 0;
	char combinations[26][26];
	int elementfrequency[26];
	bool opposed[26][26];
	stack<char> elementlist;
	string result;

	scanf("%d", &t);
	For(test, 1, t) 
	{
		Fill(combinations, 0);
		Fill(opposed, 0);
		Fill(elementfrequency, 0);
		elementlist = stack<char>();
		last = 0;
		penultimate = 0;

		scanf("%d", &nc);
		For(i, 1, nc)
		{
			scanf("%c", &aux);
			scanf("%c", &elements[0]);
			scanf("%c", &elements[1]);
			scanf("%c", &elements[2]);
			combinations[C2N(elements[0])][C2N(elements[1])]=elements[2];
			combinations[C2N(elements[1])][C2N(elements[0])]=elements[2];
		}
		scanf("%d", &no);
		For(i, 1, no)
		{
			scanf("%c", &aux);
			scanf("%c", &elements[0]);
			scanf("%c", &elements[1]);
			opposed[C2N(elements[0])][C2N(elements[1])]=true;
			opposed[C2N(elements[1])][C2N(elements[0])]=true;
		}
		scanf("%d", &ne);
		scanf("%c", &aux);
		For(i, 1, ne)
		{
			scanf("%c", &element);
			penultimate = last;
			last = element;
			elementlist.push(element);
			elementfrequency[C2N(element)]++;
			if (last != 0 && penultimate != 0)
			{
				// Combinate
				if (combinations[C2N(last)][C2N(penultimate)] != 0)
				{
					elementlist.pop();
					elementlist.pop();
					elementfrequency[C2N(last)]--;
					elementfrequency[C2N(penultimate)]--;
					if (elementlist.empty())
						aux = 0;
					else
						aux = elementlist.top();
					elementlist.push(combinations[C2N(last)][C2N(penultimate)]);
					elementfrequency[elementlist.top()]++;
					penultimate = aux;
					last = elementlist.top();
				}
				else
				{
					// Opposed
					Rep (j, 26)
					{
						if ((opposed[C2N(last)][j]) && (elementfrequency[C2N(last)] > 0) && (elementfrequency[j] > 0))
						{
							Fill(elementfrequency, 0);
							elementlist = stack<char>();
							last = 0;
							penultimate = 0;
						}
					}
				}
			}
		}

		result = "";
		while (!elementlist.empty())
		{
			result.insert(0, 1, elementlist.top());
			elementlist.pop();
			result.insert(0, ", ");
		}
		result.erase(0, 2);
		

		printf("Case #%d: [%s]\n", test, result.c_str());
	}
	
	fclose (stdin);
	fclose (stdout);

	exit(0);
}

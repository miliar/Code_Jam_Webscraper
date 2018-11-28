#pragma warning(disable: 4786)

#include <map>
#include <set>
#include <stack>
#include <cmath>
#include <queue>
#include <vector>
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
#include <fstream>
#include <iomanip>

using namespace std;




typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;


#define For(i,n) for (int i(0); i<n; i++)
#define For2(i, s, n) for(int i(s); i<n; i++)
#define For_rev(i, n) for(int i(n-1); i>=0; i--)
#define For2_rev(i, s, n) for(int i(n-1); i>=s; i--)

#define MP(a, b) make_pair(a, b)
#define All(v) v.begin(), v.end()

#define MS(a,c) memset(&a, c, sizeof(a))


template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline int Size(const T& c) { return (int)c.size(); }
template<typename T> inline void SetMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void SetMax(T& a, T b) { if (b > a) a = b; }


template <typename T> T max(T obj1, T obj2) { return obj1 < obj2 ? obj2 : obj1;}
template <typename T> T min(T obj1, T obj2) { return obj1 > obj2 ? obj2 : obj1;}


const int buff_size = 1024;
char buf[buff_size];
char *token;

void printvec(vi& v, int size)
{
	For(j, size)
	{
		printf("%d ", v[j]);
	}
	printf("\n");
}

int main() 
{
	FILE* fi = freopen("in.txt", "rt", stdin);
	FILE* fo = freopen("out.txt", "wt", stdout);

	int cn;
	//scanf("%d", &cn);
	gets(buf);
	cn = atoi(buf);
	For2(case_no, 1, cn+1) 
	{
		gets(buf);
		int size = atoi(buf);
		vs sorted;

		vi v1;
		vi v2;

		gets(buf);
		token = strtok( buf, " ");
		while( token != NULL )
		{
			v1.push_back(atoi(token));
			token = strtok( NULL, " " );
		}

		gets(buf);
		token = strtok( buf, " ");
		while( token != NULL )
		{
			v2.push_back(atoi(token));
			token = strtok( NULL, " " );
		}

		//printvec(v1,size);
		//printvec(v2,size);

		sort(All(v1));
		sort(All(v2));
		reverse(All(v2));

		//printvec(v1,size);
		//printvec(v2,size);

		int tot=0;
		For(i, size)
		{
			tot += v1[i] * v2[i];
		}
		

		printf("Case #%d: %d\n", case_no, tot);
	}

	return 0;
}


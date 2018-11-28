#define _USE_MATH_DEFINES  
#define _CRT_SECURE_NO_DEPRECATE  
  
#include <algorithm>  
#include <bitset>  
#include <cassert>  
#include <cmath>  
#include <cstdio>  
#include <cstdlib>  
#include <cstring>   
#include <deque>  
#include <functional>  
#include <iomanip>  
#include <iostream>  
#include <list>  
#include <map>  
#include <numeric>  
#include <queue>  
#include <set>  
#include <sstream>  
#include <stack>  
#include <string>  
#include <utility>  
#include <vector>  
  
using namespace std;  
  
#pragma comment(linker, "/STACK:64000000")  
  
#define problem "Khaustov"  

typedef long long int64;  
typedef unsigned long long ull;
typedef unsigned char byte;  
typedef pair<int, int> pii;
typedef pair<char, int> pci;
typedef pair<int, pii> piii;
typedef pair<int, piii> piiii;
typedef pair<pii, pii> edge;
typedef pair<int64, int64> pii64;
typedef pair<int64, pii64> shit;
typedef pair<pii64, int> piii64;
typedef pair<double, int> pdi;
typedef pair<pdi, int> pdii;
typedef pair<int, string> pis;
typedef vector<int> vi;  
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<pii> vpii;  
typedef vector<vpii> vvpii;  
typedef vector<string> vs;  
typedef vector<vs> vvs;  
typedef list<int> li;   
  
#define y1 _dsfdsfkn
#define left _dsfdsf
#define right _dfjdsj
#define link _tsu_sux
#define prime 1103
#define eps 1e-6
#define inf 123456789
#define toMod 1000000007LL

int nt;
int n, m, l;
int p;
char s[1 << 10];
string a[1 << 6];
string b[1 << 6];
char c;

int main()
{  
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

	scanf("%d", &nt);

	for (int tn = 1; tn <= nt; ++tn)
	{
		cin >> n;
		for (int i = 0; i < n; ++i)
			cin >> a[i];
		
		cin >> m;
		for (int i = 0; i < m; ++i)
		{
			cin >> b[i];
			sort(b[i].begin(), b[i].end());
		}

		cin >> l;
		p = 0;
		for (int i = 0; i < l; ++i)
		{
			cin >> c;
			s[p++] = c;
			if (p == 1) continue;
			string tmp = "";
			tmp += s[p - 1];
			tmp += s[p - 2];
			sort(tmp.begin(), tmp.end());
			for (int j = 0; j < n; ++j)
			{
				string t = a[j].substr(0, 2);
				sort(t.begin(), t.end());
				if (tmp != t) continue;
				s[p - 2] = a[j][2];
				--p;
			}
			for (int i = 0; i < p; ++i)
				for (int j = i + 1; j < p; ++j)
				{
					string tmp = "";
					tmp += s[i];
					tmp += s[j];
					sort(tmp.begin(), tmp.end());
					for (int j = 0; j < m; ++j)
					{
						if (b[j] != tmp) continue;
						p = 0;
						break;
					}
				}
		}
		printf("Case #%d: [", tn);
		for (int i = 0; i < p; ++i)
		{
			if (i) printf(", ");
			printf("%c", s[i]);
		}
		printf("]\n");
	}

    return 0;  
}
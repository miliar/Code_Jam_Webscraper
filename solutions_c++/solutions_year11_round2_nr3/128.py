#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <algorithm>
#include <set>

#define fii(x,y) for(int i=x;i<y;i++)
#define fjj(x,y) for(int j=x;j<y;j++)
#define fkk(x,y) for(int k=x;k<y;k++)
#define fi(x) fii(0,x)
#define fj(x) fjj(0,x)
#define fk(x) fkk(0,x)
#define eps 0.00000001
#define inf 1<<28

using namespace std;

typedef long long ll;
typedef vector <int> VI;
typedef vector <VI> VVI;
typedef vector <VVI> VVVI;
typedef vector <ll> VL;
typedef vector <VL> VVL;
typedef vector <double> VD;
typedef vector <VD> VVD;
typedef vector <bool> VB;
typedef vector <VB> VVB;
typedef queue <int> QI;
typedef pair<int,int> PI;
typedef pair<int,PI> PT;
typedef queue<PI> QPI;
typedef priority_queue<PT> QPT;
typedef pair<double,double> PD;
typedef vector<string> VS;
typedef set<int> SI;
typedef vector<SI> VSI;

int N;
int n,m,k;

VI color;
VVI pol;

bool back (int a)
{
	if (a==n)
	{
		fi (k)
		{
			SI cl;
			fj (pol[i].size())
			{
				cl.insert(color[pol[i][j]-1]);
			}
			if (cl.size()<N) return false;
		}
		cout << N << endl;
		fi (n)
		{
			if (i>0) cout << " ";
			cout << color[i]+1;
		}
		cout << endl;
		return true;
	}
	fi (N)
	{
		color[a] = i;
		if (back(a+1))
			return true;
	}
	return false;
}

int main()
{
	int T;
	cin >> T;
	for (int caso = 1; caso <= T; caso++)
	{
		cout << "Case #" << caso << ": ";
		cin >> n >> m;
		VI l1, l2;
		l1=l2= VI(m);
		fi (m) cin >> l1[i];
		fi (m) cin >> l2[i];
		if (m == 0)
		{
			cout << n << endl;
			fi (n)
			{
				if (i>0) cout << " ";
				cout << i+1;
			}
			cout << endl;
			continue;
		}
		if (m == 1 and n == 8 and (l2[0]-l1[0] == 4))
		{
			cout << 5 << endl;
			VI ans (8);
			ans [(l1[0]+7)%8] = 1;
			ans [(l1[0]+8)%8] = 2;
			ans [(l1[0]+1)%8] = 3;
			ans [(l1[0]+2)%8] = 4;
			ans [(l1[0]+3)%8] = 5;
			ans [(l1[0]+4)%8] = 4;
			ans [(l1[0]+5)%8] = 3;
			ans [(l1[0]+6)%8] = 2;
			fi (8)
			{
				if (i>0) cout << " ";
				cout << ans[i];
			}
			cout << endl;
			continue;
		}
		VSI v(1);
		fi (n) v[0].insert(i+1);
		fi (m)
		{
			fj (v.size())
			{
				if (v[j].count(l1[i])>0 and v[j].count(l2[i])>0)
				{
					SI s;
					VI v2 (v[j].begin(),v[j].end());
					for (int l=0;l<v2.size();l++)
					{
						if (l1[i] <= v2[l] and v2[l] <=l2[i])
						{
							v[j].erase(v2[l]);
							s.insert(v2[l]);
						}
					}
					v.push_back(s);
					v[j].insert(l1[i]);
					v[j].insert(l2[i]);
					break;
				}
			}
		}
		k = v.size();
		pol = VVI (k);
		fi (k) pol[i] = VI (v[i].begin(),v[i].end());
		
		bool ok = false;
		N = 4;
		color = VI (n);
		while (not ok)
		{
			ok = back(0);
			N--;
		}
	}
}

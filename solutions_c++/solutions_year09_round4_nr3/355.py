#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <bitset>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cfloat>

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()

#define eps 1e-8
#define pi acos(-1)

using namespace std;

struct Point
{
	int x, y;
	Point()
	{
	}
	Point(int a, int b)
	{
		x = a;
		y = b;
	}
	void show()
	{
		printf("P = (x, y) = (%d, %d)\n", x, y);
	}
};

struct Segment
{
	Point P1, P2;
	Segment()
	{
	}
	Segment(int a, int b, int c, int d)
	{
		P1 = Point(a, b);
		P2 = Point(c, d);
	}
	Segment(Point a, Point b)
	{
		P1 = a;
		P2 = b;
	}
	double mod()
	{
		return sqrt((P1.x - P2.x)*(P1.x - P2.x) + (P1.y - P2.y)*(P1.y - P2.y));
	}
	void show()
	{
		printf("A = (%d, %d) , B = (%d, %d)", P1.x, P1. y, P2.x, P2.y);
	}
};
long long area(Point P1, Point P2, Point P3)
{
	long long x1 = P1.x, y1 = P1.y;
	long long x2 = P2.x, y2 = P2.y;
	long long x3 = P3.x, y3 = P3.y;
	
	return x2*y3 + x1*y2 + y1*x3 - x2*y1 - x3*y2 - y3*x1;
}

//### DETERMINA SI P PERTENECE AL SEGMENTO S ###########################################
bool inSegment(Segment S, Point P)
{
	return (area(S.P1, S.P2, P)==0 &&
			P.x >= min(S.P1.x, S.P2.x) && P.x <= max(S.P1.x, S.P2.x) &&
			P.y >= min(S.P1.y, S.P2.y) && P.y <= max(S.P1.y, S.P2.y));
}

//### DETERMINA SI EL SEGMENTO S1 SE INTERSECTA CON EL SEGMENTO S2 #####################
bool intersecta(Segment S1, Segment S2)
{
	if(S1.mod()==0) return inSegment(S2, S1.P1);
	if(S2.mod()==0) return inSegment(S1, S2.P1);
	
	if(area(S1.P1, S1.P2, S2.P1)==0 && area(S1.P1, S1.P2, S2.P2)==0)
		return (inSegment(S1, S2.P1) || inSegment(S1, S2.P2) ||
				inSegment(S2, S1.P1) || inSegment(S2, S1.P2));
	
	return (area(S1.P1, S1.P2, S2.P1)*area(S1.P1, S1.P2, S2.P2)<=0 &&
			area(S2.P1, S2.P2, S1.P1)*area(S2.P1, S2.P2, S1.P2)<=0);
}


int n;
bool adj[20][20];
int memo[1<<17];
int memo2[1<<17];

bool valido(int m)
{
    if(memo2[m]!=-1) return memo2[m];
    
    for(int i=0; i<n; i++)
    {
        if(m & (1<<i))
        {
            for(int j=0; j<n; j++)
            {
                if(i!=j && (m & (1<<j)) && adj[i][j]==0)
                {
                    memo2[m] = 0;
                    return 0;
                }
            }
        }
    }
    memo2[m] = 1;
    return 1;
}   

int f(int mask)
{
    if(mask==0) return 0;
    if(memo[mask]!=-1) return memo[mask];
    
    int minN = 1<<30;
    
    for(int m = mask; m; m = (m-1) & mask)
    {        
        if (valido(m)) minN = min(minN, 1 + f(mask & (~m)));
    }
    memo[mask] = minN;
    return minN;
}

int main()
{
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("out.txt", "w", stdout);
        
    int nCasos;
    cin>>nCasos;
    
    for(int caso=1; caso<=nCasos; caso++)
    {
        int k;
        cin>>n>>k;
        
        int V[n][k];
        
        for(int i=0; i<n; i++)
            for(int j=0; j<k; j++)
                cin>>V[i][j];
        
        memset(adj, 0, sizeof(adj));
        
        for(int i=0; i<n; i++)
        {
            for(int j=i+1; j<n; j++)
            {
                bool ok = 1;
                for(int w=0; w<k-1; w++)
                {
                    Segment S1(w, V[i][w], w+1, V[i][w+1]);
                    Segment S2(w, V[j][w], w+1, V[j][w+1]);
                    if(intersecta(S1, S2))
                    {
                        ok = 0;
                        break;
                    }
                }
                if(ok)
                {
                    adj[i][j] = 1;
                    adj[j][i] = 1;
                }
            }
        }
        memset(memo, -1, sizeof(memo));
        memset(memo2, -1, sizeof(memo2));
        cout<<"Case #"<<caso<<": "<<f((1<<n) - 1)<<endl;
    }

    return 0;
}

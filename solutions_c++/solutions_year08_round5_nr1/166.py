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

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()

#define eps 1e-8
#define pi acos(-1)

using namespace std;

// (x, y) -> (x + 105, y + 105)

int dx[] = {0, 1, 0, -1};
int dy[] = {1, 0, -1, 0};

bool M[210][210][2];

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int nC;
	cin>>nC;
	
	for(int caso=1; caso<=nC; caso++)
	{
		cout<<"Case #"<<caso<<": ";
		
		memset(M, 0, sizeof(M));
		
		int x = 0, y = 0, p = 0;
		
		int L;
		cin>>L;
		
		for(int i=0; i<L; i++)
		{
			string s;
			int n;
			cin>>s>>n;
			
			string aux = "";
			for(int j=0; j<n; j++)
				aux += s;
			
			s = aux;
			
			for(int j=0; j<s.size(); j++)
			{
				if(s[j]=='F')
				{
					if(p==0) M[x + 105][y + 105][0] = 1;
					else if(p==1) M[x + 105][y - 1 + 105][1] = 1;
					else if(p==2) M[x + 105][y - 1 + 105][0] = 1;
					else M[x - 1+ 105][y - 1 + 105][1] = 1;
					
					x += dx[p];
					y += dy[p];
				}
				else if(s[j]=='R') p = (p+1)%4;
				else p = (p+3)%4;
			}
		}
		
		int A = 0;
		
		for(int i=0; i<210; i++)
		{
			for(int j=0; j<210; j++)
			{
				int n1 = 0, n2 = 0;
				
				for(int i2=i+1; i2<210; i2++)
					if(M[i2][j][0]) n1++;
				
				for(int i2=i; i2>=0; i2--)
					if(M[i2][j][0]) n2++;
				
				if(n1 && n2 && n1%2==0 && n2%2==0)
				{
					A++;
					continue;
				}
				
				int m1 = 0, m2 = 0;

				for(int j2=j; j2<210; j2++)
					if(M[i][j2][1]) m1++;
				
				for(int j2=j-1; j2>=0; j2--)
					if(M[i][j2][1]) m2++;
				
				if(m1 && m2 && m1%2==0 && m2%2==0)
				{
					A++;
					continue;
				}
											
			}
		}
		cout<<A<<endl;
	}
	
	return 0;
}

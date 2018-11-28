#include<iostream>
#include<vector>
#include<string>
#include<sstream>
#include<algorithm>
#include<map>
#include<list>
#include<cmath>
#include<set>

using namespace std;
#define forn(i,n) for(int i=0;i<(n);i++)
#define dforn(i,n) for(int i=(int)(n-1);i>=0;i--)
#define mp make_pair
#define pb push_back
#define all(v) v.begin(),v.end()
#define min(a,b) (a<b?a:b)
#define max(a,b) (a>b?a:b)
int h,w;
int al[150][150];
int movx[4] = {-1,0,0,1};
int movy[4] = {0,-1,1,0};
vector<int> _cl;
int cl(int i) { return (_cl[i] == -1 ? i : _cl[i] = cl(_cl[i])); }
void join(int i, int j) { if(cl(i)!=cl(j)) _cl[cl(i)] = cl(j); }

main()
{
	int n;
	cin>>n;
	forn(pp,n)
	{				
		cin>>h>>w;
		_cl.clear(); _cl.insert(_cl.begin(), (h+1)*w, -1);
		forn(i,h)
		{
			forn(j,w)
			{
				cin>>al[i][j];
			
			}
		}
		int cont =1 ;
		forn(k,h)
		{
			forn(j,w)
			{
				int x = k;
				int y = j;
				int mejori = -1;
				int mejor = 150000;
				forn(i,4)
				{
					if (x+movx[i] >= 0 &&x+movx[i] < h)
					{
						if (y+movy[i] >= 0 && y+movy[i] < w)
						{
							if (al[x+movx[i]][y+movy[i]] < al[x][y])
							{
								if (mejor > al[x+movx[i]][y+movy[i]])
								{
									mejor = al[x+movx[i]][y+movy[i]];
									mejori = i;
								}
							}
						}
					}
				}
				if(mejori != -1)
				{
					join(x*w+y, (x+movx[mejori])*w+y+movy[mejori] );
				}
			//	else cout<< al[x][y]<<endl;
			}
		}
		map<int,int> m;
		cout<<"Case #"<<pp+1<<":"<<endl;
		forn(k,h)
		{
			forn(j,w)
			{
				int aux = k*w+j;
				int ind = cl(aux);
				if (m[ind] == 0)
				{
					m[ind] = cont++;
				}
				cout<<(char)(m[ind]+'a'-1);
				if (j != w-1)
					cout<<" ";
			}
			cout<<endl;
		}
	}
}

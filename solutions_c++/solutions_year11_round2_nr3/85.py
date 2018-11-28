#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <cmath>
#include <string>

#define fr(x,y) for(int x=0; x<(y); ++x)
#define fe(x,y,z) for(int x=(y); x<(z); ++x)
#define fw(x,y,z) for(int x=(y); x<=(z); ++x)
#define df(x,y,z) for(int x=(y); x>=(z); --x)
#define mn(x,y) ((x)<(y) ? (x) : (y))
#define mx(x,y) ((x)>(y) ? (x) : (y))
#define ab(x) ((x)<0 ? (-(x)) : (x))
#define MP make_pair
#define PB push_back
#define BIG 1000000000
#define X first
#define Y second
#define dbg(x) if(DEBUG) {cout<<#x<<": "<<(x)<<endl;}
#define dout(x) if(DEBUG) {cout<<x;}
#define dline(x) if(DEBUG) {cout<<x<<endl;}
#define dbgr(x,l) if(DEBUG) {cout<<#x<<": ";fr(innercounter,l) cout<<x[innercounter]<<" ";cout<<endl;}
#define dbge(x,y,z) if(DEBUG) {cout<<#x<<": ";fe(innercounter,y,z) cout<<x[innercounter]<<" ";cout<<endl;}
#define dbgw(x,y,z) if(DEBUG) {cout<<#x<<": ";fw(innercounter,y,z) cout<<x[innercounter]<<" ";cout<<endl;}
#define dbgee(x,l1,l2) if(DEBUG) {cout<<#x<<": "<<endl;fr(icounter,l1){fr(jcounter,l2) cout<<x[icounter][jcounter]<<" ";cout<<endl;}}

bool DEBUG = false;

using namespace std;

int t,m,u[5000], v[5000],n,c[5000];
bool used[5000];
int len;
vector<int> mas[5000];

void printmas()
{
	if(DEBUG)
		{
		cout<<"mas: "<<endl;
		fr(i,len)
			{
			cout<<"["<<i<<"]: ";
			fr(j,mas[i].size())
				cout<<mas[i][j]<<" ";
			cout<<endl;
			}
		}	
}

int main()
{
#ifdef HOME
freopen("input.txt", "r",stdin);
freopen("output.txt", "w", stdout);
//DEBUG = true;
#endif
scanf("%d", &t);
fw(test,1,t)
	{
	scanf("%d%d", &n, &m);
	fr(i,m)
		{
		scanf("%d", &u[i]);
		u[i]--;
		}
	fr(i,m)
		{
		scanf("%d", &v[i]);
		v[i]--;
		}
	mas[0].clear();
	fr(i,n)
		mas[0].PB(i);
	len = 1;
	fr(i,m)
		{
		fr(j,len)
			{
			vector<int> f,s;
			int c = 0;
			fr(k,mas[j].size())
				if(mas[j][k]==u[i]||mas[j][k]==v[i])
					{
					c++;
					f.PB(mas[j][k]);
					s.PB(mas[j][k]);
					}
				else if(c==1) f.PB(mas[j][k]);
				else s.PB(mas[j][k]);
			if(c==2)
				{
				mas[j] = f;
				mas[len] = s;
				len++;
				break;
				}
			}
		dbg(u[i]);
		dbg(v[i]);
		}
	printmas();
	int ans;	
	df(nc,n,1)
		{
		int p = 1;
		fr(i,n)
			p*=nc;
		fr(mask,p)
			{
			int tmp = mask;
			fr(j,nc)
				used[j] = false;
			fr(i,n)
				{
				c[i] = tmp%nc;					
				tmp/=nc;
				used[c[i]] = true;
				}
			bool wrong = false;
			fr(j,nc)
				if(!used[j])
					{
					wrong = true;
					break;
					}					
			if(wrong) continue;					
			bool solved = true;
			fr(i,len)
				{
				fr(j,nc)
					used[j] = false;
				fr(j,mas[i].size())
					used[c[mas[i][j]]] = true;
				
				fr(j,nc)
					if(!used[j])
						{
						solved = false;
						break;
						}
	                        if(!solved) break;
				}
			if(solved)
				{
				ans = nc;
				goto A;
				}
			}
		}
	A:
	printf("Case #%d: %d\n", test, ans);
	fr(i,n)
		printf("%d ", c[i]+1);
	printf("\n");
	}
return 0;
}

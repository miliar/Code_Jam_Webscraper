#define _CRT_SECURE_NO_DEPRECATE
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <fstream>
#include <ctime>
#include <cstring>
#pragma comment(linker, "/STACK:16777216")
using namespace std;
#define pb push_back
#define ppb pop_back
#define pi 3.1415926535897932384626433832795028841971
#define mp make_pair
#define x first
#define y second
#define sqr(a) (a)*(a)
#define D(a,b) sqrt(((a).x-(b).x)*((a).x-(b).x)+((a).y-(b).y)*((a).y-(b).y))
#define pii pair<int,int>
#define pdd pair<double,double>
#define sz(x) int((x).size())
#define INF 1000000000
#define FOR(i,a,b) for (int _n(b), i(a); i <= _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define all(c) (c).begin(), (c).end()
#define SORT(c) sort(all(c))
#define rep(i,n) FOR(i,1,(n))
#define rept(i,n) FOR(i,0,(n)-1)
#define L(s) (int)((s).end()-(s).begin())
#define C(a) memset((a),0,sizeof(a))
#define val(ch) (int)(ch)-(int)('0')
#define toch(a) (char)((int)(a)+(int)('0'))
#define VI vector <int>
#define ll long long
const int MX=4000;
const int H=MX/2;
int a,b,c,d,i,j,n,m,k,kolt,w,q,now,last;
char mas[31][31];
string ans[21][21][MX+3][2];
string state[251];
VI Q;
string s;
const int di[]={1,0,-1,0};
const int dj[]={0,1,0,-1};
int main()
{
	freopen("C-small.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&kolt);
	rep(hod,kolt)
	{
		cerr<<hod<<endl;
		scanf("%d%d",&w,&q);
		C(mas);
		rept(i,w)
		{
			scanf("%s",&mas[i]);
		}
		now=0; last=1;
		rept(i,w)
		{
			rept(j,w)
			{
				FOR(z,-H,H)
				{
					if (mas[i][j]=='+' || mas[i][j]=='-') ans[i][j][z+H][0]=""; else
					if (z==mas[i][j]-'0') 
					{
						ans[i][j][z+H][0]="";
						ans[i][j][z+H][0]+=mas[i][j];
					} else
					ans[i][j][z+H][0]="";
				}
			}
		}
		Q.clear();
		rept(i,251) state[i]="b";
		k=0;
		rept(i,q)
		{
			scanf("%d",&a);
			Q.pb(a);
			if (state[a]=="b") k++;
			state[a]="";
		}
		rept(hh,L(Q))
		{
			a=Q[hh];
			if (state[a]!="") continue;
			rept(i,w)
			{
				rept(j,w)
				{
					if (ans[i][j][a+H][0]!="") 
					{
						state[a]=ans[i][j][a+H][0];
					}
				}
			}
			if (state[a]!="") k--;
		}
		int h=1;
		while (k)
		{
			h++;
			now^=1; last^=1;
			rept(i,w)
			{
				rept(j,w)
				{
					if (mas[i][j]=='+' || mas[i][j]=='-') continue;
					FOR(z,-H,H)
					{
						ans[i][j][z+H][now]="";
						// 0 0
						bool ok=0;
						rept(l,4)
						{
							int ci=i+di[l];
							int cj=j+dj[l];
							if (ci>=0 && cj>=0 && ci<w && cj<w && mas[ci][cj]=='+') ok=1;
						}
						if (ok)
						{
							int pr=z-(mas[i][j]-'0');
							if (pr>=-H && ans[i][j][pr+H][last]!="")
							{
								s=ans[i][j][pr+H][last]+"+";
								s+=mas[i][j];
								if (ans[i][j][z+H][now]=="") ans[i][j][z+H][now]=s; else
								ans[i][j][z+H][now]=min(ans[i][j][z+H][now],s);
							}
						}
						ok=0;
						rept(l,4)
						{
							int ci=i+di[l];
							int cj=j+dj[l];
							if (ci>=0 && cj>=0 && ci<w && cj<w && mas[ci][cj]=='-') ok=1;
						}
						if (ok)
						{
							int pr=z+(mas[i][j]-'0');
							if (pr<=H && ans[i][j][pr+H][last]!="")
							{
								s=ans[i][j][pr+H][last]+"-";
								s+=mas[i][j];
								if (ans[i][j][z+H][now]=="") ans[i][j][z+H][now]=s; else
								ans[i][j][z+H][now]=min(ans[i][j][z+H][now],s);
							}
						}
						// -1 -1
						if (i-1>=0 && j-1>=0)
						{
							if (mas[i-1][j]=='+' || mas[i][j-1]=='+')
							{
								int pr=z-(mas[i][j]-'0');
								if (pr>=-H && ans[i-1][j-1][pr+H][last]!="")
								{
									s=ans[i-1][j-1][pr+H][last]+"+";
									s+=mas[i][j];
									if (ans[i][j][z+H][now]=="") ans[i][j][z+H][now]=s; else
									ans[i][j][z+H][now]=min(ans[i][j][z+H][now],s);
								}
							}
							if (mas[i-1][j]=='-' || mas[i][j-1]=='-')
							{
								int pr=z+(mas[i][j]-'0');
								if (pr<=H && ans[i-1][j-1][pr+H][last]!="")
								{
									s=ans[i-1][j-1][pr+H][last]+"-";
									s+=mas[i][j];
									if (ans[i][j][z+H][now]=="") ans[i][j][z+H][now]=s; else
									ans[i][j][z+H][now]=min(ans[i][j][z+H][now],s);
								}
							}
						}
						// -1 1
						if (i-1>=0 && j+1<w)
						{
							if (mas[i-1][j]=='+' || mas[i][j+1]=='+')
							{
								int pr=z-(mas[i][j]-'0');
								if (pr>=-H && ans[i-1][j+1][pr+H][last]!="")
								{
									s=ans[i-1][j+1][pr+H][last]+"+";
									s+=mas[i][j];
									if (ans[i][j][z+H][now]=="") ans[i][j][z+H][now]=s; else
									ans[i][j][z+H][now]=min(ans[i][j][z+H][now],s);
								}
							}
							if (mas[i-1][j]=='-' || mas[i][j+1]=='-')
							{
								int pr=z+(mas[i][j]-'0');
								if (pr<=H && ans[i-1][j+1][pr+H][last]!="")
								{
									s=ans[i-1][j+1][pr+H][last]+"-";
									s+=mas[i][j];
									if (ans[i][j][z+H][now]=="") ans[i][j][z+H][now]=s; else
									ans[i][j][z+H][now]=min(ans[i][j][z+H][now],s);
								}
							}
						}
						// 1 -1
						if (i+1<w && j-1>=0)
						{
							if (mas[i+1][j]=='+' || mas[i][j-1]=='+')
							{
								int pr=z-(mas[i][j]-'0');
								if (pr>=-H && ans[i+1][j-1][pr+H][last]!="")
								{
									s=ans[i+1][j-1][pr+H][last]+"+";
									s+=mas[i][j];
									if (ans[i][j][z+H][now]=="") ans[i][j][z+H][now]=s; else
									ans[i][j][z+H][now]=min(ans[i][j][z+H][now],s);
								}
							}
							if (mas[i+1][j]=='-' || mas[i][j-1]=='-')
							{
								int pr=z+(mas[i][j]-'0');
								if (pr<=H && ans[i+1][j-1][pr+H][last]!="")
								{
									s=ans[i+1][j-1][pr+H][last]+"-";
									s+=mas[i][j];
									if (ans[i][j][z+H][now]=="") ans[i][j][z+H][now]=s; else
									ans[i][j][z+H][now]=min(ans[i][j][z+H][now],s);
								}
							}
						}
						// 1 1
						if (i+1<w && j+1<w)
						{
							if (mas[i+1][j]=='+' || mas[i][j+1]=='+')
							{
								int pr=z-(mas[i][j]-'0');
								if (pr>=-H && ans[i+1][j+1][pr+H][last]!="")
								{
									s=ans[i+1][j+1][pr+H][last]+"+";
									s+=mas[i][j];
									if (ans[i][j][z+H][now]=="") ans[i][j][z+H][now]=s; else
									ans[i][j][z+H][now]=min(ans[i][j][z+H][now],s);
								}
							}
							if (mas[i+1][j]=='-' || mas[i][j+1]=='-')
							{
								int pr=z+(mas[i][j]-'0');
								if (pr<=H && ans[i+1][j+1][pr+H][last]!="")
								{
									s=ans[i+1][j+1][pr+H][last]+"-";
									s+=mas[i][j];
									if (ans[i][j][z+H][now]=="") ans[i][j][z+H][now]=s; else
									ans[i][j][z+H][now]=min(ans[i][j][z+H][now],s);
								}
							}
						}
						// 2 0
						if (i+2<w)
						{
							if (mas[i+1][j]=='+')
							{
								int pr=z-(mas[i][j]-'0');
								if (pr>=-H && ans[i+2][j][pr+H][last]!="")
								{
									s=ans[i+2][j][pr+H][last]+"+";
									s+=mas[i][j];
									if (ans[i][j][z+H][now]=="") ans[i][j][z+H][now]=s; else
									ans[i][j][z+H][now]=min(ans[i][j][z+H][now],s);
								}
							}
							if (mas[i+1][j]=='-')
							{
								int pr=z+(mas[i][j]-'0');
								if (pr<=H && ans[i+2][j][pr+H][last]!="")
								{
									s=ans[i+2][j][pr+H][last]+"-";
									s+=mas[i][j];
									if (ans[i][j][z+H][now]=="") ans[i][j][z+H][now]=s; else
									ans[i][j][z+H][now]=min(ans[i][j][z+H][now],s);
								}
							}
						}
						// -2 0
						if (i-2>=0)
						{
							if (mas[i-1][j]=='+')
							{
								int pr=z-(mas[i][j]-'0');
								if (pr>=-H && ans[i-2][j][pr+H][last]!="")
								{
									s=ans[i-2][j][pr+H][last]+"+";
									s+=mas[i][j];
									if (ans[i][j][z+H][now]=="") ans[i][j][z+H][now]=s; else
									ans[i][j][z+H][now]=min(ans[i][j][z+H][now],s);
								}
							}
							if (mas[i-1][j]=='-')
							{
								int pr=z+(mas[i][j]-'0');
								if (pr<=H && ans[i-2][j][pr+H][last]!="")
								{
									s=ans[i-2][j][pr+H][last]+"-";
									s+=mas[i][j];
									if (ans[i][j][z+H][now]=="") ans[i][j][z+H][now]=s; else
									ans[i][j][z+H][now]=min(ans[i][j][z+H][now],s);
								}
							}
						}
						// 0 2
						if (j+2<w)
						{
							if (mas[i][j+1]=='+')
							{
								int pr=z-(mas[i][j]-'0');
								if (pr>=-H && ans[i][j+2][pr+H][last]!="")
								{
									s=ans[i][j+2][pr+H][last]+"+";
									s+=mas[i][j];
									if (ans[i][j][z+H][now]=="") ans[i][j][z+H][now]=s; else
									ans[i][j][z+H][now]=min(ans[i][j][z+H][now],s);
								}
							}
							if (mas[i][j+1]=='-')
							{
								int pr=z+(mas[i][j]-'0');
								if (pr<=H && ans[i][j+2][pr+H][last]!="")
								{
									s=ans[i][j+2][pr+H][last]+"-";
									s+=mas[i][j];
									if (ans[i][j][z+H][now]=="") ans[i][j][z+H][now]=s; else
									ans[i][j][z+H][now]=min(ans[i][j][z+H][now],s);
								}
							}
						}
						//0 -2
						if (j-2>=0)
						{
							if (mas[i][j-1]=='+')
							{
								int pr=z-(mas[i][j]-'0');
								if (pr>=-H && ans[i][j-2][pr+H][last]!="")
								{
									s=ans[i][j-2][pr+H][last]+"+";
									s+=mas[i][j];
									if (ans[i][j][z+H][now]=="") ans[i][j][z+H][now]=s; else
									ans[i][j][z+H][now]=min(ans[i][j][z+H][now],s);
								}
							}
							if (mas[i][j-1]=='-')
							{
								int pr=z+(mas[i][j]-'0');
								if (pr<=H && ans[i][j-2][pr+H][last]!="")
								{
									s=ans[i][j-2][pr+H][last]+"-";
									s+=mas[i][j];
									if (ans[i][j][z+H][now]=="") ans[i][j][z+H][now]=s; else
									ans[i][j][z+H][now]=min(ans[i][j][z+H][now],s);
								}
							}
						}
						if (z>=0 && z<=250 && (state[z]=="" || L(state[z])==L(ans[i][j][z+H][now])) && ans[i][j][z+H][now]!="")
						{
							if (state[z]=="") 
							{
								k--;
								state[z]=ans[i][j][z+H][now];
							} else
							state[z]=min(state[z],ans[i][j][z+H][now]);
						}
					}
				}
			}
		}
		printf("Case #%d:\n",hod);
		rept(i,L(Q))
		{
			printf("%s\n",state[Q[i]].c_str());
		}
	}
	cerr<<1.0*clock()/CLOCKS_PER_SEC<<endl;
}

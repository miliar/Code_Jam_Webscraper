/*
 * A.cpp
 * Another buggy code by mostafa_saad
 *
 *  Created on: May 22, 2010
 */


#include<set>
#include<map>
#include<list>
#include<iomanip>
#include<cmath>
#include<string>
#include<vector>
#include<queue>
#include<stack>
#include<complex>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<numeric>
#include<utility>
#include <functional>
#include<stdio.h>
#include<assert.h>
#include<memory.h>
using namespace std;

#define all(v)				((v).begin()), ((v).end())
#define sz(v)				((int)((v).size()))
#define clr(v, d)			memset(v, d, sizeof(v))
#define rep(i, v)		for(int i=0;i<sz(v);++i)
#define lp(i, n)		for(int i=0;i<(int)(n);++i)
#define lpi(i, j, n)	for(int i=(j);i<(int)(n);++i)
#define lpd(i, j, n)	for(int i=(j);i>=(int)(n);--i)
#define repa(v)				lpi(i, 0, sz(v)) lpi(j, 0, sz(v[i]))
#define P(x)				cout<<#x<<" = { "<<x<<" }\n"
#define pb					push_back
#define MP					make_pair

typedef vector<int>       vi;
typedef vector<double>    vd;
typedef vector< vi >      vvi;
typedef vector< vd >      vvd;
typedef vector<string>    vs;
typedef long long         ll;
typedef long double   	  ld;

const int OO = (int)1e8;	//Small -> WRONG, Large -> OVERFLOW

const double PI  = acos(-1.0);
const double EPS = (1e-7);

int dcmp(double x, double y) {	return fabs(x-y) <= EPS ? 0 : x < y ? -1 : 1;	}
int M,N;
bool maze[512][512];
//int mx[512][512];
int vis[512][512];
//vector<pair<int,int> > cr[512][512];
int main()
{
#ifndef ONLINE_JUDGE
	freopen("a.txt", "rt", stdin);
    freopen("b.txt", "wt", stdout);
#endif
	int cases;
	cin>>cases;
	string s;
	lp(cc, cases) {
		cin>>M>>N;
		clr(maze,0);
		lp(i,M){
			cin>>s;
			lp(j,sz(s)){
				int x=s[j]-'0';
				if(s[j]>='A' && s[j]<='F')
					x=s[j]-'A'+10;
				lp(k,4){
					if(x&(1<<k))
						maze[i][j*4+4-k-1]=1;
					//cr[i][j*4+4-k-1].clear();
				}
			}
		}
		map<int,int> m;
		int mm=2;
		clr(vis,0);
		while(mm!=1){
			mm=1;
			int ii,jj;
			lp(i,M)
				lp(j,N){
					if(vis[i][j])
						continue;
					int w=1;
					bool c=1;
					while(c){
						c=1;
						lp(k,w+1){
							if(maze[i+k][j+w]==maze[i+k][j+w-1] || maze[i+w][j+k]==maze[i+w-1][j+k] || vis[i+k][j+w] || vis[i+w][j+k]){
								c=0;
								break;
							}
						}
						if(c)
							w++;
					}
					if(w>mm){
						mm=w;
						ii=i;
						jj=j;
					}
				}
			if(mm!=1){
				m[-mm]++;
				lp(i,mm)
					lp(j,mm)
						vis[ii+i][jj+j]=1;
			}
		}
		/*while(mm!=1){
			mm=1;
			int ii,jj;
			lp(i,M)
				lp(j,N)
					if(!vis[i][j] && mx[i][j]>mm){
						mm=mx[i][j];
						ii=i;
						jj=j;
					}
			if(mm!=1){
				cout<<mx[2][1]<<endl;
				//cout<<ii<<" "<<jj<<" "<<mm<<endl;
				lp(i,mm)
					lp(j,mm){
						vis[ii+i][jj+j]=mm;
						lp(k,sz(cr[ii+i][jj+j])){
							int ci=cr[ii+i][jj+j][k].first;
							int cj=cr[ii+i][jj+j][k].second;
							mx[ci][cj]=min(mx[ci][cj],min(i-ci,j-cj));
						}
					}
				m[-mm]++;
			}
		}*/
		/*lp(i,M){
			lp(j,N)
			cout<<vis[i][j];
			cout<<endl;
		}*/
		lp(i,M)
			lp(j,N)
				if(!vis[i][j])
					m[-1]++;
		cout<<"Case #"<<cc+1<<": "<<sz(m)<<endl;
		for(map<int,int>::iterator it=m.begin();it!=m.end();it++)
			cout<<-it->first<<" "<<it->second<<endl;
	}

	return 0;
}

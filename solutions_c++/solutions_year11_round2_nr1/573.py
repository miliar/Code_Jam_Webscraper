// zero.lin`s google_codejam.cpp 
//


#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string.h>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstdlib>
#include <cctype>
#include <cmath>


#include "google_codejam\stdafx.h"
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vii;
typedef long long ll;

#define rep(i,n) for(int i=0;i<n;++i)
#define all(n) n.begin(),n.end()
#define sz(o) (int)(o.size())
#define mset(o,v) memset(o,v,sizeof(o))
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) 
#define mk(first,second) make_pair(first,second)
#define present(container, element) (container.find(element) != container.end()) 
#define cpresent(container, element) (find(all(container),element) != container.end())

const int inf=1<<28;
const double eps=1e-11;
int gcd(int a,int b){return b==0?a:gcd(b,a%b);}
int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	
	
	int testcase;
	scanf("%d",&testcase);
	
	rep(caseID,testcase)
	{
		char board[100][102];
		int n;
		scanf("%d ",&n);
		for(int i=0;i<n;++i)
			scanf("%s ",board[i]);
		double wp[100],owp[100],oowp[100];
		double rp[100][100];
		mset(rp,0);
		mset(wp,0);
		mset(owp,0);
		mset(oowp,0);
		for(int i=0;i<n;++i)
		{
			int ww=0,s=0;
			for(int j=0;j<n;++j)
			{	if(board[i][j]=='0')
					s++;
				else if(board[i][j]=='1')
				ww++;
			}
			s+=ww;
				wp[i]=1.0*ww/s;
			for(int j=0;j<n;++j)
			{
				if(board[i][j]=='0')
					rp[i][j]=1.0*ww/(s-1);
				else if(board[i][j]=='1')
					rp[i][j]=1.0*(ww-1)/(s-1);
			}
		}
		for(int i=0;i<n;++i)
		{
			double s=0,p=0;
			for(int j=0;j<n;++j)
				if( board[i][j]!='.')
				{
					s+=rp[j][i];
					p+=1;
				}
			
				owp[i]=1.0*s/p;
		}
		for(int i=0;i<n;++i)
		{
			double s=0,d=1,p=0;
			for(int j=0;j<n;++j)
				if(j!=i && board[i][j]!='.')
				{
					//s*=w[i];
					s+=owp[j];
					p+=1;
				}
			
				oowp[i]=1.0*s/p;
		}
		printf("Case #%d:\n",caseID+1);
		for(int i=0;i<n;++i)
		{
			cout<<(0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i])<<endl;
		}
	}
	
	return 0;
}


#include<iostream>
#include<cmath>
#include<vector>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<sstream>
#include<map>
#include<queue>
#include<set>
#define vvi vector<vector<int> >
#define co continue
#define pb push_back
#define vi vector<int>
#define vs vector<string>
#define br break
#define re return
#define ALL(v) v.begin(),v.end() 

#define REP(i,n) for(int i=0;i<(int) n;i++)
#define LL long long
#define SZ size()
#define INF (2<<29)

#define pii pair<int ,int>
#define DEBUG(x) cout<<#x<<": "<<x<<endl
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin() ; it!=(c).end() ;it++)
template <class T> inline int BITCNT(T x) { int ret=0; while (x) { ret++; x&=x-1; } return ret; }

using namespace std;
vector<LL> X , Y;
int CNT[3][3];
int main()
{
    int kases;
    cin>>kases;
    for(int kase = 1 ; kase<=kases; kase++)
    {
        LL n,A, B, C, D, x0, y0, M;
        cin>>n>>A>>B>>C>>D>>x0>>y0>>M;
        X.clear();Y.clear();
        X.push_back(x0);
        Y.push_back(y0);
        for(int i=1;i<=n-1;i++)
        {
			LL tempX = (LL)A*X.back();
			tempX = (LL)tempX + B;
			tempX %=M;
			X.push_back(tempX);
	//		cout<<tempX<< " ";
			LL tempY = (LL)C*Y.back();
			tempY = (LL)tempY + D;
			tempY %=M;
			Y.push_back(tempY);
//			cout<<tempY<<endl;
		}
		int res =0;
		for(int i=0;i<X.size();i++)
		{
			for(int j=i+1;j<X.size();j++)
			{
				for(int k=j+1;k<X.size();k++)
				{
					if((X[i]+X[j]+X[k])%3==0 && (Y[i]+Y[j]+Y[k])%3==0) res ++;
				}
			}
		}
	 cout<<"Case #"<<kase<<": "<<res<<endl;;
    }
    return 0;
}

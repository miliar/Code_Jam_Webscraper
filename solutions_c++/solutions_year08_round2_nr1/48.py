#define _CRT_SECURE_NO_DEPRECATE
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <sstream>
#include <fstream>
using namespace std;
#define pb push_back
#define ppb pop_back
#define mp make_pair
//#define pi 2*acos(0.0)
#define mp make_pair
//#define x first
//#define y second
#define sqr(a) (a)*(a)
#define pii pair<int,int>
#define pdd pair<double,double>
#define sz(c) (int)((c).size())
#define inf 1000000000
#define all(c) (c).begin(), (c).end()
#define vi vector<int>
#define vpii vector< pii >
#define vpdd vector< pdd >
#define L(s) (int)((s).end()-(s).begin())
#define ll long long
#define C(a,b) memset((a),(b),sizeof((a)))
int cnt,cc;
ll A,B,C,D,M,n,X,Y;
int i,j,k;
ll o[3][3];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>cnt;
	for(cc=1;cc<=cnt;cc++)
	{
		C(o,0);
		cin>>n>>A>>B>>C>>D>>X>>Y>>M;
		o[X%3][Y%3]++;
		for(i=1;i<n;i++)
		{
			X=(A*X+B)%M;
			Y=(C*Y+D)%M;
			o[X%3][Y%3]++;
		}
		ll rez=0,rez2=0;
		for(i=0;i<9;i++)
			for(j=i;j<9;j++)
				for(k=j;k<9;k++)
				{
					if ((i/3+j/3+k/3)%3==0)
					if ((i%3+j%3+k%3)%3==0)
					if (i==k)
						rez+=(o[i/3][i%3]*(o[i/3][i%3]-1)*(o[i/3][i%3]-2))/6;
					else
					if (i==j)
						rez+=(o[i/3][i%3]*(o[i/3][i%3]-1)*(o[k/3][k%3]))/2;
					else
					if (j==k)
						rez+=(o[i/3][i%3]*(o[j/3][j%3])*(o[j/3][j%3]-1))/2;
					else
						rez+=o[i/3][i%3]*o[j/3][j%3]*o[k/3][k%3];
					if (rez>0)
					{
						rez++;
						rez--;
					}
				}
//		for(i=0;i<n;i++)
//			for(j=i+1;j<n;j++)
//				for(k=j+1;k<n;k++)
//					if ((x[i]+x[j]+x[k])%3==0)
///						if ((y[i]+y[j]+y[k])%3==0)
//							rez2++;
		cout<<"Case #"<<cc<<": "<<rez<<endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
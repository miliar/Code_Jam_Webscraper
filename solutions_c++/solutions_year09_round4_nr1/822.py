#include <algorithm>
#include <iostream>
#include <iomanip>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <bitset>
#include <cstdio>
#include <cmath>
#include <string>
#include <stack>
#include <map>
#include <set>

using namespace std;

#define mem(a,b) (memset(a,b,sizeof(a)))
#define Out(x) (cout << #x << " = " << x << endl)

template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline void checkmod(T& a,T m){ a=(a%m+m)%m;}
template<class T> inline void out(T x, int n){  for(int i = 0; i < n; ++i)  cout << x[i] <<" " ;    cout << endl;    }
template<class T> inline void out(T x, int n, int m){  for(int i = 0; i < n; ++i)    out(x[i], m);    cout << endl;    }
template<class T> inline void out(char * x) { for(int i =0;i< (int) strlen(x); i++)  cout << x[i] <<" " ;    cout << endl;  }


const double pi = acos(-1.0);
const int INF = 0x7fffffff;

const int N = 50;

char mat[N][N];

int num[N];
int numt[N];

int main()
{
        //freopen("A-small-attempt0.in","r",stdin);
		//freopen("A-small-attempt0.out","w",stdout);

        freopen("A-large.in","r",stdin);
        freopen("A-large.out","w",stdout);

		int T;
		scanf("%d",&T);
		
		int ans;
		int i,j,k;
		int n;
		for(int cases =1 ; cases <= T;cases++)
		{
			mem(num,0);
			mem(numt,0);
			
			scanf("%d",&n);
		
			ans=0;
			for(i=1;i<=n;i++)
				for(j=1;j<=n;j++)
				{
					cin>>mat[i][j];
					mat[i][j]-='0';
				}
			
			
			for(i=1;i<=n;i++)
			{
				for(j=n;j>=1;j--)
				{
					if(mat[i][j]==1)
					{
						num[i]=j;
						break;
					}
				}
			}
			
			
			for(i=1;i<=n;i++)
			{
				if(num[i]<=i)
					continue;
				
				for(j=i+1;j<=n;j++)
					if(num[j]<=i)
						break;
				ans+=(j-i);
				
				int q=0;
				for(k=i;k<j;k++)
					numt[q++]=num[k];
				q=0;
				for(k=i+1;k<=j;k++)
					num[k]=numt[q++];
			}
			
			printf("Case #%d: ",cases);
			cout<<ans<<endl;
		}
        return 0;
}

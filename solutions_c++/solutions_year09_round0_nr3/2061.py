#include <cstring>
#include <cstdlib>
#include <iostream>
#include <cmath>
#include <utility>
#include <string>

using namespace std;

#define rep(i,n) for(int i=0; i<(n); ++i)

int N;
int ans=0;
char s1[] = "welcome to code jam";
char s2[501];
int d[2][501];
int n1=19;
int n2=0;
int lastj=0;
int sum=0;
int sum2=0;

int main()
{
	cin >> N;
	cin.getline(s2,501);
	rep(t,N)
	{
		cin.getline(s2,501);
		n2=strlen(s2);
		if(s2[n2-1]=='\r') n2--;
		//cout << n2 << endl;		
		rep(i,n2) d[1][i]=0;
		
		sum2=0;
		rep(k,n1)
		{
			lastj=-1;
			sum=0;
			rep(j,n2)
			{
				if (k>j)
					d[k%2][j]=0;
				else if (s1[n1-k-1] == s2[n2-j-1] && k==0)
					d[k%2][j]=(++sum2);
				else if (s1[n1-k-1] == s2[n2-j-1])
					//d[k%2][j]=max(d[(k+1)%2][j-1], 2*d[k%2][j-1]);
					d[k%2][j]=d[(k+1)%2][j-1] + 2*d[k%2][j-1] - sum;
				else
					d[k%2][j]=d[k%2][j-1];
				
				d[k%2][j]%=10000;
				if (s1[n1-k-1] == s2[n2-j-1])
				{
					lastj=j;
					sum+=d[(k+1)%2][lastj-1];
				}
			}
			//rep(j,n2) printf("%5d ",d[k%2][j]);
			//printf("\n");
		}
		
		ans=d[(n1-1)%2][n2-1];
		printf("Case #%d: %04d\n", t+1, ans);
	}
}

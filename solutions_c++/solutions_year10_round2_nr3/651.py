#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

#define Max 26 
#define module 100003

int a[Max][Max];
int b[Max];
int c[Max][Max];

// build combinatorial triangle
void buildc()
{
	c[1][0] = 1; 
	c[1][1] = 1;
	for(int n=2; n<Max; n++) {
		c[n][0] = 1;
		c[n][n] = 1;
		for(int k=1; k<=n-1; k++) {
			c[n][k] = (c[n-1][k-1]+c[n-1][k])%module;
		}
	}
}

void builda()
{
	buildc();
	a[2][1] = 1;
	for(int n=3; n<Max; n++) {
		a[n][n-1] = 1;
		a[n][1] = 1;
		for(int k=2; k<=n-2; k++) { // find a[n][n-k]
			a[n][n-k] = 0;
			for(int i=0; i<=k-1; i++) {
				a[n][n-k] = (a[n][n-k]+a[n-k][n-k-1-i]*c[k-1][i])%module;
			}
		}
	}
}

void buildb()
{
	for(int n=2; n<Max; n++) {
		b[n] = 0;
		for(int k=1; k<=n-1; k++) {
			b[n] = (b[n]+a[n][k])%module;
		}
	}
}

int main()
{
	//freopen("D:\\tmp\\test.txt","r",stdin);freopen("D:\\tmp\\test.out","w",stdout);
	freopen("D:\\tmp\\C-small.in","r",stdin);freopen("D:\\tmp\\C-small.out","w",stdout);
	//freopen("D:\\tmp\\C-large.in","r",stdin);freopen("D:\\tmp\\C-large.out","w",stdout);
	builda();
	buildb();
	int testcase;
	cin >> testcase;
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		int n;
		cin >> n;
		printf("Case #%d: ",caseId);
		printf("%d", b[n]);
		printf("\n");
	}

	return 0;
}
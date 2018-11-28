#include <iostream>

using namespace std;

int a[100];
char s[100][100];
int n;

void init()
{
	cin>>n;
	for (int i=0;i<n;i++)
		cin>>s[i];
}
int calc()
{
	for (int i=0; i<n;i++) {
		a[i] = -1;
		for (int j=n-1;j>=0; j--)
			if (s[i][j]=='1') {
				a[i] = j;
				break;
			}
	}
	int ans = 0;
	for (int i=0;i<n;i++) {
		for (int j=i; j<n;j++)
			if (a[j]<=i) {
				ans += j-i;
				for (int k=j-1; k>=i; k--)
					a[k+1]  = a[k];
				break;
			}
	}
	return ans;
		
}
int main()
{
	int t;
	cin>>t;
	for (int i=0;i<t;i++)
	{
		init();
		cout<<"Case #"<<i+1<<": "<<calc()<<endl;
	}
}

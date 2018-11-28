#include <iostream>
#include <string>
#include <algorithm>
#include <vector>



using namespace std;


string A[200];
string S;
int B[2000],C[2000];
int n,m,q,w,e,i,j,r,t,tt,y,u;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin >> tt;
	for (t=1; t<=tt; t++)
	{
		cin >> n;
		getline(cin,A[0]);
		for (i=0; i<n; i++)
			getline(cin,A[i]);
		cin >> m;
		getline(cin,S);
		q=0;
		for (i=0; i<m; i++)
		{
			getline(cin,S);
			for (j=0; j<n; j++)
				if (S==A[j])
				{
					B[q++]=j;
					break;
				}
		}
		m=q;
		for (i=0; i<n; i++) C[i]=0;
		q=0; w=1; int ans=0;
		for (i=0; i<m; i++)
		{
			if (C[B[i]]!=w)
			{
				q++;
				C[B[i]]++;
			}
			if (q==n)
			{
				ans++;
				q=1;
				C[B[i]]++;
				w++;
			}
		}
		cout << "Case #" << t << ": " << ans << endl;
	}



	return 0;
}

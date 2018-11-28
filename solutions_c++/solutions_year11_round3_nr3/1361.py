#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{

	int T;
	//freopen("A-large.in","r",stdin);
	cin >> T;
	int a[1000];

	for(int tNum=1; tNum<=T; ++tNum)
	{
		int n, l, h;
		cin >> n >> l >> h;
		for(int i=0; i<n; ++i)
			cin >> a[i];
		int ans=-1;
		for(int i=l; i<=h; ++i)
		{
			bool ok=true;
			for(int j=0; j<n; ++j)
			{
				if(a[j]%i!=0 && i%a[j]!=0) ok=false;
			}
			if(ok){
				ans=i;
				break;
			}
		}
		printf("Case #%d: ",tNum);
		if(ans>=0)
			printf("%d\n",ans);
		else printf("NO\n");
	}	
	
	return 0;
}

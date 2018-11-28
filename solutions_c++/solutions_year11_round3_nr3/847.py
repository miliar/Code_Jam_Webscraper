#include <iostream>
#include <iomanip>

#include <cstdio>
#include <cctype>
#include <cstring>
#include <cmath>

#include <vector>

#include <queue>
#include <stack>

#include <algorithm>

using namespace std;

int main()
{
	freopen("C-small-attempt0.in","r",stdin); freopen("C-small-out.txt","w",stdout);
	//freopen("A-large(1).in","r",stdin); freopen("A-large-out.txt","w",stdout);
	
	int t,k;
	
	int n,l,h;
	int i,j,okay;
	
	int a[100000];
	
	cin>>t;
		
	for(k=1;k<=t;k++)
	{
		cin>>n>>l>>h;
		
		for(i=0;i<n;i++)
			cin>>a[i];
			
		okay=0;
			
		for(i=l;i<=h;i++)
		{
			for(j=0;j<n;j++)
			{
				if(a[j]%i==0 || i%a[j]==0) continue;
				else break;
			}
			
			if(j==n) 
			{
				okay=1;
				break;
			}
		}
		
		cout<<"Case #"<<k<<": ";
		
		if(okay==0) cout<<"NO"<<endl;
		else cout<<i<<endl;
					
		
	}

	return 0;
}






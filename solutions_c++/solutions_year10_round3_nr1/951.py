#include<iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iostream>
#include <sstream>
#include <cstddef>
#include <algorithm>
#include <utility>
#include <iterator>
#include <numeric>
#include <list>

using namespace std;

#define pb push_back
#define OUT(c) cout<<(c)<<endl


int main()
	{
	freopen("A.in","r",stdin);
	freopen("A.out.txt","w",stdout);
	int i,t,tc=0,ans=0,n,count=0,j;
	int a[10005],b[100005];
	bool visited[100005];
	cin>>t;
	while(t--)
		{count=0;
	memset(visited,false,sizeof(visited));
	memset(a,0,sizeof(a));
	memset(b,0,sizeof(b));
		tc++;
		cin>>n;
		for(i=0;i<n;i++)
		cin>>a[i]>>b[i];
		for(i=0;i<n;i++)
			{
			for(j=0;j<n;j++)
				{
				if(i!=j&&visited[j]==0)
					{
					if((a[j]<a[i]&&b[j]>b[i])||(a[j]>a[i]&&b[j]<b[i]))
						count++;
					}
				}
			visited[i]=true;
			}
		ans=count;

		cout<<"Case #"<<tc<<": "<<ans<<endl;
		}
	
	
	return 0;
	}

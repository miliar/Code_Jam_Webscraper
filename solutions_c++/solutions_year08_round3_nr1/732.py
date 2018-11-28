/*designed by sb_dieing*/
#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
#include <set>
#include <queue>
#include <map>
#include<cstring>
#include<fstream>
using namespace std;
int l[1001];

int main()
{
        freopen("A-small-attempt0.in","r",stdin);
		freopen("A-small-attempt0.out","w",stdout);
	    int N,K,P,L;
		int i,j;
		while(cin>>N)
		{int test=1;
		for(test=1;test<=N;test++)
		{
			cin>>P>>K>>L;
			for(i=0;i<L;i++)
				cin>>l[i];
			if(P*K<L){cout<<"Impossible"<<endl;continue;}
			sort(l,l+L);
			int ans=0;
			int p=1;
			int k=1;
			for(i=L-1;i>=0;i--)
			{
				ans+=p*l[i];
                if(k>=K){k=0;p++;}
				k++;
			}
			cout<<"Case #"<<test<<": "<<ans<<endl;
        }
		}
        return 0;
}
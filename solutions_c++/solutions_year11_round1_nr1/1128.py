#include <iostream>
#include <iomanip>

#include <cstdio>
#include <cctype>
#include <cstring>
#include <cmath>

#include <queue>

#include <algorithm>

using namespace std;


int main()
{
	//freopen("A-small-attempt0.in","r",stdin); freopen("a-small-out.txt","w",stdout);
	freopen("A-large.in","r",stdin); freopen("a-large-out.txt","w",stdout);
	
	long long t,k,okay,n,pd,pg,p,q;
	
	cin>>t;
		
	for(k=1;k<=t;k++)
	{
		okay=0;
		
		cin>>n>>pd>>pg;
		
		if(pg==0 && pd>0) okay=0;
		else if(pg==100 && pd<100) okay=0;
		else if(n>=100) okay=1;
		else
		{
			for(q=n;q>=1;q--)
				for(p=q;p>=0;p--)
					if((p*100)==(q*pd)) okay=1;
		}
		
		if(okay==1) cout<<"Case #"<<k<<": Possible";
		else cout<<"Case #"<<k<<": Broken";
		
		cout<<endl;
	}

	return 0;
}






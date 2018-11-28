#include <stdio.h>
#include <iostream>
#include <map>
using namespace std;


int main()
{
int tc;
cin >>tc;
int g[1001],g1[1001];
int r,k,n;
long long ans=0;
for(int p=1;p<=tc;++p)
{
  cin>>r>>k>>n;ans=0;
  map<int,int> m,m1;


  for(int i=0;i<n;++i)
	cin>>g[i];
 
  while(r>0)
  { 
  int kk=0,j=0;
 	 while(kk<=k && j<n) {
		if (kk+g[j]>k) break;
		kk+=g[j];g1[j]=g[j]; ++j;
  	}
	  ans+=kk;
        for(int i=0;i+j<n;++i)
                g[i]=g[i+j];
        for(int i=n-j,q=0;i<n;++i,++q)
                g[i]=g1[q];

/*        if (m[j] > 0) { 
          	long long yans = m[j],rem = m1[j];
		int diff = rem-r; long long amt = ans-yans;
		ans+=amt*(r/diff);
		r%=diff;
		m.clear();m1.clear(); r-=2;
		continue;
         }*/
//	m[j]=ans; m1[j] = r;
     r--;
  } 
  cout<<"Case #"<<p<<": "<<ans<<endl;
}

}


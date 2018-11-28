#include <iostream>
#include<cstdio>
#include<algorithm>

using namespace std;

#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;

#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
#define MAXN 2001000
#define PSIZE 100000
int plist[PSIZE], pcount=0;
int prime(int n){
	int i;
	if ((n!=2&&!(n%2))||(n!=3&&!(n%3))||(n!=5&&!(n%5))||(n!=7&&!(n%7)))
		return 0;
	for (i=0;plist[i]*plist[i]<=n;++i)
		if (!(n%plist[i]))
			return 0;
	return n>1;
}
void initprime(){
	int i;
	for (plist[pcount++]=2,i=3;i<100000;++i)
		if (prime(i))
			plist[pcount++]=i;
}
int prime_factor(int n, int* f, int *nf) {
	int cnt = 0;
	int n2 = sqrt((double)n);
	for(int i = 0; n > 1 && plist[i] <= n2; ++i)
		if (n % plist[i] == 0) {
			for (nf[cnt] = 0; n % plist[i] == 0; ++nf[cnt], n /= plist[i]);
			f[cnt++] = plist[i];
		}
	if (n > 1) nf[cnt] = 1, f[cnt++] = n;
	return cnt;
}
int f[1100000],nf[110000];
int num1[111000],num2[11000];
int main()
{
    int n,temp,l,i,j,tt,x,s,r,t,ans,Min,Max,z;
    int sum;
    bool flag;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    initprime();
    cin>>t;
    for(l=1;l<=t;l++)
    {
        cin>>n;
        for(i=0;i<=n;i++)num1[i]=0;
        Max=0;
        Min=1;
        for(i=1;i<=n;i++)
        {
            z=prime_factor(i,f,nf);
            flag=false;
            for(j=0;j<z;j++)
            {
                if(num1[f[j]]<nf[j])
                {
                    flag=true;
                    num1[f[j]]=nf[j];
                }
            }
            if(flag)Min++;
        }
        for(i=0;i<=n;i++)num1[i]=0;
        for(i=2;i<=n;i++)
        {
            if(num1[i]==0)
            {
                for(j=i+i;j<=n;j+=i)num1[j]=1;
                Max++;
            }
        }
        if(Max==0)Max=1;
        ans=Min-Max;
        if(ans<0)ans=-ans;
        cout<<"Case #"<<l<<": "<<ans<<endl;
    }
    return 0;
}

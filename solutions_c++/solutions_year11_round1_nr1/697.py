#include<cstdio>
#include<cstring>
using namespace std;

 long long gcd(long long a,long long b)
 {
	 int t;
	 if (a>b) 
	 {
		 t=a;a=b;b=t;
	 }
	 if (a==0) return b;
	 else return gcd(b%a,a);
 }

 long long n;
 int T,pd,pg;
 bool p1,p2;

 int main()
 {
	 freopen("text.in","r",stdin);
	 freopen("text.out","w",stdout);
	 scanf("%d",&T);
	 for(int cas=1;cas<=T;cas++)
	 {
		 scanf("%I64d%d%d",&n,&pd,&pg);
		 long long k1,k2,k;
		 k1=pd;
		 k2=100;
		 if (k1==0) k2=1;
		 else 
		 {
			 k=gcd(k1,k2);
			 k1/=k;
			 k2/=k;
		 }
		 if (n>=k2) p1=true;
		 else p1=false;
		 if (p1)
		 {
			if ((pg==100 && pd<100) || (pg==0 && pd>0)) p2=false;
			else p2=true;
		 }
		 printf("Case #%d: ",cas);
		 if (p1 && p2) printf("Possible\n");
		 else printf("Broken\n");
	 }
	 return 0;
 }

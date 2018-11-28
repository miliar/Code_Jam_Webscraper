#include <stdio.h>
#include <string.h>
#include <math.h>
#include <algorithm>

#define EPS 1e-4

inline long long gcd(long long a,long long b) {
  if(b<0) b=-b;
  while(b) {
    long long r=a%b;
    a=b;
    b=r;
  }
  return a;
}

int factor(long long n,long long *divz) {
  int cnt=0;
  long long r;
  for(r=2;r*r*r<=n;++r) {
    while(!(n%r)) {
      divz[cnt++]=r;
      n/=r;
    }
  }
  if(n>1) {
    long long k,d;
    double pow_n=pow(n+0.0,1/6.0);
    for(k=1;k*k*k<=n;++k) {
      double x=pow_n;
      x=0.25*x/sqrt(k+0.0);
      long long up=(long long)(x+1-EPS);
      for(d=0;d<=up;++d) {
        x=sqrt(4*k*n+0.0);
        long long t=(long long)(x+EPS)+d;
        t=t*t-4*k*n;
        x=sqrt(t+0.0);
        long long s=(long long)(x+0.5);
        if(s*s==t) {
          long long A,B;
          x=sqrt(4*k*n+0.0);
          A=(long long)(x+EPS)+d;
          x=sqrt(A*A-4*k*n+0.0);
          B=(long long)(x+EPS);
          t=gcd(n,A+B);
          if(t==1 || t==n)
            t=gcd(n,A-B);
          if(t>1 && t<n) {
            s=n/t;
            divz[cnt++]=t;
            divz[cnt++]=s;
            return cnt;
          }
        }
      }
    }
    divz[cnt++]=n;
  }
  return cnt;
}

long long BIG=1000000000000000000LL;

inline bool mul(long long a,long long b,long long &c) {
	if(a>=BIG/b) {
		c=BIG;
		return false;
	}
	c=a*b;
	return true;
}

#define MAX 10100

int n,m;
long long ans, l, h;
long long f[MAX];

inline bool check(long long d) {
	if(d<l || d>h) return false;
	for(int i=0;i<n;++i)
		if((f[i]%d) && (d%f[i]))
			return false;
	return true;
}

long long divs[100000];
int count[100000];

void go(int k, long long d) {
	if(k>=m) {
		if(d<ans && check(d))
			ans=d;
		return;
	}
	for(int i=0;i<=count[k];++i) {
		go(k+1,d);
		d*=divs[k];
	}
}

long long divz[1000000];

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tests;
	scanf("%d",&tests);
	for(int test=1;test<=tests;++test) {
		fprintf(stderr,"%d\n",test);
		scanf("%d%lld%lld",&n,&l,&h);
		for(int i=0;i<n;++i)
			scanf("%lld",&f[i]);
		long long lcm=f[0];
		for(int i=1;i<n;++i) {
			long long d=gcd(lcm,f[i]);
			if(!mul(lcm/d,f[i],lcm))
				break;
		}
		ans=h+1;
		if(lcm<=h) {
			if(lcm<l) {
				long long cur=(l/lcm)*lcm;
				if(cur<l) cur+=lcm;
				if(cur<=h) ans=cur;
			}
			else ans=lcm;
		}
		for(int i=0;i<n;++i) {
			int cnt=factor(f[i],divz);
			std::sort(divz,divz+cnt);
			m=1;
			divs[0]=divz[0];
			count[0]=1;
			for(int j=1;j<cnt;++j) {
				if(divz[j]==divz[j-1]) {
					++count[m-1];
				}
				else {
					divs[m]=divz[j];
					count[m++]=1;
				}
			}
			go(0,1);
		}
		printf("Case #%d: ",test);
		if(ans>h) printf("NO\n");
		else printf("%lld\n",ans);
	}
	return 0;
}

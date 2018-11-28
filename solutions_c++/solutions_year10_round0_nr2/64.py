#include <iostream>
#include <sstream>
using namespace std;
#define REP(i,n) for (int i=0; i<(n); ++i)
typedef long long LL;
const LL MX=1000000000LL;
const int LEN=16;
struct INT {
	int d[LEN];
	INT operator-() {
		REP(i,LEN) d[i]=MX-1-d[i];
		bool r=true;
		for (int i=0; i<LEN&&r; ++i) {
			++d[i];
			r=d[i]>=MX;
			if (r) d[i]=0;
		}
		return *this;
	}
	INT(LL n=0) {
		memset(d,0,sizeof(d));
		bool plus=n>=0;
		if (!plus) n=-n;
		for (int i=0; n; ++i) d[i]=n%MX,n/=MX;
		if (!plus) *this=-*this;
	};
	int &operator[](int id) {return d[id];}
	void operator+=(LL n) {LL r=n; for(int i=0;r;++i) r+=d[i],d[i]=r%MX,r/=MX; }
	void operator*=(LL n) {LL r=0; REP(i,LEN){r+=d[i]*n;d[i]=r%MX;r/=MX;}}
	INT(char *s) {
		memset(d,0,sizeof(d));
		bool plus=true;
		if (s[0]=='+') ++s;
		else if (s[0]=='-') ++s, plus=false;
		for(int i=0;s[i];++i) *this*=10,*this+=s[i]-'0';
		if (!plus) *this=-*this;
	}
};

int t1,t0,n,k;    
INT a[1010];

bool operator==(INT n1, INT n2)
{
	for (int i=LEN-1; i>=0; --i) if (n1[i]!=n2[i]) return false;
	return true;
}
bool operator<(INT n1, INT n2)
{
	if (n1[LEN-1]>=MX/2!=n2[LEN-1]>=MX/2) return n1[LEN-1]>=MX/2;
	for (int i=LEN-1; i>=0; --i) if (n1[i]!=n2[i]) return n1[i]<n2[i];
	return false;
}
bool operator<=(INT n1, INT n2)
{
	if (n1[LEN-1]>=MX/2!=n2[LEN-1]>=MX/2) return n1[LEN-1]>=MX/2;
	for (int i=LEN-1; i>=0; --i) if (n1[i]!=n2[i]) return n1[i]<n2[i];
	return true;
}
void output(INT n)
{

	if (n<0LL) {printf("-"); output(-n); return;}
	int id=LEN-1;
	while (id&&n[id]==0) --id;
	printf("%d", n[id]);
	while (id) printf("%09d", n[--id]);
	printf("\n");
}
INT operator+(INT n1, INT n2)
{
	INT n;
	int r=0;
	REP(i,LEN) {
		n[i]=n1[i]+n2[i]+r;
		r=n[i]>=MX;
		if (r) n[i]-=MX;
	}
	return n;
}
INT operator-(INT n1, INT n2)
{
	INT n;
	int r=0;
	REP(i,LEN) {
		n[i]=n1[i]-r-n2[i];
		r=n[i]<0;
		if (r) n[i]+=MX;
	}
	return n;
}
INT operator*(INT n1, int n2)
{
	LL r=0, m=n2;
	INT n;
	REP(i,LEN) {
		r+=n1[i]*m;
		n[i]=r%MX;
		r/=MX;
	}
	return n;
}
INT operator/(INT n1, int n2)
{
	LL r=0, m=n2;
	INT n;
	for (int i=LEN-1; i>=0; --i) {
		r=r*MX+n1[i];
		n[i]=r/m;
		r%=m;
	}
	return n;
}
int operator%(INT n1, int n2)
{
	LL r=0, m=n2;
	for (int i=LEN-1; i>=0; --i) r=(r*MX+n1[i])%m;
	return r;
}
INT operator*(INT n1, INT n2)
{
	INT n;
	REP(i,LEN) REP(j,LEN-i) {
		int k=i+j;
		LL r=(LL)n1[i]*n2[j]+n[k];
		while (k<LEN&&r) {
			n[k]=r%MX;
			++k;
			r=r/MX+n[k];
		}
	}
	return n;
}
int hp_check(const INT &n1, const INT &n2)
{
	int l=0, u=MX-1;
	while (l!=u) {
		int m=(u-l+1)/2+l;
		if (n2*m<=n1) l=m;
		else u=m-1;
	}
	return l;
}
INT operator/(INT n1, INT n2)
{
	bool plus=true;
	if (n1<0LL) plus=!plus,n1=-n1;
	if (n2<0LL) plus=!plus,n2=-n2;
	INT n, r;
	for (int i=LEN-1; i>=0; --i) {
		r=r*MX+n1[i];
		n[i]=hp_check(r, n2);
		r=r-n2*n[i];
	}
	if (!plus) n=-n;
	return n;
}
INT operator%(INT n1, INT n2)
{
	bool plus=true;
	if (n1<0LL) plus=!plus,n1=-n1;
	if (n2<0LL) n2=-n2;
	INT n, r;
	for (int i=LEN-1; i>=0; --i) {
		r=r*MX+n1[i];
		n[i]=hp_check(r, n2);
		r=r-n2*n[i];
	}
	if (!plus) r=-r;
	return r;
}


INT gcd(INT a,INT b)
{
        if (a==0LL) return b;
        if (b==0LL) return a;
        return gcd(b%a,a);
}
int main()
{
    freopen("b2.in","r",stdin);
    freopen("b2.out","w",stdout);
     scanf("%d",&t1);
     char s[51];
    for (int t0=1;t0<=t1;t0++)
    {
        scanf("%d",&n);
        INT  t(0LL);
        cin>>s ;
        INT tmp1(s);
        for (int i=2;i<=n;i++) 
        {
            cin>>s;
            INT tmp(s);
            //output(tmp);
            tmp=tmp-tmp1;
            if (tmp<0LL) tmp=-tmp;
           // output(tmp);
            t=gcd(tmp,t);
        }
      //  output(t);
        printf("Case #%d: ",t0);
        output((t-tmp1%t)%t);
//        printf("\n");
    }
}

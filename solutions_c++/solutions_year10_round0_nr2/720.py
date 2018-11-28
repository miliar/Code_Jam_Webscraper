#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <set>
#include <map>
#include <queue>

using namespace std;

#define pb push_back
#define FOR(i,a,b) for(int i=a; i<=b; ++i)
#define REP(i,b) for(int i=0; i<b; i++)


typedef long long ll;
typedef vector<int> vint;
typedef pair<int,int> pii;

class Longnum {
    public:
      int s,len;
      vector<short int> nu;
             void clear()
             { s=1; len=0; nu.resize(2); }
             void write(){ 
                  if (s==-1) printf("-");
                  for (int i=len;i>0;i--) printf("%d",nu[i]); 
                  if (len==0) printf("0"); 
                  printf("\n"); 
             }
             
             friend Longnum chtolong(string c);
             friend int compabs(const Longnum &a, const Longnum &b);
             friend void sumabs(const Longnum &a, const Longnum &b, Longnum &c);
             friend void difabs(const Longnum &a, const Longnum &b, Longnum &c);
             friend void difabs(Longnum &a, const Longnum &b);
             friend void mulabs(const Longnum &a, const Longnum &b, Longnum &c);
             friend void shift(Longnum &a);
             friend void divabs(const Longnum &a, const Longnum &b, Longnum &c, Longnum &d);
             friend Longnum operator + (const Longnum &a, const Longnum &b);
             friend Longnum operator - (const Longnum &a, const Longnum &b);
             
             friend Longnum operator % (const Longnum &a, const Longnum &b);
                                                     
};

Longnum chtolong(string c){
        Longnum a;
        a.clear();
        while (c[a.len]!=0) a.len++;
        a.nu.resize(a.len+2);
        FOR(i,1,a.len+1)
                        a.nu[i]=c[a.len-i]-'0';
        while (a.len>0 && a.nu[a.len]==0) a.len--;
        return a;
}

int compabs(const Longnum &a, const Longnum &b){
    if (a.len<b.len) return 1;
    if (a.len>b.len) return -1;
    int i=a.len;
    while (i>0 && a.nu[i]==b.nu[i]) i--;
    if (i==0) return 0;
    if (a.nu[i]<b.nu[i]) return 1; 
    else return -1;
}

void sumabs(const Longnum &a, const Longnum &b, Longnum &c){
     c.clear();
     c.len=max(a.len,b.len);
     c.nu.resize(c.len+2);
     FOR(i,1,c.len+1){
                  if (i<=a.len)  c.nu[i]+=a.nu[i];
                  if (i<=b.len)  c.nu[i]+=b.nu[i];
                  if (c.nu[i]>9) { c.nu[i]-=10; c.nu[i+1]++; }
     }
     if (c.nu[c.len+1]>0) c.len++;
     c.nu.resize(c.len+2);
}

void difabs(const Longnum &a, const Longnum &b, Longnum &c){
     c.clear();
     c.len=max(a.len,b.len);
     c.nu.resize(c.len+2);
     FOR(i,1,c.len+1){    
                  if (i<=a.len)  c.nu[i]+=a.nu[i];
                  if (i<=b.len)  c.nu[i]-=b.nu[i];
                  if (c.nu[i]<0) { c.nu[i]+=10; c.nu[i+1]--; }
     }
     while (c.len>0 && c.nu[c.len]==0) c.len--;
     c.nu.resize(c.len+2);
}

void difabs(Longnum &a, const Longnum &b){
     FOR(i,1,a.len+1){
                  if (i<=a.len && i<=b.len) a.nu[i]-=b.nu[i];
                  if (a.nu[i]<0) { a.nu[i]+=10; a.nu[i+1]--; }
     }
     while (a.len>0 && a.nu[a.len]==0) a.len--;
     a.nu.resize(a.len+2);
}

void mulabs(const Longnum &a, const Longnum &b, Longnum &c){
     c.clear();
     c.len=a.len+b.len;
     c.nu.resize(c.len+2);
     FOR(i,1,a.len+1)
        FOR(j,1,b.len+1){
                         c.nu[i+j-1]+=a.nu[i]*b.nu[j];
                         if (c.nu[i+j-1]>9)
                         { c.nu[i+j]+=c.nu[i+j-1]/10; c.nu[i+j-1]%=10; }
        }
     while (c.len>0 && c.nu[c.len]==0) c.len--;
     c.nu.resize(c.len+2);
}

void shift(Longnum &a){
     for (int i=a.len;i>0;i--)
         a.nu[i+1]=a.nu[i];
     a.nu[1]=0;
     a.len++;
     while (a.len>0 && a.nu[a.len]==0) a.len--;
     a.nu.resize(a.len+2);
}

void divabs(const Longnum &a, const Longnum &b, Longnum &c, Longnum &d){
     c.clear();
     c.len=a.len;
     c.nu.resize(c.len+2);
     d.clear();
     for (int i=a.len;i>0;i--){
         shift(d);
         d.nu[1]=a.nu[i];
         if (d.len==0 && d.nu[1]!=0) { d.len=1; d.nu.resize(d.len+2); }
         while (compabs(d,b)<=0){
               difabs(d,b);
               c.nu[i]++;
         }
     }
     while (c.len>0 && c.nu[c.len]==0) c.len--;
     c.nu.resize(c.len+2);
}

Longnum operator + (const Longnum &a, const Longnum &b){
         Longnum c;
         c.clear();
         if (a.s==b.s){
                       sumabs(a,b,c); 
                       c.s=a.s;
                       return c;
         }
         int x=compabs(a,b);
         if (x==0) return c;
         if (x==1){
                   difabs(b,a,c);
                   c.s=b.s;
                   return c;
         }
         if (x==-1){
                   difabs(a,b,c);
                   c.s=a.s;
                   return c;
         }
}

Longnum operator - (const Longnum &a, const Longnum &b){
         Longnum c;
         c=b;
         if (c.len>0) c.s=-c.s;
         return a+c;
}
         
Longnum operator * (const Longnum &a, const Longnum &b){
         Longnum c;
         mulabs(a,b,c);
         c.s=a.s*b.s;
         if (c.len==0) c.s=1;
         return c;
}

Longnum operator / (const Longnum &a, const Longnum &b){
         Longnum c,d;
         divabs(a,b,c,d);
         c.s=a.s*b.s;
         if (c.len==0) c.s=1;
         if (d.len==0 || a.s>0) return c;
         if (b.s>0) c=c-chtolong("1");
         else c=c+chtolong("1");
         return c;         
}

Longnum operator % (const Longnum &a, const Longnum &b){
         Longnum c,d;
         divabs(a,b,c,d);
         d.s=1;
         if (d.len==0 || a.s>0) return d;
         Longnum e=b;
         e.s=1;
         d=e-d;
         return d;         
}

bool operator == (const Longnum &a, const Longnum &b){
     if (a.len!=b.len || a.s!=b.s) return 0;
     FOR(i,1,a.len+1)
                     if (a.nu[i]!=b.nu[i]) return 0;
     return 1;
}

Longnum gcd(Longnum a, Longnum b)
{
    Longnum  r1=a, r2=b,r3;
	while (r2.len)
	{
        r3=r1%r2;
        r1=r3;
		//r1.write(); cout << "len" << r1.len << endl;  r2.write(); 
        swap(r1,r2);
        //r1.write();   r2.write(); 
        //cout << "len" << r2.len << endl;
	}
	//printf("GCD\n");
	return r1;
}

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int c,n;
	Longnum a[1001],b[1001];
	scanf("%d",&c);
	string s;
    FOR(r,1,c)
	{
        scanf("%d",&n);
        FOR(i,1,n) { cin>>s; a[i]=chtolong(s); }
        FOR(i,1,n-1) { b[i]=a[i]-a[i+1]; b[i].s=1; /*b[i].write();*/ }
        //printf("\n");
        FOR(i,1,n-2) 
            b[n-1]=gcd(b[i],b[n-1]);
        a[1]=a[1]%b[n-1];
        if (! a[1].len==0) a[1]=b[n-1]-a[1];
        printf("Case #%d: ",r);
        a[1].write();
        
    }
	return 0;
}

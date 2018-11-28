#include<iostream>
#include<algorithm> 

using namespace std;

const int Maxd = 1000;
const int Base = 100000000;   
const int Baselen = 8;

typedef long long Tdata; 

struct bigint
{
   Tdata d[Maxd];    
   int len;
   void clear()
   {
       len = 0;  d[0] = 0;  
   }
   void zero()
   {
       len = 1;  d[0] = 0;  
   }
   bigint() { zero(); }
   bigint(Tdata x)
   {   
       clear();    
       for (;x > 0;x /= Base)
         d[len++] = x % Base;
       if (0 == len) zero();   
   }
   Tdata  operator [] (int index) const {return d[index];};
   Tdata& operator [] (int index) {return d[index];}; 
   void print();
};


bigint operator + (const bigint &A,const bigint &B)
{
     bigint R;
     int i;
     Tdata Carry = 0;
     for (i = 0; i < A.len || i < B.len || Carry > 0; i++)
     {
         if (i < A.len) Carry += A[i];
         if (i < B.len) Carry += B[i];
         R[i] = Carry % Base;
         Carry /=Base;
     }
     R.len = i;
     return R;
}

//bigint Óë Tdata Ïà³Ë 
bigint operator * (const bigint &A,const Tdata &B)
{
     bigint R;
     if (0 == B) return R;
     R.len = A.len;
     Tdata Carry = 0;
     for (int i = 0; i < A.len; i++) 
     {
        R[i] = A[i] * B + Carry;        
        Carry = R[i] / Base;
        R[i] %= Base;
     }
     if (Carry) R[R.len++] = Carry;
     return R;
}

void bigint::print()
{
     printf("%I64d",d[len - 1]);
     for (int i = len - 2; i >= 0; i--)
        printf("%08I64d",d[i]);       
     printf("\n");  
}

char s[10000];
int r[300];
int len,n;

void init()
{
    memset(r,0,sizeof(r));
    scanf("%s", s);
    len = strlen(s);
    n = 0;
    for (int i = 0; i < len ; i++)
       if (r[s[i]] == 0) r[s[i]] = ++n;
    bigint ret = 1;
    bigint ans = 0;
    if (n == 1 && len == 1)
    {
        printf("%d\n", 1);
        return;
    } else if (n == 1) n++;
    for (int i = len - 1; i >= 0 ; i--)
    {
        int k = r[s[i]];
        if (k == 2) k = 0;
          else if (k > 2) k--;
        ans = ans + ret * k;
        ret = ret * n; 
    }
    ans.print();
}

int main()
{
//    freopen("test.in","r",stdin);
//    freopen("test.out","w",stdout);
    int Case;
    scanf("%d", &Case);
    for (int i = 1; i <= Case ; i++)
    {
        printf("Case #%d: ",i);
        init();
    }
    return 0;
}

#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>

using namespace std;

int n,l,w;
int r[5000];
int v[5000];
int id[5000];

struct dtype
{
    int a,b;
};

dtype ans[5000];

int canputa(int r,int a1,int a2,int& aa)
{
    if (a1!=0 && a2!=w && r*2>a2-a1) return 0;
    if (a1!=0 && a2==w && r>a2-a1) return 0;
    if (a1==0 && a2!=w && r>a2-a1) return 0;
    if (a1==0) aa=0;else aa=a1+r;
    return 1;
}
int canputb(int r,int a1,int a2,int& aa)
{
    if (a1!=0 && a2!=l && r*2>a2-a1) return 0;
    if (a1!=0 && a2==l && r>a2-a1) return 0;
    if (a1==0 && a2!=l && r>a2-a1) return 0;
    if (a1==0) aa=0;else aa=a1+r;
    return 1;
}



void solve(dtype d1,dtype d2)
{
    if (d2.a<d1.a) return;
    if (d2.b<d1.b) return;
    if (d2.a>w) d2.a=w;
    if (d2.b>l) d2.b=l;
    for (int i=0;i<n;i++) if (v[i]==0)
    {
        int aa,bb;
        if (canputa(r[i],d1.a,d2.a,aa) && canputb(r[i],d1.b,d2.b,bb))
        {
            
            v[i]=1;ans[i].a=aa;ans[i].b=bb;
            dtype tmp1,tmp2,tmp3,tmp4,tmp5;
            tmp1.a=aa+r[i];tmp1.b=d1.b;
            tmp2.a=aa+r[i];tmp2.b=bb+r[i];
            tmp3.a=d1.a;tmp3.b=bb+r[i];
            
            tmp4.a=d2.a;tmp4.b=bb+r[i];
            tmp5.a=aa+r[i];tmp5.b=d2.b;
            
            
            if (d2.b-bb+r[i]<d2.a-aa+r[i])
            {
                solve(tmp3,tmp5);
                solve(tmp1,d2);
            }
            else
            {
                solve(tmp1,tmp4);
                solve(tmp3,d2);
            }
        }
        break;
    }
}


               
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("cb2.out","w",stdout);
    int NT,CT=0;
    cin >> NT;
    while(NT)
    {
        NT--;CT++;
        
        cin >> n >> l >> w;
        
        for (int i=0;i<n;i++) cin >> r[i];
        for (int i=0;i<n;i++) id[i]=i;
        for (int i=0;i<n;i++) for (int j=i;j<n;j++) if (r[i]<r[j])
        {
            int tmp=r[i];r[i]=r[j];r[j]=tmp;
            tmp=id[i];id[i]=id[j];id[j]=tmp;
        }
        
        memset(v,0,sizeof v);
        
        dtype tmp1,tmp2;
        tmp1.a=0;tmp1.b=0;
        tmp2.a=w;tmp2.b=l;
        
        solve(tmp1,tmp2);
        
            printf("Case #%d:",CT); 
            
        for (int i=0;i<n;i++) for (int j=i;j<n;j++) if (id[i]>id[j])
        {
            int tmp=id[i];id[i]=id[j];id[j]=tmp;
            dtype t = ans[i];ans[i]=ans[j];ans[j]=t;
        }       
        
        for (int i=0;i<n;i++)
        {
            printf(" %d %d",ans[i].b,ans[i].a);

            
            
        }
        printf("\n");
    }
}
        

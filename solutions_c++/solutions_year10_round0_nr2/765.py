#include<stdio.h>
#include<string.h>
struct array {int a[51];};

char s[100];
int n,m,i,j,k,l,t,tt;
array a[1001];

int comp(array a,array b)
{
     if (a.a[0]<b.a[0]) {return 0;}
     if (a.a[0]>b.a[0]) {return 1;}
     int i=a.a[0];
     while (i>0)
     {
           if (a.a[i]>b.a[i]) {return 1;}
           if (a.a[i]<b.a[i]) {return 0;}
           i--;
     }
     return 2;
}

void swap(array &a,array &b)
{
     array c;
     c=a;a=b;b=c;
}

void sort(int l,int r)
{
     int i,j;
     array mid;
     i=l;
     j=r;
     mid=a[(l+r)/2];
     do
     {
        while (comp(a[i],mid)==0) {i++;}
        while (comp(mid,a[j])==0) {j--;}
        if (i<=j)
        {
                 swap(a[i],a[j]);
                 i++;
                 j--;
        }
     } while (i<=j);
     if (l<j) {sort(l,j);}
     if (i<r) {sort(i,r);}
}

array minus(array a,array b)
{
      array c;
      int i,j,k,l;
      for (i=0;i<=50;i++) {c.a[i]=0;}
      for (i=1;i<=b.a[0];i++)
      {
          c.a[i]=a.a[i]-b.a[i];
          if (c.a[i]<0) {c.a[i]+=10;a.a[i+1]--;}
          j=i+1;
          while ((j<a.a[0])&&(a.a[j]<0)) {a.a[j]+=10;a.a[j+1]--;j++;}
      }
      for (i=b.a[0]+1;i<=a.a[0];i++) {c.a[i]=a.a[i];}
      c.a[0]=a.a[0];
      while ((c.a[c.a[0]]==0)&&(c.a[0]!=0)) {c.a[0]--;}
      return c;
}

void divi(array a,array b,array &d)
{
     int i,j,k,l;
     for (i=0;i<=50;i++) {d.a[i]=0;}
     for (i=a.a[0];i>0;i--)
     {
         for (j=d.a[0]+1;j>1;j--) {d.a[j]=d.a[j-1];}
         d.a[0]++;d.a[1]=a.a[i];
         if ((d.a[0]==1)&&(d.a[1]==0)) {d.a[0]=0;}
         while (comp(b,d)!=1) {d=minus(d,b);}
     }
     
}

array gcd(array a,array b)
{
      array d;
      if (b.a[0]==0) {return a;}
      else
      {
          divi(a,b,d);
          return gcd(b,d);
      }
}

int main()
{
    freopen("3.in","r",stdin);
    freopen("3.out","w",stdout);
    scanf("%d",&tt);
    for (t=1;t<=tt;t++)
    {
        printf("Case #%d: ",t);
        scanf("%d",&n);
        for (i=1;i<=n;i++) 
        {
            scanf("%s",&s);
            l=strlen(s);
            a[i].a[0]=l;
            for (j=l-1;j>=0;j--) {a[i].a[l-j]=s[j]-'0';}
        }
        sort(1,n);
        
        for (i=2;i<=n;i++) {a[i]=minus(a[i],a[1]);}
        array c;
        c=a[2];
        for (i=3;i<=n;i++) {c=gcd(a[i],c);}
        array e;
        divi(a[1],c,e);
        if (e.a[0]!=0) {e=minus(c,e);}
        for (i=e.a[0];i>0;i--) {printf("%d",e.a[i]);}
        if (e.a[0]==0) {printf("0");}
        printf("\n");
    }
    
    return 0;
}

#include <iostream>

using namespace std;

struct bigint
{
       int size,a[105];
       bigint() {size=1;memset(a,0,sizeof(a));}
       void put()
       {
            for (int i=size;i>=1;i--)
                cout<<a[i];
            cout<<endl;
       }
       bool odd() {return a[1]%2;}
       void getin()
       {
            char ch=' ';
            while (ch==' ') scanf("%c",&ch);
            size=0;memset(a,0,sizeof(a));
            while (ch>='0' && ch<='9')
            {
                  a[++size]=ch-'0';
                  scanf("%c",&ch);
            }
            for (int i=1;i<=size/2;i++) swap(a[i],a[size-i+1]);
       }
}A[1005],Tmp[100];

bigint operator -(bigint a,bigint b)
{
       int tw=0,ans;
       for (int i=1;i<=a.size;i++)
       {
           ans=a.a[i]-tw-b.a[i];
           if (ans<0) {tw=1;ans+=10;}
           else tw=0;
           b.a[i]=ans;
       }
       b.size=a.size;
       while (b.size>1 && !b.a[b.size]) b.size--;
       return b;
}

bigint operator +(bigint a,bigint b)
{
       int jw=0,ans;
       for (int i=1;i<=max(a.size,b.size);i++)
       {
           ans=a.a[i]+jw+b.a[i];
           if (ans>9) {jw=1;ans-=10;}
           else jw=0;
           b.a[i]=ans;
       }
       b.size>?=a.size;
       if (jw!=0) b.a[++b.size]=jw;
       return b;
}

bigint operator /(bigint a,int b)
{
       for (int i=a.size;i>=1;i--) {a.a[i-1]+=a.a[i]%b*10;a.a[i]/=b;}
       a.a[0]=0;
       if (!a.a[a.size]) a.size--;
       if (a.size==0) a.size=1;
       return a;
}

bool operator >(bigint a,bigint b)
{
     if (a.size>b.size) return true;
     if (a.size<b.size) return false;
     for (int i=a.size;i>=1;i--)
         if (a.a[i]>b.a[i]) return true;
         else if (a.a[i]<b.a[i]) return false;
     return false;
}

bool operator <=(bigint a,bigint b)
{
     return !(a>b);
}

bool operator ==(bigint a,bigint b)
{
     if (a.size!=b.size) return false;
     for (int i=1;i<=a.size;i++)
         if (a.a[i]!=b.a[i]) return false;
     return true;
}

bigint gcd(bigint a,bigint b)
{
       //a.put();b.put();
       if (a.size==1 && a.a[1]==0) return b;
       if (b.size==1 && b.a[1]==0) return a;
       if (a.odd())
          if (b.odd())
             if (a>b) return gcd(a-b,b);
             else return gcd(a,b-a);
          else return gcd(a,b/2);
       else if (b.odd()) return gcd(a/2,b);
            else {
                     bigint t=gcd(a/2,b/2);
                     return t+t;
                 }
}

int N,T;

int main(){
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    cin>>T;
    for (int i=1;i<=T;i++)
    {
        int N;
        scanf("%d",&N);
        bigint s;
        for (int j=1;j<=N;j++) 
        {
            A[j].getin();
            if (j!=1) 
               if (j==2) 
                  if (A[j]>A[j-1]) s=A[j]-A[j-1];
                  else s=A[j-1]-A[j];
               else if (A[j]>A[j-1]) s=gcd(s,A[j]-A[j-1]);
                    else s=gcd(s,A[j-1]-A[j]);
            //cout<<"******\n";
        }
        Tmp[0]=s;
        bigint res;
        for (int j=1;j<=100;j++)
        {
            Tmp[j]=Tmp[j-1]+Tmp[j-1];
            if (Tmp[j]>A[1]) 
            {
                for (int k=j-1;k>=0;k--)
                    if (Tmp[k]+res<=A[1]) res=res+Tmp[k];
                break;
            }
        }
        if (res==A[1]) cout<<"Case #"<<i<<": 0\n";
        else {
                 bigint ans=s-(A[1]-res);
                 cout<<"Case #"<<i<<": ";ans.put();
             }
    }
    return 0;
}

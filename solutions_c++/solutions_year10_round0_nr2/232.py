#include<fstream>
#include<cstring>

using namespace std;

const char iname[]="B.in";
const char oname[]="B.out";
const int maxn=1005;
const int maxc=160;

ifstream f(iname);
ofstream g(oname);

void add(int A[], int B[])
{
      int i, t = 0;
      for (i=1; i<=A[0] || i<=B[0] || t; i++, t/=10)
              A[i] = (t += A[i] + B[i]) % 10;
      A[0] = i - 1;
}

void mul(int A[], int B[])
{
      int i, j, t, C[maxc];
      memset(C, 0, sizeof(C));
      for (i = 1; i <= A[0]; i++)
      {
              for (t=0, j=1; j <= B[0] || t; j++, t/=10)
                      C[i+j-1]=(t+=C[i+j-1]+A[i]*B[j])%10;
              if (i + j - 2 > C[0]) C[0] = i + j - 2;
      }
      memcpy(A, C, sizeof(C));
}

void sub(int A[], int B[])
{
      int i, t = 0;
      for (i = 1; i <= A[0]; i++)
              A[i] += (t = (A[i] -= ((i <= B[0]) ? B[i] : 0) + t) < 0) * 10;
      for (; A[0] > 1 && !A[A[0]]; A[0]--);
}

int cmp(int A[],int B[])
{
    if(A[0]<B[0])
        return -1;
    if(B[0]<A[0])
        return 1;
    for(int i=A[0];i;--i)
        if(A[i]<B[i])
            return -1;
        else
            if(A[i]>B[i])
                return 1;
    return 0;
}

void mul(int A[], int B)
{
      int i, t = 0;
      for (i = 1; i <= A[0] || t; i++, t /= 10)
              A[i] = (t += A[i] * B) % 10;
      A[0] = i - 1;
}

void div(int A[], int B)
{
      int i, t = 0;
      for (i = A[0]; i > 0; i--, t %= B)
              A[i] = (t = t * 10 + A[i]) / B;
      for (; A[0] > 1 && !A[A[0]]; A[0]--);
}

void mod(int A[],int B[])
{
    int step[maxc],ans[maxc];
    memset(step,0,sizeof(step));
    memset(ans,0,sizeof(ans));
    step[0]=step[1]=1;
    for(;cmp(step,A)==-1;mul(step,2));
    for(ans[0]=1;step[0]!=1||step[1]!=0;div(step,2))
    {
        add(ans,step);
        if(cmp(ans,A)==1)
        {
            sub(ans,step);
            continue;
        }
        int aux[maxc];
        memset(aux,0,sizeof(aux));
        aux[0]=1;
        add(aux,ans);
        mul(aux,B);
        if(cmp(aux,A)==1)
            sub(ans,step);
    }
    mul(ans,B);
    sub(A,ans);
}


void cmmdc(int A[],int B[])
{
    if(B[1]==0&&B[0]==1)
        return;
    int C[maxc],auxB[maxc];
    memset(C,0,sizeof(C));
    memset(auxB,0,sizeof(auxB));
    C[0]=1;
    auxB[0]=1;
    add(auxB,B);
    add(C,A);
    mod(C,auxB);
    cmmdc(auxB,C);
    memset(A,0,sizeof(C));
    for(int i=0;i<=auxB[0];++i)
        A[i]=auxB[i];
}

int cmmdc(int a,int b)
{
    if(b==0)
        return a;
    return cmmdc(b,a%b);
}
long long test2(long long indice)
{
    long long n,i,j;
    long long a[maxn],ans,base;

    f>>n;
    for(i=1;i<=n;++i)
        f>>a[i];
    a[n+1]=a[1];
    base=a[1];
    for(i=1;i<=n;++i)
        a[i]=max(a[i+1]-a[i],a[i]-a[i+1]);
    if(indice==246)
    {
        for(i=1;i<=n;++i)
            g<<a[i]<<"\n";
    }
    for(i=2;i<=n;++i)
        a[1]=cmmdc(a[1],a[i]);
    if(indice==246)
    {
        g<<a[1]<<"\n";
    }
    long long rez=base%a[1];
    if(indice==246)
    {
        g<<rez<<"\n";
    }
    rez=a[1]-rez;
    if(rez==a[1])
        rez=0;
    g<<"Case #"<<indice<<": "<<rez<<"\n";
}

void show(int A[])
{
    for(int i=A[0];i;--i)
        g<<A[i];
    g<<"\n";
}
int test(int indice)
{
    int n,i,j;
    if(indice==246)
    {
        indice+=1;
        indice-=1;
    }
    char s[maxc];
    int a[maxn][maxc],base[maxc],step[maxc],ans[maxc];
    memset(a,0,sizeof(a));
    memset(base,0,sizeof(base));

    f>>n;
    for(i=1;i<=n;++i)
    {
        for(j=0;j<maxc;++j)
            s[j]=0;
        f>>s;
        if(s[j-1]=='\n')
            --j;
        for(j=0;s[j];++j);
        for(--j;j>=0;--j)
            a[i][++a[i][0]]=s[j]-'0';
    }

    a[n+1][0]=1;
    base[0]=1;
    add(base,a[1]);
    add(a[n+1],a[1]);
    for(i=1;i<=n;++i)
        if(cmp(a[i],a[i+1])==1)
            sub(a[i],a[i+1]);
        else
        {
            int aux[maxc];
            memset(aux,0,sizeof(aux));
            aux[0]=1;
            add(aux,a[i+1]);
            sub(aux,a[i]);
            memset(a[i],0,sizeof(a[i]));
            for(j=0;j<=aux[0];++j)
                a[i][j]=aux[j];
        }
    if(indice==246)
    {
        for(i=1;i<=n;++i)
            show(a[i]);
    }

    for(i=2;i<=n;++i)
        cmmdc(a[1],a[i]);

    if(indice==246)
    {
        show(a[1]);
    }

    memset(ans,0,sizeof(ans));
    ans[0]=1;
    add(ans,base);
    mod(ans,a[1]);
    if(indice==246)
    {
        show(ans);
    }
    if(ans[0]!=1||ans[1]!=0)
        sub(a[1],ans);
    else
        a[1][0]=1,a[1][1]=0;

    g<<"Case #"<<indice<<": ";
    for(i=a[1][0];i;--i)
        g<<a[1][i];
    g<<"\n";
}

int main()
{
    int t,i;
    f>>t;
    for(i=1;i<=t;++i)
        test(i);
}

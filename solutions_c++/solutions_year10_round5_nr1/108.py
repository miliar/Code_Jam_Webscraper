#include <cstdio>
#include <vector>

using namespace std;

int d,k;
int D;
vector<int> in;

vector<int> primes;

inline int mulmod(int a,int b,int m)
{
    return (a*(long long)b)%m;
}

int pow(int a,int n,int m)
{
    if(a==0)
        return 0;
    if(n==0)
        return 1;
    if(n%2==0)
    {
        return pow(mulmod(a,a,m),n/2,m);
    }
    else
        return mulmod(a,pow(mulmod(a,a,m),n/2,m),m);
}

int inv(int x,int prim)
{
    return pow(x,prim-2,prim);
}

int tp(int prim)
{
    for(int i=0;i<k;i++)
        if(in[i]>=prim)
            return -1;
    int x = (in[1]-in[0]+prim)%prim;
    int y = (in[2]-in[1]+prim)%prim;
    if(x==0 && y!=0)
        return -1;
    int A;
    int B;
    if(x==0 && y==0)
    {
        A = 1;
        B = 0;
    }
    else if(x!=0 && y==0)
    {
        A = 0;
        B = in[1];
    }
    else
    {
        A = mulmod(y,inv(x,prim),prim);
        B = in[1]-mulmod(A,in[0],prim);
        B %= prim;
        B += prim;
        B %= prim;
    }
//    printf("A=%d, B=%d\n",A,B);
    for(int i=1;i<k;i++)
    {
        int x = in[i-1];
        x = mulmod(x,A,prim);
        x += B;
        x %= prim;
        if(x != in[i])
        {
//            printf("%d instead of %d\n",x,in[i]);
            return -1;
        }
    }
    int X = in[k-1];
    X = mulmod(X,A,prim);
    X += B;
    X %= prim;
    return X;

}

void tst()
{
    scanf("%d%d",&d,&k);
    D = 1;
    for(int i=0;i<d;i++)
        D*=10;
    in.resize(k);
    for(int i=0;i<k;i++)
        scanf("%d",&in[i]);

    if(k<3)
    {
        if(in[0]==in[1])
        {
            printf("%d\n",in[0]);
            return;
        }
        puts("I don't know.");
        return;
    }
    int guess=-1;
    for(int ip=0;ip<primes.size();ip++)
    {
        if(primes[ip]>=D)
            break;

        int test = tp(primes[ip]);
//        printf("for %d %d\n",primes[ip],test);

        if(test==-1)
            continue;

        if(guess==-1)
            guess = test;
        else if(guess != test)
        {
            puts("I don't know.");
            return;
        }
    }
    if(guess==-1)
    {
            puts("I don't know.");
            return;
    }
    printf("%d\n",guess);
}

int main()
{
    vector<bool> isprime(1000000,true);
    isprime[0]=isprime[1]=false;
    for(int i=2;i<isprime.size();i++)
        if(isprime[i])
        {
            primes.push_back(i);
            for(int j=2*i;j<isprime.size();j+=i)
                isprime[j]=false;
        }

    

    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        printf("Case #%d: ",i);
        tst();
    }
}

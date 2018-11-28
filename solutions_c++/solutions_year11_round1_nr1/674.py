#include <cstdio>
#include <algorithm>

using namespace std;

int gcd(int a,int b)
{
    while (a>0)
    {
        b=b%a;
        swap(a,b);
    }
    return b;
}

bool fnd(long long N,int Pd,int Pg)
{
    int k=gcd(Pd,100);
    int Wd=Pd/k,D=100/k,Ld=D-Wd;
    k=gcd(Pg,100);
    int Wg=Pg/k,G=100/k,Lg=G-Wg;
    int coeff = 1;
    if (Wg==0 && Wd!=0)
        return false;
    if (Wg!=0 && Wg<Wd && Wd/Wg+(Wd%Wg>0)>coeff)
        coeff = Wd/Wg+(Wd%Wg>0);
    if (Lg==0 && Ld!=0)
        return false;
    if (Lg!=0 && Lg<Ld && Ld/Lg+(Ld%Lg>0)>coeff)
        coeff = Ld/Lg+(Ld%Lg>0);
    if (G!=0 && G<D && D/G+(D%G>0)>coeff)
        coeff = D/G+(D%G>0);
    Wg*=coeff;
    G*=coeff;
    Lg*=coeff;
    if (D<=N)
        return true;
    return false;
}

int main()
{
    int T;
    scanf("%d",&T);
    for (int t=1;t<=T;++t)
    {
        printf("Case #%d: ",t);
        long long N;
        int Pd,Pg;
        scanf("%lld%d%d",&N,&Pd,&Pg);
        if (fnd(N,Pd,Pg))
            printf("Possible\n");
        else
            printf("Broken\n");
    }
    return 0;
}

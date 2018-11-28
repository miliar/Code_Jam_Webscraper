#include <cstdio>
#include <string>
#include <vector>

using namespace std;

const int BASE = 1000000000;
const int DIGS = 9;
const int LEN = 7;

struct liczba
{
    int t[LEN];
    int l;
    liczba() : l(1) { t[0]=0; };
    liczba(int m) : l(1) { t[0]=m; }
};

void wypisz(liczba& x)
{
    printf("%d",x.t[x.l-1]);
    for (int i=x.l-2; i>=0; --i) printf("%0*d",DIGS,x.t[i]);
}

void czytaj(liczba& x)
{
    char s[LEN*DIGS+1];
    scanf("%s",s);
    int j=strlen(s);
    if (j%DIGS==0) x.l=j/DIGS;
    else x.l=j/DIGS + 1;
    --j;
    for (int i=0; i<x.l; ++i)
    {
        x.t[i]=0;
        for (int k=max(0,j-DIGS+1); k<=j; ++k) x.t[i]=10*x.t[i]+(s[k]-'0');
        j-=DIGS;
    }
}

bool operator<(const liczba& x, const liczba& y)
{
    if (x.l<y.l) return true;
    if (x.l>y.l) return false;
    int i=x.l-1;
    while (i>=0 && x.t[i]==y.t[i]) --i;
    if (i<0) return false;
    if (x.t[i]<y.t[i]) return true;
    return false;
}

bool operator>(const liczba& x, const liczba& y)
{
    return y<x;
}

liczba operator+ (const liczba& x, const liczba& y)
{
    liczba z;
    z.l=min(x.l,y.l);
    int c=0;
    for (int i=0; i<z.l; ++i)
    {
        z.t[i]=(x.t[i]+y.t[i]+c)%BASE;
        c=(x.t[i]+y.t[i]+c)/BASE;
    }
    while (z.l<x.l)
    {
        z.t[z.l]=(x.t[z.l]+c)%BASE;
        c=(x.t[z.l]+c)/BASE;
        ++z.l;
    }
    while (z.l<y.l)
    {
        z.t[z.l]=(y.t[z.l]+c)%BASE;
        c=(y.t[z.l]+c)/BASE;
        ++z.l;
    }
    if (c>0)
    {
        z.t[z.l]=c;
        ++z.l;
    }
    return z;
}

liczba operator- (const liczba& x, liczba& y)
{
    liczba z;
    z.l=x.l;
    int c=0;
    for (int i=0; i<x.l; ++i)
    {
        if (i<y.l) z.t[i]=x.t[i]-y.t[i]+c;
        else z.t[i]=x.t[i]+c;
        if (z.t[i]<0)
        {
            z.t[i]+=BASE;
            c=-1;
        }
        else c=0;
    }
    while (z.l>1 && z.t[z.l-1]==0) --z.l;
    return z;
}

bool operator==(const liczba& x, int m)
{
    return x.l==1 && x.t[0]==m;
}

int operator% (const liczba& x, int y)
{
    long long z = static_cast<long long>(x.t[x.l-1])%y;
    for (int i=x.l-2; i>=0; --i) z=(z*BASE+x.t[i])%y;
    return static_cast<int>(z);
}

liczba operator*(const liczba& x, int y)
{
    liczba z;
    if (y==0)
    {
        z.l=1;
        z.t[0]=0;
        return z;
    }
    z.l=x.l;
    int c=0;
    for (int i=0; i<x.l; ++i)
    {
        z.t[i]=int((static_cast<long long>(x.t[i])*y+c)%BASE);
        c=int((static_cast<long long>(x.t[i])*y+c)/BASE);
    }
    while (c>0)
    {
        z.t[z.l]=c%BASE;
        c/=BASE;
        ++z.l;
    }
    return z;
}

liczba operator/(const liczba& x, int y)
{
    liczba z;
    int c=0;
    z.l=x.l;
    for (int i=x.l-1; i>=0; --i)
    {
        z.t[i]=int((static_cast<long long>(c)*BASE+static_cast<long long>(x.t[i]))/y);
        c=int((static_cast<long long>(c)*BASE+static_cast<long long>(x.t[i]))%y);
    }
    while (z.l>1 && z.t[z.l-1]==0) --z.l;
    return z;
}

liczba operator*(liczba x, liczba y)
{
    liczba z, zero(0);
    z=zero;
    while (y>zero)
    {
        if (y%2==1) z=z+x;
        x=x*2;
        y=y/2;
    }
    return z;
}

liczba operator/ (const liczba& x, const liczba& y)
{
    liczba pom,z;
    z.l=x.l-y.l+1;
    pom.l=y.l;
    for (int i=0; i<pom.l; ++i) pom.t[pom.l-i-1]=x.t[x.l-1-i];
    int i=x.l-y.l;
    while (i>=0)
    {
        int a=0,b=BASE-1;
        while (a<b)
        {
            int c=(a+b)/2 + 1;
            liczba aux=y*c;
            if (aux>pom) b=c-1;
            else a=c;
        }
        z.t[i]=a;
        liczba aux=y*a;
        pom=pom-aux;
        for (int j=pom.l-1; j>=0; --j) pom.t[j+1]=pom.t[j];
        ++pom.l;
        --i;
        if (i>=0) pom.t[0] = x.t[i];
    }
    while (z.l==0 && z.t[z.l-1]==0) --z.l;
    return z;
}

liczba operator% (const liczba& x, const liczba& y)
{
    liczba aux=x/y;
    liczba aux2=y*aux;
    return x-aux2;
}

liczba NWD(const liczba& a, const liczba& b)
{
    if (b==0) return a;
    return NWD(b,a%b);
}

liczba NWD(const vector<liczba>& V)
{
    liczba wynik(0);
    int size=V.size();
    for (int i=0; i<size; ++i) wynik=NWD(wynik,V[i]);
    return wynik;
}   

vector<liczba> V;

liczba a,b;

int main()
{       
    int C;
    scanf("%d",&C);
    for (int nr=1; nr<=C; ++nr)
    {
        int N;
        scanf("%d",&N);
        
        V.resize(N-1);
        czytaj(b);
		liczba first=b;
        
        for (int i=0; i<N-1; ++i)
        {
            a=b;
            czytaj(b);
            if (a>b) V[i]=a-b;
            else V[i]=b-a;
        }
        liczba gcd=NWD(V);
        liczba aux=first%gcd;
        liczba aux2=gcd-aux;
        liczba wynik=aux2%gcd;
		printf("Case #%d: ",nr);
		wypisz(wynik);
        printf("\n");
    }
    return 0;
}

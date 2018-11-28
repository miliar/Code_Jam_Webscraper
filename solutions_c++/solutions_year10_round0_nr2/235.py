#include <iostream>
#include <cstdlib>
#include <string>

using namespace std;

#define maxsize 100

struct hp
{
    int len;
    int s[maxsize+1];
};


void input(hp &a,string str)
{
    int i;
    while(str[0]=='0' && str.size()!=1)
        str.erase(0,1);
    a.len=(int)str.size();
    for(i=1;i<=a.len;++i)
        a.s[i]=str[a.len-i]-48;
    for (i=a.len+1;i<=maxsize;++i)
        a.s[i]=0;
}

void print(const hp &y)
{
    int i;
    for(i=y.len;i>=1;i--)
        cout<<y.s[i];
    printf("\n");
}

void plus(const hp &a,const hp &b,hp &c) //高精度加法c=a+b
{
    int i,len;
    for(i=1;i<=maxsize;i++) c.s[i]=0;
    if(a.len>b.len) len=a.len;
    else len=b.len;
    for(i=1;i<=len;i++)
    {
        c.s[i]+=a.s[i]+b.s[i];
        if(c.s[i]>=10)
        {
            c.s[i]-=10;
            c.s[i+1]++;
        }
    }
    if(c.s[len+1]>0) len++;
    c.len=len;
}

void subtract(const hp &a,const hp &b,hp &c) //高精度减法c=a-b
{
    int i,len;
    for(i=1;i<=maxsize;i++) c.s[i]=0;
    if(a.len>b.len) len=a.len;
    else len=b.len;
    for(i=1;i<=len;i++)
    {
        c.s[i]+=a.s[i]-b.s[i];
        if(c.s[i]<0)
        {
            c.s[i]+=10;
            c.s[i+1]--;
        }
    }
    while(len>1&&c.s[len]==0) len--;
    c.len=len;
}

int compare(const hp &a,const hp &b)
{
    int len;
    if(a.len>b.len) len=a.len;
    else len=b.len;
    while(len>0 && a.s[len]==b.s[len]) len--;
    if(len==0) return 0;
    else return a.s[len]-b.s[len];
}

void multiply(const hp &a,int b,hp &c) //高精度*单精度
{
    int i,len;
    for(i=1;i<=maxsize;i++) c.s[i]=0;
    len=a.len;
    for(i=1;i<=len;i++)
    {
        c.s[i]+=a.s[i]*b;
        c.s[i+1]+=c.s[i]/10;
        c.s[i]%=10;
    }
    len++;
    while(c.s[len]>=10)
    {
        c.s[len+1]+=c.s[len]/10;
        c.s[len]%=10;
        len++;
    }
    while(len>1&&c.s[len]==0) len--;
    c.len=len;
}

void multiplyh(const hp &a,const hp &b,hp &c) //高精度*高精度
{
    int i,j,len;
    for(i=1;i<=maxsize;i++) c.s[i]=0;
    for(i=1;i<=a.len;i++)
        for(j=1;j<=b.len;j++)
        {
            c.s[i+j-1]+=a.s[i]*b.s[j];
            c.s[i+j]+=c.s[i+j-1]/10;
            c.s[i+j-1]%=10;
        }
    len=a.len+b.len+1;
    while(len>1&&c.s[len]==0) len--;
    c.len=len;
}

void divide(const hp &a,int b,hp &c,int &d) //高精度/单精度 {d为余数}
{
    int i,len;
    for(i=1;i<=maxsize;i++) c.s[i]=0;
    len=a.len;
    d=0;
    for(i=len;i>=1;i--)
    {
        d=d*10+a.s[i];
        c.s[i]=d/b;
        d%=b;
    }
    while(len>1&&c.s[len]==0) len--;
    c.len=len;
}

void multiply10(hp &a)     //高精度*10
{
    int i;
    for(i=a.len;i>=1;i--)
        a.s[i+1]=a.s[i];
    a.s[1]=0;
    a.len++;
    while(a.len>1&&a.s[a.len]==0) a.len--;
}

void divideh(const hp &a,const hp &b,hp &c,hp &d)//高精度/高精度{d为余数}
{
    hp e;
    int i,len;
    for(i=1;i<=maxsize;i++)
    {
        c.s[i]=0;
        d.s[i]=0;
    }
    len=a.len;
    d.len=1;
    for(i=len;i>=1;i--)
    {
        multiply10(d);
        d.s[1]=a.s[i];
        while(compare(d,b)>=0)
        {
            subtract(d,b,e);
            d=e;
            c.s[i]++;
        }
    }
    while(len>1&&c.s[len]==0) len--;
    c.len=len;
}


hp zero;
string st_zero("0");
char buff[200];
int C , N;
hp t[2000];

hp gcd( hp &a , hp& b )
{
	if ( compare( b , zero ) == 0 ) return a;
	hp d;
	hp c;
	divideh( a , b , c , d );
	return gcd( b , d );
	
}


int main()
{
	int i , j , c;
	freopen("B-small.in" , "r" , stdin );
	freopen("B-small.out" , "w" , stdout );
	
	input( zero , st_zero );
	
	scanf("%d",&C);
	for( c = 1 ; c <= C ; c++ )
	{
		
		hp S;
		scanf("%d",&N);
		
		for( i = 1 ; i <= N ; i++ )
		{
			scanf("%s" ,buff);
			string stemp(buff);
			input( t[i] , stemp );
		}
		
		compare(t[1],t[2])>0?subtract( t[1] , t[2] , S ):subtract( t[2] , t[1]  , S );
		for( i = 2 ; i < N ; i++ )
		{
			hp tt;
			compare(t[i],t[i+1])>0?subtract( t[i] , t[i+1] , tt ):subtract( t[i+1] ,t[i]  , tt );
			S = gcd( S , tt );
		}
		hp resdiv , resd;
		divideh( t[1] , S , resdiv , resd );
		if( compare( resd , zero ) == 0 )
		{
			printf("Case #%d: 0\n" , c);
		}else
		{
			subtract( S , resd , resdiv );
			printf("Case #%d: " , c);
			print( resdiv );
			
		}
	}
	
	
}

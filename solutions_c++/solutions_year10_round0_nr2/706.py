#include <iostream>
#include <string.h>

#define DIGIT	4
#define DEPTH	10000
#define MAX     100
typedef int bignum_t[MAX+1];


using namespace std;
int read(bignum_t a,istream& is=cin){
	char buf[MAX*DIGIT+1],ch;
	int i,j;
	memset((void*)a,0,sizeof(bignum_t));
	if (!(is>>buf))	return 0;
	for (a[0]=strlen(buf),i=a[0]/2-1;i>=0;i--)
		ch=buf[i],buf[i]=buf[a[0]-1-i],buf[a[0]-1-i]=ch;
	for (a[0]=(a[0]+DIGIT-1)/DIGIT,j=strlen(buf);j<a[0]*DIGIT;buf[j++]='0');
	for (i=1;i<=a[0];i++)
		for (a[i]=0,j=0;j<DIGIT;j++)
			a[i]=a[i]*10+buf[i*DIGIT-1-j]-'0';
	for (;!a[a[0]]&&a[0]>1;a[0]--);
	return 1;
}

void write(const bignum_t a,ostream& os=cout){
	int i,j;
	for (os<<a[i=a[0]],i--;i;i--)
		for (j=DEPTH/10;j;j/=10)
			os<<a[i]/j%10;
}

int comp(const bignum_t a,const bignum_t b){
	int i;
	if (a[0]!=b[0])
		return a[0]-b[0];
	for (i=a[0];i;i--)
		if (a[i]!=b[i])
			return a[i]-b[i];
	return 0;
}

int comp(const bignum_t a,const int b){
	int c[12]={1};
	for (c[1]=b;c[c[0]]>=DEPTH;c[c[0]+1]=c[c[0]]/DEPTH,c[c[0]]%=DEPTH,c[0]++);
	return comp(a,c);
}

int comp(const bignum_t a,const int c,const int d,const bignum_t b){
	int i,t=0,O=-DEPTH*2;
	if (b[0]-a[0]<d&&c)
		return 1;
	for (i=b[0];i>d;i--){
		t=t*DEPTH+a[i-d]*c-b[i];
		if (t>0) return 1;
		if (t<O) return 0;
	}
	for (i=d;i;i--){
		t=t*DEPTH-b[i];
		if (t>0) return 1;
		if (t<O) return 0;
	}
	return t>0;
}


void add(bignum_t a,const bignum_t b){
	int i;
	for (i=1;i<=b[0];i++)
		if ((a[i]+=b[i])>=DEPTH)
			a[i]-=DEPTH,a[i+1]++;
	if (b[0]>=a[0])
		a[0]=b[0];
	else
		for (;a[i]>=DEPTH&&i<a[0];a[i]-=DEPTH,i++,a[i]++);
	a[0]+=(a[a[0]+1]>0);
}

void sub(bignum_t a,const bignum_t b){
	int i;
	for (i=1;i<=b[0];i++)
		if ((a[i]-=b[i])<0)
			a[i+1]--,a[i]+=DEPTH;
	for (;a[i]<0;a[i]+=DEPTH,i++,a[i]--);
	for (;!a[a[0]]&&a[0]>1;a[0]--);
}


void sub(bignum_t a,const int b){
	int i=1;
	for (a[1]-=b;a[i]<0;a[i+1]+=(a[i]-DEPTH+1)/DEPTH,a[i]-=(a[i]-DEPTH+1)/DEPTH*DEPTH,i++);
	for (;!a[a[0]]&&a[0]>1;a[0]--);
}

void sub(bignum_t a,const bignum_t b,const int c,const int d){
	int i,O=b[0]+d;
	for (i=1+d;i<=O;i++)
		if ((a[i]-=b[i-d]*c)<0)
			a[i+1]+=(a[i]-DEPTH+1)/DEPTH,a[i]-=(a[i]-DEPTH+1)/DEPTH*DEPTH;
	for (;a[i]<0;a[i+1]+=(a[i]-DEPTH+1)/DEPTH,a[i]-=(a[i]-DEPTH+1)/DEPTH*DEPTH,i++);
	for (;!a[a[0]]&&a[0]>1;a[0]--);
}


void mul(bignum_t c,const bignum_t a,const bignum_t b){
	int i,j;
	memset((void*)c,0,sizeof(bignum_t));
	for (c[0]=a[0]+b[0]-1,i=1;i<=a[0];i++)
		for (j=1;j<=b[0];j++)
			if ((c[i+j-1]+=a[i]*b[j])>=DEPTH)
				c[i+j]+=c[i+j-1]/DEPTH,c[i+j-1]%=DEPTH;
	for (c[0]+=(c[c[0]+1]>0);!c[c[0]]&&c[0]>1;c[0]--);
}

void cp(bignum_t a, bignum_t b)
{
    memcpy(a, b, sizeof(bignum_t));
}

void div(bignum_t c,bignum_t ta,const bignum_t b){
	int h,l,m,i;
	bignum_t a;
	cp(a, ta);
	memset((void*)c,0,sizeof(bignum_t));
	c[0]=(b[0]<a[0]+1)?(a[0]-b[0]+2):1;
	for (i=c[0];i;sub(a,b,c[i]=m,i-1),i--)
		for (h=DEPTH-1,l=0,m=(h+l+1)>>1;h>l;m=(h+l+1)>>1)
			if (comp(b,m,i-1,a)) h=m-1;
			else l=m;
	for (;!c[c[0]]&&c[0]>1;c[0]--);
	c[0]=c[0]>1?c[0]:1;
}



void mod(bignum_t c, bignum_t a, bignum_t b)
{
    bignum_t t, t1, t2;
    div(t, a, b);
    mul(t1, b, t);
    cp(t2, a);
    sub(t2, t1);
    cp(c, t2);
}

int N;
bignum_t t[1200];
bignum_t m[1200];

void gcd(bignum_t c, bignum_t ta, bignum_t tb)
{
    bignum_t tmp, a, b;
    cp(a, ta); cp(b, tb);
    if(comp(a, b) < 0)
    {
        cp(tmp, a);
        cp(a, b);
        cp(b, tmp);
    }
    while(comp(b, 0) > 0)
    {
        mod(tmp, a, b);
        cp(a, b);
        cp(b, tmp);
    }
    cp(c, a);
}

int main()
{
    int C, test, i;
    bignum_t GCD, d;
    scanf("%d", &C);
    for(test = 1; test <= C; test ++)
    {
        scanf("%d", &N);
        for(i = 0; i < N; i ++)
            read(t[i], cin);
        for(i = 1; i < N; i ++)
        {
            cp(m[0], t[0]);
            cp(m[i], t[i]);
            if(comp(m[0], m[i]) < 0)
                sub(m[i], m[0]);
            else
            {
                sub(m[0], m[i]);
                cp(m[i], m[0]);
            }            
        }
        cp(GCD, m[1]);
        for(i = 2; i < N; i ++)
            gcd(GCD, m[i], GCD);
        mod(d, t[0], GCD);
        if(comp(d, 0) == 0)
        {
            printf("Case #%d: 0\n", test);
            continue;
        }
        sub(GCD, d);
        printf("Case #%d: ", test);
        write(GCD, cout);
        printf("\n");
    }
    
    return 0;
} 





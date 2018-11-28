#include <stdio.h>
#include <iostream.h>
#include <string.h>
#include <stdlib.h>

#define DIGIT	4
#define DEPTH	10000
#define MAX     100
typedef int bignum_t[MAX+1];

int read(bignum_t a,char * buf){
	char ch;
	int i,j;
	memset((void*)a,0,sizeof(bignum_t));
	
	for (a[0]=strlen(buf),i=a[0]/2-1;i>=0;i--)
		ch=buf[i],buf[i]=buf[a[0]-1-i],buf[a[0]-1-i]=ch;
	for (a[0]=(a[0]+DIGIT-1)/DIGIT,j=strlen(buf);j<a[0]*DIGIT;buf[j++]='0');
	for (i=1;i<=a[0];i++)
		for (a[i]=0,j=0;j<DIGIT;j++)
			a[i]=a[i]*10+buf[i*DIGIT-1-j]-'0';
	for (;!a[a[0]]&&a[0]>1;a[0]--);
	return 1;
}

void write(const bignum_t a){
	int i,j;
	for (printf("%d",a[i=a[0]]),i--;i;i--)
		for (j=DEPTH/10;j;j/=10)
			printf("%d",a[i]/j%10);
		printf("\n");
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
int comp(const bignum_t a,const bignum_t b){
	int i;
	if (a[0]!=b[0])
		return a[0]-b[0];
	for (i=a[0];i;i--)
		if (a[i]!=b[i])
			return a[i]-b[i];
	return 0;
}

int compare( const void *arg1, const void *arg2 )
{
	return comp( * ( bignum_t* ) arg1, * ( bignum_t* ) arg2 );
}
void sub(bignum_t a,const bignum_t b){
	int i;
	for (i=1;i<=b[0];i++)
		if ((a[i]-=b[i])<0)
			a[i+1]--,a[i]+=DEPTH;
		for (;a[i]<0;a[i]+=DEPTH,i++,a[i]--);
		for (;!a[a[0]]&&a[0]>1;a[0]--);
}
void GCD(bignum_t a,bignum_t b)
{
	while (comp(a,b) != 0)
	{
		if (comp(a,b) > 0)
		{
			sub(a,b);
		}
		else
		{
			sub(b,a);
		}
	}
}

int main()
{
	int C,times,N,i,j;
	char tmp_buf[64];
	bignum_t a[1024],d[1024];
	freopen("B-small-attempt0(2).in","r",stdin);
	freopen("2.out","w",stdout);
	scanf("%d",&C);
	for (times=1; times<=C; ++times)
	{
		memset(a,0,sizeof(a));
		memset(d,0,sizeof(d));
		scanf("%d ",&N);
		for (i=0; i<N; ++i)
		{
			memset(tmp_buf,0,sizeof(tmp_buf));
			scanf("%s",tmp_buf);
			read(a[i],tmp_buf);
		}
		qsort(a,N,sizeof(bignum_t),compare);
		for (i=1,j=1; i<N; ++i)
		{
			d[j][0] = 1;
			add(d[j],a[i]);
			sub(d[j],a[i-1]);
			if (d[j][1] > 0 || d[j][0] > 1) j++;
		}
		for (i=2; i<j; ++i)
		{	
			GCD(d[i-1],d[i]);
		}
		while (comp(d[j-1],a[0]) < 0)
			sub(a[0],d[j-1]);
		sub(d[j-1],a[0]);
		printf("Case #%d: ",times);
		write(d[j-1]);
	}
	return 0;
}





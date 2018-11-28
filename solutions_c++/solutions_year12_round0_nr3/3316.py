#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int mul[7]={1,10,100,1000,10000,100000,1000000};
char rec[10][10];


int change(char s[],int len)
{
	int sum=0;
	for(int i=0;i<len;i++)
	{
		sum+=(s[i]-'0')*mul[len-i-1];
	}
	return sum;
}

int wei(int n)
{
	if(n<10)
		return 1;
	else if(n<100)
		return 2;
	else if(n<1000)
		return 3;
	else if(n<10000)
		return 4;
	else if(n<100000)
		return 5;
	else if(n<1000000)
		return 6;
	else if(n<10000000)
		return 7;
}

void ch(int n,char s[])
{
	int len=wei(n);
	for(int i=len-1;i>=0;i--)
	{
		s[i]=n%10+'0';
		n/=10;
	}
	s[len]='\0';
}

void yiwei(char a[],int n,int l)
{
	char b[10];
	int m;
	m=strlen(a)-n;
	strcpy(b,a+n);
	strcpy(b+m,a);
	b[l]='\0';
	strcpy(a,b);
}

bool judge(char rec[10][10],int n,char s[10])
{
	for(int i=0;i<n;i++)
		if(strcmp(rec[i],s)==0)
			return false;
	return true;
}

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("out.out","w",stdout);
	int t;
	int a,b;
	int i,j;
	long long ans;
	char sa[10],sb[10];
	scanf("%d",&t);
	int cs=1;
	while(t--)
	{
		ans=0;
		scanf("%s%s",sa,sb);
		int lena=strlen(sa);
		int lenb=strlen(sb);
		a=change(sa,lena);
		b=change(sb,lenb);
		char mids[10];
		for(i=a;i<=b;i++)
		{
//			cout<<endl<<i<<endl;
			ch(i,mids);
			int l=strlen(mids);
			int k=0;
			for(j=1;j<l;j++)
			{
				yiwei(mids,1,l);
//				cout<<mids<<endl;
				if(strcmp(rec[k],mids)==0)
					break;
				int m=change(mids,l);
				if(m>i&&m<=b&&wei(m)==wei(i)&&judge(rec,k,mids))
				{
					ans++;
					strcpy(rec[k++],mids);
//					cout<<"      here"<<endl;
				}
			}
		}
		printf("Case #%d: %lld\n",cs++,ans);
	}
	return 0;
}
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>

struct Bignum
{
	int len,a[55];
};

int T=0,c,n;
Bignum a[1005];

void swap(Bignum &a,Bignum &b)
{
	Bignum temp;
	temp=a;a=b;b=temp;
}
void blank(Bignum &a)
{
	a.len=0;
	for (int i=0;i<55;i++)
		a.a[i]=0;
}

bool operator >(const Bignum a,const Bignum b)
{
	if (a.len>b.len)
		return true;
	if (a.len<b.len)
		return false;
	for (int i=a.len;i>=1;i--)
		if (a.a[i]>b.a[i])
			return true;
		else
			if (a.a[i]<b.a[i])
				return false;
	return false;
}

Bignum operator -(const Bignum a,const Bignum b)
{
	Bignum ret;
	ret=a;
	for (int i=1;i<=a.len;i++)
	{
		ret.a[i]-=b.a[i];
		if (ret.a[i]<0)
			ret.a[i]+=10,ret.a[i+1]--;
	}
	while ((ret.len>0) && (ret.a[ret.len]==0))
		ret.len--;
	return ret;
}

Bignum operator *(const Bignum a,const Bignum b)
{
	Bignum ret;
	blank(ret);
	for (int i=1;i<=a.len;i++)
	for (int j=1;j<=b.len;j++)
	{
		ret.a[i+j-1]+=a.a[i]*b.a[j];
		if (ret.a[i+j-1]>=10)
			ret.a[i+j]+=ret.a[i+j-1]/10,ret.a[i+j-1]%=10;
	}
	ret.len=a.len+b.len-1;
	ret.len+=(ret.a[ret.len+1]!=0);
	while (ret.a[ret.len]>=10)
		ret.a[ret.len+1]=ret.a[ret.len]/10,ret.a[ret.len]%=10;
	return ret;
}

Bignum operator /(const Bignum p,const Bignum b)
{
	Bignum ret,a;
	blank(ret);
	a=p;
	ret.len=a.len-b.len+1;

	for (int i=a.len;i>=b.len;i--)
	while (true)
	{
		bool larger=true;
		if (a.a[i+1]==0)
    		for (int j=0;j<b.len;j++)
        		if (a.a[i-j]>b.a[b.len-j])
        			break;
        		else
        			if (a.a[i-j]<b.a[b.len-j])
        			{
        				larger=false;
        				break;
        			}
		if (larger==false)
			break;
		ret.a[i-b.len+1]++;
		for (int j=b.len-1;j>=0;j--)
		{
			a.a[i-j]-=b.a[b.len-j];
			if (a.a[i-j]<0)
				a.a[i-j]+=10,a.a[i-j+1]--;
		}
	}

	while (ret.len>0 && (ret.a[ret.len]==0))
		ret.len--;
	return ret;
}

Bignum operator %(const Bignum a,const Bignum b)
{
	return a-(a/b)*b;
}

Bignum gcd(const Bignum a,const Bignum b)
{
	if (b.len==0)
		return a;
	else
		return gcd(b,a%b);
}

void qsort(int l,int r)
{
	int i=l,j=r;
	Bignum mid=a[(l+r)>>1];
	do
	{
		while (mid>a[i]) i++;
		while (a[j]>mid) j--;
		if (i<=j)
			swap(a[i++],a[j--]);
	} while (i<=j);
	if (i<=r) qsort(i,r);
	if (l<=j) qsort(l,j);
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	scanf("%d",&c);
	while (c>0)
	{
		c--;T++;
		scanf("%d",&n);
		for (int i=1;i<=n;i++)
		{
			char t[55];
			scanf("%s",t);
			blank(a[i]);
			a[i].len=strlen(t);
			for (int j=1;j<=a[i].len;j++)
				a[i].a[j]=t[a[i].len-j]-'0';
		}
		qsort(1,n);

		Bignum ans;
		blank(ans);
		for (int i=1;i<n;i++)
			ans=gcd(a[i+1]-a[i],ans);
		printf("Case #%d: ",T);
		ans=(ans-a[1]%ans)%ans;
		ans.len+=(ans.len==0);
		for (int i=ans.len;i>=1;i--)
			printf("%d",ans.a[i]);
		printf("\n");
	}

	fclose(stdin);fclose(stdout);
	return 0;
}

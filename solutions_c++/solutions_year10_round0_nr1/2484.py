#include <iostream>
#include<fstream>
#include <string>
#include <stdio.h>
#include <vector>
#include <set>
#include <map>
#include<math.h>
#include<sstream>
#include <algorithm>
using namespace std;
int main()
{
	long t,n,k,h,i;
	ofstream fo("G:\\ASmallAns.txt",ios_base::out);
	freopen("G:\\aIN.txt","rt",stdin);

	scanf("%ld",&t);
	for (i = 0; i<t; i++)
	{
		h=1;
		fo<<"Case #"<<i+1<<": ";
		scanf("%ld%ld",&n,&k);
		for (int j=0; j<n;j++)
			h*=2;
		if (k%h == h-1)
			fo<<"ON"<<endl;
		else
			fo<<"OFF"<<endl;
	}
	return 0;
}
/*
long GCD(long a,long b)
{
	if (b== 0)
		return a;
	else
		return GCD(b, a%b);
}

int main()
{
	long t,n,i,j,d;
	long a[10];
	ofstream fo("G:\\BSmallAnsb.txt",ios_base::out);
	freopen("G:\\bIN.txt","rt",stdin);

	scanf("%ld",&t);
	for (i = 0; i<t; i++)
	{
		fo<<"Case #"<<i+1<<": ";
		scanf("%ld",&n);

		for (j=0;j<n;j++)
		{
			scanf("%ld",&a[j]);
		}

		if (a[0]==a[1] || a[0]==a[2])
		{
			a[0]=a[2];
			a[2]=0;
			n--;
		}
		
		if (a[1]==a[2])
		{
			a[2]=0;
			n--;
		}

		if (n == 2)
		{
			fo<<abs(a[0]-a[1]) - a[0]%abs(a[0]-a[1])<<endl;
		}
		else
		{
			d= GCD(abs(a[0]-a[1]), abs(a[1]-a[2]));
			d= GCD(d, abs(a[0]-a[2]));
			fo<<d-a[0]%d<<endl;
		}
	}
	
	return 0;
}
/*int ans[50] = {0};
void Add(long num)
{
	int i;
	for (i = 0;i <50;i++)
	{
		num+=ans[i];
		ans[i]=num%10;
		num=num/10;
	}
}
long  a[1005],b[1005],c[1005],d[1005];
int main()
{
	long  t,r,k,n, i,j,ij,s,p,q,h;

	ofstream fo("G:\\CSmallAnsb.txt",ios_base::out);
	freopen("G:\\IN.txt","rt",stdin);

	scanf("%d",&t);
	for (i = 0; i<t; i++)
	{
		for (j=0;j<50;j++)
			ans[j]=0;
		fo<<"Case #"<<i+1<<": ";
		scanf("%d",&r);
		scanf("%d",&k);
		scanf("%d",&n);

		for (j=0;j<n;j++)
		{
			scanf("%d",&a[j]);
			b[j]=-1;
			c[j]=-1;
			d[j]=0;
		}

		
		for (j=0;j<n;j++)
		{
			h= a[j]; ij=(j+1)%n;
			while(1)
			{
				if (ij == j)
					break;
				if (h+a[ij]>k)
					break;
				h=h+a[ij];
				ij=(ij+1)%n;
			}
			b[j]=ij;
			c[j]=h;
		}

		s=0;p=0;
		while(d[s]==0 && r>0)
		{
			r--;
			Add(c[s]);
			p++;
			d[s]=p;
			s=b[s];
		}
		q=r/(p-d[s]+1);

		ij=0;
		for (j=0;j<50;j++)
		{
			ij = ans[j]*q +ij;
			ans[j] = ij%10;
			ij = ij/10;
		}

		r=r%p;
		while(r-->0)
		{
			Add(c[s]);
			s=b[s];
		}

		j=49;
		while(ans[j]==0 && j>=0)
			j--;

		while(j>=0)
		{
			fo<<ans[j];
			j--;
		}
		fo<<endl;
		
	}
	
	return 0;

}

/*
		s=0;p=0;q=-1;
		while(r-->0)
		{
			q=p;h=0;
			while(1)
			{
				h+=a[p];
				if (h > k)
					break;
				s+=a[p];
				p = (p+1)%n;
				if (p==q)
					break;
			}
		}

		fo<<s<<endl;
		*/
/*int main()
{
	long t,n,k,m;
	ofstream fo("G:\\ASmallAns.txt",ios_base::out);

	scanf("%d",&t);
	for (int i = 0; i<t; i++)
	{
		fo<<"Case #"<<i+1<<": ";
		scanf("%d",&n);
		scanf("%d",&k);
		m = n*2-1;
		if (m>=k && (m-k)%2==0)
			fo<<"ON"<<endl;
		else
			fo<<"OFF"<<endl;	
	}


	return 0;
}
*/
/*int a[3000];
int main()
{
	int i,j,n,m,c,k,h;
	
	ofstream fo("G:\\ASmallAns.txt",ios_base::out);

	scanf("%d",&n);
	k = 1;
	while(n-->0)
	{
		scanf("%d",&c);
		scanf("%d",&m);
		for (i = 0; i<m; i++)
			scanf("%d",&a[i]);

		h =0;
		fo<<"Case #"<<k<<": ";
		for (i = 0 ; i < m;i++)
		{
			for (j = i+1; j<m ;j++)
				if (a[i]+a[j] == c)
				{
					fo<<i+1<<" "<<j+1<<endl;
					//printf("Case #%d: %d %d\n",k,i,j);
					h=1;
					break;
				}
			if (h == 1)
				break;

		}
		if (h == 0)
			fo<<endl;
		k++;
	}
	return 0;
}

/*char szdis[5005][16];
char str[1000];
char temp[16][30];
int tn[16];
int len,dis,num;
long find()
{
	int i,j,ij,ok;
	long k=0;
	for (i=0;i<dis;i++)
	{
		ok=0;
		for (j=0;j<len;j++)
		{
			ok=1;
			for (ij=0;ij<tn[j];ij++)
				if (szdis[i][j]==temp[j][ij])
				{
					ok=0;
					break;
				}
			if (ok==1)
				break;

		}
		if (ok==0)
			k++;
	}
	return k;
}
int main()
{
	ofstream fo("G:\\ASmallAns.txt",ios_base::out);
	int i,j,k,n;
	scanf("%d%d%d",&len,&dis,&num);
	for (i=0;i<dis;i++)
		scanf("%s",&szdis[i]);
	for (n=1; n<=num;n++)
	{
		scanf("%s",&str);
		k=0;
		memset(tn,0,sizeof(tn));
		i=0;
		int l = strlen(str);
		for (j=0;j<l; j++)
		{
			if (str[j]=='(')
			{
				j++;
				while(str[j]!=')')
				{
					temp[i][tn[i]]=str[j];
					j++;
					tn[i]++;
				}
			}
			else
			{
				temp[i][tn[i]]=str[j];
				tn[i]++;				
			}			
			i++;
		}
		fo<<"Case #"<<n<<": "<<find()<<endl;
		//printf("Case #%d: %ld\n",n,find());
	}

	fo.close();
	cin>>i;


	return 0;
}
*/
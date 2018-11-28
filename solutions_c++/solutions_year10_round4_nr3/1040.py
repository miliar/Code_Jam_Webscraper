#include <iostream>
#include<fstream>
#include <string.h> 
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
	int map[210][210];
	long t,i,j,x1,x2,y1,y2,m,r,ans,k;
	ofstream fo("G:\\BSmallAnsc1.txt",ios_base::out);
	//freopen("G:\\bin.txt","rt",stdin);
	scanf("%d",&t);
	k=1;
	while(t-->0)
	{
		fo<<"Case #"<<k<<": ";
		k++;
		ans = 0;
		scanf("%d",&r);
		for (i=0;i<205;i++)
			for (j=0;j<205;j++)
				map[i][j]=0;
		m =0;
		while(r-->0)
		{
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for (i=x1;i<=x2;i++)
				for (j=y1;j<=y2;j++)
				{
					if (map[i][j]==0)
						m++;
					map[i][j]=1;
				}
		}
		
		ans = 0;
		while(m!=0)
		{
			m=0;
			ans++;
			for (i=104;i>0;i--)
				for (j=104;j>0;j--)
				{
					if (map[i][j]==0)
					{
						if (map[i][j-1]==1 && map[i-1][j]==1)
						{
							map[i][j]=1;m++;
						}
					}
					else
					{
						if (map[i][j-1]==1 || map[i-1][j]==1)
						{
							map[i][j]=1;m++;
						}
						else
							map[i][j]=0;

					}
				}
		}

		fo<<ans<<endl;
	}
	return 0;
}
	/*
	for (k = 0; k<t; k++)
	{
		fo<<"Case #"<<i+1<<": ";
		scanf("%d%d",&n,&m);
		::memset(a, 0, sizeof(a));
		::memset(b, 0, sizeof(b));
		for (i=0;i<n;i++)
			scanf("%s", &a[i]);
		for (i=0;i<m;i++)
			scanf("%s", &b[i]);
		sort(b, b+m);

	}
	return 0;
}
/*
/*
struct aa{
	char name[21];
};
bool cmp(aa a,aa b)
{
	if (strcmp(a.name,b.name)>=0)
		return false;
	else
		return true;
}


aa arr[10005];
aa brr[10];
long n;
int find()
{
	int ans,i,j,ij;
	i=0;j=n-1;
	while(i<j)
	{
		ij=(i+j)/2;
		if (strcmp(arr[ij].name,brr[0].name)>=0)
			j=ij;
		else
			i=ij+1;
	}

	ans =0;
	while(ans<8 && i<n && strncmp(brr[0].name, arr[i].name, strlen(brr[0].name)) ==0)
	{
		ans++;
		strcpy(brr[ans].name, arr[i].name);
		i++;
	}

	return ans;
}

int main()
{
	long i,q,m;
	scanf("%d",&n);
	for (i=0;i<n;i++)
		scanf("%s",&arr[i].name);
	sort(arr, arr+n,cmp);
	scanf("%d",&q);
	while(q-->0)
	{
		scanf("%s",&brr[0].name);
		m = find();
		if (m==0)
			printf("%s\n",brr[0].name);
		else
		{
			for (i=1;i<m;i++)
				printf("%s ",brr[i].name);
			printf("%s\n",brr[m].name);
		}
	}

	cin>>i;
	return 0;
}
/*char c[10002];
long arr[2000];
long b[10002];
long brr[1000005];
int main()
{
	long N=10002;
	long  i,j,n,m,k,t,ij,r;
	long a[11] = {6,2,5,5,4,5,6,3,7,6,0};
	
	arr[0]=2;
	k=1;
    for(i = 1; i <= N; i++)
        c[i] = 0;
    for(n = 2; n <= N; n += 2)
        c[n] = 1;
    for(i = 3; i <= N ; i += 2)
	{
		if (c[i]==0)
		{
			
			arr[k]=i;
			k++;
			for(n = i + i; n <= N; n += i)
			   c[n] = 1;
		}
	}

	scanf("%d",&t);
	while(t-->0)
	{
		scanf("%d%d",&n,&m);
		for (i=0;i<1000005;i++)
			brr[i]=0;
		for (i=1;i<10;i++)
		{
			if (a[i]<=n && m*(a[i]-2) + a[i]%m<=n*m)
				brr[m*(a[i]-2) + a[i]%m]++;
		}
		for (i=2;i<n;i++)
			for(j=0;j<m;j++)
			{
				if (brr[m*(i-2) + j] >0)
				{
					for (ij=0;ij<10;ij++)
						if (i+a[ij]<=n)
						{
							brr[m*(i+a[ij]-2) + (j*10+ij)%m]+=brr[m*(i-2) + j];
							brr[m*(i+a[ij]-2) + (j*10+ij)%m]%=1000000007;
						}
				}
			}
		if (n<2)
			printf("0\n");
		else
		{
			i=0;
			r=0;
			while (arr[i]<m)
			{
				r+=brr[m*(n-2) +arr[i]];
				r%=1000000007;
				i++;
			}
			printf("%d\n",r);

		}
	}
	return 0;
}
/*
int main()
{
	long n,i,k,r,j;
	long a[35];
	char arr[35];
	a[0]=1;
	for (i=1;i<31;i++)
	{
		if (i%2==1)
			a[i]=(a[i-1]*26)%10000;
		else
			a[i]=a[i-1]%10000;
	}

	scanf("%d",&n);
	scanf("%s",&arr);
	if (n==1)
		printf("%d\n",int(arr[0]-'a')+1);
	else
	{
		r=0;
		i=0;
		while(1)
		{
			k=int(arr[i]-'a');
			r=(r+k*a[n-2*(i+1)])%10000;
			if (arr[i]>arr[n-1-i])
			{
				j=n-1-i-1;
				while(j>i && arr[j] == 'a')
				{
					arr[j]='z';
					j--;
				}

				if (j==i)
					break;
				arr[j]=arr[j]-1;
			}
			i++;
			if (i==n/2 && n%2==1)
			{				
				r=(r+1+int(arr[i]-'a'))%10000;
				
				break;
			}

			if (i+1==n/2 && n%2==0)
			{
				if (arr[i]>arr[n-1-i])
					r=(r+int(arr[i]-'a'))%10000;
				else
					r=(r+1+int(arr[i]-'a'))%10000;
				break;
			}

		}
		printf("%d\n",r);
	}



	return 0;
}
/*
struct aa{
	double a;
	double b;
};
aa arr[105];
aa brr[105];

int main()
{
	long i,n,m,t,s,k;
	double ai,bi,a,b,r,r1;
	scanf("%d",&t);
	while(t-->0)
	{
		scanf("%d%d",&n,&m);
		a=0;b=0;
		for (i=0;i<n;i++)
		{
			scanf("%lf%lf",&ai,&bi);
			a= a+ai*bi;
			b= b+bi;
		}

		for (i=0;i<m;i++)
			scanf("%lf%lf",&arr[i].a,&arr[i].b);
		r = a/b;
		s=0;
		while(r<90.000)
		{
			k=-1;r1=r;
			for (i=0;i<m;i++)
			{
				if (arr[i].b>0 && (a+arr[i].a*arr[i].b)/(b+arr[i].b) > r1)
				{
					k=i;
					r1=(a+arr[i].a*arr[i].b)/(b+arr[i].b);
				}
			}

			if (k== -1)
				break;

			r=r1;
			a+=arr[k].a*arr[k].b;
			b+=arr[k].b;
			arr[k].b=-1;
			s++;
		}

		if (r<90.000)
			printf("Impossible\n");
		else
			printf("%d\n",s);

	}
	return 0;
}
/*
struct aa{
	char name[15];
	long k;
};

bool cmp(aa a,aa b)
{
	if (strcmp(a.name,b.name)>=0)
		return false;
	else
		return true;
}
aa arr[10005];
int main()
{
	long t,x,s,n,m,i,j;
	char name[15];
	scanf("%d",&t);
	while(t-->0)
	{
		scanf("%d",&x);
		scanf("%d",&s);
		for(i=0;i<s;i++)
		{
			scanf("%d %d",&n,&m);
			for (j=0;j<n;j++)
				scanf("%s",&name);
			scanf("%s",&arr[i].name);
			if (n*x>=m)
				arr[i].k = m;
			else
				arr[i].k = n*x;
		}
		sort(arr, arr+s,cmp);
		i=0;
		while(i<s)
		{
			j=i+1;
			while(j<s && strcmp(arr[i].name,arr[j].name) == 0)
			{
				arr[i].k +=arr[j].k;
				j++;
			}
			printf("%s %d\n",arr[i].name, arr[i].k);
			i=j;
		}
		if (t!=0)
			printf("\n");
	}
	return 0;
}
/*
char str[1000005];
int main()
{
	char a;
	long  b,n,len;
	scanf("%d",&n);
	while(n-->0)
	{
		scanf("%s",&str);
		len = strlen(str);

	}
	return 0;
}
/*
struct arr{
	char ch[25];
};
arr a[10005];
arr b[10005];
bool cmp(arr a,arr b)
{
	if (strcmp(a.ch,b.ch)>=0)
		return false;
	else
		return true;
}

int main()
{
	long i,n,m;
	scanf("%d", &n);
    for (i=0;i<n;i++)
		scanf("%s", &a[i].ch);

	sort(a,a+n,cmp);
	
	scanf("%d",&m);
	for (i=0;i<m;i++)
	{
		scanf("%s",&b[i].ch);
		find();
	}

	for (i=0;i<m;i++)
	{
	}

	return 0;
}
/*
int main()
{
	long a,b,r,t,n,m,c;
	char arr[1005];
	cin>>t;
	while(t-->0)
	{
		//memset(arr, 0, sizeof(arr));
		for (n=0;n<1002;n++)
			arr[n]=0;
		scanf("%d %s %d", &a,&arr,&b);
		n=0;
		while(arr[n] == '^')
			n++;
		n++;
		r=0;m=1;
		while(a!=0 || b!=0)
		{
			c= (a%n + b%n)%n;
			r+=c*m;
			m*=n;
			a=a/n;
			b=b/n;
		}
		cout<<r<<endl;
	}
	return 0;
}
/*
int main()
{
	long n,m,t,i,j,ij;
	bool y;
	long a[105];
	long b[105];
	cin>>t;
	while (t-->0)
	{
		cin>>n;
		for (i =0;i<n;i++)
			scanf("%d",&a[i]);
		for (i=0;i<n;i++)
			b[i]=0;


		for (i=0;i<n;i++)
		{
			y = false;

			for (j=0;j<n;j++)
			{
				if (j!=i)
				{
					for (ij=0;ij<n;ij++)
					{
						if (ij!=i && ij!=j && a[i]==a[j]+a[ij])
						{
							y=true;
							break;
						}
					}
				}
				if (y==true)
					break;
			}

			if (y==true)
				b[i]=1;
		}
	
		m=0;
		for (i=0;i<n;i++)
			m+=b[i];
		cout<<m<<endl;
		
	}
	return 0;
}
/*int main()
{
	long n,m;
	m=0;
	cin>>n;
	while(n>0)
	{
		if (n%7!=0 && n/10!=7 && n%10!=7)
			m=m+n*n;
		n--;
	}
	cout<<m<<endl;

	return 0;
}
/*int main()
{
	long t,s,m,h,d,n,y,i;
	long a[5] = {365,365,366,365,0};
	long b[13] = {31,28,31,30,31,30,31,31,30,31,30,31};
	while(scanf("%d",&t)!=-1)
	{
		s = t%60;
		t = t/60;
		m = t%60;
		t = t/60;
		h = t%24;
		t = t/24;
		y = 1970;
		i=0;
		while(t>=a[i])
		{
			t-=a[i];
			y++;
			i++;
			i=i%4;
		}
		
		if (i==2)
			b[1]=29;
		i=0;
		n = 1;
		while(t>=b[i])
		{
			t-=b[i];
			n++;
			i++;
		}
		d=t+1;
	
		printf("%d-",y);
		if (n<10)
			printf("0%d-",n);
		else
			printf("%d-",n);

		if (d<10)
			printf("0%d ",d);
		else
			printf("%d ",d);

		if (h<10)
			printf("0%d:",h);
		else
			printf("%d:",h);

		if (m<10)
			printf("0%d:",m);
		else
			printf("%d:",m);

		if (s<10)
			printf("0%d\n",s);
		else
			printf("%d\n",s);
	}
	return 0;
}
/*
string a[101];
string b[101];

int main()
{
	int t,k,i,n,m;
	ofstream fo("G:\\CSmallAnsc1.txt",ios_base::out);
	//freopen("G:\\bin.txt","rt",stdin);
	scanf("%d",&t);
	for (k = 0; k<t; k++)
	{
		fo<<"Case #"<<i+1<<": ";
		scanf("%d%d",&n,&m);
		::memset(a, 0, sizeof(a));
		::memset(b, 0, sizeof(b));
		for (i=0;i<n;i++)
			scanf("%s", &a[i]);
		for (i=0;i<m;i++)
			scanf("%s", &b[i]);
		sort(b, b+m);

	}
	return 0;
}
/*
long arr[1000005];
int main()
{
	int i,t,y;
	double x;
	for (i=0;i<3140;i++)
		arr[i]=1;
	for (i=3140;i<1000001;i++)
		arr[i]=(arr[i-1000]+arr[i-3140])%1000000007;
	scanf("%d",&t);
	while(t-->0)
	{
		scanf("%lf",&x);
		if (x<0.0)
			printf("0\n");
		else
		{
			x = x*1000;
			y = int(x);
			
			printf("%d\n", arr[y]);
		}

	}

	return 0;
}
/*int main()
{
	long t,a,b,i,r;
	long arr[35];
	scanf("%d",&t);


	while(t-->0)
	{
		scanf("%d%d",&a,&b);
		arr[0]=a%9907;
		for (i=1;i<31;i++)
			arr[i] = (arr[i-1]*arr[i-1])%9907;

		r=1;i=0;
		while(b>0)
		{
			if (b%2==1)
				r=r*arr[i]%9907;
			i++;
			b=b/2;
		}
		printf("%d\n", r);
	}
	return 0;
}
/*
int main()
{
	long t;
	scanf("%d",&t);

	while(t-->0)
	{
		scanf("%d",&t);
	}
	printf("%d\n", a+b);


	return 0;
}
/*
int ok(long x,long y)
{
	long z;

	if (y>x)
	{
		z=x;
		x=y;
		y=z;
	}

	if (x==y)
		return 0;
	
	if (x%y==0)
		return 1;

	if (ok(y, x%y)==0)
		return 1;

	if (x < 2*y)
		return 0;
	else
		return 1;

}
int main()
{
	long  t,k,n, i,j,ij,d,a,m,ji,r,a1,a2,b1,b2;

	ofstream fo("G:\\CSmallAnsc1.txt",ios_base::out);
	//freopen("G:\\bin.txt","rt",stdin);

	scanf("%d",&t);
	for (i = 0; i<t; i++)
	{
		fo<<"Case #"<<i+1<<": ";
		scanf("%d",&a1);
		scanf("%d",&a2);
		scanf("%d",&b1);
		scanf("%d",&b2);
		r=0;
		for (j=a1;j<=a2;j++)
			for(ij=b1;ij<=b2;ij++)
			{
				if (ok(j,ij) ==1)
					r++;
			}

		fo<<r<<endl;
	}

	return 0;
}
/*
long Count(long x,long y,long z)
{
	if (z==0)
	{
		if (x==y)
			return 0;
		else
			return -1;
	}

	long num =0;
	long h=0;
	if (x>y)
	{
		h=x;
		x=y;
		y=h;
	}

	while(x+z<y)
	{
		num++;
		x=x+z;
	}
	return num;
}

int main()
{
	long  t,k,n, i,j,ij,d,a,m,ji,r;
	long  ans[300];
	long  arr[300];
	long  temp[300];

	ofstream fo("G:\\BBigAnsc1.txt",ios_base::out);
	//freopen("G:\\bin.txt","rt",stdin);

	scanf("%d",&t);
	for (i = 0; i<t; i++)
	{
		fo<<"Case #"<<i+1<<": ";
		scanf("%d",&d);
		scanf("%d",&a);
		scanf("%d",&m);
		scanf("%d",&n);
		for (j=0;j<n;j++)
			scanf("%d",&arr[j]);

		for (j=0;j<256;j++)
			ans[j] = abs(j-arr[0]);
		ans[256]=d;

		for (j=1;j<n;j++)
		{
			for (ij=0;ij<300;ij++)
				temp[ij]=-1;
			temp[256] = ans[256]+d;

			for (ij =0;ij<256;ij++)
			{
				temp[ij] = ans[ij] + d;
				if (temp[ij] > ans[256] + abs(ij-arr[j]))
					temp[ij]= ans[256] + abs(ij-arr[j]);
				
				for (ji=0;ji<256;ji++)
				{
					k = Count(ji,ij,m);
					if (k!=-1)
					{
						k=k*a;
						k=k+ans[ji] + abs(arr[j]-ij);
						if (temp[ij]>k)
							temp[ij]=k;
					}					
				}
			}

			for (ij=0;ij<=256;ij++)
				ans[ij]=temp[ij];
		}


		r=ans[0];
		for (ij=0;ij<=256;ij++)
		{
			if (r>ans[ij])
				r=ans[ij];
		}
	
		fo<<r<<endl;		
	}
	return 0;
}

/*int main()
{
	long  t,r,k,n, i,j,ij,s,p,q,h,b;
	char  map[55][55];
	int ans[55][55];

	ofstream fo("G:\\ABigAnsc.txt",ios_base::out);
	freopen("G:\\IN.txt","rt",stdin);

	scanf("%d",&t);
	for (i = 0; i<t; i++)
	{
		fo<<"Case #"<<i+1<<": ";
		scanf("%d",&n);
		scanf("%d",&k);
		r=0;b=0;
		for (j=0;j<55;j++)
		{
			for (ij=0;ij<55;ij++)
				map[j][ij]='.';
		}

		for (j = 0; j<n;j++)
			scanf("%s",&map[j]);

	
		for (j = 0; j<n;j++)
		{
			ij = n-2;
			while(ij>=0)
			{
				if ((map[j][ij] != '.') && (map[j][ij+1] == '.') && (ij+1<n))
				{
					map[j][ij+1]=map[j][ij];
					map[j][ij]='.';
					ij++;
				}
				else
					ij--;
			}
		}

	

		for (j=0;j<n;j++)
		{
			for (ij=0;ij<n;ij++)
			{
				s=1;
				p=j;q=ij+1;
				while((q<n) && (map[j][ij] == map[p][q]))
				{
					s++;q++;
				}

				if (s>=k)
				{
					if (map[j][ij] == 'R')
						r=1;
					else if (map[j][ij] == 'B')
						b=1;
				}

				s=1;
				p=j+1;q=ij;
				while((p<n) && (map[j][ij] == map[p][q]))
				{
					s++;p++;
				}

				if (s>=k)
				{
					if (map[j][ij] == 'R')
						r=1;
					else if (map[j][ij] == 'B')
						b=1;
				}

				s=1;
				p=j+1;q=ij+1;
				while((p<n) && (q<n) && (map[j][ij] == map[p][q]))
				{
					s++;p++;q++;
				}

				if (s>=k)
				{
					if (map[j][ij] == 'R')
						r=1;
					else if (map[j][ij] == 'B')
						b=1;
				}

				s=1;
				p=j+1;q=ij-1;
				while((p<n) && (q>=0) && (map[j][ij] == map[p][q]))
				{
					s++;p++;q--;
				}

				if (s>=k)
				{
					if (map[j][ij] == 'R')
						r=1;
					else if (map[j][ij] == 'B')
						b=1;
				}

			}
		}

		if (r==1 && b==1)
			fo<<"Both"<<endl;
		else if (r==0 && b==0)
			fo<<"Neither"<<endl;
		else if (r==0 && b==1)
			fo<<"Blue"<<endl;
		else if (r==1 && b==0)
			fo<<"Red"<<endl;		
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

	ofstream fo("G:\\CSmallAnsc.txt",ios_base::out);
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

		if (d[s] != 0)
		{
			for (j=0;j<50;j++)
				ans[j]=0;

			q=b[s];
			Add(c[s]);
			while(q != s)
			{
				Add(c[q]);
				q= b[q];
			}

			q=1+r/(p-d[s]+1);

			ij=0;
			for (j=0;j<50;j++)
			{
				ij = ans[j]*q +ij;
				ans[j] = ij%10;
				ij = ij/10;
			}

			r=r%(p-d[s]+1);
			q=s;
			while(r-->0)
			{
				Add(c[q]);
				q=b[q];
			}

			r = 0;
			while(r!=s)
			{
				Add(c[r]);
				r=b[r];
			}
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
	ofstream fo("G:\\BSmallAns.txt",ios_base::out);
	//freopen("G:\\bIN.txt","rt",stdin);

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

		sort(a,

		if (n == 2)
		{
			if (a[0]%a[1]==0 || a[1]%a[0]==0)
				fo<<0<<endl;
			else
				fo<<abs(a[0]-a[1]) - a[0]%abs(a[0]-a[1])<<endl;
		}
		else
		{
			d= GCD(abs(a[0]-a[1]), abs(a[1]-a[2]));
			d= GCD(d, abs(a[0]-a[2]));
			if (a[0]%d==0)
				fo<<0<<endl;
			else
				fo<<d-a[0]%d<<endl;
		}
	}
	
	return 0;
}
/*
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
#include<iostream>

using namespace std;


char a[510];
int b [510][3];
int ans;
int len;
string s = "welcome to code jam";
int slen=19;


void solve()
{
	int i,j;
	for(i=0;i<len;++i)
		b[i][0]=b[i][1]=b[i][2]=0;
	ans=0;
	for(i=0;i<len;++i)
	{
		if(a[i]=='w')
		{
			b[i][0]=1;
			continue;
		}
		if(a[i]=='e')
		{
			for(j=i-1;j>=0;--j)
			{
				if(a[j]=='w')
					b[i][0]+=b[j][0];
				if(a[j]=='m')
					b[i][1]+=b[j][0];
				if(a[j]=='d')
					b[i][2]+=b[j][0];
			}
		}
		if(a[i]=='l')
		{
			for(j=i-1;j>=0;--j)
			{
				if(a[j]=='e')
					b[i][0]+=b[j][0];
			}
		}
		if(a[i]=='c')
		{
			for(j=i-1;j>=0;--j)
			{
				if(a[j]=='l')
					b[i][0]+=b[j][0];
				if(a[j]==' ')
					b[i][1]+=b[j][1];
			}
		}
		if(a[i]=='o')
		{
			for(j=i-1;j>=0;--j)
			{
				if(a[j]=='t')
					b[i][1]+=b[j][0];
				if(a[j]=='c')
				{
					b[i][0]+=b[j][0];
					b[i][2]+=b[j][1];
				}
			}
		}
		if(a[i]=='m')
		{
			for(j=i-1;j>=0;--j)
			{
				if(a[j]=='a')
					b[i][1]+=b[j][0];
				if(a[j]=='o')
					b[i][0]+=b[j][0];
			}
		}
		if(a[i]==' ')
		{
			for(j=i-1;j>=0;--j)
			{
				if(a[j]=='o')
					b[i][1]+=b[j][1];
				if(a[j]=='e')
				{
					b[i][0]+=b[j][1];
					b[i][2]+=b[j][2];
				}
			}
		}
		if(a[i]=='t')
		{
			for(j=i-1;j>=0;--j)
			{
				if(a[j]==' ')
					b[i][0]+=b[j][0];
			}
		}
		if(a[i]=='d')
		{
			for(j=i-1;j>=0;--j)
			{
				if(a[j]=='o')
					b[i][0]+=b[j][2];
			}
		}
		if(a[i]=='j')
		{
			for(j=i-1;j>=0;--j)
			{
				if(a[j]==' ')
					b[i][0]+=b[j][2];
			}
		}
		if(a[i]=='a')
		{
			for(j=i-1;j>=0;--j)
			{
				if(a[j]=='j')
					b[i][0]+=b[j][0];
			}
		}
		b[i][0]=b[i][0]%10000;
		b[i][1]=b[i][1]%10000;
		b[i][2]=b[i][2]%10000;
	}
	for(i=0;i<len;++i)
		if(a[i]=='m')
			ans=(ans+b[i][1])%10000;
	
}

void print ( int x )
{
	if(x<1000)
		cout<<'0';
	if(x<100)
		cout<<'0';
	if(x<10)
		cout<<'0';
	cout<<x<<endl;
}



int main()
{
	freopen("answer.txt","w",stdout);
	int n;
	cin>>n;
	char zibil;
	cin.get(zibil);
	int i;
	for(i=0;i<n;++i)
	{
		cin.getline(a,510,'\n');
		len=strlen(a);
		cout<<"Case #"<<i+1<<": ";
		solve();
		print(ans);
	}
	return 0;
}
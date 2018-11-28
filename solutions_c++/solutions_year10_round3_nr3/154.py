#include<iostream>
#include<map>
using namespace std;

#define MAXN 515

int te,m,n;
bool bo[MAXN][MAXN];
bool used[MAXN][MAXN];
int f1[MAXN][MAXN],f2[MAXN][MAXN];
int ans;
map<int,int> aa;

bool OK2(int i,int j,int k)
{
	if(i+k-1>=m||j+k-1>=n)
	{
		return false;
	}
	for(int ii=i;ii<=i+k-1;++ii)
	{
		for(int jj=j;jj<=j+k-1;++jj)
		{
			if(used[ii][jj])
			{
				return false;
			}
		}
	}
	for(int ii=i;ii<=i+k-1;++ii)
	{
		for(int jj=j;jj<j+k-1;++jj)
		{
			if(bo[ii][jj]==bo[ii][jj+1])
			{
				return false;
			}
		}
	}
	for(int jj=j;jj<=j+k-1;++jj)
	{
		for(int ii=i;ii<i+k-1;++ii)
		{
			if(bo[ii][jj]==bo[ii+1][jj])
			{
				return false;
			}
		}
	}
	for(int ii=i;ii<=i+k-1;++ii)
	{
		for(int jj=j;jj<=j+k-1;++jj)
		{
			used[ii][jj]=true;
		}
	}
	return true;
}

void pp()
{
	for(int i=0;i<m;++i)
	{
		for(int j=0;j<n;++j)
		{
			if(!used[i][j]&&bo[i][j])
			{
				cout<<1;
			}
			else
			{
				cout<<0;
			}
		}
		cout<<endl;
	}
}

void OK1(int k)
{
	if(k==2)
	{
		//pp();
	}
	for(int i=0;i<m;++i)
	{
		for(int j=0;j<n;++j)
		{
			if(!used[i][j]&&OK2(i,j,k))
			{
				aa[k]++;
			}
		}
	}
}

void Sm()
{
	memset(used,false,sizeof(used));
	aa.clear();
	ans=0;
	int mm;
	if(m>n)
	{
		mm=n;
	}
	else
	{
		mm=m;
	}
	for(int k=mm;k>=1;--k)
	{
		OK1(k);
	}
}

int main()
{
	freopen("Cs.in","r",stdin);
	freopen("Cs.txt","w",stdout);
	cin>>te;
	for(int ca=1;ca<=te;++ca)
	{
		cin>>m>>n;
		memset(bo,false,sizeof(bo));
		for(int i=0;i<m;++i)
		{
			getchar();
			for(int j=0;j<n/4;++j)
			{
				char ch;
				cin>>ch;
				int tmp;
				if(ch>='0'&&ch<='9')
				{
					tmp=ch-'0';
				}
				else
				{
					tmp=ch-'A'+10;
				}
				bo[i][j*4]=tmp&8;
				bo[i][j*4+1]=tmp&4;
				bo[i][j*4+2]=tmp&2;
				bo[i][j*4+3]=tmp&1;
			}
		}
		//pp();
		/*
		*/
		/*
		for(int i=0;i<m;++i)
		{
		f1[i][n-1]=1;
		for(int j=n-2;j>=0;--j)
		{
		if(bo[i][j]==bo[i][j+1])
		{
		f1[i][j]=1;
		}
		else
		{
		f1[i][j]=f1[i][j+1]+1;
		}
		}
		}
		for(int j=0;j<n;++j)
		{
		f2[m-1][j]=1;
		for(int i=m-2;i>=0;--i)
		{
		if(bo[i][j]==bo[i+1][j])
		{
		f2[i][j]=1;
		}
		else
		{
		f2[i][j]=f2[i+1][j]+1;
		}
		}
		}
		*/
		Sm();
		printf("Case #%d: %d\n",ca,aa.size());
		for(map<int,int>::reverse_iterator mip=aa.rbegin();mip!=aa.rend();mip++)
		{
			printf("%d %d\n",mip->first,mip->second);
		}
	}
	return 0;
}

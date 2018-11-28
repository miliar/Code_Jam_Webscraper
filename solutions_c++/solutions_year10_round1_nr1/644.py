#include<cstdio>
#include<cstring>
#define N 55
int n,k;
char a[N][N];
char b[N][N];
int rez;
char msg[4][10];
inline void citire()
{
	scanf("%d%d\n",&n,&k);
	for(int i=1; i<=n; ++i)
		fgets(a[i]+1,N-1,stdin);
}
inline void rotate()
{
	for(int i=1,j1=1; i<=n; ++i,++j1)
	{
		for(int j=1,i1=n; j<=n; ++j,--i1)
			b[i][j]=a[i1][j1];
	}

	char v[N]={0};
	int nr=0;
	for(int j=1; j<=n; ++j)
	{
		nr=0;
		for(int i=n; i>0; --i)
		{
			if(b[i][j]=='R' || b[i][j]=='B')
				v[++nr]=b[i][j];
		}

                for(int i=n,t=1; i>0 && t<=nr; --i,++t)
			b[i][j]=v[t];
		for(int i=n-nr; i>0; --i)
			b[i][j]='.';
	}
}
inline void rezolva()
{
	int rd=0,bl=0;

	for(int i=1; i<=n; ++i)
	{
		rd=0,bl=0;
		for(int j=1; j<=n; ++j)
		{
			if(b[i][j]=='R')
			{
				++rd;
				bl=0;
				if(rd==k)
					rez|=1;
				continue;
			}
			if(b[i][j]=='B')
			{
				++bl;
				rd=0;
				if(bl==k)
					rez|=2;
				continue;
			}
			rd=bl=0;
		}
	}

	for(int j=1; j<=n; ++j)
	{
		rd=bl=0;
		for(int i=1; i<=n; ++i)
		{
			if(b[i][j]=='R')
			{
				++rd;
				bl=0;
				if(rd==k)
					rez|=1;
				continue;
			}
			if(b[i][j]=='B')
			{
				++bl;
				rd=0;
				if(bl==k)
					rez|=2;
				continue;
			}
			rd=bl=0;
		}
	}

	for(int i1=1; i1<=n; ++i1)
	{
		rd=bl=0;
		for(int i=i1,j=1; i>0 && j<=n; --i,++j)
		{
			if(b[i][j]=='R')
			{
				++rd;
				bl=0;
				if(rd==k)
					rez|=1;
				continue;
			}
			if(b[i][j]=='B')
			{
				++bl;
				rd=0;
				if(bl==k)
					rez|=2;
				continue;
			}
			rd=bl=0;
		}  
	}
	for(int j1=2; j1<=n; ++j1)
	{
		rd=bl=0;
		for(int i=n,j=j1; i>0 && j<=n; --i,++j)
                {
			if(b[i][j]=='R')
			{
				++rd;
				bl=0;
				if(rd==k)
					rez|=1;
				continue;
			}
			if(b[i][j]=='B')
			{
				++bl;
				rd=0;
				if(bl==k)
					rez|=2;
				continue;
			}
			rd=bl=0;
		} 
	}

	for(int j1=n; j1>0; --j1)
	{
		rd=bl=0;
		for(int i=1,j=j1; i<=n && j<=n; ++i,++j)
		{
                	if(b[i][j]=='R')
			{
				++rd;
				bl=0;
				if(rd==k)
					rez|=1;
				continue;
			}
			if(b[i][j]=='B')
			{
				++bl;
				rd=0;
				if(bl==k)
					rez|=2;
				continue;
			}
			rd=bl=0;
		} 
	}
    	for(int i1=2; i1<=n; ++i1)
	{
		rd=bl=0;
		for(int i=i1,j=1; i<=n && j<=n; ++i,++j)
		{
                	if(b[i][j]=='R')
			{
				++rd;
				bl=0;
				if(rd==k)
					rez|=1;
				continue;
			}
			if(b[i][j]=='B')
			{
				++bl;
				rd=0;
				if(bl==k)
					rez|=2;
				continue;
			}
			rd=bl=0;
		} 
	}
}
int main()
{
	freopen("pa.in","r",stdin);
	freopen("pa.out","w",stdout);

	int T;
	scanf("%d",&T);
	++T;
	strcpy(msg[0],"Neither");
        strcpy(msg[1],"Red");
	strcpy(msg[2],"Blue");
	strcpy(msg[3],"Both");

	for(int i=1; i<T; ++i)
	{
		rez=0;
		citire();
		rotate();
		rezolva();
		printf("Case #%d: %s\n",i,msg[rez]);
	}

	return 0;
}


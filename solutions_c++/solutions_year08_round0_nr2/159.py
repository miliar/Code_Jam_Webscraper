#include <stdio.h>
#include <string.h>
#define oo 1000
struct Tcar
{
	int t;
	char d,I;
}	c[oo];
int A,B,N,Case,T;
struct Ttirp
{
	int st,en;
	inline void readin()
	{
		char s[20],*tmp;
		int x,y;
		//start
		scanf("%s",s);
		tmp=strchr(s,':');
		*tmp=' ';
		sscanf(s,"%d%d",&x,&y);
		st=x*60+y;
		//end
		scanf("%s",s);
		tmp=strchr(s,':');
		*tmp=' ';
		sscanf(s,"%d%d",&x,&y);
		en=x*60+y+T;
	}
}	a[oo],b[oo];
int M,AnsA,AnsB;

inline int Get_Car(char ch)
{
	for (int i=1;i<=M;++i)
		if (c[i].d=='W' && c[i].I==ch) return i;
	c[++M].d='W';
	c[M].I=ch;
	
	if (ch=='A') ++AnsA;
	else ++AnsB;
	
	return M;
}

int main()
{
	freopen("i.txt","r",stdin);
	freopen("o.txt","w",stdout);
	
	for (scanf("%d",&N);N;N--)
	{
		scanf("%d%d%d",&T,&A,&B);
		M=AnsA=AnsB=0;
		for (int i=1;i<=A;++i)
			a[i].readin();
		for (int j=1;j<=B;++j)
			b[j].readin();
		
		for (int t=0;t<=1440+T;++t)
		{
			//do car
			for (int i=1;i<=M;++i)
				if (c[i].t==t)
					if (c[i].d=='R')
					{
						c[i].I=c[i].I=='A'?'B':'A';
						c[i].d='W';
						c[i].t=t;
					}
			
			for (int i=1;i<=A;++i)
				if (a[i].st==t)
				{
					int x=Get_Car('A');
					c[x].d='R';
					c[x].t=a[i].en;
				}
			for (int i=1;i<=B;++i)
				if (b[i].st==t)
				{
					int x=Get_Car('B');
					c[x].d='R';
					c[x].t=b[i].en;
				}
		}
		
		printf("Case #%d: %d %d\n",++Case,AnsA,AnsB);
	}
	return 0;
}

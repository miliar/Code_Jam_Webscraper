#include <iostream>
using namespace std;

int i,j,k,p,t;
char x;
int f[20];

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	scanf("%d",&t);
	scanf("%c",&x);
	for (p=1; p<=t; p++)
	{
		memset(f,0,sizeof(f));
		while (scanf("%c",&x))
		{
			if (x=='\r' || x=='\n') break;
			if (x=='w') f[1]++;
			if (x=='e') {f[2]+=f[1]; f[7]+=f[6]; f[15]+=f[14];}
			if (x=='l') f[3]+=f[2]; 
			if (x=='c') {f[4]+=f[3]; f[12]+=f[11];}
			if (x=='o') {f[5]+=f[4]; f[10]+=f[9]; f[13]+=f[12];}
			if (x=='m') {f[6]+=f[5]; f[19]+=f[18];}
			if (x==' ') {f[8]+=f[7]; f[11]+=f[10]; f[16]+=f[15];}
			if (x=='t') f[9]+=f[8];
			if (x=='d') f[14]+=f[13];
			if (x=='j') f[17]+=f[16];
			if (x=='a') f[18]+=f[17];
			
			for (j=1; j<20; j++)
				f[j]%=10000;
		}
		printf("Case #%d: %04d\n",p,f[19]);
	}

//	system("pause");
	return 0;
}

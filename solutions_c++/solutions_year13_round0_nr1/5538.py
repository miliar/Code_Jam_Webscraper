#include<iostream>
#include<cstdio>

using namespace std;
char a [10][10];

int Xr[10];
int Xc[10];
int Xd[10];

int Or[10];
int Oc[10];
int Od[10];

inline int get(char c,char p)
{
	if( c == p || c == 'T')
		return 1;
	return 0;
}
int main()
{
	freopen("in.txt","rt",stdin);
	freopen("A_out.txt","wt",stdout);
	int TC;
	scanf("%d",&TC);
	for(int tc = 1;tc<= TC; tc++)
	{
		memset(Xr,0,sizeof(Xr));
		memset(Xc,0,sizeof(Xc));
		memset(Xd,0,sizeof(Xd));
		memset(Or,0,sizeof(Or));
		memset(Oc,0,sizeof(Oc));
		memset(Od,0,sizeof(Od));
		int empty = 0;
		bool Owin,Xwin;
		Owin = Xwin = false;

		for(int i=0;i<4;i++)
		{
			scanf("%s",a[i]);
			for(int j=0;j<4;j++)
			{
				Xr[i] += get(a[i][j],'X');
				Xc[j] += get(a[i][j],'X');
				if( Xr[i] == 4 || Xc[j] == 4)
					Xwin = true;

				Or[i] += get(a[i][j],'O');
				Oc[j] += get(a[i][j],'O');
				if( Or[i] == 4 || Oc[j] == 4)
					Owin = true;
				
				if( a[i][j] == '.')
					++empty;
			}

			Xd[0] += get(a[i][i],'X');
			Xd[1] += get(a[i][3-i],'X');

			if(Xd[0] == 4 || Xd[1] == 4)
				Xwin = true;

			Od[0] += get(a[i][i],'O');
			Od[1] += get(a[i][3-i],'O');
			if( Od[0] == 4 || Od[1] == 4)
				Owin = true;
		}
		
		printf("Case #%d: ",tc);
		if( Xwin )
			printf("X won");
		else if( Owin )
			printf("O won");
		else if( empty == 0)
			printf("Draw");
		else
			printf("Game has not completed");
		printf("\n");

	}
	return 0;
}
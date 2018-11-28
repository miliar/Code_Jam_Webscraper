#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int T;
int NA,NB;
int nalist[200][2];
int nblist[200][2];

int eventna[60*24+1000][2];	// 1 is arrive,0 is departure
int eventnb[60*24+1000][2];

int needa,needb;


int inputatime()
{
	int t;
	char a,b,c,d,e;
	while( scanf("%c",&a) && (a=='\n'||a=='\r'||a==' ') );

	scanf("%c%c%c%c",&b,&c,&d,&e);
	t = ((int)(a-'0')*10+(b-'0'))*60+((d-'0')*10 + (e-'0'));
	return t;
}

int make()
{
	int i,a,b,t1,t2;
	scanf("%d %d %d",&T,&NA,&NB);
	memset(eventna,0,sizeof(eventna));
	memset(eventnb,0,sizeof(eventnb));
	for(i=0;i<NA;i++)
	{
		a = inputatime();
		b = inputatime();
		nalist[i][0] = a;
		nalist[i][1] = b;
		eventna[a][0] ++;
		eventnb[b+T][1] ++;
	}
	for(i=0;i<NB;i++)
	{
		a = inputatime();
		b = inputatime();
		nblist[i][0] = a;
		nblist[i][1] = b;
		eventnb[a][0] ++;
		eventna[b+T][1] ++;
	}

	needa = a = 0;
	needb = b = 0;
	for(i=0;i<60*24;i++)
	{
		t1 = a + eventna[i][1] - eventna[i][0];
		if( t1 < 0 )
		{
			needa += abs(t1);
			t1 = 0;
		}
		a = t1;
		

		t2 = b + eventnb[i][1] - eventnb[i][0];
		if( t2 < 0 )
		{
			needb += abs(t2);
			t2 = 0;
		}
		b = t2;
	}
	return 1;
}

int main()
{
	int i;
	int casen;
	freopen("output.txt","w",stdout);
	scanf("%d",&casen);
	for(i=1;i<=casen;i++)
	{
		make();
		printf("Case #%d: %d %d\n",i,needa,needb);
	}
	return 0;
}
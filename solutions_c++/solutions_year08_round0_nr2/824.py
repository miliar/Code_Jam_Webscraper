#include <stdio.h>
#include <string.h>

int timetable[2][101][3]={0};
int T,NA,NB;

void readtime(FILE *f,int &from,int &to)
{
	char str[20]={0};
	fgets(str,20,f);
	if(strlen(str)<11)fgets(str,20,f);
	from=((str[0]-'0')*10+(str[1]-'0'))*60+((str[3]-'0')*10+(str[4]-'0'));
	to=((str[6]-'0')*10+(str[7]-'0'))*60+((str[9]-'0')*10+(str[10]-'0'));
}

int locktrains(int at,int wh)
{
	int min=24*60,from=4,pos=0;
	int t;
	if((wh<0)||(wh==0))
	{
		for(t=0;t<NA;t++)
		{
			if((timetable[0][t][0]<min)&&(timetable[0][t][2]==0)&&(timetable[0][t][0]>=at))
			{
				min=timetable[0][t][0];
				pos=t;
				from=0;
			}
		}
	}
	if((wh<0)||(wh==1))
	{
		for(t=0;t<NB;t++)
		{
			if((timetable[1][t][0]<min)&&(timetable[1][t][2]==0)&&(timetable[1][t][0]>=at))
			{
				min=timetable[1][t][0];
				pos=t;
				from=1;
			}
		}
	}
	if(from==4)return 4;
	timetable[from][pos][2]=1;
	locktrains(timetable[from][pos][1]+T,from^1);
	return from;
}

int main()
{
	FILE *in,*out;
	in=fopen("input.txt","r");
	out=fopen("output.txt","w");
	
	int N,n;
	fscanf(in,"%i",&N);
	for(n=0;n<N;n++)
	{
		memset(timetable,0,sizeof(timetable));
		fscanf(in,"%i",&T);
		fscanf(in,"%i %i",&NA,&NB);
		int t;
		for(t=0;t<NA;t++)
		{
			readtime(in,timetable[0][t][0],timetable[0][t][1]);
		}
		for(t=0;t<NB;t++)
		{
			readtime(in,timetable[1][t][0],timetable[1][t][1]);
		}
		int trainfrom[2]={0};
		int f=locktrains(0,-1);
		while(f!=4)
		{
			trainfrom[f]++;
			f=locktrains(0,-1);
		}
		fprintf(out,"Case #%i: %i %i\n",n+1,trainfrom[0],trainfrom[1]);
	}
	fclose(in);
	fclose(out);
	return 0;
}
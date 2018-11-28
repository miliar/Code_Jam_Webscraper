
#include <fstream.h>
#include <windows.h>
int a[1000][2];
int b[1000][2];
int tal[2400];
int tbl[2400];
int tar[2400];
int tbr[2400];
int convert(char *s)
{
	return (s[0]-'0')*1000+(s[1]-'0')*100+(s[3]-'0')*10+(s[4]-'0');
}
void main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");
	int z, t;
	in>>t;

	for(z=0;z<t;z++)
	{
		int T,NA,NB;
		in>>T;
		in>>NA>>NB;
		int i;
		memset(tal,0,sizeof(tal));
		memset(tar,0,sizeof(tar));
		memset(tbl,0,sizeof(tbl));
		memset(tbr,0,sizeof(tbr));
		for(i=0;i<NA;i++)
		{
			char t1[100],t2[100];
			in>>t1>>t2;
			tal[convert(t1)]++;
			tbr[convert(t2)]++;
			a[i][0]=convert(t1);
			a[i][1]=convert(t2);
		}
		for(i=0;i<NB;i++)
		{
			char t1[100],t2[100];
			in>>t1>>t2;
			tbl[convert(t1)]++;
			tar[convert(t2)]++;
			b[i][0]=convert(t1);
			b[i][1]=convert(t2);
		}
		int time;
		int availtrainA=0;
		int availtrainB=0;
		int sentA=0;
		int sentB=0;
		for(time=0;time<2400;time++)
		{
			if( time-T>=0)
			{
				if( tar[time-T] )
					availtrainA+=tar[time-T];
				if( tbr[time-T] )
					availtrainB+=tbr[time-T];
			}
			availtrainA-=tal[time];
			availtrainB-=tbl[time];
			if( availtrainA < 0)
			{
				sentA+=-availtrainA;
				availtrainA=0;
			}
			if( availtrainB < 0)
			{
				sentB+=-availtrainB;
				availtrainB=0;
			}
		}
		out<<"Case #"<<z+1<<": "<<sentA<<" "<<sentB<<endl;
	}
}
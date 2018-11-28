#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define MAX 100



//Name : GetNextToken
//This function returns next word from the bufer
//Parameters 
//buf : string buffer to scan.
//Returns: Next word from the buffer
char *GetNextToken(char *buf)
{
	char *token=NULL;
	int i=0;

	while(buf[i] != ' ' && buf[i] != '\0')
	{
		i++;
	}
	token = (char*)malloc(i+1);
	memset(token,0,i+1);
	strncpy(token,buf,i);
	return token;
}



struct TeamWin
{
	int total;
	int totalwin;
	int opp[MAX-1];
	int oppwin[MAX-1];
	float wp;
	float owp;
	float oowp;
};

int GetNonPlayedCount(char *stat,int totalmatch)
{
	int i;
	int count =0;
	for(i=0;i<totalmatch;i++)
	{
		if(stat[i]=='.')
			count++;
	}
	return count;

}

int GetWinCount(char *stat,int totalmatch)
{
	int i;
	int count =0;
	for(i=0;i<totalmatch;i++)
	{
		if(stat[i]=='1')
			count++;
	}
	return count;

}

int GetLossCount(char *stat,int totalmatch)
{
	int i;
	int count =0;
	for(i=0;i<totalmatch;i++)
	{
		if(stat[i]=='0')
			count++;
	}
	return count;

}

void SetOpponent(char *stat,int opp[],int oppwin[],int totalmatch)
{
	int i;
	int j=0;
	for(i=0;i<totalmatch;i++)
	{
		if(stat[i]=='1' || stat[i]=='0')
		{
			opp[j]=i;
			if(stat[i]=='1')
				oppwin[j]=1;
			else
				oppwin[j]=0;
			j++;
		}

	}
}

 float GetOppositeWP(struct TeamWin twp[MAX],int team)
{
	struct TeamWin t= twp[team];
	float wp =0;
	float oo=0;
	int i,j;
	for(i=0;i<t.total; i++)
	{
		oo=twp[t.opp[i]].wp;
		for(j=0;j<twp[t.opp[i]].total;j++)
		{
		if(twp[t.opp[i]].opp[j]==team)
		{
			if(twp[t.opp[i]].oppwin[j] == 1)
			{
				if(twp[t.opp[i]].totalwin != 0)
				oo = (float)(twp[t.opp[i]].totalwin - 1) / (float)(twp[t.opp[i]].total - 1);
			}
			else
			{
				oo = (float)twp[t.opp[i]].totalwin / (float)(twp[t.opp[i]].total -1);
			}
		}
		}
		wp +=oo ;
	}
	return wp/t.total;
}

float GetOppositeOWP(struct TeamWin twp[MAX],int team)
{
	struct TeamWin t= twp[team];
	float owp =0;
	int i;
	for(i=0;i<t.total; i++)
	{
		owp += twp[t.opp[i]].owp;
	}
	return owp/t.total;
}


void ExecuteTestCase(char team[MAX][MAX],int caseno,int teamcount)
{
	struct TeamWin wp[MAX]={0};
	int owp[MAX]={0};
	int oowp[MAX]={0};
	int i;
	float RPI=0;
	for(i=0;i<teamcount;i++)
	{
		wp[i].total = teamcount - GetNonPlayedCount(team[i],teamcount);
		wp[i].totalwin = GetWinCount(team[i],teamcount);
		wp[i].wp = (float)wp[i].totalwin/(float)wp[i].total;
		SetOpponent(team[i],wp[i].opp,wp[i].oppwin,teamcount);
	}

	for(i=0;i<teamcount;i++)
	{
	wp[i].owp = GetOppositeWP(wp,i);
	}
	for(i=0;i<teamcount;i++)
	{
	wp[i].oowp = GetOppositeOWP(wp,i);
	}
	printf("Case #%d:\n",caseno);
	for(i=0;i<teamcount;i++)
	{
		RPI=0;
		RPI= (0.25 * wp[i].wp) + (0.50 * wp[i].owp) + (0.25 * wp[i].oowp);
		printf("%.14g\n",RPI);
	}
}



int main(int argc,char *argv[])
{

	int i=0;
	int c=0;
	char testcase[BUFSIZ]="";
	int testcasecount=0;
	int candycount=0;
	int noofteams=0;
	int j;
	char team[MAX][MAX];
	FILE *fp=NULL;
	if(argc < 1)
	{
		fprintf(stderr,"Error : input file missing\n");
		exit(-1);
	}
	fp = fopen(argv[1],"r");
	if(NULL == fp)
	{
		fprintf(stderr,"Input file read error ");
		exit(-1);
	}

	fgets(testcase,BUFSIZ,fp);
	testcasecount = atoi(testcase);

	while(c < testcasecount)
	{
		memset(team,0,MAX*MAX);
		memset(testcase,0,BUFSIZ);
		noofteams=0;
		fgets(testcase,BUFSIZ,fp);
		noofteams= atoi(testcase);
		for(i=0;i<noofteams;i++)
		{
		memset(testcase,0,BUFSIZ);
		fgets(testcase,BUFSIZ,fp);
		for(j=0;j<noofteams;j++)
		team[i][j]=testcase[j];
		}
		ExecuteTestCase(team,c+1,noofteams);
		c++;
	}


	return 0;
}

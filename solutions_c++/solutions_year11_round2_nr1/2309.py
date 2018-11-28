#include <cstdio>
using namespace std;

bool hasplayed[105][105];
double wp[105][105]; // the wp of team i, excluding any games played against team j.
double owp[105];
double oowp[105];
bool haswon[105][105];
int numplayed[105];
int numwon[105];
double rpi[105];

void reset()
{
    for(int i=0; i<105; i++)
    {
	for(int j=0; j<105; j++)
	{
	    hasplayed[i][j]=0;
	    haswon[i][j]=0;
	    wp[i][j]=0;
	}
	owp[i]=0;
	oowp[i]=0;
	rpi[i]=0;
	numplayed[i]=0;
	numwon[i]=0;
    }
}

void printstuff(int n)
{
    printf("owp:\n");
    for(int i=0; i<n; i++)
    {
	printf("%lf\n", owp[i]);
    }

    printf("numplayed:\n");
    for(int i=0; i<n; i++)
    {
	printf("%d\n", numplayed[i]);
    }
    

}


int main()
{
    FILE* filein = fopen("q1in.txt", "r");
    FILE* fileout = fopen("q1out.txt", "w");

    int numtest;
    fscanf(filein, "%d", &numtest);
    for(int currtest=0; currtest<numtest; currtest++)
    {
	int numteams;
	fscanf(filein, "%d", &numteams);
	for(int i=0; i<numteams; i++)
	{
	    for(int j=0; j<numteams; j++)
	    {
		char tempc;
		fscanf(filein, "%c", &tempc);
		while(!(tempc == '0' || tempc == '1' || tempc == '.'))
		{
		    fscanf(filein, "%c", &tempc);
		}
		if(tempc=='0')
		{
		    hasplayed[i][j]=true;
		    haswon[i][j]=false;
		    numplayed[i]++;
		}
		if(tempc=='1')
		{
		    hasplayed[i][j]=true;
		    haswon[i][j]=true;
		    numplayed[i]++;
		    numwon[i]++;
		}
	//	printf("%c", tempc);
		// doesn't matter if it's a dot
	    }
	  //  printf("\n");
	}
	for(int i=0; i<numteams; i++)
	{
	    for(int j=0; j<numteams; j++)
	    {
		double top;
		double bottom;
		if(hasplayed[i][j])
		{
		    if(haswon[i][j])
		    {
			//wp[i][j]=(((double)(numwon[i]-1))/((double)(numplayed[i]-1)));
			top = (double)(numwon[i]-1);
			bottom = (double)(numplayed[i]-1);
		    }
		    else
		    {
			//wp[i][j]=(((double)numwon[i])/((double)(numplayed[i]-1)));
			top = (double)(numwon[i]);
			bottom = (double)(numplayed[i]-1);
		    }
		//    printf("for %d, disc %d: %lf / %lf\n", i, j, top, bottom);
		    wp[i][j]=top/bottom;
		}
		else
		{
		    wp[i][j]=((double)numwon[i]/(double)numplayed[i]);
		}
	    }
	    wp[i][i]=((double)numwon[i]/(double)numplayed[i]);
	}
	for(int i=0; i<numteams; i++)
	{
	    double culmwp=0.0;
	    for(int j=0; j<numteams; j++)
	    {
		if(hasplayed[i][j])
		{
		    culmwp+=wp[j][i];
		}
	    }
	    culmwp/=(double)numplayed[i];
	    owp[i]=culmwp;
	}
	for(int i=0; i<numteams; i++)
	{
	    double culmowp=0.0;
	    for(int j=0; j<numteams; j++)
	    {
		if(hasplayed[i][j])
		{
		    culmowp+=owp[j];
		}
	    }
	    culmowp/=(double)numplayed[i];
	    oowp[i]=culmowp;
	}
	fprintf(fileout, "Case #%d:\n", currtest+1);
	for(int i=0; i<numteams; i++)
	{
	    rpi[i] = (0.25*wp[i][i]) + (0.5*owp[i]) + (0.25*oowp[i]);
	    fprintf(fileout,"%.12lf\n", rpi[i]);
	}

/*	printf("******\n");
	for(int i=0; i<numteams; i++)
	{
	    for(int j=0; j<numteams; j++)
	    {
		printf("%lf ", wp[i][j]);
	    }
	    printf("\n");
	}
	printf("******\n");
	printstuff(numteams);*/
	reset();
    }
}

#include <cstdio>
#include <algorithm>
using namespace std;

int numTeams;
char** schedule = NULL;
double* wp = NULL;
double* owp = NULL;
double* oowp = NULL;

#define WIN 49
#define LOSE 48
#define NOPLAY 46


void processing(char** schedule) {
    
    int gamesOwp[numTeams][numTeams];
    int gamesOwpWon[numTeams][numTeams];
    
    for(int i=0; i < numTeams; i++) 
    {
        for(int j=0; j < numTeams; j++) 
        {
            gamesOwp[i][j] = 0;
            gamesOwpWon[i][j] = 0;
        }
    }
    
    for(int i=0; i < numTeams; i++) 
    {
        int games = 0;
        int gamesWon = 0;
        for(int j = 0; j < numTeams; j++) 
        {
            if(i == j) continue;
            if(schedule[i][j] == NOPLAY) {
            } else if(schedule[i][j] == WIN) {
                for(int g = 0; g < numTeams; g++) {
                    if(g == i) continue;
                    if(g == j) continue;
                    gamesOwp[i][g]++;
                    gamesOwpWon[i][g]++;
                }
                games++;
                gamesWon++;
            } else if(schedule[i][j] == LOSE) {
                for(int g = 0; g < numTeams; g++) {
                    if(g == i) continue;
                    if(g == j) continue;
                    gamesOwp[i][g]++;
                }
                games++;
            }
        }
        if(games > 0) {
            wp[i] = (double)gamesWon/(double)games;
        } else {
            wp[i] = 0;
        }
    }
    
    for(int i = 0; i < numTeams; i++)
    {
        double sum = 0;
        double divider = 0;
        for(int j = 0; j < numTeams; j++) {
            if(i == j) continue;
            // Is an opponent?
            if(schedule[i][j] == NOPLAY) continue;
            sum += (double)gamesOwpWon[j][i]/(double)gamesOwp[j][i];
            divider++;
        }
        if(divider > 0)
            owp[i] = sum/divider;
        else
            owp[i] = 0;
    }
    
    for(int i = 0; i < numTeams; i++)
    {
        double sum = 0;
        double divider = 0;
        for(int j = 0; j < numTeams; j++) {
            if(i == j) continue;
            // Is an opponent?
            if(schedule[i][j] == NOPLAY) continue;
            sum += owp[j];
            divider++;
        }
        if(divider > 0)
            oowp[i] = sum/divider;
        else
            oowp[i] = 0;
    }
    
    
}

int main ()
{
	int T, TC = 1;
    int numTeamsC, numTeamsCInner;

    for(scanf("%d", &T); TC <= T; TC++)
    {
        scanf("%d", &numTeams);
        schedule = new char*[numTeams];
        wp = new double[numTeams];
        owp = new double[numTeams];
        oowp = new double[numTeams];
        
	    for(numTeamsC = 1; numTeamsC <= numTeams; numTeamsC++)
		{
            schedule[numTeamsC-1] = new char[100];
            scanf("%s\n", schedule[numTeamsC-1]);
      	}
        processing(schedule);
		printf("Case #%d:\n", TC);
        for(int i = 0; i < numTeams; i++) {
            double rpi = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
            printf("%f\n", rpi);
        }
        delete wp;
        delete owp;
        delete oowp;
    }

    return 0;
}

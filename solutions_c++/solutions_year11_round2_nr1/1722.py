#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <map>
#include <vector>
#include <iostream>
#include <sstream>

using namespace std;

#ifndef max
#define max(a,b) ( (a > b) ? a : b)
#endif

float wp(char** games, int numTeams, int team, int skip){
  float numWins = 0.0f;
  float numGames = 0.0f;
  for(int i = 0; i < numTeams; i++){
    if(i == skip) continue;
    if(games[team][i] != '.'){
      numGames += 1.0f;
      if(games[team][i] == '1'){
	numWins += 1.0f;
      }
    }
  }
  return numWins/numGames;
}

float owp(char** games, int numTeams, int team){
  float total = 0.0f;
  float numOpponents = 0.0f;
  for(int i = 0; i < numTeams; i++){
    if(games[team][i] != '.'){
      total += wp(games, numTeams, i, team);
      numOpponents += 1.0f;
    }
  }
  return total/numOpponents;
}

float oowp(char** games, int numTeams, int team){
  float total = 0.0f;
  float numOpponents = 0.0f;
  for(int i = 0; i < numTeams; i++){
    if(games[team][i] != '.'){
      total += owp(games, numTeams, i);
      numOpponents += 1.0f;
    }
  }
  return total/numOpponents;
}

float rpi(char** games, int numTeams, int team){
  return (0.25f*wp(games, numTeams, team, -1)) + 
    (0.50f*owp(games, numTeams, team)) + (0.25f*oowp(games, numTeams, team));
}

int main(int argc, char** argv){
  char** games = NULL;
  if(argc > 1){
    FILE* file = fopen(argv[1], "r");
    char line[1024];
    if(file != NULL){
      fgets(line, 1024, file);
      int numCases = atoi(line);
      for(int i = 0; i < numCases; i++){
	fgets(line, 1024, file);
	int numTeams = atoi(line);

	games = new char*[numTeams];
	for(int j = 0; j < numTeams; j++){
	  games[j] = new char[numTeams];
	  fgets(line, 1024, file);
	  memcpy(games[j], line, numTeams*sizeof(char));
	}

	printf("Case #%d:\n", i+1);

	for(int j = 0; j < numTeams; j++){
	  printf("%f\n", rpi(games, numTeams, j));
	}

	for(int j = 0; j < numTeams; j++){
	  delete[] games[j];
	}
	delete[] games;	

      }
      fclose(file);
    }
  }
  return 0;
}


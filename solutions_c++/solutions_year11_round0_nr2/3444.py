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

int main(int argc, char** argv){
  vector<char> elements;
  map<string,char> combines;
  map<string,char> opposes;
  if(argc > 1){
    FILE* file = fopen(argv[1], "r");
    char line[1024];
    if(file != NULL){
      fgets(line, 1024, file);
      int numCases = atoi(line);
      for(int i = 0; i < numCases; i++){
	fgets(line, 1024, file);
	char* tokens = strtok(line, " ");
	int numCombines = atoi(tokens);
	for(int j = 0; j < numCombines; j++){
	   tokens = strtok(NULL, " ");

	   char comb[3];
	   comb[0] = tokens[0];
	   comb[1] = tokens[1];
	   comb[2] = '\0';
	   string s = comb;
	   combines[s] = tokens[2];

	}
	tokens = strtok(NULL, " ");
	int numOpposes = atoi(tokens);
	for(int k = 0; k < numOpposes; k++){
	  tokens = strtok(NULL, " ");

	   char opp[3];
	   opp[0] = tokens[0];
	   opp[1] = tokens[1];
	   opp[2] = '\0';
	   string s = opp;
	   opposes[s] = 'y';
	}
	tokens = strtok(NULL, " ");
	int n = atoi(tokens);
	tokens = strtok(NULL, " ");

	for(int h = 0; h < n; h++){
	  elements.push_back(tokens[h]);
	  int size = elements.size();
	  if(size > 1){
	    stringstream ss;
	    string temp;
	    ss << elements[size-2] << elements[size-1];
	    ss >> temp;
	    string revTemp;
	    stringstream rss;
	    rss << elements[size-1] << elements[size-2];
	    rss >> revTemp;
	    if(combines.find(temp) != combines.end()){
	      char fused = combines[temp];
	      elements.erase(elements.begin() + size - 1);
	      elements.erase(elements.begin() + size  - 2);
	      elements.push_back(fused);
	    }
	    else if(combines.find(revTemp) != combines.end()){
	      char fused = combines[revTemp];
	      elements.erase(elements.begin() + size - 1);
	      elements.erase(elements.begin() + size  - 2);
	      elements.push_back(fused);
	    }
	    size = elements.size();
	    if(size > 1){
	      char opp = elements[size - 1];
	      for(int i = 0; i < size - 1; i++){
		stringstream ss;
		string temp;
		ss << elements[i] << opp;
		ss >> temp;

		stringstream rss;
		string revTemp;
		rss << opp << elements[i];
		rss >> revTemp;

		if(opposes.find(temp) != opposes.end() ||
		   opposes.find(revTemp) != opposes.end()){
		  elements.clear();
		}
	      }
	    }
	  }
	}

	printf("Case #%d: [", i+1);
	for(unsigned int i = 0; i < elements.size(); i++){
	  printf("%c", elements[i]);
	  if(elements.size() - i > 1) printf(", ");
	}
	printf("]\n");
	elements.clear();
	combines.clear();
	opposes.clear();
      }
      fclose(file);
    }
  }
  return 0;
}


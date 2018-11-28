#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define MAX_LIST_SIZE 101

typedef struct{
	int8_t against[MAX_LIST_SIZE];
	int wins;
	int total;
	float owp, wp, oowp;
} team_t;

//Input stdin, output stdout. Obvious use of fd's!
int main(int argc, char* argv[]){
	int testcases, curcase;
	team_t teams[MAX_LIST_SIZE];
	int teamcount;

	//Get count of test cases
	fscanf(stdin, "%d", &testcases);

	//Solve all test cases
	for(curcase=1; curcase<=testcases; curcase++){
		//Get team count
		fscanf(stdin, "%d\n", &teamcount);
		
		//Get list of wins/losses
		for(int j=0; j<teamcount; j++){
			teams[j].wins = teams[j].total = 0;
			//Read all for one team
			for(int k=0; k<teamcount; k++){
				char res = fgetc(stdin);
				if(res == '.')teams[j].against[k] = 0;
				if(res == '1'){ teams[j].against[k] = 1; teams[j].wins++; teams[j].total++; }
				if(res == '0'){ teams[j].against[k] = -1; teams[j].total++; }
			}
				
			//Go ahead and calculate our own win ratio
			teams[j].wp = (float)teams[j].wins / (float)teams[j].total;
			
			//Read newline character
			fgetc(stdin);
		}
		
		//Calculate OWP of each
		for(int j=0; j<teamcount; j++){
			float temp = 0.0f, total = 0.0f;
			//Go over all ones we competed with
			for(int k=0; k<teamcount; k++){
				if(teams[j].against[k] == 0)continue;
				total += 1.0f;
				
				//Get contributation to owp
				if(teams[j].against[k] == 1){
					temp += (float)(teams[k].wins)/(float)(teams[k].total-1);
				} else{
					temp += (float)(teams[k].wins-1)/(float)(teams[k].total-1);
				}
			}
			teams[j].owp = temp / total;
		}
		
		//Calculate OOWP
		for(int j=0; j<teamcount; j++){
			float temp = 0.0f;
			for(int k=0; k<teamcount; k++){
				if(teams[j].against[k] == 0)continue;
				temp += teams[k].owp;
			}
			teams[j].oowp = temp / (float)teams[j].total;
		}

		printf("Case #%d:\n", curcase);
		for(int k=0; k<teamcount; k++){
			printf("%f\n", (teams[k].wp*0.25f + teams[k].owp*0.5f + teams[k].oowp*0.25f));
		}
	}

	return 0;
}

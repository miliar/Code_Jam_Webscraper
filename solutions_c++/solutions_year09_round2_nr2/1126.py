#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <algorithm>

using namespace std;

/*void GenerateString(string prefix, string model){
    


}

string Solve(string number){
    int ln = number.length();  
    
	// generate all possible strings
	for (int i = 0; i < ln; i++){



	}
}*/


int main()
{
	char filename[16];
	char infile[16], outfile[16];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");

	FILE *inf=fopen(infile, "r"), *outf=fopen(outfile, "w");
	//FILE *inf=fopen("A-large.in", "r"), *outf=fopen("A-large.out", "w");

	int N;
	fscanf(inf, "%d\n", &N);
    char lint[32];
  
	for(int m=1; m<=N; m++)
	{
		fgets(lint, 24, inf);	
		string  temp(lint);
		//cout << temp << endl;
		int ln = temp.length();

		if( next_permutation(lint, lint + ln - 1) ) {
			fprintf(outf, "Case #%d: %s", m, lint);
		} else {
			prev_permutation(lint, lint + ln - 1);
			//cout << lint << endl;
			char temp;
			for (int k = ln; k >= 0; k--){
				lint[k+1] = lint[k];						   
			}
			lint[0] = '0';
            next_permutation(lint, lint + ln);
            fprintf(outf, "Case #%d: %s", m, lint);
		}
	}

	fclose(inf); fclose(outf);
	return 0;
}

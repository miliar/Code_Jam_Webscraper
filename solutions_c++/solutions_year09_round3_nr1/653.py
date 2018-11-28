#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <algorithm>
#include <set>

using namespace std;

vector<long> pwr;
int base;

long Power(int exp){
	if (exp == 0) { pwr[exp] = 1; return 1; }
	if (pwr[exp] == 0) {
        pwr[exp] = base * Power(exp - 1);

        return pwr[exp];
	} else {
        return pwr[exp];
	}
}


int main()
{
	char filename[16];
	char infile[16], outfile[16];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");

	FILE *inf=fopen(infile, "r"), *outf=fopen(outfile, "w");


	int N;
	fscanf(inf, "%d\n", &N);
    char input[32];

	for (int k = 0; k < 65; k++){
		pwr.push_back(0);
	}
  
	for(int m=1; m<=N; m++)
	{
		pwr.clear();
		for (int k = 0; k < 65; k++){
		pwr.push_back(0);
	    }
		fgets(input, 24, inf);	
		string  temp(input);
		
		int ln = temp.length() - 1;
        //cout << ln << temp << endl;

		set<char> sett(input, input + ln);
        base = sett.size();
		if (base <= 1)  base = 2;
       // cout << base << endl;

        vector<int> vec(255, -1);
		vec[(int)input[0]] = 1;
		long long res = Power(ln - 1); 

		int minimum = 0;

		for (int i = 1; i < ln; i++){
			if (vec[(int)input[i]] != -1){
				res += vec[(int)input[i]] * Power(ln - i - 1);
			} else { 
				if (minimum == 1) minimum++;
                vec[(int)input[i]] = minimum;
				minimum++;
                res += vec[(int)input[i]] * Power(ln - i - 1);
			}
			//if (m == 12) cout << res << endl;
		}


		
        fprintf(outf, "Case #%d: %d\n", m, res);

	}

	fclose(inf); fclose(outf);
	return 0;
}
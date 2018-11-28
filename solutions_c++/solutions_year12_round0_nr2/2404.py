#include <string>
#include <fstream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <iostream>

using namespace std;

int best_results(vector<int>& scores, int surprises, int p);

int main(int argc, char** argv)
{
	
	FILE *fp1, *fp2;
	int cases, dancers, surprises, p;

	fp1 = fopen("input.in", "r");
	if(fp1 == NULL) return 1;
	fp2 = fopen("result.out", "w");
	if(fp2 == NULL) return 1;

	fscanf(fp1, "%d", &cases);
	for(int i = 0; i < cases; ++i) {
		fscanf(fp1, "%d", &dancers);
		fscanf(fp1, "%d", &surprises);
		fscanf(fp1, "%d", &p);
		//cout << dancers << " " << surprises << " " << p << " ";
		vector<int> scores;
		int score;
		for(int j = 0; j < dancers; ++j) {
			fscanf(fp1, "%d", &score);
			scores.push_back(score);
			//cout << score << " ";
		}
		//cout << endl;
		int best = best_results(scores, surprises, p);
		fprintf(fp2, "Case #%d: %d\n", i+1, best);
	}
	fclose(fp1);
	fclose(fp2);
	return 0;
}

int best_results(vector<int>& scores, int surprises, int p)
{
	int result = 0;
	for(int i = 0; i < scores.size(); ++i) {
		int base = scores[i] / 3;
		
		switch(scores[i] % 3) {
			case 0:
				if(base >= p)
					result++;
				else {
					if(surprises > 0 && base > 0 && base+1 >= p) {
						result++;
						surprises--;
					}
				}
				break;
			case 1:
				if(base+1 >=p || base >= p)
					result++;
				else {
					if(surprises > 0 && base+1 >= p) {
						result++;
						surprises--;
					}
				}
				break;
			case 2:
				if(base >= p || base+1 >=p)
					result++;
				else {
					if(surprises > 0 && base+2 >= p) {
						result++;
						surprises--;
					}
				}
		}
	
	}

	return result;

}

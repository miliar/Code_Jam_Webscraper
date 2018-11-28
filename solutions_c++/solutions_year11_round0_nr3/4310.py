#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <vector>

using namespace std;

bool finished = false;
unsigned int best_team1_weight = 0;
unsigned int best_team2_weight = 0;
unsigned int best_pile = 0;
bool possible = false;

void process_solution(int solution[], int k, vector<int> weights) {
	int i;				/* counter */
	unsigned int team1_weight = 0;
	unsigned int team1_normal_weight = 0;
	unsigned int team2_weight = 0;
	unsigned int team2_normal_weight = 0;
	unsigned int diff;
		
	//for (i = 0; i < k; i++) {
		//cout << solution[i] << endl;
	//}

	for (i=0; i<k; i++) {
		if (solution[i] == 1) { team1_weight = team1_weight ^ weights[i]; team1_normal_weight += weights[i]; }
		if (solution[i] == 2) { team2_weight = team2_weight ^ weights[i]; team2_normal_weight += weights[i]; }
	}
	if (team1_weight == 0 || team2_weight == 0) return;
	diff = abs(team1_weight - team2_weight);
	if (diff == 0) {
		possible = true;
		//cout << team1_weight << " " << team2_weight << endl;
		//for (i = 0; i < k; i++) {
		//	cout << solution[i] << endl;
		//}
		if (team1_normal_weight > best_pile) best_pile = team1_normal_weight;
		if (team2_normal_weight > best_pile) best_pile = team2_normal_weight;
	}
}

bool is_a_solution(int solution[], int k, int n) {
	//int i;
	return (k == n);
	/*
	int count_1 = 0, count_2 = 0;
	//cout << "passei" << endl;
	if (k == n) {		
		for (i = 0; i < n; i++) {
			if (solution[i] == 1) count_1++;
			if (solution[i] == 2) count_2++;
		}
		//cout << count_1 << " " << count_2 << endl;
		if (abs(count_1 - count_2) > 1)
			return false;
		else return true;
	} else return false;*/
}

void construct_candidates(int solution[], int k, int n, int c[], int *ncandidates, vector<int> weights) {
	int i;
	//int weight_1 = 0, weight_2 = 0;
	int weight = 0;
	c[0] = 1;
	c[1] = 2;
	*ncandidates = 2;

}


void backtrack(int solution[], int k, vector<int> weights) {
        int c[2];           /* candidates for next position */
        int ncandidates;                /* next position candidate count */
       int i;                          /* counter */
       
       //for (i = 0; i < weights.size(); i++) {
	//		cout << solution[i] << endl;
		//}

        if (is_a_solution(solution,k,weights.size()))
            process_solution(solution,k,weights);
        else {
				//cout << k << endl;
				//if (k == weights.size()) return;
                k = k+1;
                construct_candidates(solution,k,weights.size(),c,&ncandidates, weights);
                //cout << "passei" << endl;
                for (i=0; i<ncandidates; i++) {
						//cout << "cheguei" << endl;
                        solution[k] = c[i];
                        //cout << "cheguei" << endl;
                        backtrack(solution,k,weights);
                        //if (k == weights.size()) finished = true;
						if (finished) return;	/* terminate early */
       		}
		}
}

int main() {
	int num_cases, num_people, weight;
	int casen = 1;
	vector<int> weights;
	int solution[100];
	int i, j;
	int first_weight, second_weight;
	
	
	scanf("%d", &num_cases);
	while (num_cases > 0) {
		weights.clear();
		best_pile = 0;
		possible = false;
		
		scanf("%d", &num_people);
		for (i=0; i < num_people; i++) {
				scanf("%d", &weight);
				weights.push_back(weight);
				solution[i] = 0;
		}
		
		//for (i = 0; i < num_people; i++) {
		//	cout << weights[i] << endl;
		//}

		backtrack(solution, -1, weights);

		cout << "Case #" << casen++ << ": ";
		if (possible)
			cout << best_pile << endl;
		else cout << "NO" << endl;
		
		//for (i = 0; i < num_people; i++) {
		//	cout << weights[i] << endl;
		//}
	
		num_cases--;
	}

	

}

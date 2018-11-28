/*
 * dancers.cpp
 *
 *  Created on: Apr 13, 2012
 *      Author: kazemjahanbakhsh
 */
#include <iostream>

using namespace std;

//check if the solution is feasible
bool feasible(int points, int p, int& surp){
	int res = points % 3;
	int q1 = points / 3;
	int q2 = q1;
	if(res == 0){
		if(q1 >= p)
			return true;
		else{
			if(q1+1 >= p){
				q2--;
				if(q2 >= 0){
					surp++;
					return true;
				}
			}
		}
	}else if(res == 1){
		q1++;
		if(q1 >= p)
			return true;
	}else{
		q1++;
		if(q1 >= p)
			return true;
		else{
			if(q1+1 >= p){
				q2--;
				if(q2 >= 0){
					surp++;
					return true;
				}
			}
		}
	}

	return false;
}

int main(){
	int T, S, N, p, sol, surp, psurp;
	int tot_scores;
	cin >> T;
	for(int i = 0; i < T; i++){
		sol = 0;
		surp = 0;	//the surprising solutions
		psurp = 0;	//potential surprising
		cin >> N >> S >> p;
		for(int j = 0; j < N; j++){
			cin >> tot_scores;
			if(tot_scores != 30 && tot_scores != 29 && tot_scores != 1 && tot_scores != 0)
				psurp++;
			if(feasible(tot_scores, p, surp)){
				sol++;
			}
		}
		if(surp <= S){
			//if(S > sol - except)	sol = 0;
			if(S > psurp)	sol = 0;
		}else{
			sol = sol + S - surp;
		}

		cout << "Case #" << i+1 << ": " << sol << endl;
	}
	return 0;
}


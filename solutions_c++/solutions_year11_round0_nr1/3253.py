#include <iostream>
#include <fstream>
#include <cmath>
#define MAX_IN 100
using namespace std;

struct action
{
	char auth;
	int nr;
};

int strategy(action v[MAX_IN], int N)
{
	int i = 0, j = 0, t = 0, road = 0;;
	int gasitO = 0, gasitB = 0;
	action orange, black, targetO, targetB;
	orange.auth = 'O'; orange.nr = 1; black.auth = 'B', black.nr = 1;
	while(i < N || j < N) {
		if(!gasitO) {
			if(v[i].auth == 'O') {
				targetO.auth = v[i].auth; targetO.nr = v[i].nr;
				gasitO = 1;
			}
			else {
				i++;
				if(i >= N)
					gasitO = 1;
				}
		}
		if(!gasitB) {
			if(v[j].auth == 'B') {
				targetB.auth = v[j].auth; targetB.nr = v[j].nr;
				gasitB = 1;
			}
			else {
				j++;
				if(j >= N)
					gasitB = 1;
				}
		}										
		if(gasitO && gasitB) {
			if(i < j) {
				road = (targetO.nr - orange.nr >= 0 ? targetO.nr - orange.nr : orange.nr - targetO.nr);
				orange.nr = targetO.nr; 
				i++;
				gasitO = i < N ? 0 : 1;
				t += road + 1;
				if(j < N) {
					if(targetB.nr > black.nr) {
						black.nr = (black.nr + road + 1 > targetB.nr ? targetB.nr : black.nr + road + 1);
					}				
					else if(targetB.nr < black.nr) {
						black.nr = (black.nr - road - 1 < targetB.nr ? targetB.nr : black.nr - road - 1);
					}
				}
			}	
			else if(j < i) {
				road = (targetB.nr - black.nr >= 0 ? targetB.nr - black.nr : black.nr - targetB.nr);
				black.nr = targetB.nr; 
				j++;
				gasitB = j < N ? 0 : 1;
				t += road + 1;
				if(i < N) {
					if(targetO.nr > orange.nr) {
						orange.nr = (orange.nr + road + 1 > targetO.nr ? targetO.nr : orange.nr + road + 1);
					}		
					else if(targetO.nr < orange.nr) {
						orange.nr = (orange.nr - road - 1 < targetO.nr ? targetO.nr : orange.nr - road - 1);
					}
				}
			}
		}
	}		
	return t;
}

int main()
{
	ifstream in("A-large.in");
	ofstream out("output.txt");
	int T, N;
	action v[MAX_IN];
	in >> T;
	for(int j = 0; j < T; j++) {
		in >> N;	
		for(int i = 0; i < N; i++)
			in >> v[i].auth >> v[i].nr;
		int t = strategy(v, N);	
		out << "Case #" << j + 1 << ": " << t << endl;
	}
		
	return 0;
}

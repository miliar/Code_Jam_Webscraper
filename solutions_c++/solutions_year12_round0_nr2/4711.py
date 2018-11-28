#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
using namespace std;

int main () {
	int T, N, S, p, result, actualscore, neededscore, neededscore_surprising;
	ofstream myoutfile;
	ifstream myinfile;
	myoutfile.open ("out.txt");
	myinfile.open("in.txt");

	myinfile >> T;
	int i = 1;
	while (i<=T) {
		myinfile >> N >> S >> p;
		neededscore = 3 * p - 2;
		neededscore_surprising = 3 * p - 4;
		result = 0;
		for (int j = 0; j < N; j++)
		{
			myinfile >> actualscore;
			if(actualscore >= neededscore)
				result++;
			else
				if(actualscore >= neededscore_surprising && S > 0 && actualscore > 0)
				{
					result++;
					S--;
				}
		}
		myoutfile << "Case #" << i << ": " << result << '\n';
		i++;
	}
	myoutfile.close();
	myinfile.close();
	return 0;
}
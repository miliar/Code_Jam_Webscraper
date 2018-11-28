#include<vector>
#include<iostream>
#include<fstream>

using namespace std;

struct schedule{
	int i;//i-th operation
	int number;//move to number-th position
};

int main(int argc, char *argv[])
{
	ifstream ifs(argv[1]);
	int n;
	ifs >> n;
	for(int i=0;i<n;i++){
		int m;
		ifs >> m;
		vector<char> type(m), type_O, type_B;
		vector<int> number(m), number_O, number_B;
		vector<schedule> schedule_O, schedule_B;
		for(int j=0; j<m; j++){
			ifs >> type[j] >> number[j];
			schedule s = {j, number[j]};
			if(type[j] == 'O')
				schedule_O.push_back(s);
			else
				schedule_B.push_back(s);
		}

		vector<schedule>::iterator k_O = schedule_O.begin();
		vector<schedule>::iterator k_B = schedule_B.begin();
		int posO = 0, posB = 0;
		int j = 0, step = 0;
		while(j < m){
			bool isO;
			if(k_O == schedule_O.end())
				isO = false;
			else if(k_B == schedule_B.end())
				isO = true;
			else if(k_O != schedule_O.end() && k_B != schedule_B.end())
				isO = (*k_O).i < (*k_B).i;

			if(isO){
				if(posO < (*k_O).number)
					posO++;
				else if(posO > (*k_O).number)
					posO--;
				else{
					//push button
					k_O++;
					j++;
				}
				
				if(k_B != schedule_B.end()){
					if(posB < (*k_B).number)
						posB++;
					else if(posB > (*k_B).number)
						posB--;
				}
			}
			else{
				if(posB < (*k_B).number)
					posB++;
				else if(posB > (*k_B).number)
					posB--;
				else{
					//push button
					k_B++;
					j++;
				}
				
				if(k_O != schedule_O.end()){
					if(posO < (*k_O).number)
						posO++;
					else if(posO > (*k_O).number)
						posO--;
				}
			}
			step++;
		}
		cout << "Case #" << i+1 << ": " << step-1 << endl;
	}
}
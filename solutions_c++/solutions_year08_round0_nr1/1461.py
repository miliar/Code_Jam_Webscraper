#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
#include <map>


using namespace std;

#define WORD_SIZE       100
#define NAMES_AMOUNT 	150

map <string, int> hash;


int find_min(int table[], int n){

int i, min;
	min = table[0];
	printf("find min");
	for(i = 1; i < n; i++){
		if (table[i] < min){
			min = table[i];
		}
		printf("%d ", table[i]);
	}
	printf("\n");
	
	return min;

}


int main(){
	string line, current_line;

	char * cline;
	int N, names, queries, big, n, q, i, res, Count, Res = 0;
	string table_of_names[NAMES_AMOUNT];
	
	int counter[NAMES_AMOUNT], was[NAMES_AMOUNT];
	ofstream fout("A-large.out");
	ifstream f("A-large.in");
	//map <string, int> hash;
	if (f.is_open()){
		//f >> N;
		//std::cout << N << endl;
		getline(f, line);
		sscanf(line.c_str(), "%d", &N);
		
		for (big = 1; big <= N; big ++){
			//cout << "TUTAJ" << endl;
			getline(f, line);
			//cout << "test " << line.c_str() << endl;
			sscanf(line.c_str(), "%d ", &names);
			//f >> names;
			//std::cout << "names: " << names << endl;
			//getline(f, line);
			/* celaning counters */
			for (i = 0; i < NAMES_AMOUNT; i++ ){
				counter[i] = 0;
				was[i] = 0;
			}
			Count = 0;
			Res = 0;
			for(n = 1; n <= names; n++){
				getline(f, line);
				//printf("name: %s \n", line.c_str());
				hash[line] = n - 1;
				
				

			}
			//f >> queries;
			getline(f, line);
			sscanf(line.c_str(), "%d",  &queries);
			if (queries > 0){
				getline(f, line);
				current_line = line;
				was[hash[line]] = 1;
				Count = 1;
				for (q = 2; q <= queries; q++){
					//cout << q << " Count: " << Count << endl;	
					getline(f, line);
					//printf("current_line: %s, hash[line]: %d, hash[cur_line]: %d \n", current_line.c_str(), hash[line], hash[current_line]);
					if (!was[hash[line]]){
						was[hash[line]] = 1;
						Count++;
					}
					if (hash[line] != hash[current_line]){
							
						counter[hash[current_line]]++;
						current_line = line;
					
					}
					if (Count == names){
						Count = 1;
						Res++;
						for (i = 0; i < names; i++){
							was[i] = 0;
						}
						was[hash[current_line]] = 1;
					}
				}
				//res = find_min(counter, names);

			}
			else{
				//res = 0;
				Res = 0;

			}
			/*for (i = 1; i <= 5; i++ ){
				getline(f, line);
				std::cout << i << " line: " << line.c_str()  << endl;
			}*/
			//getline(f,line);
			//cout << "koniec " << line.c_str() << endl;
			//f >> names;
			//cout << "koniec " << names;
			fout << "Case #" << big << ": " << Res << endl;
		}/* for big */
		fout << flush;
		fout.close();
		f.close();

	}/*if is open */




}/* main() */

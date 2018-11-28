#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
using namespace std;

int main (int argc, char** argv) {
  string line;
  ifstream myfile (argv[1]);
  char outfile[255];
	sprintf(outfile, "%s.out", argv[1]);
  ofstream out ( outfile);
  if (myfile.is_open())
  {
	
      getline (myfile,line);
	int cases_count = atoi(line.c_str());
	for(int ni = 0; ni < cases_count; ni++) {
		//int switch_count = 0;
      		getline (myfile,line);
		int time_turnaround = atoi(line.c_str());
		cout << "time turn around :" << time_turnaround << endl;
      		//getline (myfile,line);
		// get Number of trips
		int NA, NB;
		myfile >> NA;
		myfile >> NB;
		
		cout << "name trips :" << NA << " " << NB << endl;
      			getline (myfile,line);
		vector<int> times_a_departure; 
		map<int,int> map_start_a;
		vector<int> times_a_arrive;
		vector<int> times_b_departure; 
		vector<int> times_b_arrive;
		map<int,int> map_start_b;
		for(int j = 0; j < NA; j++){
			int time = 0;
      			getline (myfile,line);
			cout << "Line for get time: " << line << endl;
			time = atoi(line.substr (0,2).c_str()) * 60 + atoi(line.substr(3,2).c_str());
			cout << time << endl;
			times_a_departure.push_back(time);
      			//getline (myfile,line);
			//cout << "Line for get time: " << line << endl;
			int ar;
			ar = atoi(line.substr (6,2).c_str()) * 60 + atoi(line.substr(9,2).c_str());
			//cout << time << endl;
			times_a_arrive.push_back( ar);
			map_start_a[j]=1;
		}
		for(int j = 0; j < NB; j++){
			int tmp;
			int time = 0;
      			getline (myfile,line);
			cout << "Line for get time: " << line << endl;
			time = atoi(line.substr (0,2).c_str()) * 60 + atoi(line.substr(3,2).c_str());
			cout << time << endl;
			times_b_departure.push_back(time);
      			//getline (myfile,line);
			//cout << "Line for get time: " << line << endl;
			int ar;
			ar = atoi(line.substr (6,2).c_str()) * 60 + atoi(line.substr(9,2).c_str());
			//cout << time << endl;
			times_b_arrive.push_back( ar);
			map_start_b[j]=1;
		}
		
		//sort(times_a_departure.begin(), times_a_departure.end());
		//sort(times_b_departure.begin(), times_b_departure.end());
		//sort for two keys order
	 for (int pass=1; pass < NA; pass++) {  // count how many times
       // This next loop becomes shorter and shorter
           for (int i=0; i < NA-pass; i++) {
                    if ((times_a_departure[i] > times_a_departure[i+1]) ||
			(times_a_departure[i] == times_a_departure[i+1] && times_a_arrive[i] > times_a_arrive[i+1])) {
                                       // exchange elements
                                        int temp = times_a_departure[i]; times_a_departure[i] = times_a_departure[i+1]; times_a_departure[i+1] = temp;
                                        temp = times_a_arrive[i]; times_a_arrive[i] = times_a_arrive[i+1]; times_a_arrive[i+1] = temp;
            }
           }
       }
	 for (int pass=1; pass < NB; pass++) {  // count how many times
       // This next loop becomes shorter and shorter
           for (int i=0; i < NB-pass; i++) {
                    if ((times_b_departure[i] > times_b_departure[i+1]) ||
			(times_b_departure[i] == times_b_departure[i+1] && times_b_arrive[i] > times_b_arrive[i+1])) {
                                       // exchange elements
                                        int temp = times_b_departure[i]; times_b_departure[i] = times_b_departure[i+1]; times_b_departure[i+1] = temp;
                                        temp = times_b_arrive[i]; times_b_arrive[i] = times_b_arrive[i+1]; times_b_arrive[i+1] = temp;
            }
           }
       }
       
		int i = 0, j = 0;
		int start_a = 0; 
		int start_b = 0; 	
			
		while ( i < NA || j < NB ) {
			int compare_a = 10000000;
			int compare_b = 10000000;
			if( i != NA)
			compare_a = times_a_departure[i];
			if( j != NB)
			compare_b = times_b_departure[j];
			if (compare_a < compare_b) {
				for( int k = j; k <NB; k++){
					int arr_d = times_a_arrive[i] + time_turnaround;
					if(arr_d <= times_b_departure[k] && map_start_b[k] != 0){
						map_start_b[k] = 0;
						break;
					}
				}
				i++;
			} else {
				for( int k = i; k <NA; k++){
					int arr_d = times_b_arrive[j] + time_turnaround;
					if(arr_d <= times_a_departure[k] && map_start_a[k] !=0){
						map_start_a[k] = 0;
						break;
					}
				}
				j++;
			} 	
		}
		
		for( int k = 0; k <NA; k++)
			start_a += map_start_a[k];
		for( int k = 0; k <NB; k++)
			start_b += map_start_b[k];
		out << "Case #" << ni + 1 << ": " << start_a << " " <<  start_b << endl;	
		
	}
    myfile.close();
    out.close();
  }

  else cout << "Unable to open file"; 

  return 0;
}


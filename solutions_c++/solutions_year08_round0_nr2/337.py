#include "iostream"
#include "cstdlib"
#include "string"
#include "stdio.h"

using namespace std;
#define COUT cout

int main(int argc, char * argv[]) {

	if(argc != 2) {
		cout << "usage: program_name input_file" << endl;
		exit(1);
	}
	
	FILE * fp = fopen(argv[1],"r");
	if(!fp) {
		cout << "input file " << argv[1] << " not exists" << endl;
		exit(2);
	}
	
	int num_testcase;
	char buffer[256];
	fgets(buffer, 256, fp);
	sscanf(buffer,"%d",&num_testcase); // 1st line
	//COUT << "num_testcase: " << num_testcase << endl;
	for(int i = 0; i < num_testcase; i++) {
		int turnaround, num_A, num_B;
		int num_time = 0;
		int time[1000];
		int todo[1000]; // 0 - leave A, 1 - arrive A, 2 - leave B, 3 - arrive B
		fgets(buffer, 256, fp);
		sscanf(buffer,"%d",&turnaround); // 2nd line
		fgets(buffer, 256, fp);
		sscanf(buffer,"%d %d",&num_A,&num_B); // 3rd line
		//COUT << "turnaround num_A num_B: " << turnaround << " " << num_A << " " << num_B << endl;
		for(int j = 0; j < num_A; j++) {
			int t1,t2,t3,t4;
			fgets(buffer, 256, fp);
			sscanf(buffer,"%d:%d %d:%d",&t1,&t2,&t3,&t4);
			time[num_time] = t1 * 60 + t2;
			todo[num_time] = 0;
			num_time++;
			time[num_time] = t3 * 60 + t4 + turnaround;
			todo[num_time] = 3;
			num_time++;
		}
		for(int j = 0; j < num_B; j++) {
			int t1,t2,t3,t4;
			fgets(buffer, 256, fp);
			sscanf(buffer,"%d:%d %d:%d",&t1,&t2,&t3,&t4);
			time[num_time] = t1 * 60 + t2;
			todo[num_time] = 2;
			num_time++;
			time[num_time] = t3 * 60 + t4 + turnaround;
			todo[num_time] = 1;
			num_time++;
		}
		
		//sort
		for(int j = 0; j < num_time; j++) { // safe
			for(int k = 0; k < num_time - 1; k++) {
				if((time[k] > time[k + 1]) ||
				   (time[k] == time[k + 1] &&
				    (todo[k + 1] == 1 || todo[k + 1] == 3) &&
					(todo[k] == 0 || todo[k] == 2))) {
					int time_temp = time[k];
					int todo_temp = todo[k];
					time[k] = time[k + 1];
					todo[k] = todo[k + 1];
					time[k + 1] = time_temp;
					todo[k + 1] = todo_temp;
				}			
			}
		}
		
		//for(int j = 0; j < num_time; j++) {
		//	COUT << time[j] << " : " << todo[j] << endl;
		//}
		
		int start_A = 0, start_B = 0;
		int current_A = 0, current_B = 0;
		
		for(int j = 0; j < num_time; j++) {
			if(todo[j] == 0) { // 0 - leave A
				if(current_A == 0) {
					start_A++;
					current_A++;
				}
				current_A--;
			} else if(todo[j] == 1) { // 1 - arrive A
				current_A++;
			} else if(todo[j] == 2) { // 2 - leave B
				if(current_B == 0) {
					start_B++;
					current_B++;
				}
				current_B--;
			} else if(todo[j] == 3) { // 3 - arrive B
				current_B++;			
			}
		}
		
		cout << "Case #" << (i+1) << ": " << start_A << " " << start_B << endl;
	}
	
	return 0;
	
}

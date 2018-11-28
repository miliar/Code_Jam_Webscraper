// Developed in visual C++ 2008 express edition
#include <iostream>
#include <fstream>



using namespace std;

int main(void){

	ifstream infile("A-large.in",ios::binary | ios::in );
	ofstream outfile("A-large.out",ios::binary | ios::out );


	int T;
	int moves;

	int total_time;
	int compensate_time;
	int blue_position;
	int orange_position;

	char curr_bot;
	char prev_bot;

	int steps;

	infile>>T;

//	int temp1;
//	int temp2;

	for(int i=0;i<T;i++){      // main loop

		infile>>moves;

total_time=0;
compensate_time=0;
blue_position=1;
orange_position=1;

curr_bot = 'P';
prev_bot = 'P';

char flag;
		for(int j=0;j<moves;j++){

			infile>>curr_bot;
			infile>>steps;

			if(curr_bot != prev_bot){
				flag='d';
			}
			else{
				flag='s';
			}

			switch(flag){

				case 'd':
					if (curr_bot == 'O'){

						int temp;
						temp=abs(steps - orange_position) + 1;
						if(compensate_time >= temp){
							total_time = total_time + 1; 
							compensate_time = 1;
						}else{

							int temp1;
							temp1 = temp - compensate_time;
							compensate_time = temp1;
							total_time = total_time + temp1;

						}
						
						orange_position = steps;

					}
					else{
						int temp;
						temp=abs(steps - blue_position) + 1;

						if(compensate_time >= temp){

							total_time = total_time + 1; 
							compensate_time = 1;
						
						}else{
			
							int temp1;
							temp1 = temp - compensate_time;
						    compensate_time = temp1;
							total_time = total_time + temp1;

						}

						blue_position = steps;

					}

					break;
//>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
				case 's':
					
					if (curr_bot == 'O'){
						
						int temp;
						temp=abs(steps - orange_position) + 1;
						total_time = total_time + temp; 
						compensate_time = compensate_time + temp;
                        orange_position = steps;
		
					}
					else{
	
						int temp;
						temp=abs(steps - blue_position) + 1;
						total_time = total_time + temp; 
						compensate_time = compensate_time + temp;
						blue_position = steps;
					
					}
				
					break;

			}

prev_bot=curr_bot;
		}
		outfile<<"Case #"<<i+1<<": "<<total_time<<"\n";

	}

}
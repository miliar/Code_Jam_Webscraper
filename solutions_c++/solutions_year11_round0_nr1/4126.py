/*
 * main.cpp
 *
 *  Created on: May 7, 2011
 *      Author: stefan
 */

#include <iostream>
#include <fstream>
#include <stdlib.h>

using namespace std;

#define MAX_BUTTONS 100

int main(){
	char file_name[] = "input.txt";
	ifstream in(file_name);

	if(in.is_open()){
		int T;
		in>>T;

		for(int round = 0; round < T; round++){
			int N;
			in>>N;

			char r[N];
			int m[N];

			int total_time = 0;

			int position_orange = 1;
			int position_blue = 1;

			int spare_orange_moves = 0;
			int spare_blue_moves = 0;

			for(int i = 0; i < N; i++){
				in>>r[i]>>m[i];

#ifdef DEBUG
				cout<<r[i]<<" "<<m[i]<<endl;
				cout<<"\tORANGE: "<<position_orange<<"; BLUE: "<<position_blue<<endl;
#endif

				int distance_to_execute = 0;
				switch (r[i]) {
					case 'O':
						distance_to_execute = abs(position_orange - m[i]) + 1;

#ifdef DEBUG
						cout<<"\tde: "<<distance_to_execute<<endl;

						cout<<"\ttime_before: "<<total_time<<endl;
#endif

						total_time = total_time +
								((spare_orange_moves - distance_to_execute) < 0 ?
										abs(spare_orange_moves - distance_to_execute) :
										1);

#ifdef DEBUG
						cout<<"\ttime_after: "<<total_time<<endl;
#endif

						spare_blue_moves = spare_blue_moves +
								((spare_orange_moves - distance_to_execute) < 0 ?
										abs(spare_orange_moves - distance_to_execute) :
										1);
						spare_orange_moves = 0;

						position_orange = m[i];

						break;
					case 'B':
						distance_to_execute = abs(position_blue - m[i]) + 1;

#ifdef DEBUG
						cout<<"\tde: "<<distance_to_execute<<endl;

						cout<<"\ttime_before: "<<total_time<<endl;
#endif

						total_time = total_time +
								((spare_blue_moves - distance_to_execute) < 0 ?
										abs(spare_blue_moves - distance_to_execute) :
										1);

#ifdef DEBUG
						cout<<"\ttime_after: "<<total_time<<endl;
#endif


						spare_orange_moves = spare_orange_moves +
								((spare_blue_moves - distance_to_execute) < 0 ?
										abs(spare_blue_moves - distance_to_execute) :
										1);
						spare_blue_moves = 0;

						position_blue = m[i];

						break;
					default:
						break;
				}
#ifdef DEBUG
				cout<<"\tspare_orange: "<<spare_orange_moves<<endl;
				cout<<"\tspare_blue: "<<spare_blue_moves<<endl;

				cout<<endl;
#endif
			}

			cout<<"Case #"<<round+1<<": "<<total_time<<endl;
#ifdef DEBUG
			getchar();
#endif
		}
	}
	else{
#ifdef DEBUG
		cerr<<"File "<<file_name<<" could not be read!"<<endl;
#endif
	}


	return 0;
}

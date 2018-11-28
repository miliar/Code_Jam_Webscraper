//      dancing.cpp
//      
//      Copyright 2012 Antonio <antonio@antonio-laptop>
//      
//      This program is free software; you can redistribute it and/or modify
//      it under the terms of the GNU General Public License as published by
//      the Free Software Foundation; either version 2 of the License, or
//      (at your option) any later version.
//      
//      This program is distributed in the hope that it will be useful,
//      but WITHOUT ANY WARRANTY; without even the implied warranty of
//      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//      GNU General Public License for more details.
//      
//      You should have received a copy of the GNU General Public License
//      along with this program; if not, write to the Free Software
//      Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
//      MA 02110-1301, USA.


//      bots.cpp
//      
//      Copyright 2011 Antonio <antonio@antonio-laptop>
//      
//      This program is free software; you can redistribute it and/or modify
//      it under the terms of the GNU General Public License as published by
//      the Free Software Foundation; either version 2 of the License, or
//      (at your option) any later version.
//      
//      This program is distributed in the hope that it will be useful,
//      but WITHOUT ANY WARRANTY; without even the implied warranty of
//      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//      GNU General Public License for more details.
//      
//      You should have received a copy of the GNU General Public License
//      along with this program; if not, write to the Free Software
//      Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
//      MA 02110-1301, USA.


#include <iostream>
#include <fstream>
#include <string.h>
#include <cstdlib>

using namespace std;


//Logic
int main(int argc, char** argv)
{
	char cycles_char[4] = {0};
	int cycles = 0;
	char dancers[3] = {0};
	char surprise[3] = {0};
	char best[2] = {0};
	int operations= 0;
	
	
	string filename = argv[1];
	//Open the filename
	ifstream file_inst (filename.c_str());
	ofstream file_output;
	file_output.open("dancing_googlers.out",ios::out);
	file_inst >> cycles_char;
	cycles = atoi(cycles_char);
	for(int i = 0 ; i < cycles ; i++)
	{
		//Parse every line
		int dancers_int = 0;
		int surprise_int = 0;
		int best_int = 0;
		file_inst >> dancers;
		dancers_int = atoi(dancers);
		file_inst >> surprise;
		surprise_int = atoi(surprise);
		file_inst >> best;
		best_int = atoi(best);
		char total_points [dancers_int][2];
		int total_points_int [dancers_int]; //= {0};
		bool point_above [dancers_int]; //= {false};
		bool special_case_needed [dancers_int]; //= {false};
		for (int xx = 0 ; xx < dancers_int ; xx++)
		{
				point_above[xx] = false;
				special_case_needed[xx] = false;
		}
		for (int r = 0; r < dancers_int ; r++)
		{
				//Analyze every candidate to see if he or she is a candidate
				file_inst >> total_points[r];
				total_points_int[r] = atoi(total_points[r]);
				cout << "The value of total_points is " <<  total_points_int[r] << endl;
				int average = total_points_int[r] / 3;
				if(average >= (best_int - 2))
				{
					cout << "The value of average is "<<average << " and best_in "<<best_int << endl;
					//Possible candidate
					if(average >=  best_int)
					{
							//For sure better
							cout << "For sure it is better" << endl;
							point_above[r] = true;
					}
					//Yes
					else if(average >= (best_int - 1 ))
					{
						float precision = float(total_points_int[r]) / 3;
						cout << "The value of precision inside yes is "<<precision << endl;
						if(precision > float(best_int - 1))
						{
								point_above[r] = true;
								cout << "Enter value above "<<endl;
						}
						else if(precision == float(best_int - 1) && precision > 0)
						{
								cout << "Enter equal" << endl;
								special_case_needed[r] = true;	
						}
					}
					//Yes with special case
					else if(average >= (best_int - 2))
					{
						float precision = float(total_points_int[r]) / 3;
						if(precision > float(best_int - 2) + 0.5 && precision > 0)
						{
							cout << "The value of precision inside special case is "<<precision << endl;
							cout << "Enter special case" << endl;
							special_case_needed[r] = true;	
						}
					}					
				}		
		}
		int max_dancers_p = 0;
		for(int p = 0; p < dancers_int; p++)
		{
			if(point_above[p] == true)
			{
					cout << "Point above is true" << endl;
					max_dancers_p++;
			}
			else if (special_case_needed[p] == true)
			{
				cout << "The value of suprise int is "<<surprise_int << endl;
				if(surprise_int > 0)
				{
					max_dancers_p++;
					surprise_int--;
				}
			}
		}
		//Print the maximum is 			
		cout<<"THE MAXIMUM NUMBER OF DANCERS IS "<<max_dancers_p << endl;
		file_output<<"Case #"<<i+1<<": "<<max_dancers_p << endl;
	}
	file_inst.close();
	file_output.close();
	return 0;
}


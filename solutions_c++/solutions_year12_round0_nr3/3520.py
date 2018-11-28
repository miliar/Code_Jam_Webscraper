//      recycled.cpp
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
#include <cmath>
using namespace std;


//Logic
int main(int argc, char** argv)
{
	char cycles_char[4] = {0};
	int cycles = 0;
	
	char high_limit[7] = {0};
	char low_limit[7] = {0}; 
	string filename = argv[1];
	//Open the filename
	ifstream file_inst (filename.c_str());
	ofstream file_output;
	file_output.open("recycled.out",ios::out);
	file_inst >> cycles_char;
	cycles = atoi(cycles_char);
	for(int ii = 0 ; ii < cycles ; ii++)
	{
		//Parse every line
		int less_limit = 0;
		int bigger_limit = 0;
		file_inst >> low_limit;
		less_limit = atoi(low_limit);
		cout << "Lower limit is "<<less_limit <<  endl;
		file_inst >> high_limit;
		bigger_limit = atoi(high_limit);
		cout << "Bigger limit is "<<bigger_limit << endl;
		//Calculate the number of decimals
		int dec_degree = 0;
		int counter_degree = 1;
		int divisor = pow(10,counter_degree);
		int temp_calc = (bigger_limit/divisor);
		while (temp_calc > 0)
		{
			//cout << "Enter the while and temp_calc is " <<temp_calc << endl;
			//cout << "The value of divisor is "<<divisor << endl;
			counter_degree++;
			dec_degree++;
			divisor = pow(10,counter_degree);
			temp_calc = (bigger_limit/divisor);
		}
		cout << "The value of dec degrees is " << dec_degree <<  endl;
		int matches = 0;
		int last = -989846;
		int last_temp = 788798;
		int first = -145641;
		for (int i = less_limit ; i <= bigger_limit ; i++)
		{
			//Analyze every number, i number, c candidate
			if(dec_degree == 0)
				break;
			for (int c = less_limit ; c <= bigger_limit ; c++)
			{
				//Do all the possible combinations for that candidate
				for (int x = 1 ; x <= dec_degree ; x++)
				{
					//last = c/(x*10);
					if(c >= i)
					{
						break;
					}
					last_temp = c/(pow(10,x));
					last = c - last_temp*pow(10,x);
					if (i == 21 && c == 12)
					{
						cout << "The value of last is "<<last << endl;
					}
					//First bad calculates
					first = i/(pow(10,dec_degree + 1 - x));
					if (i == 21 && c == 12)
					{
						cout << "The value of first is "<<first << endl;
					}
					if(last == first)
					{
						//Check rest of number is equal
						if( i == 21 && c == 12)
						{
								cout << "Enter las first yeah!!" << endl;
						}
						int remaining_i = i - first*pow(10,dec_degree + 1 - x);
						int remaining_c = (c - last)/(pow(10,x));
						if( i == 21 && c == 12)
						{
								cout << "Remanining i is " << remaining_i << " Remaining c is "<<remaining_c <<  endl;
						}
						if( remaining_i == remaining_c)
						{
								matches++;
								break;
						}
					};
					//If no match	
				}					
			}
			int last = -989846;
			int last_temp = 788798;
			int first = -145641;
		} 
		
		
		//Print the maximum is 			
		cout<<"THE MAXIMUM NUMBER OF RECYCLES IS "<<matches << endl;
		file_output<<"Case #"<<ii+1<<": "<<matches << endl;
	}
	file_inst.close();
	file_output.close();
	return 0;
}


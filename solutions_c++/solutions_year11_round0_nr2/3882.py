//      magicka.cpp
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

//Functions pre
bool are_combinations(char * invoked_array, char matrix_combinations[37][4], int * index, int matrix_size);
bool are_opposed(char * invoked_array, char matrix_opposed[29][3], int * index, int matrix_size);



using namespace std;
int main(int argc, char** argv)
{
	string filename = argv[1];
    ifstream file_input (filename.c_str());
	ofstream file_output;
	file_output.open("magicka.out",ios::out);
	int cases = 0;
    file_input >> cases;
	//cout << cases << endl;
	for(int i = 0; i < cases ; i++)
	{
			//Recognize the number of combinations
			int combinations = 0;
			file_input >> combinations;
			//cout<<"The value of combinations is "<<combinations<<endl;
			//Save every combination of elements
			char matrix_combination[37][4] = {{0},{0}};
			//int combinations_in = combinations * 3;
			for(int j = 0; j < combinations ; j++)
			{
					file_input >> matrix_combination[j][0]; 
				    file_input>> matrix_combination[j][1];
				    file_input>>matrix_combination[j][2];
			}
			//Once that done, store the oppsite elements
			int oppose = 0;
			file_input >> oppose;
			//cout<<"The value of oppose is "<<oppose<<endl;
			char matrix_opposed[29][3] = {{0},{0}};
			//cout << "The value of oppose is "<<oppose << endl;
			//int oppose_in = oppose * 2;
			for(int j = 0 ; j < oppose ; j ++)
			{
					file_input>>matrix_opposed[j][0];
					file_input>>matrix_opposed[j][1];
			}
			//Start the invocation, always checking for possible combinations and opposed letters
			char invoked_array[100] = {0};
			int invoked = 0;
			int index = 0;
			bool modification_combinations = false;
			bool modification_opposed = false;
			file_input >> invoked;
			//cout<<"THe value of invoked is "<<invoked<<endl;
			for(int j = 0; j<invoked; j++)
			{
					file_input >> invoked_array[index];
					//cout<<"The value of invoked array is "<<invoked_array[index]<<endl;
					//Analyze for possible combinations
					modification_combinations = are_combinations(invoked_array,matrix_combination, &index, combinations);
					//Analyze for possible 
					modification_opposed = are_opposed(invoked_array, matrix_opposed,&index, oppose);
					if(modification_combinations == false && modification_opposed == false)
						index++;
					//cout<<"The value of index is "<<index<<endl;
					modification_combinations = false;
					modification_opposed = false;
			}
			i++;
			file_output<<"Case #"<<i<<": "<<"[";
			i--;
			index--;
			for(int z = 0 ; z <= index; z++)
			{
				if(z < index)
					file_output<<invoked_array[z]<<", ";
				else if (z==index)
					file_output<<invoked_array[z]<<"]"<<endl;
			}
			if(index == -1)
				file_output<<"]"<<endl;
	}
	return 0;
}

bool are_combinations(char * invoked_array, char matrix_combinations[37][4], int * index, int matrix_size)
{
		//Check if there are combinations in the invoked array
		char (*matrix)[4] = matrix_combinations; 
		char * array = invoked_array;
		int indice = *index;
		int last_analyzed = indice - 1;
		int tamano_matriz = matrix_size;
		int less_index = -1;
		bool hit = false;
		for(int i = 0 ; i < tamano_matriz; i++)
		{
			char temporal_one =  matrix[i][0];
			char temporal_two = matrix[i][1];
			char result_in_case = matrix[i][2];
			//cout<<"Temporal_one is "<<matrix[i][0]<<endl;
			//cout<<"Temporal two is "<<matrix[i][1]<<endl;
			//cout<<"Temporal three is "<<matrix[i][2]<<endl;
			if((temporal_one ==  array[indice] || temporal_two == array[indice]) && (temporal_one == array[last_analyzed] || temporal_two == array[last_analyzed]) && (array[indice] != array[last_analyzed] || temporal_two == temporal_one))
			{
					//The we gotta make the subsitution
					array[indice] = 0;
					array[last_analyzed] = result_in_case;
					indice--;//Point to the new end
					last_analyzed = indice - 1;				
					less_index = indice;
					hit = true;
					i = 0;
			}
		}
		int *indice_mod = index;
		if(less_index != -1)
			{
			less_index++;
			*indice_mod = less_index;
			}
		//cout<<"The index in combination is "<<*indice_mod<<endl;
		//cout<<"The value of hit is "<<hit<<endl;
		return hit;
}

bool are_opposed(char * invoked_array, char matrix_opposed[29][3], int * index, int matrix_size)
{
	char (*matrix)[3] = matrix_opposed;
	char * array = invoked_array;
	int *indice =  index;
	int indice_temporal = *indice;
	int tamano_matriz = matrix_size;
	//bool hit = false;
	bool first_one = false;
	bool second_one = false;
	for(int i = 0 ; i < tamano_matriz; i++)
	{
		for(int p = 0 ; p < 2 ; p++)
		{
			for(int k=0; k <= indice_temporal ; k++)
			{
				//cout<<"Array k is "<<array[k]<<endl;
				//cout<<"Marix [i][p] is "<<matrix[i][p]<<endl;
					if(array[k]==matrix[i][p])
					{
							//cout<<"Found true someting"<<endl;
							if(p==0)
								first_one = true;
							else if (p == 1)
								second_one=true;
					}	
			}
			if(first_one == true && second_one == true)
			{//Eliminate all values in the array
				while(indice_temporal >= 0)
				{
						array[indice_temporal] = 0;
						indice_temporal--;
				}
				*indice=0;
				return true;	
			}
		}
	}
	return false;
}


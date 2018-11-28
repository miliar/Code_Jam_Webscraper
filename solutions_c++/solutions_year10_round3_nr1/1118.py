//      main.cpp
//      
//      Copyright 2010 Ryan <ryan@ryan-laptop>
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

#include <fstream>
#include <iostream>
#include <string>

using namespace std;\

/*

struct directory
 {  
	  string name;
	  directory *subs[1000];
	  int numsubs;
 };

directory *existing[1000];

*/

int A[1500];
int B[1500];


int total,intersect;


int main(int argc, char** argv)
{
	
	
	
	int tempA;
	int tempB;
	int wires;
		
	ifstream fp("input.in");
    ofstream op ("output.txt");
	fp >> total;
	for ( int i = 1; i <= total; i++){
		intersect = 0;
		fp >> wires;
		for ( int j = 0; j < wires; j++){
			fp >> A[j];
			fp >> B[j];
		}
		for ( int k = 0; k < wires; k++){
			tempA = A[k];
			tempB = B[k];
			for ( int l = 0; l < wires; l++){
				if ( l != k ){
					if ( (A[l] < tempA && B[l] > tempB) || (A[l] > tempA && B[l] < tempB)){
						intersect++;
						
					}
				}
			}
		}
		op << "Case #" << i <<": " << intersect/2 << endl;
	}
}
		
		
	
		
	
		


/***************************************************************************
 *   Copyright (C) 2008 by Eugene   *
 *   eugene@eugene-desktop   *
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 *   This program is distributed in the hope that it will be useful,       *
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
 *   GNU General Public License for more details.                          *
 *                                                                         *
 *   You should have received a copy of the GNU General Public License     *
 *   along with this program; if not, write to the                         *
 *   Free Software Foundation, Inc.,                                       *
 *   59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.             *
 ***************************************************************************/


#ifdef HAVE_CONFIG_H
#include <config.h>
#endif

#include <iostream>
#include <fstream>
#include <iomanip.h>
#include <cstdlib>
#include <string>

using namespace std;

int N = 0;
int S = 0;
int Q = 0;
int switches = 0;

string engines[100] = {""};
bool marked[100] = {false};

int clearEngines() {	
	for (int i=0; i<S; i++) engines[i] = "";	
	return 1;
}

int clearMarks() {
	for (int i=0; i<S; i++) marked[i] = false;
	return 1;
}

int mark(string engine) {
	for (int i=0; i<S; i++) {
		if (engines[i] == engine) {
			marked[i] = true;
		}
	}
		
	return 1;		
}

bool allMarked() {
	
	for (int i=0; i<S; i++) {
		if (!marked[i]) return false;
	}
	
	return true;
}


int main(int argc, char *argv[])
{

	ifstream input;
	input.open("input");
	
	ofstream output;
	output.open("output");
	
	input >> N;
	
	string temp;
	for (int X=0; X<N; X++) {
		
		clearEngines();
		clearMarks();
		
		switches = 0;
		
		input >> S;
		
		int i = 0;		
		for (i=0; i<S; i++) {
			input >> temp;
			engines[i] = temp;
			//cout << i << ":" << temp << endl;
		}
		
		input >> Q;		
		for (i=0; i<Q; i++) {
			input >> temp;
			//cout << i << ":" << temp << endl;
			
			mark(temp);
			if (allMarked()) {
				clearMarks();
				switches++;
				mark(temp);
			}
			
		}
		
		output << "Case #" << X+1 << ": " << switches << endl;
		
		
	}

  return EXIT_SUCCESS;
}

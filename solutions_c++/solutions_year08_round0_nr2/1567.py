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
#include <cstdlib>
#include <fstream>
#include <string>
#include <algorithm>


using namespace std;

int N = 0;
int T = 0;
int NA = 0;
int NB = 0;

int times[400];
int t = 0;

int a, b;
int aStart, bStart;

struct route {
	int start;
	int end;
	bool sent;
	bool came;
} A[100], B[100];

int clearRoutes() {
	
	for (int i=0; i<NA; i++) {
		A[i].start = 0;
		A[i].end = 0;
		A[i].sent = false;
		A[i].came = false;
	}
	
	for (int i=0; i<NB; i++) {
		B[i].start = 0;
		B[i].end = 0;
		B[i].sent = false;
		B[i].came = false;
	}
	
}

int main(int argc, char *argv[])
{
  ifstream input;
	input.open("input");
	
	ofstream output;
	output.open("output");
	
	input >> N;
	
	for (int x=0; x < N; x++) {
		
		input >> T;
		input >> NA;
		input >> NB;
		
		clearRoutes();
		
		int i = 0;
		int t = 0;
		
		string temp;
		
		int h = 0;
		int m = 0;
				
		for (i=0; i < NA; i++) {
			input >> temp;			
			sscanf(temp.c_str(), "%d:%d", &h, &m);
			A[i].start = h*60 + m;
			
			times[t] = h*60 + m;
			t++;
			
			input >> temp;
			sscanf(temp.c_str(), "%d:%d", &h, &m);
			A[i].end = h*60 + m + T;
			
			times[t] = h*60 + m + T;
			t++;
			
			//cout << h << " : " << m << endl;
		}
		
		for (i=0; i < NB; i++) {
			input >> temp;
			sscanf(temp.c_str(), "%d:%d", &h, &m);
			B[i].start = h*60 + m;
			
			times[t] = h*60 + m;
			t++;
			
			input >> temp;			
			sscanf(temp.c_str(), "%d:%d", &h, &m);
			B[i].end = h*60 + m + T;
			
			times[t] = h*60 + m + T;
			t++;
			
			//cout << h << " : " << m << endl;
		}
		
		int elements = sizeof(times) / sizeof(times[0]);		
		std::sort(times, times + t);
		
		//for (i = 0; i < t; ++i) cout << times[i] << ' ';
		
		int r;
		
		a = 0;
		b = 0;
		aStart = 0;
		bStart = 0;
		
		for (i=0; i<t; i++) {
			
			for (r=0; r< NA; r++) {				
				if ((A[r].end == times[i]) && (A[r].came == false)) {
					// train came to B
					
					b++;
					A[r].came = true;
				}				
			}
								
			for (r=0; r<NB; r++) {
				if ((B[r].end == times[i]) && (B[r].came == false)) {
					// train came to A
					
					a++;
					B[r].came = true;
				}
			}
			
			for (r=0; r< NA; r++) {				
				if ((A[r].start == times[i]) && (A[r].sent == false)) {
					// start new train from A
					
					if (a == 0) {
						aStart++;
					} else {
						a--;
					}
					
					A[r].sent = true;										
				}				
			}
			
			for (r=0; r< NB; r++) {
				if ((B[r].start == times[i]) && (B[r].sent == false)) {
					// start new train from B
					
					if (b == 0) {
						bStart++;
					} else {
						b--;
					}
					
					B[r].sent = true;
				}
			}
		}
		
		output << "Case #" << x+1 << ": " << aStart << " " << bStart << endl;

	}

  return EXIT_SUCCESS;
}

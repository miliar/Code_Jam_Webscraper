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
#include <algorithm>
#include <vector>
#include <math.h>

using namespace std;

vector<long long> freq;
long long P, K, L;

int main(int argc, char *argv[])
{
  ifstream input;
	input.open("input");
	
	ofstream output;
	output.open("output");
	
	long long C;
	
	input >> C;
	
	for (long long x=1; x<=C; x++) {
		
		input >> P >> K >> L;
		
		freq.clear();
		freq.resize(L+1);
		
		long long l = 0;
		long long f;
		for (l=1; l<= L; l++) {
			input >> f;
			freq[l] = f;
		}
		
		sort(freq.begin(), freq.end());
		
		output << "Case #" << x << ": ";		
		
		if (K*P < L) {
			output << "Impossible";
		} else {
		
			long long presses = 0;
					
			for (l=L; l>0; l--) {
				
				double repeats;
				repeats = floor(1+floor((L-l)/K));
				
				//cout << freq[l] << "*" << repeats << "+";
				
				presses+= freq[l]*repeats;
			}
			
			output << presses;
		
		}
		
		output << endl;
	}

  return EXIT_SUCCESS;
}

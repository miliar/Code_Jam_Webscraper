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
#include <math.h>
#include <vector>

using namespace std;

const double eps = 1e-12;

typedef struct point {
	int x, y;
};

vector<point> trees;
vector<long long> treeX, treeY;
long long n, A, B, C, D, M; 
long long xx0, yy0;

bool inTree(long long a, long long b, long long c) {
	
	double xa = treeX[a];
	double xb = treeX[b];
	double xxc = treeX[c];
	
	double ya = treeY[a];
	double yb = treeY[b];
	double yyc = treeY[c];
	
	double xc = ((xa+xb+xxc)/3);
	double yc = ((ya+yb+yyc)/3);
	
	
	//cout << xc << " " << yc << " ";
	/*
	for(int i=0; i<n; i++) {
		if ((treeX[i] == xc) && (treeY[i] == yc))  {
			return true;
		}
	}
	*/
	
	//cout << xc << " " << yc << " ";
	
	
	if ((fabs(xc - round(xc)) < eps) && (fabs(yc - round(yc)) < eps)) {
		return true;
	}
	
	/*
	for (int i=0; i<n; i++) {
		
		double xi = treeX[i];
		
		if ((fabs(xc - xi) < eps)  && (fabs(yc - round(yc)) < eps)) {
			
			//cout << xc << " " << yc << " ";
			return true;	
			
		}
	}
	
	for (int j=0; j<n; j++) {
				
		double yi = treeY[j];
				
		if ((fabs(yc - yi) < eps) && (fabs(xc - round(xc)) < eps)) {
			
			//cout << xc << " " << yc << " ";
			return true;
		}
	}
	*/
	/*
	for (int i=0; i<n; i++) {
		
		double xi = treeX[i];
		
		if ((fabs(xc - xi) < eps)) {
			
			for (int j=0; j<n; j++) {
				
				double yi = treeY[j];
				
				if ((fabs(yc - yi) < eps)) {
			
					return true;
				}
			}				
		}
	}
	*/
	return false;
}

int main(int argc, char *argv[])
{
	ifstream input;
	input.open("input");
	
	ofstream output;
	output.open("output");
	
	long long N;
	
  input >> N;
	long long i;
	long long X, Y;
	long long T = 0;
	for (int x=0; x < N; x++) {		
		
		A = 0; B = 0; C = 0; D = 0; xx0 = 0; yy0 = 0; M = 0; n = 0;
		
		input >> n >> A >> B >> C >> D >> xx0 >> yy0 >> M;
		
		treeX.clear();
		treeY.clear();
		
		X = xx0;
		Y = yy0;
		
		for (i=0; i < n; i++) {
			
			//cout << X << " " << Y << endl;
			treeX.push_back(X);
			treeY.push_back(Y);
			X = (A * X + B)%M;
			Y = (C * Y + D)%M;
		}
		
		long long a, b, c;
		T = 0;
		for (a=0; a < n; a++) {
			for (b=a+1; b<n; b++) {
				for (c=b+1; c<n; c++) {
					if (inTree(a,b,c)) {
						T++;
					}
				}
			}
		}
		//cout << endl;
		output << "Case #" << x+1 << ": " << T << endl;
		
	}

  return EXIT_SUCCESS;
}

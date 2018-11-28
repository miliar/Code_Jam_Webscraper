//      main.cpp
//      
//      Copyright 2012 Alessio Barducci <alessio@alessio-laptop>
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
#include <vector>
#include <iomanip>

using namespace std;


int main(int argc, char** argv)
{
	ifstream in("A-small-attempt0.in");
	ofstream out("output.txt");
	int T;
	in >> T;
	
	for (int i = 0; i < T; i++)
	{
		cout << i << endl;
		int A, B;
		in >> A >> B;
		vector<double>* p = new vector<double>;
		for (int j = 0; j < A; j++)
		{
			double tmp;
			in >> tmp;
			p->push_back(tmp);
		}
		
		int* right = new int[A]();
		for (int j = 0; j < A; j++)
			right[j] = 0;
		
		double* exp = new double[A + 2]();
		for (int j = 0; j < A + 2; j++)
			exp[j] = 0;
		
		bool cont = true;
		while (cont)
		{
			int minErr = -1;
			double prob = 1;
			for (int j = 0; j < A; j++)
				if (right[j] == 0)
					prob = prob * p->at(j);
				else
				{
					prob = prob * (1 - p->at(j));
					if (minErr == -1)
						minErr = j;
				}
		
			
				int case1 = 0;
				if (minErr == -1)
					case1 = B - A + 1;
				else
					case1 = B - A + 1 + B + 1;
				
				exp[0] += prob * (double)case1;
					
				
				for (int j = 0; j < A; j++)
				{
					int case2;
					if (minErr == -1 || minErr >= (A - (j + 1)))
						case2 = (j + 1) + (B - A + (j+1)) + 1;
					else
						case2 = (j + 1) + (B - A + (j+1)) + 1 + B + 1;
					
					exp[j + 1] += prob * (double)case2;
				}
			
			int case3 = 1 + B + 1;
			exp[A + 1] += prob * (double)case3;
			
			
			/*cout << prob << endl;
			cout << case1 << " ";
			for (int j = 0; j < A; j++)
				cout << case2[j] << " ";
			cout << case3 << endl;
			cout << endl << endl;*/
			
			int id = A - 1;
			right[id]++;
			
			while (right[id] == 2)
			{
				id--;
				right[id + 1] = 0;
				right[id]++;
				if (id < 0)
					cont = false;
			}
		}
		
		int min = 0;
		for (int j = 1; j < A + 2; j++)
			if (exp[j] < exp[min])
				min = j;
				
		out<< fixed << setprecision(6) << "Case #" << i+1 << ": " << (double)exp[min] << endl;
				
		//delete[] right;
		//delete exp;
		//delete p;
	}
	
	in.close();
	out.close();
		
	return 0;
}

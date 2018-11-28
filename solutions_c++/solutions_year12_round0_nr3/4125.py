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
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <sstream>

using namespace std;

int main(int argc, char** argv)
{
	ifstream in("C-small-attempt0.in");
	ofstream out("output.txt");
	
	int T;
	in >> T;
	
	for (int i = 0; i < T; i++)
	{
		int a, b;
		in >> a >> b;
		vector<int> found1;
		vector<int> found2;
		
		for (int j = a; j <= b; j++)
		{
			string value;
			stringstream out1;
			out1 << j;
			value = out1.str();
			
			for (int k = 1; k < value.size(); k++)
			{
				string value2 = value;
				value2 = value.substr(k, value.size() - k + 1) + value.substr(0, k);
				
				
				if (value2.compare(value) != 0 && value[0] != '0' && value2[0] != '0' &&
					value.size() == value2.size())
				{
					int n = atoi(value.c_str());
					int m = atoi(value2.c_str());
					if (m >= a && m <= b && n < m)
					{
						bool tmpFound = false;
						/*for (int ii = 0; ii < found.size(); ii++)
							if (found.at(ii) == m)
							{
								tmpFound = true;
								ii = found.size();
							}*/
						if (!tmpFound)
						{
							found1.push_back(n);
							found2.push_back(m);
							//out << n << " " << m << endl;
						}
					}
				}
			}
		}
		for (int j = 0; j < found1.size(); j++)
			for (int k = j+1; k < found1.size(); k++)
				{
					if (found1.at(j) == found1.at(k) && found2.at(j) == found2.at(k))
					{
						found1.erase(found1.begin() + k);
						found2.erase(found2.begin() + k);
						k--;
					}
				}
		
		out << "Case #" << i+1 << ": ";
		out << found1.size() << endl;
	}	
	
	out.close();
	
	return 0;
}

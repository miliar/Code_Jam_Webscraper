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

using namespace std;

const char voca[26] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q'
					, 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};

int main(int argc, char** argv)
{
	//find the language
	
	ifstream in("input.txt");
	ifstream in2("res.txt");
	string tmp;
	getline(in, tmp);
	int N = atoi(tmp.c_str());
	
	vector<char> original;
	vector<char> google;
	
	for (int i = 0; i < N; i++)
	{
		getline(in, tmp);
		string tmp2;
		getline(in2, tmp2);
		
		//cout << tmp.c_str() << endl << tmp2.c_str() << endl;
		for (int j = 0; j < tmp.size(); j++)
		{
			char a = tmp[j];
			if (a != ' ')
			{
				bool found = false;
				for (int k = 0; k < google.size(); k++)
					if (google.at(k) == a)
					{
						found = true;
						k = google.size();
					}
				if (!found)
				{
					google.push_back(a);
					original.push_back(tmp2[j]);
				}
			}
		}
	}
	
	//add the hint
	original.push_back('z');
	google.push_back('q');
	
	//find the left one
	vector<char> tmpChar1;
	vector<char> tmpChar2;
	
	for (int i = 0; i < 26; i++)
	{
		tmpChar1.push_back(voca[i]);
		tmpChar2.push_back(voca[i]);
	}

	
	for (int i = 0; i < google.size(); i++)
	{
		for (int j = 0; j < tmpChar1.size(); j++)
			if (tmpChar1.at(j) == original.at(i))
			{
				tmpChar1.erase(tmpChar1.begin() + j);
				j = tmpChar1.size();
			}
		for (int j = 0; j < tmpChar2.size(); j++)
			if (tmpChar2.at(j) == google.at(i))
			{
				tmpChar2.erase(tmpChar2.begin() + j);
				j = tmpChar2.size();
			}
	}
	
	if (tmpChar1.size() == 1)
	{
		original.push_back(tmpChar1.at(0));
		google.push_back(tmpChar2.at(0));
	}
	
	/*cout << google.size() << endl;
	for (int i = 0; i < google.size(); i++)
	{
		cout << original.at(i) << " " << google.at(i) << endl;
	}*/
	
	in.close();
	in2.close();
	
	//translate the input
	
	in.open("A-small-attempt0.in");
	ofstream out("out.txt");
	
	getline(in, tmp);
	N = atoi(tmp.c_str());
	
	for (int i = 0; i < N; i++)
	{
		getline(in, tmp);
		string output = tmp;
		for (int j = 0; j < tmp.size(); j++)
		{
			char a = tmp[j];
			if (a != ' ')
			{
				for (int k = 0; k < google.size(); k++)
				 if (google.at(k) == a)
				 {
					 output[j] = original.at(k);
					 k = google.size();
				 }
			}
		}
		out << "Case #" << i+1 << ": ";
		out << output << endl;
	}
	
	
	return 0;
}

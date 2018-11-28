#include <fstream>
#include <iostream>
#include <utility>
#include <algorithm>
#include <cmath>
#include <string>

using namespace std;

struct combination {
	char b1, b2, nb;
};

struct opposition {
	char o1, o2;
};

combination combines [36];
opposition opposes [28];
string input;
string elem_list;
int C, D, N;


int isCombined(char a, char b) //returns index or -1
{
	for(int i = 0; i < C; ++i)
	{
		if(((combines[i].b1 == a) && (combines[i].b2 == b))	|| ((combines[i].b1 == b) && (combines[i].b2 == a)))
			return i;
	}
	return -1;
}

bool isApposed(char a, char b)
{
	for(int i = 0; i < D; ++i)
	{
		if(((opposes[i].o1 == a) && (opposes[i].o2 == b))
			|| ((opposes[i].o1 == b) && (opposes[i].o2 == a)))
			return true;
	}
	
	return false;
}

int main () 
{
	ifstream in("in.in");
	ofstream out("out.out");

	int T;
	
	in >> T;
	
	for(int i = 0; i < T; ++i)
	{
		
		
		in >> C;
		
		string tmp;
		for(int j = 0; j < C; ++j)
		{
			in >> tmp;
			combines[j].b1 = tmp[0];
			combines[j].b2 = tmp[1];
			combines[j].nb = tmp[2];
		}
		
		in >> D;
		for(int j = 0; j < D; ++j)
		{
			in >> tmp;
			opposes[j].o1 = tmp[0];
			opposes[j].o2 = tmp[1];
		}
		
		in >> N;
		
		in >> input;
				
		elem_list = input[0];
		
		for(int j = 1; j < N; ++j)
		{
			elem_list += input[j];
			
			if(elem_list.length() == 1) //if the previous step erased it
				continue;
			
			int com = isCombined(elem_list[elem_list.length() - 2], elem_list[elem_list.length() - 1]);
			if (com != -1)
			{
				elem_list.erase(elem_list.length() - 1, 1);
				elem_list[elem_list.length() - 1] = combines[com].nb;
			}
			
			
			for(int k = 0; k < elem_list.length() - 1; ++k)
			{
				bool needbreak = false;
				for(int l = k + 1; l < elem_list.length(); ++l)
					if (isApposed(elem_list[k], elem_list[l]))
					{
						elem_list = "";
						needbreak = true;
						break;
					}
				if(needbreak)
					break;
			}
		}
		
		out << "Case #" << i+1 << ": [";
		if(elem_list.length() == 0)
			out << "]\n";
		else
		{
			out << elem_list[0];
			for(int j = 1; j < elem_list.length(); ++j)
				out << ", " << elem_list[j];
			out << "]\n";
		}
		
	}
	
}
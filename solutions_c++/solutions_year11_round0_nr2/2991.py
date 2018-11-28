#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

#define CALL_MACRO(x, y)	if(x=='Q') {y(0)}\
							else if(x=='W')	{y(1)}\
							else if(x=='E')	{y(2)}\
							else if(x=='R') {y(3)}\
							else if(x=='A') {y(4)}\
							else if(x=='S') {y(5)}\
							else if(x=='D') {y(6)}\
							else if(x=='F') {y(7)}

#define IF_CONDITION(x) if(current_combine_string[1]=='Q') {combine_mtx[x][0] = current_combine_string[2]; combine_mtx[0][x] = current_combine_string[2];}\
						else if(current_combine_string[1]=='W') {combine_mtx[x][1] = current_combine_string[2]; combine_mtx[1][x] = current_combine_string[2];}\
						else if(current_combine_string[1]=='E') {combine_mtx[x][2] = current_combine_string[2]; combine_mtx[2][x] = current_combine_string[2];}\
						else if(current_combine_string[1]=='R') {combine_mtx[x][3] = current_combine_string[2]; combine_mtx[3][x] = current_combine_string[2];}\
						else if(current_combine_string[1]=='A') {combine_mtx[x][4] = current_combine_string[2]; combine_mtx[4][x] = current_combine_string[2];}\
						else if(current_combine_string[1]=='S') {combine_mtx[x][5] = current_combine_string[2]; combine_mtx[5][x] = current_combine_string[2];}\
						else if(current_combine_string[1]=='D') {combine_mtx[x][6] = current_combine_string[2]; combine_mtx[6][x] = current_combine_string[2];}\
						else if(current_combine_string[1]=='F') {combine_mtx[x][7] = current_combine_string[2]; combine_mtx[7][x] = current_combine_string[2];}

#define IF_CONDITION_BOOL(x)	if(current_destroy_string[1]=='Q') {destroy_mtx[x][0] = true; destroy_mtx[0][x] = true;}\
								else if(current_destroy_string[1]=='W') {destroy_mtx[x][1] = true; destroy_mtx[1][x] = true;}\
								else if(current_destroy_string[1]=='E') {destroy_mtx[x][2] = true; destroy_mtx[2][x] = true;}\
								else if(current_destroy_string[1]=='R') {destroy_mtx[x][3] = true; destroy_mtx[3][x] = true;}\
								else if(current_destroy_string[1]=='A') {destroy_mtx[x][4] = true; destroy_mtx[4][x] = true;}\
								else if(current_destroy_string[1]=='S') {destroy_mtx[x][5] = true; destroy_mtx[5][x] = true;}\
								else if(current_destroy_string[1]=='D') {destroy_mtx[x][6] = true; destroy_mtx[6][x] = true;}\
								else if(current_destroy_string[1]=='F') {destroy_mtx[x][7] = true; destroy_mtx[7][x] = true;}

#define CHECK_COMBINE(x)	if(element_list[size-2]=='Q') {ans = combine_mtx[x][0];}\
							else if(element_list[size-2]=='W') {ans = combine_mtx[x][1];}\
							else if(element_list[size-2]=='E') {ans = combine_mtx[x][2];}\
							else if(element_list[size-2]=='R') {ans = combine_mtx[x][3];}\
							else if(element_list[size-2]=='A') {ans = combine_mtx[x][4];}\
							else if(element_list[size-2]=='S') {ans = combine_mtx[x][5];}\
							else if(element_list[size-2]=='D') {ans = combine_mtx[x][6];}\
							else if(element_list[size-2]=='F') {ans = combine_mtx[x][7];}\
							else {ans = '.';}

#define CHECK_DESTROY(x)	if(destroy_mtx[x][0]) {destroy = does_exist(element_list, 'Q');}\
							if(destroy_mtx[x][1]) {destroy = does_exist(element_list, 'W');}\
							if(destroy_mtx[x][2]) {destroy = does_exist(element_list, 'E');}\
							if(destroy_mtx[x][3]) {destroy = does_exist(element_list, 'R');}\
							if(destroy_mtx[x][4]) {destroy = does_exist(element_list, 'A');}\
							if(destroy_mtx[x][5]) {destroy = does_exist(element_list, 'S');}\
							if(destroy_mtx[x][6]) {destroy = does_exist(element_list, 'D');}\
							if(destroy_mtx[x][7]) {destroy = does_exist(element_list, 'F');}	

bool does_exist (string element_list, char query)
{
	element_list.pop_back();
	unsigned sf = element_list.find(query);

	if (sf == string::npos)
		return false;
	else
		return true;
}

int main()
{
	ifstream input("input.txt");
	ofstream output("output.txt");

	unsigned T;
	input >> T;

	for(unsigned t=0; t<T; ++t)
	{
		unsigned C;
		input >> C;

		vector<vector<char> > combine_mtx;

		vector<char> dummy(8,'.');
		for(unsigned i=0; i<8; ++i)
			combine_mtx.push_back(dummy);

		string current_combine_string;

		for(unsigned c=0; c<C; ++c)
		{
			input >> current_combine_string;

			CALL_MACRO(current_combine_string[0], IF_CONDITION)
		}

		unsigned D;
		input >> D;

		vector<vector<bool> > destroy_mtx;

		vector<bool> bool_dummy(8,false);
		for(unsigned i=0; i<8; ++i)
			destroy_mtx.push_back(bool_dummy);

		string current_destroy_string;

		for(unsigned d=0; d<D; ++d)
		{
			input >> current_destroy_string;

			CALL_MACRO(current_destroy_string[0], IF_CONDITION_BOOL)
		}

		unsigned N;
		input >> N;

		string sequence;
		input >> sequence;

		string element_list = "";
		element_list = element_list + sequence[0];

		for(unsigned n=1; n<N; ++n)
		{
			element_list = element_list + sequence[n];
			unsigned size = element_list.size();

			char ans;

			if(size > 1)
			{
				CALL_MACRO(element_list[size-1], CHECK_COMBINE)

				if(ans!='.')
				{
					element_list.pop_back();
					element_list.pop_back();
					element_list.push_back(ans);
				}
				else
				{
					bool destroy = false;

					CALL_MACRO(element_list[size-1], CHECK_DESTROY)

					if(destroy)
						element_list = "";
				}
			}
		}

		output << "Case #" << t+1 << ": " << "[";

		unsigned size = element_list.size();

		for (unsigned i = 0; i<size; ++i)
		{
			output << element_list[i];

			if (i+1 < size)
				output << ", ";
		}

		output << "]" << endl;
	}

	input.close();
	output.close();
	return 0;
}

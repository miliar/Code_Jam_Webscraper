#include <iostream>
#include <cmath> 
#include <vector>
#include <algorithm>
#include <numeric>
#include <stack>
#include <queue>
#include <map>
#include <sstream>
#include <set>
#include <list>
#include <utility>
#include <iomanip>
#include <cmath>
#include <fstream>
#include <windows.h>

using namespace std; 

int dwg(vector<int>scores, int S, int p)
{
	int cases = 0;
	for(int i = 0; i < scores.size(); i++){
		int base = scores[i] / 3;
		vector< vector<int> >result;

		switch(scores[i] % 3) 
		{
		case 0:
			{

				if(base >= p){
					cases++;
				}else{
					if(S > 0 && base > 0 && (base + 1) >= p){
						cases++;
						S--;
					}
				}
				break;
			}
		case 1:
			{

				if(base >= p || (base + 1) >= p){
					cases++;
				}else{
					if(S > 0 && (base + 1) >= p) {
						cases++;
						S--;
					}
				}
				break;
			}
		case 2:
			{

				if((base + 1) >= p || base >= p){
					cases++;
				}else{
					if(S > 0 && (base + 2) >= p){
						cases++;
						S--;
					}
				}
				break;
			}
		}
	}
	return cases;
}

void main()
{
	int n, j = 1; 
	string in;

	string filename = "B-small-attempt0.in";
	fstream fin(filename.c_str(), ios::in);
	fstream fout("output.txt", ios::out);

	fin >> n;
	fin.ignore();

	while(n--){
		string out = "";
		int N, S, p, t;
		vector<int>scores;
		stringstream ss;
		ss << "Case #" << j << ": ";

		fin >> N >> S >> p; 

		while(N--){
			int temp; 
			fin >> temp; 
			scores.push_back(temp);
		}

		t = dwg(scores, S, p);

		ss << t;
		getline(ss, out);
		if(n != 0)
			out += "\n";
		
		fout << out;
		j++;
	}
	system("pause");
}
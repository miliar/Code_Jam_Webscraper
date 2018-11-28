//============================================================================
// Name        : acm.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>

using namespace std;

int main() {
	int l,d,n;
	char words[5000][15];
	ifstream fcin;
	ofstream fcout;
	fcout.open("output.txt");
	fcin.open("A-large.in");
//	fcin.open("A-small-attempt3.in");

	fcin >> l >> d >> n;
	for( int i = 0 ; i < d ; ++i )
	{
		fcin >> words[i];
	}
	char test_case[500];
	for( int i = 0 ; i < n ; ++i )
	{
		int count = 0;
		fcin >> test_case;
		int t_n = strlen(test_case);
		for(int j = 0 ; j < d ; ++j )
		{
			bool pattern_fit = true;
			for(int k = 0 ; k < l ; ++k )
			{
				int index=0;
				int t=0;
//				bool inside_parenthesis=false;
				for(t=0; t < t_n ; ++t){
					if(index == k) break;
					if(test_case[t]=='(')
					{
						while(test_case[++t]!=')')
						{
						}
						++index;
					}else{
						++index;
					}
				}
				if(test_case[t] == '('){
					bool flag = false;
					for(;t< t_n ; ++t)
					{
						if(test_case[t] == ')'){
							flag = false;
							break;
						}
						if(test_case[t]==words[j][k])
						{
							flag = true;
							break;
						}
					}
					if(!flag){
						pattern_fit = false;
						break;
					}
				}else if(test_case[t] != words[j][k])
				{
					pattern_fit = false;
					break;
				}
			}
			if(pattern_fit) ++count;
		}
		cout << "Case #" << i+1 <<": " << count << endl;
		fcout << "Case #" << i+1 <<": " << count << endl;
	}
	return 0;
}

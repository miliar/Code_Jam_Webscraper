/*
 * b.cpp
 *
 *  Created on: 2012-04-15
 *      Author: Rumman
 */
#include <string>
#include <stdio.h>
#include <fstream>
#include <string.h>
#include <cstdlib>
#include <ctype.h>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int maxPosbleGglrs(vector<int>, int, int);

int main() {
	ofstream fout ("output.txt");
	ifstream fin ("input.txt");
	int counter = 0 ;
	fin >> counter;//Taking number of test cases
	cout << "There will be "<<counter<<" input. "<<endl;
	for(int i = 0; i<counter;i++)
	{
		// n = Number of googlers S number of surprise, p best result
		int  n = 0, s =0, p =0;
		vector<int> googlers;
		vector<int>::iterator it;
		int temployee;
		int result;
		fin >> n >> s >> p;
		cout<< "Number of googlers: "<< n <<", surprise elements :"<< s <<", max posibble value :"<< p <<endl;
		//adding googlers
		for(int j = 0; j<n; j ++)
		{
			fin >> temployee;
			googlers.push_back(temployee);
		}
		sort (googlers.begin(), googlers.end());
		reverse (googlers.begin(), googlers.end());
		cout << "Googlers score:";
	    for (it=googlers.begin(); it!=googlers.end(); ++it)
			cout << " " << *it;
	    cout<<endl;
	    result = maxPosbleGglrs(googlers, s, p);
	    cout<<"Output "<<result<<endl;
	    fout<<"Case #"<<i+1<<": "<<result<<endl;
	}
	return 0;
}

int maxPosbleGglrs(vector<int> googlers, int s, int p)
{
	int result = 0;
	int score;
	if(p == 0) return googlers.size();
	for(int i = 0; i<googlers.size()  ;i++)
	{
		score = googlers[i];
		if(score == 0) continue;
		else if(score/3 >= p || ( score - p )/2 >= ( p - 1))
		{
			result++;
		}
		else if(( score - p )/2 >= ( p - 2) && s != 0 )
		{
			result++;
			s--;
		}
	}
	return result;
}






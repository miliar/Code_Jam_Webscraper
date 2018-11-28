// test.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<iostream>
#include<fstream>
#include<vector>
using namespace std;
int case_num = 0;
int* candys;
int* answers;
int candy_num;
void caculate(int case_index);
void loadData()	{
	ifstream fin("in.txt");
	fin>>case_num;
	answers = new int[case_num];
	for(int i = 0; i < case_num; i++){
		
		fin >> candy_num;
		//cout<<"#"<<candy_num<<endl;
		candys = new int[candy_num];
		for(int j = 0; j < candy_num;j++)	{
			fin>> candys[j];
			//cout<<candys[j];
		}
		//cout<<endl;
		caculate(i);
	}
}
void caculate(int case_index)	{
	vector<vector<int> > candys_binary(candy_num);
	int max_length = 0;

	for(int i = 0 ; i < candy_num;i++)	{
		int num = candys[i];
		//cout<<num<<"\t";
		do {
			int reminder = num%2;
			candys_binary[i].push_back(reminder);
			//cout<<reminder;
			num = num/2;
		}while(num > 0);
		//cout<<endl;
		if(candys_binary[i].size() > max_length)
			max_length = candys_binary[i].size();
		

	}
	int* one_count = new int[max_length];
	for(int i = 0; i < max_length; i++)
		one_count[i] = 0;

	for(int i = 0 ; i < candy_num;i++)	{
		for(int j = 0; j < candys_binary[i].size(); j++)	{
			one_count[j] += candys_binary[i][j];
		}
	}
	bool possible = true;

	for(int i = 0 ; i < max_length; i++)	{
		//cout<<one_count[i];
		if(one_count[i] %2 != 0)	{
			possible = false;
			break;
		}
	}
	//cout<<endl;
	if(!possible)	{
		answers[case_index] = -1;
		return;
	}
	else {
		int min_candy = INT_MAX;
		int candy_sum = 0;
		for(int i = 0 ;i < candy_num;i++)	{
			if(candys[i] < min_candy)	
				min_candy = candys[i];
			candy_sum += candys[i];
		}
		answers[case_index] = candy_sum - min_candy;
	}
	


}
void output()	{
	ofstream fout("out.txt");
	for(int i = 0; i < case_num; i++)	{
		fout<<"Case #"<<i+1<<": ";
		if(answers[i] == -1)
			fout<<"NO";
		else fout<<answers[i];
		fout<<endl;
	}
}
int _tmain(int argc, _TCHAR* argv[])
{
	loadData();
	output();

	return 0;
}


#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <fstream>
#include <string>

using namespace std;

ofstream outfile;

//char modify_chars( char str)
//{
//	switch( str )
//	{
//	case 'a':
//		return 'y';
//	case 'b':
//		return 'h';
//	case 'c'://
//		return 'e';
//	case 'd':
//		return 's';
//	case 'e':
//		return 'o';
//	case 'f'://
//		return 'c';
//	case 'g':
//		return 'v';
//	case 'h':
//		return 'x';
//	case 'i'://
//		return 'd';
//	case 'j':
//		return 'u';
//	case 'k':
//		return 'i';
//	case 'l':
//		return 'g';
//	case 'm':
//		return 'l';
//	case 'n'://
//		return 'b';
//	case 'o':
//		return 'k';
//	case 'p':
//		return 'r';
//	case 'q':
//		return 'z';
//	case 'r':
//		return 't';
//	case 's':
//		return 'n';
//	case 't':
//		return 'w';
//	case 'u':
//		return 'j';
//	case 'v':
//		return 'p';
//	case 'w'://
//		return 'f';
//	case 'x':
//		return 'm';
//	case 'y'://
//		return 'a';
//	case 'z':
//		return 'q';
//	default:
//		break;
//	}
//}
//
//void translation (string &input)
//{
//	for(int i = 0; i <input.size(); ++i)
//	{
//		if(input[i] == ' ') continue;
//		if(input[i] < 97 && input[i] > 122) continue;
//		input[i] = modify_chars(input[i]);
//	}
//}

/*QUESTION #2*/
void dance(const int &size, const int &surprise, const int &p, const vector<int> &input)
{
	

	int ret_value = 0;
	int total_surprise = 0;
	int maybe_surp = 0;
	int mustbe_surp = 0;
	if(p==0)
	{
		outfile<<size<<endl;
		return;
	}

	for(int i = 0; i < size; i++)
	{
		if(input.at(i) >= 29)				//case >= 29
		{
			ret_value++;
			//cout<<"case >28"<<endl;
		}
		else if(input.at(i) / p <= 1)  //case 1  special cases for p=2 and p=3
		{
			if(p == 2 && input.at(i) >1)
			{
				if(mustbe_surp < surprise)
				{
					ret_value++;
					mustbe_surp++;
				}
			}
			else if(p == 3 &&  input.at(i) == 5)
			{
				if(mustbe_surp < surprise)
				{
					ret_value++;
					mustbe_surp++;
				}
			}
		}
		else if(input.at(i) / p == 2)   //case 2
		{
			//cout<<"case 2"<<endl;
			int difference = p - (input.at(i) % p);
			if(difference == 1 || difference == 2)		// subcase of case 2
			{
				ret_value++;
				maybe_surp++;
			}
			else if(difference == 3 || difference ==4)		// subcase of case 2
			{
				if(mustbe_surp < surprise)
				{
					ret_value++;
					mustbe_surp++;
				}
			}
		}
		else										//case 3
		{
			ret_value++;
			maybe_surp++;
			//cout<<"case 3"<<endl;
		}
	}
	//cout<<"ret: "<<ret_value<<"  must:"<<mustbe_surp<<"  maybe:"<<maybe_surp<<endl;
	outfile<<ret_value<<endl;
}


int main()
{
	ifstream infile;
	

	infile.open("c:\\google\\B-small-attempt1.in");
	outfile.open("c:\\google\\result.txt");

	int case_number = 0;
	int num_google = 0;
	int surprise = 0;
	int p = 0;
	infile>>case_number;
	//cout<<case_number<<endl;
	for( int i = 0; i < case_number; i++)
	{
		infile>>num_google;
		infile>>surprise;
		infile>>p;
		//cout<<num_google<<" ";
		//cout<<surprise<<" ";
		//cout<<p<<" ";

		vector<int> input;
		if(!infile.fail())
		{
			for(int j = 0; j < num_google; j++)
			{
				int value;
				infile>>value;
				input.push_back(value);
			}
			outfile<< "Case #"<<i+1<<": ";
			dance(num_google, surprise, p, input);
		}

	/*	vector<int>::const_iterator it;
		for(it = input.begin(); it != input.end(); it++)
		{
			cout<<*it<<" ";
		}
		cout<<endl;*/
	}













	//int i = 1;
	//if(!infile.fail())
	//{
	//		infile>>case_number;
	//		string str;
	//		getline(infile,str);
	//		while(getline(infile,str))
	//		{
	//			translation(str);
	//			outfile<< "Case #"<<i<<": ";
	//			outfile<<str<<endl;
	//			i++;
	//		}
	//}
	system("pause");
	return 0;
}

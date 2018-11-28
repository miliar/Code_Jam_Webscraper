#include<iostream>
#include <fstream>
#include<stdlib.h>
#include<string>


using namespace std;
string map2Grese(string input);
void learn(string input, string output);


int main()

{
	ifstream infile;
	infile.open("input.txt");

	ofstream outfile;

	//learn("de kr kd eoya kw aej tysr re ujdr lkgc jv","so it is okay if you want to just give up");
	int Num = 0 ;
	infile >> Num;
	infile.ignore();
	//6cout<<"Num"<<Num<<endl;
	string testCase;
	string output;
	outfile.open("output.txt");
	for(int i = 0; i< Num ; i++)
	{
		getline(infile,testCase);
		
		cout<<"Case #"<<i+1<<": "<<map2Grese(testCase)<<endl;
		outfile<<"Case #"<<i+1<<": "<<map2Grese(testCase)<<endl;
	}
	outfile.close();
	infile.close();


}


string map2Grese(string ip)
{

//	cout<<ip<<endl;
	string alphaset = "abcdefghijklmnopqrstuvwxyz";
	string greseset = "ynficwlbkuomxsevzpdrjgthaq";
	string ouput;
	int i = 0;
	bool match = false;
	for( ; i<ip.size();i++)
	{

		for(int j =0 ; j<26;j++)
		{
			if(greseset[j] == ip[i]){
				ouput.push_back(alphaset[j]);
				match = true;
			}
		}	
		if(!match)
			ouput.push_back(' ');
		match = false;
	}
	
	return ouput;

}

//void learn(string input, string output)
//{
//
//	cout<<""<<endl;
//	for(int i =0 ; i<input.size();i++)
//	{
//		cout<<output[i]<<":"<<input[i]<<endl;
//
//	}
//
//}
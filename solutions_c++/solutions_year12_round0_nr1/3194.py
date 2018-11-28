//Template for Google Code Contest
#include <iostream>
#include <fstream>
#include <string>
#include <new>
#include <vector>
#include <bitset>
#include <cstring>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

//Divides String By Spaces
vector<string> Divide(string str)
{
	vector<string> Data;
	//for each space found
	int Count = 0;
	int pos = 0;
	while (str.find(" ",pos)!=string::npos){
		int st = str.find(" ",pos);
		Data.push_back(str.substr(pos, (st)-pos)); //Attach chars left of current space
		Count++; //Set Input for Next
		pos = str.find(" ",pos)+1; //Jump past current space
	}
	Data.push_back(str.substr(pos, str.length()-pos)); //Attach chars right of last space
	return Data;
}

char HashMap(char X) {
	string Source = "zqeyejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
	string Out =    "qzoaour language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";
	//string Source = "y n f i c w l b k u o m x s e v z p d r j g a t h a set k oset xa ynfd";
	//string Out =    "a b c d e f g h i j k l m n o p q r s t u v w x y z now i know my abcs";

	if (X != ' ') {
		for (int i=0; i < Source.length(); i++) {
			if ((Source.c_str())[i] == X) {
				return (Out.c_str())[i];
			}
		}
	}
	return X;
}
int main()
{
	//arr is allocated
	ifstream Input("input.in");
	string Line;
	getline(Input, Line);
	int NumCases = atoi(Line.c_str());
	vector<string> Lines;
	vector<string> Out;
	for (int i=0; i < NumCases; i++) {
		getline(Input,Line);
		Lines.push_back(Line);
	}
	for (int i=0; i < NumCases; i++) {
		string Translate = "";
		for (int j=0; j < Lines[i].length(); j++) {
			Translate += HashMap((Lines[i].c_str())[j]);
		}
		Out.push_back(Translate);
		cout << "Finished Case #:" << i+1 << endl;
	}
	cout << "Starting Output" << endl;
	ofstream Output("output.in");
	for (int i=0; i < NumCases; i++) {
		Output << "Case #" << i + 1 << ": " << Out[i] << endl;
	}
	return(0);
}

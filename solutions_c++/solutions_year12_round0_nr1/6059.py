#include<string>
#include<vector>
#include<iostream>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <map>
#include <set>
#include <iterator>
#include <algorithm>
#include <queue>
#include <functional>
#include <sstream>
#include <complex>
#include <ctype.h>
#include <math.h>
#include <stdlib.h>
#include <ctime>
#include <iomanip>
#include <time.h>
#include <string.h>
using namespace std;

void findLetterStr(string::iterator str1, string::iterator str2)
{
	while(str1!=str2)
	{
		if(*str1=='y') *str1= 'a';
		else if(*str1=='n') *str1= 'b';
		else if(*str1=='f') *str1= 'c';
		else if(*str1=='i') *str1= 'd';
		else if(*str1=='c') *str1= 'e';
		else if(*str1=='w') *str1= 'f';
		else if(*str1=='l') *str1= 'g';
		else if(*str1=='b') *str1= 'h';
		else if(*str1=='k') *str1= 'i';
		else if(*str1=='u') *str1= 'j';
		else if(*str1=='o') *str1= 'k';
		else if(*str1=='m') *str1= 'l';
		else if(*str1=='x') *str1= 'm';
		else if(*str1=='s') *str1= 'n';
		else if(*str1=='e') *str1= 'o';
		else if(*str1=='v') *str1= 'p';
		else if(*str1=='z') *str1= 'q';
		else if(*str1=='p') *str1= 'r';
		else if(*str1=='d') *str1= 's';
		else if(*str1=='r') *str1= 't';
		else if(*str1=='j') *str1= 'u';
		else if(*str1=='g') *str1= 'v';
		else if(*str1=='t') *str1= 'w';
		else if(*str1=='h') *str1= 'x';
		else if(*str1=='a') *str1= 'y';
		else if(*str1=='q') *str1= 'z';

		str1++;
	}


}

int main() 
{
	
	string intputStr;
	ifstream myfile;
	myfile.open ("A-small-attempt4.in");
	ofstream outputFile ("output.txt");

	for(int i=0; i<=30; ++i)
	{
		getline(myfile,intputStr);
		string::iterator itr1=intputStr.begin();
		string::iterator itr2 = intputStr.end (); 

		findLetterStr(itr1,itr2);

		if(i!=0)
			outputFile<<"Case #"<<i<<": "<< intputStr<<endl; 

	}
}
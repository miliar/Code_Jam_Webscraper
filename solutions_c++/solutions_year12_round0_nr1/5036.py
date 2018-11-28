// DWtG.cpp : main project file.

#include "stdafx.h"
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>


using namespace System;

using namespace System;
using namespace System::IO;
using namespace std;

int main(array<System::String ^> ^args)
{

	String^ fileName = "A-Small.in";

	array<char>^goglang = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' '};

	array<char>^englang = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q',' '};


	ifstream infile("A-small.in",ios::binary | ios::in );
	ofstream outfile("A-small.out",ios::binary | ios::out );

	int tst_cases;

	string str;
	
	
	infile>>tst_cases;

	for(int i=0; i<=tst_cases; i++){
		

		getline(infile,str);

	if(i!=0){

		outfile<<"Case #"<<i<<": ";

	int str_size = str.size();
	
	if(infile.eof()){
		str_size = str_size;
	}

	for(int j=0; j<str_size; j++){
	
	outfile<<englang[Array::IndexOf(goglang,str[j])];
	}

	outfile<<"\n";

		}

		


	}


    return 0;
}

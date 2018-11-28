// CodeJam_Qual_2.cpp : Defines the entry point for the console application.
// Hello GOOGLE! I haven't programed in C++ for a long time!
// I could whip this out quickly with MATLAB, but figured I'd get back into using 
// a real programming language!

#include "stdafx.h"
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <string> 
#include <vector>
#include <algorithm>

    using namespace std;

int main()
{
	float x;
	int cases, C, D, N;
	ifstream fp_in;
	ofstream fp_out;
	string c1[36], d1[28], c2;
	string base;
	
	fp_in.open("B-small-attempt0.in", ios::in);
	fp_out.open("test.out",ios::out);
	fp_in >> cases ;

	for (int i=1;i <cases+1;i++)
	{
		cout << "STARTING CASE:" << i << endl;
		c1[0].clear();
		d1[0].clear();
		c2.clear();
		//Load number of COMBOS
		fp_in >> C;
	//	cout <<"C="<< C << endl;
		
		if (C > 0){
			for(int k=0;k<(C);k++){
				fp_in >> c1[k];
			}
		}

		//Load number of DESTRUCTOS
		fp_in >> D;
	//	cout <<"D="<< D << endl;

		if (D > 0){
			for(int k=0;k<(D);k++){
				fp_in >> d1[k];
			}
		}

		//NUmber of lines
		fp_in >> N;
		//cout << "N="<< N << endl;
		//Load in base
		fp_in >> base;
	//	cout <<"Base="<<base <<endl;
    ///


		string list, tmp;
		list.assign(base);  //This one is easy
		if (!c1[0].empty())
		{
			c2.assign(c1[0]);
			c2.replace(0,1,c1[0],1,1);
			c2.replace(1,1,c1[0],0,1);
		}

		list.assign(base,0,1);
		//int listpos;
		
		//cout <<"C1="   << c1[0]<< " C2=" << c2<<endl;
		//cout <<"C2="<<c2 << endl;
		//cout <<"D1=" << d1[0] << endl;
		//listpos=1;
		//for(int k=0;k<N-1;k++)   //increment over each char in list.
		int y=1;
		while (y < N) 
		{
			list.append(base,y,1);  //get next char
			y++;
		//	cout << "LISTSTART=" << list << endl;
		
			if (!c1[0].empty())
			//	cout <<"List=" << list <<" size="<<list.size()<< " LC1="<<list.compare(list.size()-2,2,c1[0],0,2) <<"  LC2="<<c2<<"  "<<list.compare(list.size()-2,2,c2,0,2) << endl;
				if (list.compare(list.size()-2,2,c1[0],0,2) == 0 || list.compare(list.size()-2,2,c2,0,2) == 0 )
				{
					list.replace(list.size()-2,2,c1[0],2,1);
					//listpos--;
			//		cout << "found one" << y << "listpos="<<listpos<< endl;
				}
			if (!d1[0].empty())
			{
				if(  (list.find(d1[0].at(0)) < 10000) && (list.find(d1[0].at(1)) < 10000) ){
		//			cout << "LIST=" << list << endl;
					//listpos=0;
					list.clear();
					list.append(base,y,1);  //get next char
					y++;
				}
			}
	
		
	
		//listpos++;
				
		}
		//cout <<"LIST="<<list<<endl;;
		
		cout <<"Size="<<list.size() << endl;
		fp_out <<"Case #" << i <<":"<<" [";
		if (list.size()>0)
		{
			for(int z=0; z < list.size()-1; z++){
				fp_out <<list.at(z) <<", ";
			}
			fp_out << list.at(list.size()-1) ;
		}
		fp_out << "]"<< endl;
	}

	

	
	string str1 = "ystring";
    string str2 = "String";
    string str3 = "secod string";

	str1.clear();
	str1.append(str2);
	cout << str1 << endl;
		
	system("PAUSE");
	fp_in.close();
	fp_out.close();
	return 0;
}
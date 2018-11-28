//============================================================================
// Name        : codejamc.cpp
// Author      : Tizz
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <sstream>

using namespace std;

int main() {
	ofstream fout("c.out");
	ifstream fin("c.in");
	int t;
	int a,b;
	fin>>t;
int count=0;
	for(int i=0;i<t;i++){
count=0;
			fin>>a>>b;

			//	o<<a;
				string sa,sb;

				for(int ac=a;ac<b;ac++){
					for(int bc=ac+1;bc<=b;bc++){
						ostringstream oa;
						ostringstream ob;
						oa<<ac;sa=oa.str();
						ob<<bc;sb=ob.str();
						string s;
					//	cout<<sb<<endl;
						if(sa.size()>1)
						for(int k=1;k<sa.size();k++){

						s=sa.substr(k,sa.size()-k)+sa.substr(0,k);

						if(s==sb){
							count++;
							break;
						}
						}


					}
				}

fout<<"Case #"<<i+1<<": "<<count<<endl;
	}





}


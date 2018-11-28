//Google CodeJam
//Author : Harish Surana<surana4u@gmail.com>

#include <iostream>
#include <vector>
#include <list>
#include <string>
#include <sstream>
#include <fstream>
using namespace std;
main(){
	int N;								//Number of cases
	int T;								//Turnaround time
	int NA;								//Number of trips from A to B
	int NB;								//Number of trips from B to A
	
	list<int> timeA;					//Time at which trains are require at A it store minutes 
	list<int> timeB;					//Time at which trains are require at B it store minutes 
	list<int> resA;						//It stores varius resources available at A
	list<int> resB;						//It stores varius resources available at B
	
    fstream fin("input.in",ios::in);	//Input File
	string sLine;						//Inout Line
	if(!fin){
		cout<<"File input.in could not be opened";
		return -1; // ERROR 
	}
	fstream fout("output.out",ios::out);//Output File
	if(!fout){
		cout<<"File output.out could not be opened";
		return -1; // ERROR 
	}
	getline(fin,sLine);
    N=atoi(sLine.c_str());
	//fout<<N<<"\n";
	for(int k=0;k<N;k++){

	getline(fin,sLine);
    T=atoi(sLine.c_str());
	getline(fin,sLine);
    sscanf(sLine.c_str(),"%d %d",&NA,&NB);
	int hh1,mm1,hh2,mm2;

	//Reading time of trains required at A
	for(int i=0;i<NA;i++){
		getline(fin,sLine);
		sscanf(sLine.c_str(),"%d:%d %d:%d",&hh1,&mm1,&hh2,&mm2);
		timeA.push_back(hh1*60+mm1);
		resB.push_back(hh2*60+mm2+T);
	}

	//Reading time of trains required at B
	for(int j=0;j<NB;j++){
		getline(fin,sLine);
		sscanf(sLine.c_str(),"%d:%d %d:%d",&hh1,&mm1,&hh2,&mm2);
		timeB.push_back(hh1*60+mm1);
		resA.push_back(hh2*60+mm2+T);
	}	
	timeA.sort();
	timeB.sort();
	resA.sort();
	resB.sort();
	
	list<int> A;
	list<int> B;

	list<int>::iterator i1;
	for(i1=timeA.begin(); i1 != timeA.end(); ++i1){
		if(resA.size()>0){
			if(*resA.begin()<=*i1){
				resA.pop_front();
			}
			else{
				A.push_back(*i1);
			}
		}
		else{
				A.push_back(*i1);
			}
	}

	for(i1=timeB.begin(); i1 != timeB.end(); ++i1){
		if(resB.size()>0){
			if(*resB.begin()<=*i1){
				resB.pop_front();
			}
			else{
				B.push_back(*i1);
			}
		}
		else{
				B.push_back(*i1);
			}
	}
	
	//for(i1=A.begin(); i1 != A.end(); ++i1){cout<<*i1<<"\t";}
	//for(i1=B.begin(); i1 != B.end(); ++i1){cout<<*i1<<"\t";}


	fout<<"Case #"<<k+1<<": "<<A.size()<<" "<<B.size()<<"\n";

	timeA.clear();
	timeB.clear();
	resA.clear();
	resB.clear();
	A.clear();
	B.clear();
	
	}
	fin.close();
	fout.close();
}
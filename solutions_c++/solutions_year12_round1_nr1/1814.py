/*
 * Password.cpp
 *
 *  Created on: Apr 28, 2012
 *      Author: avikramj
 */



#include<iostream>
#include<sstream>
#include<string>
#include<fstream>
#include<vector>
#include <iomanip>
#include <limits>
using namespace std;

double getExpKeyStrokes(string s1,string s2);
int main(){
	char buf[1000];
	ifstream in("A-small-attempt0.in");
	ofstream out("A-small-attempt0.out");
	int numCases;
	int i=1;
	bool b1=false;
	double d1;
	string s1,s2;
	if(in.getline(buf,110))
		sscanf(buf,"%d",&numCases);
	while(in.getline(buf,110)){
		//		cout<<"Enters\n";
		if(!b1){
			b1=true;
			string temp(buf);
			s1=temp;
		}
		else{
			b1=false;
			string temp(buf);
			s2=temp;
			d1=getExpKeyStrokes(s1,s2);
			out<<"Case #"<<i<<": "<<setprecision(6)<<fixed<<d1<<endl;
			i++;
		}



	}
	return 0;
}



double getExpKeyStrokes(string s1,string s2){
	istringstream st1(s1);
	istringstream st2(s2);
	double ans=0.0;
	vector<int> vi;
	vector<double> vd;
	vector<double> vd_cand;

	int i;double d;
	while(st1>>i){
		vi.push_back(i);
	}
	while(st2>>d){
		vd.push_back(d);
	}
	vd_cand.push_back(1.0*(vi[0]+vi[1]+1));
	double prob=1;
	for(i=1;i<=vd.size();i++){
		prob*=vd[i-1];
		vd_cand.push_back(((vi[0]+vi[1]-2*i+1)*prob+(1-prob)*(vi[0]+2*vi[1]+2-2*i))*1.0);
	}
	ans=1.0*(vi[1]+2);
	for(i=0;i<vd_cand.size();i++){
		if(ans>vd_cand[i])
			ans=vd_cand[i];
	}



	return ans;
}

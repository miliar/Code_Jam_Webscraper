/* Google Code Jam 2009
   Round 2

   Problem: A

   author: David Volgyes

 */

#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <stdint.h>
using namespace std;

// ----------------------------------------------------------------------------------------

#define FOR(variable,min,max) for(int variable=min;variable<=max;++variable)
#define REVERSE_FOR(variable,max,min) for(int variable=max;variable>=min;--variable)
#define foreach(variable,vector) for(int variable=0;variable<vector.size();++variable)
#define reverse_foreach(variable,vector) for(int variable=vector.size()-1;variable>=0;--variable)
#define sort(vector) sort(vector.begin(),vector.end())
#define reverse_sort(vector) sort(vector.begin(),vector.end())

template <class T>
std::ostream & operator<<(ostream& out,vector<T>& vect)
{
	out<<"[";
	if (vect.size()) out<<vect[0];
	for(int i=1;i<vect.size();i++)
		out<<","<<vect[i];
	out<<"]"<<std::endl;
	return out;
}

// ----------------------------------------------------------------------------------------

long long int Power(long long int x,int exp)
{
	long long int result=1;
	for(int i=0;i<exp;++i) result*=x;
	return result;
}


int main() {
	int numberOfTestCases;
	int Case=0,N;
	string text;
	getline(std::cin,text);
	numberOfTestCases=atoi(text.c_str());
	vector<char> chars;
	// Main loop
	do{
		Case=Case+1;
		string result="";
		cin>>N;
		vector<int> pos;
		pos.resize(N);
		FOR(i,0,N-1){
			getline(std::cin,text);
			pos[i]=0;
		FOR(j,0,N-1){
			char input;
		cin>>input;
		if (input=='1')pos[i]=j;
		}
		}
		int swap=0;
		FOR(i,0,N-1){
		if (pos[i]>i) {
			FOR(j,i+1,N-1){
				if (pos[j]<=i) {
					int temp=pos[j];
					REVERSE_FOR(k,j-1,i) pos[k+1]=pos[k];
					pos[i]=temp;
					swap+=j-i;
					break;
				}
			}
		}
		}


		cout<<"Case #"<<Case<<": "<<swap;
		//printf("",);
		//cout<<;
		cout<<endl;
	}
	while(Case<numberOfTestCases);
	return 0;
}

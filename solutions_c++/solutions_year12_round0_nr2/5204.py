#include <stdlib.h>
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include<sstream>
#include <algorithm>
using namespace std; 
vector<int> scores;
int numGooglers;
int numSurprising;
int P;
int maxNum = -1;

struct Triplet {
int maxScore;
bool isSurprising;
};
void getSets(vector<Triplet> & posSets, int score) {
	Triplet nonSurp;
	Triplet Surp;
	if (score==30 || score ==0) {
		nonSurp.maxScore=score/3; nonSurp.isSurprising=false;
		Surp.maxScore=score/3; Surp.isSurprising=false;
	}
	else if(score==1) {
	nonSurp.maxScore=1; nonSurp.isSurprising=false;
		Surp.maxScore=1; Surp.isSurprising=false;
	}
	else if(score%3==0) {
		nonSurp.maxScore=score/3; nonSurp.isSurprising=false;
		Surp.maxScore=(score/3)+1; Surp.isSurprising=true;
	}
	else if(score%3==1) {
		nonSurp.maxScore=(score/3)+1; nonSurp.isSurprising=false;
		Surp.maxScore=(score/3)+1; Surp.isSurprising=true;
	}
	else {
		nonSurp.maxScore=(score/3)+1; nonSurp.isSurprising=false;
		if((score/3)+2<=10) {
		Surp.maxScore=(score/3)+2; Surp.isSurprising=true;
		}
		else {
		Surp = nonSurp;
		}
	}
	posSets.push_back(Surp); posSets.push_back(nonSurp);
}
void recSolve(int index, int curSurprising, int curMax) {
	if(index>=scores.size()) {
		//cout<<"Reached index > scores.size for index, curSurprising,curMax = "<<index<<curSurprising<<curMax<<endl;
		if(curMax >maxNum && curSurprising == numSurprising) {
			maxNum=curMax;
			//cout<<"Satisfied if for index, curSurprising,curMax = "<<index<<curSurprising<<curMax<<endl;
		}
	}
	if(index<scores.size()) {
	vector<Triplet> posSets;
	
	getSets(posSets,scores.at(index));
	for(int i =0;i<posSets.size();i++) {
		if(!posSets[i].isSurprising) {
			if(posSets[i].maxScore>=P) {
			//cout<<"Not surprising and >= P	for index and max score "<<index<<" " <<posSets[i].maxScore<<endl;		
				recSolve(index+1,curSurprising,curMax+1);
			
			}
			else {
				//cout<<"Not surprising and < P	for index and max score "<<index<<" " <<posSets[i].maxScore<<endl;
				recSolve(index+1,curSurprising,curMax);

			}
		}
		else {
			if(curSurprising<numSurprising) {
				if(posSets[i].maxScore>=P)  { 
				//	cout<<"Surprising and >= P and curSurp < numSurp	for index and max score and curSurp "<<index<<" " <<posSets[i].maxScore<<" " <<curSurprising<<endl;				
					recSolve(index+1,curSurprising+1,curMax+1);
				}
				else {
				recSolve(index+1,curSurprising+1,curMax);
				//cout<<"Surprising and < P and curSurp < numSurp	for index and max score and curSurp "<<index<<" " <<posSets[i].maxScore<<" " <<curSurprising<<endl;				
				}
			}
			else  {
				
			}
		}
	}
	}

}
void getResult(ofstream & myfile, int num) {
	recSolve(0,0,0);
	myfile<<"Case #"<<num<<": "<<maxNum<<endl;

}

int main () {
ofstream myfile; myfile.open("output.txt");
ifstream infile ("B-small-attempt0.in");
string line;
int numCases;
while(infile.good()) {
getline(infile,line);
numCases= atoi(line.c_str());
for(int i =1;i<=numCases;i++)
{
scores.clear();
maxNum=-1;
getline(infile,line);
istringstream tokenizer(line);
string token;
getline(tokenizer, token, ' ');
        istringstream int_iss(token);
        int_iss >> numGooglers;
getline(tokenizer, token, ' ');
        istringstream int_iss2(token);
        int_iss2 >> numSurprising;
getline(tokenizer, token, ' ');
        istringstream int_iss3(token);
        int_iss3 >> P;
int temp;
for(int s =0;s<numGooglers;s++) {
getline(tokenizer, token, ' ');
        istringstream int_iss4(token);
        int_iss4 >> temp;

	scores.push_back(temp) ;

}
getResult(myfile,i);
}
}
infile.close();
myfile.close();

return 0;

}
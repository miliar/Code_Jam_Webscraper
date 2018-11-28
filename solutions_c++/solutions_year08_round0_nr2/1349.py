#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <utility>
using namespace std;

void getData(ifstream & infile,int & T,int & NA,int & NB,vector<pair<int,int> > & AtoB,vector<pair<int,int> > & BtoA){
	string temp;
	infile>>T;
	infile>>NA>>NB;
	for (int i=1;i<=NA;i++){
		pair<int,int> p;
		infile>>temp;
		p.first=atoi(temp.substr(0,2).c_str())*60+atoi(temp.substr(3,2).c_str());
		infile>>temp;
		p.second=atoi(temp.substr(0,2).c_str())*60+atoi(temp.substr(3,2).c_str());
		AtoB.push_back(p);
	}
	for (int i=1;i<=NB;i++){
		pair<int,int> p;
		infile>>temp;
		p.first=atoi(temp.substr(0,2).c_str())*60+atoi(temp.substr(3,2).c_str());
		infile>>temp;
		p.second=atoi(temp.substr(0,2).c_str())*60+atoi(temp.substr(3,2).c_str());
		BtoA.push_back(p);
	}
}

int calc(int T,int NA,int NB,vector<pair<int,int> > AtoB,vector<pair<int,int> > BtoA){
	vector<bool> B(NB,true);
	pair<int,int> temp;
	for (int i=0;i<NA;i++){
		for (int j=i+1;j<NA;j++){
			if (AtoB.at(i).first>AtoB.at(j).first){
				temp=AtoB.at(i);
				AtoB.at(i)=AtoB.at(j);
				AtoB.at(j)=temp;
			}
		}
	}
	for (int i=0;i<NB;i++){
		for (int j=i+1;j<NB;j++){
			if (BtoA.at(i).second>BtoA.at(j).second){
				temp=BtoA.at(i);
				BtoA.at(i)=BtoA.at(j);
				BtoA.at(j)=temp;
			}
		}
	}
	int t=NA;
	for (int i=0;i<NA;i++){
		for (int j=0;j<NB;j++){
			if (B.at(j)&&AtoB.at(i).first>=BtoA.at(j).second+T){
				B.at(j)=false;
				t--;
				break;
			}
		}
	}
	return t;
}

int main(){
	int N;
	int T;
	int NA;
	int NB;
	vector<pair<int,int> > AtoB;
	vector<pair<int,int> > BtoA;
	ifstream infile("B-small.in");
	ofstream outfile("B-small.out");

	infile>>N;
	for (int i=1;i<=N;i++){
		AtoB.clear();
		BtoA.clear();
		getData(infile,T,NA,NB,AtoB,BtoA);
		outfile<<"Case #"<<i<<": "<<calc(T,NA,NB,AtoB,BtoA)<<" "<<calc(T,NB,NA,BtoA,AtoB)<<endl;
	}
	return 0;
}
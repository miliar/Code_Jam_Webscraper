#include<iostream>
#include<fstream>
#include<sstream>
#include<vector>
using namespace std;
int ToMinute(string time){
	int h,m;
	sscanf(time.c_str(),"%d:%d",&h,&m);
	return 60*h+m;
}
int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("B-large.in");
	fout.open("result");
	if(!fin){
		cerr<<"cannot open input file!"<<endl;
		system("pause");
		return -1;
	}
	int n;
	string skip;
	fin>>n;
	for(int i=0;i<n;i++){
		int time;
		int nA,nB;
		vector<int> tableA,tableB,tempA;
		fin>>time;
		fin>>nA>>nB;
		for(int j=0;j<nA;j++){
			string leave,arrive;
			fin>>leave>>arrive;
			tempA.push_back(ToMinute(leave));
			tableB.push_back(-ToMinute(arrive)-time);
		}
		for(int j=0;j<nB;j++){
			string leave,arrive;
			fin>>leave>>arrive;
			tableB.push_back(ToMinute(leave));
			tableA.push_back(-ToMinute(arrive)-time);
		}
		for(int j=0;j<tempA.size();j++){
			tableA.push_back(tempA[j]);
		}
		for(int j=0;j<tableA.size();j++){
			for(int k=tableA.size()-1;k>j;k--){
				if(tableA[k]*tableA[k]<tableA[k-1]*tableA[k-1]){
					int temp;
					temp=tableA[k];
					tableA[k]=tableA[k-1];
					tableA[k-1]=temp;
				}
			}
		}
		for(int j=0;j<tableB.size();j++){
			for(int k=tableB.size()-1;k>j;k--){
				if(tableB[k]*tableB[k]<tableB[k-1]*tableB[k-1]){
					int temp;
					temp=tableB[k];
					tableB[k]=tableB[k-1];
					tableB[k-1]=temp;
				}
			}
		}
		int trainA=0,trainB=0;
		int countA=0,countB=0;
		for(int j=0;j<tableA.size();j++){
			if(tableA[j]<0){
				trainA++;

			}
			else{
				if(trainA>0) trainA--;
				else	countA++;				
			}
		}
		for(int j=0;j<tableB.size();j++){
			if(tableB[j]<0){
				trainB++;
			}
			else{
				if(trainB>0) trainB--;
				else	countB++;
			}
		}
		fout<<"Case #"<<i+1<<": "<<countA<<' '<<countB<<endl;
	}
}

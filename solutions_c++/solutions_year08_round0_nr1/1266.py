//Google CodeJam
//Author : Harish Surana<surana4u@gmail.com>

#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <fstream>
using namespace std;
main(){
	int N;								//Number of cases
	int S;								//Number of servers
	int Q;								//Number of queries
	int count;							//Required Number 
	//int *temp;
	vector<string> SL;					//Server List
	vector<string> QL;					//Query List
    fstream fin("input.in",ios::in);	//Input File
	string sLine;
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
	for(int i=0;i<N;i++){
		count=0;
		//Reading List of servers
		getline(fin,sLine);
		S=atoi(sLine.c_str());
		//fout<<S<<"\n";
		for(int j=0;j<S;j++){
			getline(fin,sLine);
			//fout<<sLine<<"\n";
			SL.push_back(sLine.c_str());
		}
		
		//Reading List of Queries
		getline(fin,sLine);
		Q=atoi(sLine.c_str());
		//fout<<Q<<"\n";
		for(int k=0;k<Q;k++){
			getline(fin,sLine);
			//fout<<sLine<<"\n";
			QL.push_back(sLine.c_str());
		}

		//Main Logic
		int solved;
		solved=0;
		//cout<<SL.size();
		int *temp=new int[SL.size()];
		int processed;
		processed=0;
		do{

			for(int ii=0;ii<SL.size();ii++)
			{
				//cout<<SL.at(ii);
				temp[ii]=-1;
				int jj=0;
				jj=processed;
				for(;jj<QL.size();jj++)
				{
					if(SL.at(ii)==QL.at(jj))
					{
						temp[ii]=jj;
						break;
					}
				}
			}

			int max;
			max=0;
			for(ii=0;ii<SL.size();ii++)
			{
				
				
				if(temp[ii]>max){
					max=temp[ii];
				}
				else if(temp[ii]==-1){
					solved=1;
					break;
				}
			}

			if(solved!=1){
				processed=max;
				count+=1;
			}
/*
			if(processed==SL.size()){
				solved=1;
			}
*/
		} while(solved!=1);

		fout<<"Case #"<<i+1<<": "<<count<<"\n";
		//Clearing List of servers
		SL.clear();
		//Clearing List of Queries
		QL.clear();
	}
	
	fin.close();
	fout.close();
}
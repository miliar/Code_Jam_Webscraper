#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

bool check(int points, int min, int &surprising){
	int ypol=points%3;
	int dier=points/3;

	

	if(dier>=min)
		return 1;

	if(points<2)
		return 0;
	
	if(ypol==0){
		if(dier+1>=min){
			if(dier+1>=min-1 && surprising>0){
				surprising--;
				return 1;
			}else
				return 0;
		}
	}

	if(ypol==1){
		if(dier+1>=min){
			return 1;
		}
		/*if(dier+1>=min-1 && surprising>0){
			surprising--;
			return 1;
		}else*/
			return 0;
		
	}

	if(ypol==2){
		if(dier+1>=min){
			return 1;
		}
		if(dier+2>=min){

			if(dier+1>=min-1 && surprising>0){
				surprising--;
				return 1;
			}else
				return 0;
		}
	}
	return 0;
}

int main(int argc, char* argv[])
{
	ifstream fin ("B-small-attempt3.in");
	//ifstream fin ("B-large.in");
    ofstream fout ("output.out");

	int googlers=3;
	int surprising=0;
	int p=8;
	

	int cases;
	fin >> cases;

	cout<<cases;
	
	string buffer;
	getline(fin,buffer); //ignore first line

	for(int i=1;i<=cases;i++){
		fout << "Case #"<<i<<": ";
		
		fin>>googlers;
		fin>>surprising;
		fin>>p;

		int counter=0;
		int next;
		for(int i=0;i<googlers;i++){	
			fin>>next;
			counter+=check(next,p,surprising);

		}
			

		fout<<counter<<endl;
	}

	fin.close();
	fout.close();

	




	system("pause");
	return 0;
}
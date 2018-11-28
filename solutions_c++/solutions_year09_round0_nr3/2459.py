#include <iostream>
#include <string>
#include <fstream>

#include <cmath>
using namespace std;

ifstream fin("C-small-attempt1.in");
ofstream fout("B-Small.out");

char line[31];
string word = "welcome to code jam";
int count;
int length;
void recurson(int l_index,int index){

	for(int i = l_index ; i < length; i++){
		if(line[i] == word[index]){	
			recurson(i+1,index+1);
			if(index == 18){
				count++;
			}
		
		}
	}
	return ;
}

void process(){
	int result;
	int w_index = 0;
	int flag = 0;
	
	fin.getline(line,31,'\n');

	result  = atoi(line);

	for(int i = 0 ; i < result ; i++){
		fin.getline(line,31,'\n');
		length = strlen(line);
		count = 0;
		for(int k = 0 ; k < length ; k++){
			if(line[k] == 'w'){
				recurson(k+1,1);
			}
		}
		fout<<"Case #"<<i+1<<": ";
		if(count < 10)
			fout<<"000"<<count<<endl;
		else if(count < 100)
			fout<<"00"<<count<<endl;
		else if(count < 1000)
			fout<<"0"<<count<<endl;
		else
			fout<<count<<endl;
	}
}


int main(){
	
	process();

	return 0;
}
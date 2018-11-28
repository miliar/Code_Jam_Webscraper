#include <iostream>
#include <string>
#include <fstream>

using namespace std;

ifstream fin("A-large.in");
ofstream fout("test.out");

int length;
int language;
int test;
string Language[5000];

void input(){
	fin>>length>>language>>test;
	
	for(int i = 0 ; i < language ; i++){
		fin>>Language[i];
	}
}

void process(){
	string temp;
	string input;
	int result ;
	int index ;
	int flag;
	int p_flag;
	
	
	for(int i = 0 ; i < test ; i++){
		fin>>input;
		result = 0;
		
		for(int k = 0 ; k < language ; k++){
			temp = Language[k];
			index = 0;
			flag = 0;
			p_flag = 0;

			for( int l = 0 ; l < input.length() ; l++){
				if(input[l] == '('){
					p_flag = 1;
					continue;
				}
				else if(input[l] == ')'){
					index++;
					p_flag = 0;
					if(flag == 0)
						break;
					flag =0;
				}
				else if(input[l] == temp[index]){
						if(p_flag == 0)
						index++;
						else if(p_flag == 1)
							flag = 1;
				}
				else if(input[l] != temp[index]){
						if(p_flag == 0)
							break;
				}
			}
			
			if( l == input.length())
				result++;
		}
		
		fout<<"Case #"<< i+1 <<": "<<result<<endl;
	}
}


int main(){
	
	input();
	process();

	return 0;
}
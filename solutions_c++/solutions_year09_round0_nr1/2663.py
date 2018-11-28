#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<string>
#include<cstring>
#include<map>


using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::map;

int main(){

	int L, D, N;
	cin >> L >>  D >> N;
	string words[5000];
	int ok[5000];

	for(int i=0; i<D;i++){
		string temp;
		cin >> temp;
		words[i]=temp;
		ok[i] = 0;
	}
	for(int i=0; i<N; i++){
		string temp; 
		cin >> temp;
		int size=0;
		//cout << temp << endl;
		for(int j=0; j< temp.length(); j++){
			if( temp[j] == '('){
				while( temp[j] != ')'){
					j++;
					for(int k=0; k<D; k++){
						if(ok[k] == size ){
							//cout << words[k] << endl;
							if( words[k].at(size) == temp[j]) ok[k] = size+1;
						}
					}
				}
			}else{
				for(int k=0; k<D; k++){
					if(ok[k] == size ){
						//cout << words[k] << endl;
						if( words[k].at(size) == temp[j]) ok[k] = size+1;
					}
				}
				
			}
			size++;
		}
		int count=0;
		int o=i+1;
		for(int j=0; j<D;j++){
			if(ok[j] >= size) count++;
			ok[j]=0;
		}
		cout<< "Case #" << o << ": " << count << endl; 
		//exit(0);
	}	
}

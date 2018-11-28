#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char* argv[]){
	int numOfCases;
	char translation_rules[] = {'y','h', 'e', 's','o','c', 'v', 'x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	char old_line[200];
	

	ofstream output;
	ifstream input;
	
	input.open(argv[1]);
	if (!input){
		cout << "Cannot open file "<<argv[1]<<endl;
		return -1;
	}
	cout << "File "<< argv[1] <<" opened for reading" <<endl;

	output.open(argv[2]);
	if (!output){
		cout << "Cannot open file "<<argv[2]<<endl;
		return -1;
	}
	cout << "File "<< argv[2] <<" opened for writing" <<endl;

	input>>numOfCases;
	input.getline(old_line, 200);


	for(int i=0; i<numOfCases; i++){
		input.getline(old_line, 200);
		int j=0;
		output<<"Case #"<<i+1<<": ";
		while(old_line[j]!='\0'){
			if (old_line[j]!=' ') output<<translation_rules[old_line[j]-97];
			else output<<old_line[j];
			j++;
		}
		output<<endl;
	}

	cout<<"Translation finished"<<endl;

	input.close();
	output.close();

	return 0;


}
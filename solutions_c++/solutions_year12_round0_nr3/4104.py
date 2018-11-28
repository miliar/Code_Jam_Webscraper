#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;


string rotate(string a){
	//moves first number to last pos 14->41

	string out;

	for(int i=1;i<a.size();i++){
		out.push_back(a.at(i));

	}

	out.push_back(a.at(0));//writes the 1st number
	return out;
}

/*bool check(string a,int max){
	string rotatedA=rotate(a);

	int intA=atoi(a.c_str());
	int intRotatedA=atoi(rotatedA.c_str());

	if(intRotatedA>max)
		return 0;

	return intA<intRotatedA;
	
}*/

int count(string original,int min, int max){
	int intOriginal=atoi(original.c_str());
	int count=0;

	string rotatedA=original;
	int intRotatedA;

	do{
		rotatedA=rotate(rotatedA);	
		intRotatedA=atoi(rotatedA.c_str());
		if(intRotatedA>=min && intRotatedA<=max && intRotatedA!=intOriginal){
			count++;
			

		}

	}while(intRotatedA!=intOriginal); 

	return count;

}

string i2string(int i) {
	char buffer[10];
	itoa(i,buffer,10);

	string out=buffer;
	return out;

}

int main(int argc, char* argv[])
{
	ifstream fin ("C-small-attempt2.in");
	//ifstream fin ("B-large.in");
    ofstream fout ("output.out");
	

	int cases;
	fin >> cases;

	cout<<cases;
	
	string buffer;
	getline(fin,buffer); //ignore first line

	for(int i=1;i<=cases;i++){
		fout << "Case #"<<i<<": ";
		
		
		int numA;
		fin>>numA;
		int numB;
		fin>>numB;

		int counter=0;

	
		for(int i=numA;i<=numB;i++){
			string str;
			str=i2string(i);
			counter+=count(str,numA,numB);


		}
		
		if(counter%2==1)
			cout<<i<<endl;
	
		fout<<counter/2;
			
		fout<<endl;
	}

	fin.close();
	fout.close();

	

	system("pause");
	return 0;
}
#include <iostream>
#include <fstream>
#include <string>

#define PATHIN "C-small-attempt0.in"
#define PATHOUT "C-small-attempt0.out"

using namespace std;


void int2str(int a,string & astr){
	char x[7];
	itoa(a,x,10);
	astr=x;
}

bool isAllSame(string x){
	for(int i=1 ; i<x.length() ; i++){
		if(x[i]!=x[i-1])
			return false;
	}
	return true;
}


int countIt(int min,int max){

	string curStr,minStr,maxStr;
	string temp;
	int count = 0;


	int2str(min,minStr);
	int2str(max,maxStr);

	for(int i=min ; i<=max ; i++){
		int2str(i,curStr);	


		if(isAllSame(curStr))
			continue;


		for(int j=curStr.length()-1 ; j>0 ; j--){
			temp="";
			temp.append(curStr,j,curStr.length()-j);
			temp.append(curStr,0,j);

			if(atoi(temp.c_str())<=max && atoi(temp.c_str())>i)
			{
				count++;
			}
		}
	}

	return count;
}

void main(){
	fstream FILEIN(PATHIN);
	fstream FILEOUT(PATHOUT);

	int count;
	int A,B;

	FILEIN>>count;

	for(int i=0 ; i<count ; i++){
		FILEIN>>A>>B;
		FILEOUT<<"Case #"<<i+1<<": ";
		FILEOUT<<countIt(A,B)<<endl;

		cout<<"Case #"<<i+1<<": ";
		cout<<countIt(A,B)<<endl;
	}
}
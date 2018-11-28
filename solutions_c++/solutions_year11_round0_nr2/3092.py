#include <math.h>
#include <stdlib.h>

#include <iostream>
#include <fstream>
#include <string.h>
using namespace std;

#define MAX_CASES 100

class Case{
	int C,D,N;
	char combine[3][50],oppose[2][50],invoke[100];

public:

	Case(){
		C=D=N=0;
	}

	void AddCombine(char *inCombine){
		combine[0][C]=inCombine[0];
		combine[1][C]=inCombine[1];
		combine[2][C]=inCombine[2];
		C++;
	}

	void AddOppose(char *inOppose){
		oppose[0][D]=inOppose[0];
		oppose[1][D]=inOppose[1];
		D++;
	}

	void AddInvoke(char *inInvoke,int inN){
		for (int i=0;i<inN;i++){
			invoke[i]=inInvoke[i];
		}
		N=inN;
	}

	bool Combine(char a,char b, char *c){
		if (C==0) return false;
		for (int i=0;i<C;i++){
			if ((a==combine[0][i])&&(b==combine[1][i])){
				*c=combine[2][i];
				return true;
			}
			if ((b==combine[0][i])&&(a==combine[1][i])){
				*c=combine[2][i];
				return true;
			}
		}
		return false;
	}

	bool Opposed(char a, char b){
		if (D==0) return false;
		for (int i=0;i<D;i++){
			if ((a==oppose[0][i])&&(b==oppose[1][i])) return true;
			if ((b==oppose[0][i])&&(a==oppose[1][i])) return true;
		}
		return false;
	}

	int GetFinalElementList(char *list){
		int result;
		char c;

		list[0]=invoke[0];
		result=1;
		if (N==1) return result;

		for (int i=1;i<N;i++){
			list[result]=invoke[i];
			result++;
			if (result>1){
				if (Combine(list[result-2],invoke[i],&c)) {
					list[result-2]=c;
					result--;
				}else{
					if (result>0){
						for (int j=0;j<result;j++){
							if (Opposed(list[j],invoke[i])) result=0;
						}
					}
				}
			}
		}
		return result;
	}
};


int main(){
	ifstream in("inputFile");
	ofstream out("outputFile");

	char item[100];
	int number,T;

	Case cases[MAX_CASES];

	in >> T;

	for (int i=0;i<T;i++){
		in >> number;
		if (number>0){
			for (int j=0;j<number;j++){
				in >> item;
				cases[i].AddCombine(item);
			}
		}
		in >> number;
		if (number>0){
			for (int j=0;j<number;j++){
				in >> item;
				cases[i].AddOppose(item);
			}
		}
		in >> number;
		in >> item;
		cases[i].AddInvoke(item,number);
	}

	in.close();

	for (int i=0;i<T;i++){
		number=cases[i].GetFinalElementList(item);
		out << "Case #" << i+1 << ": [";
		if (number>0){
			out << item[0];
			if (number>1){
				for (int j=1;j<number;j++){
					out << ", " << item[j];
				}
			}
		}
		out <<"]" << endl;
	}

	out.close();

	return 0;
}

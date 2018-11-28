#include <iostream>
#include <string>
using namespace std;


void solveEachCase();

void main(){

	int caseNum;
	cin >> caseNum;
	for(int i = 1; i <= caseNum; i++){
		cout << "Case #" << i << ":"<<endl;
		solveEachCase();
		//if(i!= caseNum)
		//	cout << endl;
	}

}

void solveEachCase(){
	int pNum;
	cin >> pNum;
	int* resBoard = (int*) malloc(pNum*pNum*sizeof(int));

	char* str = (char*) malloc((pNum + 10)*sizeof(char));
	string temp;
	for(int i = 0; i < pNum; i++){
		//cin.getline(str, pNum + 10);
		cin >> temp;
		for(int j =0; j < pNum; j++){
			if(temp.at(j) == '.')
				resBoard[i*pNum +j] = -1;
			else if(temp.at(j)=='0')
				resBoard[i*pNum +j] = 0;
			else if(temp.at(j)=='1')
				resBoard[i*pNum +j] = 1;
		}

	}

	//for(int i = 0; i < pNum; i++){
	//	for(int j = 0; j < pNum; j++)
	//		cout << resBoard[i*pNum +j] <<":";
	//	cout << endl;
	//}

	double* wp = (double*) malloc(pNum* sizeof(double));
	int* gameNum = (int *) malloc(pNum* sizeof(int));
	for(int i =0; i < pNum; i++){
		wp[i] = 0; //init
		gameNum[i] = 0;
		for(int j = 0; j < pNum; j++){
			if(resBoard[i * pNum +j] >= 0){
				wp[i] += resBoard[i * pNum +j];
				gameNum[i]++;
			}

		}
		if(gameNum[i]!=0)
			wp[i] = wp[i]*1.0/gameNum[i];
		//cout << wp[i]<<endl;
	}

	double* owp = (double*) malloc(pNum* sizeof(double));

	for(int i = 0; i < pNum; i++){
		owp[i] = 0;//init
		int oNum = 0;
		for(int j = 0; j < pNum;j++){
			if(resBoard[i*pNum +j]>=0){
				oNum ++;
				double temp1 = wp[j]*gameNum[j] - resBoard[j* pNum +i];
				if(gameNum[j]>=2)
					temp1 = temp1/(gameNum[j]-1);
				else
					temp1 = 0;
				owp[i] += temp1;
			}
		}
		if(oNum > 0)
			owp[i] = owp[i]/oNum;
		/*cout <<owp[i]<<endl;*/
	}

	double* oowp = (double*) malloc(pNum*sizeof(double));
	for(int i = 0; i< pNum; i++){
		oowp[i] = 0;
		int temp2 = 0;
		for(int j = 0; j < pNum; j++){
			if(resBoard[i*pNum + j] >= 0){
				temp2 ++;
				oowp[i] += owp[j];
			}
		}
		if(temp2 > 0)
			oowp[i] = oowp[i]/temp2;
		/*cout<<oowp[i]<<endl;*/
	}
	for(int i = 0; i< pNum; i++){
		double rpi = 0.25* wp[i] + 0.5* owp[i] +0.25* oowp[i];
		cout << rpi<<endl;
	}
}
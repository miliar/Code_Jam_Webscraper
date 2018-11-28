#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <math.h>
#include <unordered_map>
using namespace std;
typedef std::tr1::unordered_map<int, int>HashMap;

bool find(int *set, int max, vector<int> &out1, vector<int> &out2)
{
	HashMap sum;
	int bitNumMax = (int)pow(2,(float)max);
	for(int i = 0; i <  bitNumMax; i++){
		int tempSum = 0;
		int k = max - 1;
		for(int j = 1; j <= bitNumMax; j *= 2){
			if(i & (bitNumMax / j)){
				tempSum += set[k];
			}
			k--;
		}
		HashMap::iterator it = sum.find(tempSum);
		if(it != sum.end()){
			int find = it->second;
			k = max - 1;
			for(int j = 1; j <= bitNumMax; j *= 2){
				if(find & (bitNumMax / j)){
					out1.push_back(set[k]);
				}
				if(i & (bitNumMax / j)){
					out2.push_back(set[k]);
				}
				k--;
			}
			return true;
		}
		else{
			if(tempSum != 0)
			sum.insert(HashMap::value_type(tempSum, i));
		}
	}
	return false;
}

int main()
{
	vector<int> hi;

	int iCaseNum = 0;
	
	cin >> iCaseNum;
	int **iInput = (int**)malloc(sizeof(int*) * iCaseNum);
	int **iOutput = (int**)malloc(sizeof(int*) * iCaseNum);
	int *iResultNum = (int*)malloc(sizeof(int) * iCaseNum);
	cin.clear();
	cin.sync();
	for(int iCase = 0; iCase < iCaseNum; iCase++){
		int iSetNum = 0;
		cin >> iSetNum;
		iResultNum[iCase] = iSetNum;
		iInput[iCase] = (int*)malloc(sizeof(int) * iSetNum);
		for(int i = 0; i < iSetNum; i++){
			cin >> iInput[iCase][i];
		}
	}
	for(int iCase = 0; iCase < iCaseNum; iCase++){
		
		//iResultNum[iCase] = iSetNum;
		//iOutput[iCase] = (int*)malloc(sizeof(int) * iSetNum);
	}
	for(int iCase = 0; iCase < iCaseNum; iCase++){
		cout << "Case #" << iCase + 1<< ":" << endl;
		vector<int> a, b;
		if(find(iInput[iCase], iResultNum[iCase],a,b)){
			for(int i = 0; i < (int)a.size(); i++){
				cout << a[i];
				if(i != a.size() - 1) cout << " ";
				else cout << endl;
			}
			for(int i = 0; i < (int)b.size(); i++){
				cout << b[i];
				if(i != b.size() - 1) cout << " ";
				else cout << endl;
			}
		}
		else cout << "Impossible" << endl;
	}
	system("pause");
	return 0;
}
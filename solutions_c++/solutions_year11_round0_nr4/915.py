#include <iostream>
#include <vector>
#include <stdio.h>


using namespace std;

vector<int> dataset;

int elementsInRightPlace(){
	int counter=0;
	for(int i=0; i<dataset.size(); i++){
		if(dataset[i]==(i+1)) counter++;
	}
	return counter;
};


int main(){
	int cases;
	cin >> cases;
	
	for(int i=0;i<cases;i++){
		int n;
		double hits;
		dataset.clear();

		cin >> n;
		for(int j=0; j<n; j++){
			int tmp;
			cin >> tmp;
			dataset.push_back(tmp);
		}
		float bad = n-elementsInRightPlace();
		printf("Case #%d: %.6f\n",i+1,bad);	
	}
	
	return 0;
}
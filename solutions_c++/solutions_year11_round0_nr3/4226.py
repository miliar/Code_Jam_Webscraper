#include <iostream>
#include <fstream>
using namespace	std;
int calculateMax(int num, int *value);
int main (int argc, char * const argv[]) {
    ifstream is("C-large.in");
	int num = 0;
	int *numforeach =NULL;
	int **value = NULL;
	is >> num;
	cout << num;
	value = new int*[num];
	numforeach = new int[num];
	for (int i = 0;i<num ; i++){
		is >> numforeach[i];
		cout << numforeach[i];
		value[i] = new int[numforeach[i]];
		for (int j = 0; j< numforeach[i] ; j++){
			is >> value[i][j];
			cout << value[i][j];
		}
	}
//begin the algorithm
	ofstream os("result");
	for (int i = 0; i<num ; i++){
		int result = calculateMax(numforeach[i],value[i]);
		os << "Case #"<<i+1<<": ";
		if (result < 0){
			os << "NO" <<endl;
		} else {
			os << result <<endl;
		}
	}
	os.close();
	return 0;
}

int calculateMax(int num, int *value){
	unsigned int result = -1;
	unsigned int sum = 0;
	int xsum = 0;
	int min = 1000000;
	for (int i=0 ; i<num; i++){
		sum +=value[i];
		xsum ^= value[i];
		if (value[i] < min) min = value[i];
	}
	if (xsum !=0) return -1;
	else result = sum - min;
	return result;
}

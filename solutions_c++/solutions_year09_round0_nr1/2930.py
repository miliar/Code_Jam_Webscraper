#include <iostream>
#include <fstream>

using namespace std;

int main() {
	int L,D,N;
	
	int i, j, s;

	cin >> L >> D >> N;

	ofstream fout("result.txt");

	char **word = new char * [D];
	for( i=0; i<D; i++ ) {
		word[i] = new char [L+1];
		cin >> word[i];
	}

	char **input = new char *[N];
	for( i=0; i<N; i++ ) {
		input[i] = new char [28*L+10];
		cin >> input[i];
	}

	bool equal = true;
	int equal_count = 0;
	bool ee = false;

	int k=0;


	for( s=0; s<N; s++ ) {

	//用D个词来匹配这个case
	for ( i=0; i<D; i++ ) {
		//假设第i个词与模式匹配
		equal = true;
		k = 0;
		//对第i个词遍历
		for( j=0; j<L; j++ ) {
			//如果不是左括号(则是正常词
			if( input[s][k]!='(' ) {
				//有相等则继续
				if( input[s][k] == word[i][j] ) {
					k++;
					continue;
				}
				//不相等，这个词肯定不匹配
				else {
					equal = false;
					break;
				}
			}
			//如果是左括号，则是模式
			else if( input[s][k] == '(' ) {
				k++;
				//假设和这个模式不匹配
				ee = false;
				//到达右括号之前
				while( input[s][k] != ')' ) {
					//如果有相等
					if( input[s][k] == word[i][j] ) {
						//模式匹配，
						ee = true;
						//遍历至右括号
						while( input[s][k] != ')' ) k++;
						//再往下走一格
						k++;
						//已经走到模式外，跳出模式匹配
						break;
					}
					//如果未到模式边上，则继续前进
					else {
						k++;
					}
				}
				//退出模式时，如果模式内不匹配，则也别接着比了
				if( ee == false ) {
					equal = ee;
					break;
				}
			}
			else {
				cout << "go to error place\n";
			}
		}
		//一个词比完，结果如果是false，则不增加
		if( equal ) equal_count++;
	}
	fout << "Case #" << s+1 << ": " << equal_count << endl;
	equal_count = 0;
	}


	for( i=0; i<N; i++ ) {
		delete [] input[i];
	}
	delete [] input;

	for( i=0; i<D; i++ ) {
		delete [] word[i];
	}
	delete [] word;
	return 0;
}
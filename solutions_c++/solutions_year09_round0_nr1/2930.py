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

	//��D������ƥ�����case
	for ( i=0; i<D; i++ ) {
		//�����i������ģʽƥ��
		equal = true;
		k = 0;
		//�Ե�i���ʱ���
		for( j=0; j<L; j++ ) {
			//�������������(����������
			if( input[s][k]!='(' ) {
				//����������
				if( input[s][k] == word[i][j] ) {
					k++;
					continue;
				}
				//����ȣ�����ʿ϶���ƥ��
				else {
					equal = false;
					break;
				}
			}
			//����������ţ�����ģʽ
			else if( input[s][k] == '(' ) {
				k++;
				//��������ģʽ��ƥ��
				ee = false;
				//����������֮ǰ
				while( input[s][k] != ')' ) {
					//��������
					if( input[s][k] == word[i][j] ) {
						//ģʽƥ�䣬
						ee = true;
						//������������
						while( input[s][k] != ')' ) k++;
						//��������һ��
						k++;
						//�Ѿ��ߵ�ģʽ�⣬����ģʽƥ��
						break;
					}
					//���δ��ģʽ���ϣ������ǰ��
					else {
						k++;
					}
				}
				//�˳�ģʽʱ�����ģʽ�ڲ�ƥ�䣬��Ҳ����ű���
				if( ee == false ) {
					equal = ee;
					break;
				}
			}
			else {
				cout << "go to error place\n";
			}
		}
		//һ���ʱ��꣬��������false��������
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
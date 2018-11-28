#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <string>
using namespace std;

string Invoke(vector<string> &base, vector<string> &opposed, vector<char> &elements, int &C, int &D)
{
	string result;
	bool hasCombined = false;

	if (base.size() == 0 && opposed.size() == 0) {
		for(int i = 0; i < elements.size(); i++)
			result += elements[i];
	}
	else {
		vector<char>::iterator iteB0;
		vector<char>::iterator iteB1;
		vector<char>::iterator iteC0;
		vector<char>::iterator iteC1;

		if (base.size() != 0) {
			for(int i = 0; i < C; i++) {
				if (elements.size() == 1) {
					iteB0 = find(elements.end() - 1, elements.end(), base[i][0]);
					iteB1 = find(elements.end() - 1, elements.end(), base[i][0]);
				}
				else {
					if (base[i][0] != base[i][1]) {
						iteB0 = find(elements.end() - 2, elements.end(), base[i][0]);
						iteB1 = find(elements.end() - 2, elements.end(), base[i][1]);
					}
					else {
						iteB0 = find(elements.end() - 2, elements.end(), base[i][0]);
						if (iteB0 != elements.end() && iteB0 == elements.end() - 1) 
							iteB1 = find(elements.end() - 2, elements.end(), base[i][1]);
						else iteB1 = find(elements.end() - 1, elements.end(), base[i][1]);
					}
				}
		

				if (elements.size() > 1) {
					if (base[i][0] == base[i][1]) {
						if ((iteB0 == elements.end() - 1 && iteB1 == elements.end() - 2 ) || (iteB0 == elements.end() - 2 && iteB1 == elements.end() - 1 )) {								// ==combine���� �悤�₭R, I, R���o���Ƃ��낾���獢��. �Y��ɏ������Ƃ�������orz
							elements.erase(elements.end() - 2, elements.end());		// ���������������Ƃ��ɂ��ڂ�
							elements.push_back(base[i][2]);
							hasCombined = true;
						}
					}
					else {
						if (/*(elements[])*/iteB0 != elements.end() && iteB1 != elements.end()) {		// �p�d�̎��ɂ����ɂ��Ă��܂�orz						// ==combine���� �悤�₭R, I, R���o���Ƃ��낾���獢��. �Y��ɏ������Ƃ�������orz
							elements.erase(elements.end() - 2, elements.end());		// ���������������Ƃ��ɂ��ڂ�
							elements.push_back(base[i][2]);
							hasCombined = true;
						}
					}
				}
				if (hasCombined) break;		// combine�͂P��
			}
		}

		if (!hasCombined && opposed .size() != 0 && elements.size() > 1) {
			for(int i = 0; i < D; i++) {
				iteC0 = find(elements.begin(), elements.end(), opposed[i][0]);
				iteC1 = find(elements.begin(), elements.end(), opposed[i][1]);	// �����������l�ɏꍇ�킯�H�@���艟������

				if (iteC0 != elements.end() && iteC1 != elements.end()) {
					elements.erase(elements.begin(), elements.end());		
					break;														// �폜�͂P��ł������낤
				}
			}
		}

		for(int i = 0; i < elements.size(); i++)
			result += elements[i];
	}
	
	return result;
}

int main() {
	/*ifstream cin("B-small-attempt3.in");	// cin���t�@�C���Ɋ��蓖�ĂāA��͕��ʂɎg��.
	ofstream ofs("B-smallOa.txt");*/
	ifstream cin("B-large.in");	
	ofstream ofs("B-largeO.txt");

	int T, C, D, N;
	vector<string> base;		// [0]��[1]��combine�����[2]�ɂȂ�
	vector<string> opposed;		// [0]��[1]��(�w�肳�ꂽ������)�ł���������
	vector<char> elements;
	string result, tmp;

	cin >> T;
	for(int i = 0; i < T; i++) {
		elements.clear();
		result = "";
		base.clear();
		opposed.clear();

		cin >> C;
		for(int j = 0; j < C; j++) {
			string tmp;
			cin >> tmp;
			base.push_back(tmp);
		}

		cin >> D;
		for(int j = 0; j < D; j++) {
			string tmp;
			cin >> tmp;
			opposed.push_back(tmp);
		}

		cin >> N >> tmp;
		//elements.resize(1);
		for(int j = 0; j < N; j++) {
			elements.push_back(tmp[j]);

			result = Invoke(base, opposed, elements, C, D);
		}

		//ofs << "Case #" << i + 1 << ": [" << result << "]" << endl;
        ofs << "Case #" << i + 1 << ": [" << flush;
		for(int j = 0; j < result.size(); j++)
			if (j != result.size() - 1) ofs << result[j] << ", " << flush;
			else ofs << result[j] << "" << flush;
		ofs << "]" << endl;
	}
}

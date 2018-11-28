// R1A_A.cpp : �������̨Ӧ�ó������ڵ㡣
//

#include "stdafx.h"
#include <fstream>
#include <string>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <vector>
#include <bitset>
#include <math.h>
#include <algorithm>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	fstream infile, outfile;
	infile.open("A-large.in", fstream::in);
	outfile.open("A-large.out", fstream::out);
	string line;

	int CaseNum;
	int A, B;
	int N;
	double tmp;
	vector<double> ps;
	double p=1.0f;
	double result = 0;

	if(infile){
		infile >> CaseNum;
		for(int i=0; i<CaseNum; ++i){
			p=1.0f;
			ps.clear();
			infile >> A >> B;
			// ��ȡ����
			for(int j=0; j<A; ++j){
				infile >> tmp;
				ps.push_back(tmp);
			}

			// �����3�����
			result = (double)B+2.0f;
			//cout << result << ", ";

			// �����1 2 ���
			p = 1.0f;
			for(int j=A; j>=0; --j){
				N = A-j;
				if(N > 0){
					p = p * ps[N-1];
				}
				tmp = (double)(B-N+1)*p + (double)(B-N+1+B+1)*(1.0f-p) + (double)j;
				//cout << tmp << ", ";

				if(result >= tmp){
					result = tmp;
				}
			}
			//cout << endl;
			
			outfile << "Case #" << i+1 << ": ";
			outfile << setprecision(6);
			outfile << fixed << setprecision(6)<< result << endl;
			cout << "Case #" << i+1 << ": ";
			
			cout << fixed << setprecision(6)<< result << endl;
		}
	}
	infile.close();
	outfile.close();
	return 0;
}


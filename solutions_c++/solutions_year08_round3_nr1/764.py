//============================================================================
// Name        : google_code_common.cpp
// Author      : muramasa
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================
//using boost
//using gnu mp
#include <vector>
#include <numeric>
#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <algorithm>
#include <boost/lexical_cast.hpp>
#include <boost/format.hpp>
#include <boost/numeric/ublas/matrix.hpp>   // 普通の行列用のヘッダ
#include <boost/numeric/ublas/vector.hpp>   // 普通のベクトル用のヘッダ
#include <boost/numeric/ublas/io.hpp>       // ストリーム入出力用ヘッダ
#include <gmpxx.h>
using namespace std;
using boost::lexical_cast;

vector<string> split_to_words(string split_key,string paragraf){
	vector<string> answer_words;
	if(split_key.empty()==true || paragraf.empty()==true){
		return answer_words;
	}
	for (bool end_flag = false; end_flag == false;) {
		string::size_type index = paragraf.find(split_key.c_str());
		if (index < 1) {
			//もう割れない
			end_flag = true;
		} else {
			answer_words.push_back(paragraf.substr(0, index));
			//行末にスペースがあったときの対策
			if(index < paragraf.size()-split_key.size()){
				paragraf = paragraf.substr(index + split_key.size());
			}else{
				end_flag = true;
			}
		}
	}
	return answer_words;
}

namespace ublas=boost::numeric::ublas;
int main() {
	//boost 使用時の定義
    typedef ublas::matrix<double> dmatrix;
    typedef ublas::vector<double> dvector;

	//入力ファイル指定 Select input file
	ifstream ifs("1.in");
	//出力ファイル指定 Select output file
	ofstream ofs("A-small.out", std::ios::out | std::ios::trunc);
	//caseを取得　get cases
	string buf;
	getline(ifs, buf);
	int cases = lexical_cast<int> (buf);
	cout << "cases : " << cases << endl;
	//caseごとの処理　doing in cases
	for (int j = 0; j < cases; j++) {
		cout << "case : " << j << endl;
		long P,K,L;
		ifs >> P >> K >> L;
		long mini_P = L/K;
		cout << "mini_P : " << mini_P;
		long max_P = mini_P+1;
		cout << " max_P : " << max_P;
		long max_Keys = L%K;
		cout << " max_Keys : " << max_Keys << endl;
		vector<long> freqs;
		for(int i=0;i<L;++i){
			long temp;
			ifs>>temp;
			freqs.push_back(temp);
		}
		sort(freqs.begin(),freqs.end());
		long sum_push=0;
		for(long n=0;n<freqs.size();++n){
			if(n<max_Keys){
				sum_push +=freqs[n]*max_P;
				cout << "in max : " << freqs[n]<< endl;
			}else{
				long temp=0;
				temp = (n-max_Keys)/K;
				temp = mini_P-temp;
				sum_push += freqs[n]*temp;
				cout << "temp : " << temp;
				cout << " num : " << freqs[n] << endl;
			}
		}
		ofs << "Case #" << j + 1 << ": " << sum_push
		<< endl;
	}
	return 0;
}

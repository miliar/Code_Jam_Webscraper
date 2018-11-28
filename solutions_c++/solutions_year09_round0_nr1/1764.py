// GoogleCodeJum.cpp : コンソール アプリケーションのエントリ ポイントを定義します。
//

#include "stdafx.h"
#include <algorithm>
#include <deque>
#include <iostream>
#include <functional>
#include <string>

using namespace std;

string LETTERS[5000];
int GOOD[5000];
int  L,D,N;


int check_answer(){
	int i = 0;
	int answer = 0;
	while(i < D){
		if(GOOD[i] == 1)
			answer++;
		i++;
	}
	return answer;
}

void check_letters(string in, int pos){

	int i = 0;
	int j;
	char a;
	int length = in.size();
	int NOWGOOD[5000] = {0};
	//cout << pos <<in << length << endl;

	while(i < length){
		a = in.at(i);
		j=0;
		while(j < D){
			if((GOOD[j] == 0)||(NOWGOOD[j] == 1)){
				;
			}	
			else if(a == LETTERS[j].at(pos)){
				NOWGOOD[j] = 1;
				
			}
			else if(i == length - 1){
				GOOD[j] = 0;
				
			}
			j++;
		}
		i++;
	}

	return;	
}

void check_letter(char a,int pos){

int i = 0;
while (i < D){
	if(a != LETTERS[i].at(pos))
		GOOD[i] = 0;
	i++;
}
return;

}


void calc(string question){

	int i = 0;
	int j;
	int pos = 0;
	int length = question.size();

	while(i < length){

		if(question.at(i) == '('){
			j = i+2;
			while(question.at(j) != ')'){
				j++;
			}
			check_letters(question.substr(i+1, j-i-1),pos);
			i = j;
		}
		else{
			check_letter(question.at(i),pos);
		}
		i++;
		pos++;
	}

	return;
}



int _tmain(int argc, _TCHAR* argv[])
{
	using namespace std;
	int loop;
	int count = 0;
	long answer = 0;
	int i;
	string question;

	cin >> L >> D >> N;
	loop = D;
	i = 0;
	//cout << L << D << N;

	while(loop--){
		cin >> LETTERS[i];
		i++;
	}

	loop = N;
	while(loop--){
		//cout << "LOOP <<" << loop;
		i=0;
		while(i < D){
			GOOD[i] = 1;
			i++;
		}

		cin >> question;
		
		calc(question);

		//out
		count++;
		cout << "Case #" << count << ": " << check_answer() << endl;

	}

	return 0;
	
}
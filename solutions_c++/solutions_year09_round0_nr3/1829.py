// GoogleCodeJum.cpp : コンソール アプリケーションのエントリ ポイントを定義します。
//

#include "stdafx.h"
#include <algorithm>
#include <deque>
#include <iostream>
#include <functional>
#include <string>

using namespace std;

string L("welcome to code jam");

char question[502];
long question_length;

int calc(int i,int now){
	
	int my_now = now;
	long answer = 0;

	while(my_now < question_length){
		if(L.at(i) == question[my_now]){
			if(i == 18)
				answer++;
			else
				answer += calc(i+1,my_now + 1);
		}
		my_now++;
	}
	return answer;
}


int _tmain(int argc, _TCHAR* argv[])
{
	using namespace std;
	int loop;
	int count = 0;
	long answer = 0;
	int print_answer;

	cin >> loop;
	cin.getline(question, 502);

	while(loop--){
		
		cin.getline(question, 502);
		int i = 0;
		while(1){
			if(question[i] == '\0')
				break;
			i++;
		}

		question_length = i;
		//cout << question_length << question << i;

		answer = calc(0,0);

		print_answer = answer % 10000;


		//out
		count++;
		if(print_answer >= 1000)
			cout << "Case #" << count << ": " << print_answer << endl;
		else if(print_answer >= 100)
			cout << "Case #" << count << ": 0" << print_answer << endl;
		else if(print_answer >= 10)
			cout << "Case #" << count << ": 00" << print_answer << endl;
		else
			cout << "Case #" << count << ": 000" << print_answer << endl;

	}

	return 0;
	
}
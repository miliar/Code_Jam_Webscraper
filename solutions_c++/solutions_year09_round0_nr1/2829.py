#include "stdafx.h"
#include <string>
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

const int MAXN = 5000;

vector<string> dictionary;
string words[MAXN],now,ans; 
bool hash[MAXN][26];
int total,digit,L,D,N;;

void init(string s)
{
	memset(hash,false,sizeof(hash));
	for (int i = 0 ; i < MAXN ; ++i){
		words[i] = "";
	}
	ans.erase();
	for (int i = 0 ; i < L ; ++i)
		ans += " ";
	int now = 0;
	while (!s.empty()){
		if (s[0] != '('){
			s.insert(0,"(");
			s.insert(2,")");
		}
		int p1 = s.find("(") , p2 = s.find(")");
		string temp = s.substr(1,p2-1);
		words[now++] = temp;
		for (int i = 0 ; i < temp.size() ; ++i)
			hash[now-1][int(temp[i])-97] = true;
		s.erase(0,p2+1);
	}
	digit = now;
}

//void search(int depth)
//{
//	if (depth == L){
//		for (int i = 0 ; i < D ; ++i)
//			if (dictionary[i] == ans){
//				++total;
//				return;
//			}
//	}
//	for (int i = 0 ; i < words[depth].size() ; ++i){
//		ans[depth] = words[depth][i];
//		search(depth+1);
//	}
//		
//}

bool bingo(string dic)
{
	for (int i = 0 ; i < L ; ++i)
		if (!hash[i][int(dic[i])-97])
			return false;
	//for (int i = 0 ; i < D ; ++i){
	//	for (int j = 0 ; j < L ; ++j){
	//		if (!hash[j][int(dictionary[i][j])-97])
	//			break;
	//	}
	//	++total;
	//}
	return true;
}




int main()
{
	ifstream input("A_small.in");
	ofstream output("A_small.out");
	input >> L >> D >> N;
	digit = 0;
	for (int i = 0 ; i < D ; ++ i){
		string temp = "";
		char ch;
		for (int i = 1 ; i <= L ; ++i){
			input >> ch;
			temp += ch;
		}
		dictionary.push_back(temp);
	}

	for (int i = 0 ; i < N ; ++i){
		now = "";
		char ch;
		int count = 0;
		bool flag = false;
		while (1){
			input >> ch;
			now += ch;
			if (ch == '(')
				flag = true;
			if ('a' <= ch && ch <= 'z')
				if (!flag)
					++count;
			if (ch == ')'){
				flag = false;
				++count;
			}
			if (count == L)
				break;
		}
		init(now);
		total = 0;
		for (int j = 0 ; j < D ; ++j)
			if (bingo(dictionary[j]))
				++total;

		output << "Case #" << i+1  << ": " << total << endl;
	}
			

	input.close();
	output.close();
	return 0;
} 

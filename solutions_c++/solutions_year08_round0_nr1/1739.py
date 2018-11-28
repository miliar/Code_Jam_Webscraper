// A.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <fstream>
#include <ctime>

using namespace std;

#define MAX_N     20
#define MAX_S     100
#define MAX_Q     1000
#define MAX_SNAME 100

// query 에 search engine 하나라도 빠져있는가? ( 종료조건판정 )
bool is_query_empty(int S, const vector<int>& q, int sep_start, int sep_end)
{
	vector<bool> check_s;
	check_s.resize(S, false); // 기본값 : false

	// 각 검색엔진이름이 존재한다 체크
	for(int qi=sep_start; qi<=sep_end; ++qi)
		check_s[q[qi]] = true;

	// 하나라도 비었으면 true
	for(int si=0; si<S; ++si)
		if(!check_s[si])
			return true;

	return false;
}

int solve_case(int S, const vector<int>& q)
{
	int Q = q.size();
	int check_s[MAX_S];
	int other_count = 0;
	int result = 0;

	memset(check_s, 0, sizeof(check_s));

	for(int qi=0; qi<Q; ++qi)
	{
		if(!check_s[q[qi]])
		{
			check_s[q[qi]] = 1;
			other_count = other_count + 1;
		}
		if(other_count == S)
		{
			memset(check_s, 0, sizeof(check_s));
			other_count = 1;
			check_s[q[qi]] = 1;
			++result;
		}
	}

	return result;
}

int main(int argc, char* argv[])
{
	int N; // 1 ~ 20
	int S; // 2 ~ 100
	int Q; // 0 ~ 1000

	vector<string> s; // char s[MAX_S][MAX_SNAME]
	vector<string> q2; // char q2[MAX_Q][MAX_SNAME]; // 추후 int q[MAX_Q]; 로 변경 ( 단지, s 의 인덱스만 가지면 됨 )
	vector<int> q; // 인덱스로 변경

	map<string, int> s_map; // 스트링 -> int, 역 매핑

	cin >> N;

	// each case
	for(int ni=0; ni<N; ++ni)
	{
		string temp;

		// input S, ss
		cin >> S;
		getline(cin, temp); // new line
		s.resize(S);
		for(int si=0; si<S; ++si)
		{
			getline(cin, s[si]);
			s_map[s[si]] = si; // q2 to q 를 위한
		}
		
		// input Q, qs
		cin >> Q;
		getline(cin, temp); // new line
		//cin.sync();
		q2.resize(Q);
		for(int qi=0; qi<Q; ++qi)
			getline(cin, q2[qi]);

		// q2 to q ( // q2[qi] 에 들어있는 걸로 매핑 )
		q.resize(Q);
		for(int qi=0; qi<Q; ++qi)
			q[qi] = s_map[q2[qi]];

		// solve
		//test(s, q);
		printf("Case #%d: %d\n", ni+1, solve_case(S, q));
	}

	return 0;
}


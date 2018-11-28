#include<iostream>
#include<cstdio>
using namespace std;

int main(int artc, char* argv[]) {

    int TIME;// number of test
    int answer;// Final answer
    cin >> TIME;
    int dir[2][100],dir_O[100], dir_B[100], turn[100], OB[100];
    int O_count, B_count,count[2];
    int N;
    char S;
    int now_O, now_B, now[2];
    int tmp_in;
    for (int t = 0 ; t < TIME; t++) {
	O_count = B_count = answer = 0;
	count[0] = count[1] = 0;
	now_O = now_B = 1;
	now[0] = now[1] = 1;
	cin >> N;
	//cout << N ;
	for (int i = 0 ; i < N; ++i) {
	    cin >> S >>tmp_in ;
	    if (S=='O') {/*
		dir_O[O_count] = tmp_in;
		turn[i] = 0;
		OB[i] = O_count;
		O_count++;*/
		dir[0][count[0]] = tmp_in;
		turn[i] = 0;
		OB[i] = count[0];
		count[0]++;
	    }
	    else {/*
		dir_B[B_count] = tmp_in;
		turn[i] = 1;
		OB[i] = B_count;
		B_count++;*/
		dir[1][count[1]] = tmp_in;
		turn[i] = 1;
		OB[i] = count[1];
		count[1]++;
	    }
//	    printf(" %c %d",turn[i]==0?'O':'B',turn[i]==0?dir_O[O_count-1]:dir_B[B_count-1]);
//  	    printf(" %c %d",turn[i]==0?'O':'B',dir[turn[i]][count[turn[i]]-1] );
	}
//	cout << endl;
	int now_turn, pre_turn;
	int turn_between;
	answer = 0;
	pre_turn = now_turn = turn[0];
	turn_between = dir[now_turn][OB[0]] - now[now_turn] + 1;
	now[now_turn] = dir[now_turn][OB[0]];
	
	answer += turn_between;
	int dis;
	for (int i = 1 ; i < N; ++i) {
	    now_turn = turn[i];
	    if (now_turn == pre_turn) {
		dis = dir[now_turn][OB[i]] - now[now_turn];
		if (dis < 0 ) dis *=-1;
		answer += dis + 1;
		turn_between += dis + 1;
		now[now_turn] = dir[now_turn][OB[i]];
	    }
	    else {
		pre_turn = now_turn;
		dis = dir[now_turn][OB[i]] - now[now_turn];
		if (dis < 0) dis *= -1;
		if (turn_between >= dis ) {
		    turn_between = 1;
		    answer += 1;
		    now[now_turn] = dir[now_turn][OB[i]];
		}
		else {
		    answer += dis - turn_between + 1;
		    turn_between = dis - turn_between + 1;
		    now[now_turn] = dir[now_turn][OB[i]];
		}   
	    }
	}
	//output
	printf("Case #%d: %d\n", t+1, answer);
    }
    return 0;
}

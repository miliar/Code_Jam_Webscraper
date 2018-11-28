#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;

struct inp {
	char color;
	int bNo;
	int Next;
};

int main() {
	int T, N, R, B, i, j, flag;
	struct inp in[100];
	cin >> T;
	for ( j = 1; j <= T; j++ ) {
		scanf("%d", &N);
		
		for ( i = 0; i < N; i++ ) {
			cin >> in[i].color;
			cin >> in[i].bNo;
		}
			
		char curBot = in[N-1].color;
		int curPos = N-1;
		int pastPos = curPos;
		in[N-1].Next = 0;
		for ( i = N-2; i>=0; i-- ) {
			if ( curBot == in[i].color) {
				in[i].Next = in[pastPos].Next;
				curPos = i;
			}
			else {
				curBot = in[i].color;
				in[i].Next = curPos;
				pastPos = i;
				curPos = pastPos;
			}
		}
//		for ( i = 0; i < N; i++ ) {
//			printf("%c--%d--%d\n", in[i].color, in[i].bNo, in[i].Next);
//		}
		int curOrangePos = 1;
		int curBluePos = 1;
		int destPos;
		int time = 0;
		int OrangeDest, blueDest, next;
		for ( i = 0; i < N; i++ ) {
			next = in[i].Next;
		//	if ( next != 0 ) {
                //		OrangeDest = in[next].bNo;
		//		blueDest = in[next].bNo;
		//	}
			curBot = in[i].color;
			destPos = in[i].bNo;
			if ( curBot == 'O' ) {
				if ( next != 0 ) 
                			blueDest = in[next].bNo;
				while ( curOrangePos != destPos ) {
					if ( curOrangePos < destPos )
						curOrangePos++;
					else 
						curOrangePos--;
					time++;
					if ( (blueDest < curBluePos) )
						curBluePos--;
					else if ( (blueDest > curBluePos))
						curBluePos++;
	//				printf("%d    O-%d\t|\t B-%d\n", time, curOrangePos, curBluePos);
				}
			}
			else {
				if ( next != 0 ) 
                			OrangeDest = in[next].bNo;
                                while ( curBluePos != destPos ) {
                                        if ( curBluePos < destPos )
                                                curBluePos++;
                                        else
                                                curBluePos--;
                                        time++;
                                        if ( (OrangeDest < curOrangePos) )
                                                curOrangePos--;
                                        else if ( (OrangeDest > curOrangePos) )
                                                curOrangePos++;
	//				printf("%d    O-%d\t|\t B-%d\n", time, curOrangePos, curBluePos);
                                }
			}
			if ( curBot == 'B' ) {
				if ( next != 0 ) 
                			OrangeDest = in[next].bNo;
				if ( OrangeDest < curOrangePos )
                               		curOrangePos--;
                                else if ( OrangeDest > curOrangePos )
                                        curOrangePos++;
				time++;
			}
			else if ( curBot == 'O' ) {
				if ( next != 0 ) 
                			blueDest = in[next].bNo;
				time++;
				if ( blueDest < curBluePos )
					curBluePos--;
				else if ( blueDest > curBluePos )
					curBluePos++;
			}
	//		printf("%d    O-%d\t|\t B-%d\n", time, curOrangePos, curBluePos);
		}
		printf("Case #%d: %d\n",j , time);
	}
	return 0;
}


#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <math.h>

using namespace std;

const int MAX = 60;

int T;
fstream	fin;
fstream fout;
int N;
char events[1010][MAX];
char minEvent[MAX];
char gcdTime[MAX];

inline int isGreater(char *A, char *B){
	for(int i=MAX-1; i>=0; i--)
		if(A[i] < B[i])
			return -1;
		else if(A[i] > B[i])
			return 1;
	
	return 0;
}

inline bool isZero(char *A){
	for(int i=MAX-1; i>=0; i--)
		if(A[i])
			return false;
	return true;
}

inline void subtract(char *A, char *B){
	bool carry=false;
	for(int i=0; i<MAX; i++){
		char a, b;
		a = A[i]; b = B[i];
		if(carry) b++;

		if(a < b){
			carry = true;
			A[i] = a+10-b;
		}
		else{
			carry = false;
			A[i] = a-b;
		}
	}
}

inline void getGCD(char *A){
	char *minT, *maxT;
	minT = gcdTime;
	maxT = A;
	while(1){
		int re = isGreater(minT, maxT);
		if(re > 0)
			swap(minT, maxT);
		else if(re == 0)
			return;
		subtract(maxT, minT);
	}
}

void main()
{
	fin.open("z:\\input.txt", ifstream::in);
	fout.open("z:\\output.txt", ifstream::out);


	fin >> T;

	for(int t = 1; t <= T; t++) {
		fin >> N;
		char tmp[MAX];
		memset(events, 0, sizeof(events));
		memset(minEvent, 0, sizeof(minEvent));
		memset(gcdTime, 0, sizeof(gcdTime));
		for(int i=0; i<N; i++){
			fin >> tmp;
			int length = strlen(tmp);
			for(int j=0; j<length; j++)
				events[i][length-1-j] = tmp[j]-'0';
		}


		memcpy(minEvent, events[0], MAX);
		for(int i=1; i<N; i++){
			if(isGreater(minEvent, events[i])>0)
				memcpy(minEvent, events[i], MAX);
		}
		for(int i=0; i<N; i++)
			subtract(events[i], minEvent);

		
		int minID;
		for(minID=0; minID<N && isZero(events[minID]); minID++);
		for(int i=minID+1; i<N; i++)
			if(!isZero(events[i]) && isGreater(events[minID], events[i])>0)
				minID = i;
		memcpy(gcdTime, events[minID], MAX);

		for(int i=0; i<N; i++)
			if(!isZero(events[i]))
				getGCD(events[i]);

		while(isGreater(minEvent, gcdTime)>0)
			subtract(minEvent, gcdTime);
		subtract(gcdTime, minEvent);
		int i;
		for(i=MAX-1;i>=0 && gcdTime[i]==0; i--);

		if(i>=0){
			for(int j=0; j<=i; j++)
				tmp[j] = gcdTime[i-j]+'0';
			tmp[i+1] = 0;
		}
		else{
			tmp[0] = '0';
			tmp[1] = 0;
		}
		

		fout << "Case #" << t <<": " << tmp << endl;
	}

	fin.close();
	fout.close();
}
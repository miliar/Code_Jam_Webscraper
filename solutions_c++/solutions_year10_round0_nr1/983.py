#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int P; // max # of powered snapper
int s[30]; // on/off status

bool checkstatus(int N, int K)
{
	int i,k;
	// initialize
	P = 1; 
	for(i=0; i<N; i++) {
		s[i] = 0; 
	}

	// start flipping fingers
	for(k=0; k<K; k++) {
		// flip the ones that are powered on
		for(i=0; i<P; i++) {
			s[i] = 1-s[i];
		}
		// update P
		for(i=0; i<N; i++) {
			if (s[i]==0)
				break;
		} 
		if (i==N)
			P = N;
		else
			P = i+1;
	}

	// check if the light is on or off
	if(P!=N) 
		return false;
	else {
		for(i=0; i<N; i++) {
			if(s[i]==0)
				return false;
		}
		return true;
	}
}

int main()
{
	//freopen("D:\\tmp\\test.txt","r",stdin);freopen("D:\\tmp\\test.out","w",stdout);
	freopen("D:\\tmp\\A-small.in","r",stdin);freopen("D:\\tmp\\A-small.out","w",stdout);
	//freopen("D:\\tmp\\A-large.in","r",stdin);freopen("D:\\tmp\\A-large.out","w",stdout);
	int testcase;
	cin >> testcase;
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		int N, K;
		scanf("%d",&N);
		scanf("%d", &K);
		bool result = checkstatus(N, K);
		string str;
		if (result) {
			str = "ON";
		}
		else 
			str = "OFF";
		printf("Case #%d: %s\n",caseId,str.c_str());
	}

	return 0;
}
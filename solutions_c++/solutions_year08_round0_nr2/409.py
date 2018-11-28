// codejam_b.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

struct timeseg{
	int sh, sm, eh, em, type;
	timeseg(){sh=sm=eh=em=type=0;}
	timeseg(int sh, int sm, int eh, int em, int type):sh(sh),sm(sm),eh(eh),em(em),type(type){}
	bool operator<(const timeseg &S)const{
		return (sh < S.sh || (sh == S.sh && sm < S.sm)) || ((sh==S.sh&&sm==S.sm) && (eh < S.eh || (eh == S.eh && em < S.em)));
	}
	bool operator>(const timeseg &S)const{
		return (sh > S.sh || (sh == S.sh && sm > S.sm)) || ((sh==S.sh&&sm==S.sm) && (eh > S.eh || (eh == S.eh && em > S.em)));
	}
	bool operator==(const timeseg &S)const{
		return sh==S.sh&&sm==S.sm&&eh==S.eh&&em==S.em;
	}
	void print(){
		printf("%c: %d:%d ~ %d:%d\n", type?'B':'A', sh, sm, eh, em);
	}
};

int _tmain(int argc, _TCHAR* argv[])
{
	int T, Case=0;
	scanf("%d", &T);
	while (T--){
		int Turn;
		int NA, NB;
		scanf("%d", &Turn);
		scanf("%d%d", &NA, &NB);
		vector<timeseg> TimeLine;
		for (int i = 0 ; i < NA+NB; ++i){
			timeseg X;
			scanf("%d:%d %d:%d", &X.sh, &X.sm, &X.eh, &X.em);
			X.type = i >= NA;
			TimeLine.push_back(X);
		}
		sort(TimeLine.begin(), TimeLine.end());
		int aa=0, ab=0;
		priority_queue<timeseg, vector<timeseg>, greater<timeseg> > QA, QB;
		int TZ = TimeLine.size();
		for (int i = 0 ; i < TZ; ++i){
			timeseg X = TimeLine.front();
			TimeLine.erase(TimeLine.begin());
			if (X.type){ //B
				timeseg Y;
				if (QB.empty()){
					ab++;
					Y.sh = X.eh;
					Y.sm = X.em;
					Y.sm += Turn;
					if (Y.sm > 59) Y.sm -= 60, Y.sh++;
					//printf("New Train From B to A: "); Y.print();
					QA.push(Y);
				}else{
					Y = QB.top();
					ab++;
					if (Y.sh < X.sh || (Y.sh == X.sh && Y.sm <= X.sm)){
						//printf("Existing ");
						QB.pop();
						ab--;
					}
					timeseg Z;
					Z.sh = X.eh;
					Z.sm = X.em+Turn;
					if (Z.sm > 59) Z.sm -= 60, Z.sh++;
					//printf("Train From B to A: "); Z.print();
					QA.push(Z);
				}
			}else{ //A
				timeseg Y;
				if (QA.empty()){
					aa++;
					Y.sh = X.eh;
					Y.sm = X.em;
					Y.sm += Turn;
					if (Y.sm > 59) Y.sm -= 60, Y.sh++;
					//printf("New Train From A to B: "); Y.print();
					QB.push(Y);
				}else{
					Y = QA.top();
					aa++;
					if (Y.sh < X.sh || (Y.sh == X.sh && Y.sm <= X.sm)){
						//printf("Existing ");
						QA.pop();
						aa--;
					}
					timeseg Z;
					Z.sh = X.eh;
					Z.sm = X.em+Turn;
					if (Z.sm > 59) Z.sm -= 60, Z.sh++;
					//printf("Train From A to B: "); Z.print();
					QB.push(Z);
				}
			}
		}
		printf("Case #%d: %d %d\n", ++Case, aa, ab);
	}
	//scanf("%d", &T);
	return 0;
}


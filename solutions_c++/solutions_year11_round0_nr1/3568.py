#include <stdio.h>
#include <string.h>
#include "stdlib.h"
#include "unistd.h"
#include "math.h"
#include <string>
#include <sys/types.h>
#include <vector>
#include <map>
#include <list>
#include <deque>
#include <set>
using namespace std;

int main(int argc, char *argv[]) {
//input
	int T;
	scanf("%d\n", &T);
	for (int i=0;i<T;++i)
	{
		int N;
		scanf("%d", &N);
		int steps=0;
		int Opos=1;
		int Bpos=1;
		int Omom=0;
		int Bmom=0;
		int act=0; //Robot O starts
		for (int ii=0;ii<N;++ii)
		{
			char robot=getchar();
			if(robot!='O' || robot != 'B') {
				robot=getchar();
			}
			int P;
			if(robot == 'O') {
				scanf("%d", &P);
				if(act==0) {
					Omom+=abs(Opos-P)+1;
					steps+=abs(Opos-P)+1;
					Opos=P;
				} else {
					act = 0;
					int k=abs(Opos-P) - Bmom;
					Bmom = 0;
					Opos=P;
					Omom+=1;
					steps+=1;
					if(k>0) {
						Omom+= k;
						steps+=k;
					}
				}
			} else if(robot =='B') {
				scanf("%d", &P);
				if(act==1) {
					Bmom+=abs(Bpos-P)+1;
					steps+=abs(Bpos-P)+1;
					Bpos=P;
				} else {
					act = 1;
					int k=abs(Bpos-P) - Omom;
					Omom = 0;
					Bpos=P;
					Bmom+=1;
					steps+=1;
					if(k>0) {
						Bmom += k;
						steps+=k;
					}
				}
			} else {
				fprintf(stderr, "WTF");
			}
		}
		printf("Case #%i: %i\n", i+1, steps);
	}
}








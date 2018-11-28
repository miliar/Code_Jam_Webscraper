#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstring>
#include <cctype>
#include <new>
#include <cassert>
#include <vector>
#include <algorithm>
#include <stack>
using namespace std;

#define N 10000


int main(void) {	
	int numCases;
	cin >> numCases;
	
	int vines, waitlistSize, finalDistance;
	int i, v, reach, newReach;
	int *dist, *length, *seenReach, *isInWaitlist, *waitlist;
	dist = new int[N];
	length = new int[N];
	seenReach = new int[N];
	isInWaitlist = new int[N];
	waitlist = new int[N];
	
	for (int caseNum = 1; caseNum <= numCases; caseNum++) {
		cin >> vines;
		for (i=0; i<vines; i++) cin >> dist[i] >> length[i];
		cin >> finalDistance;
		
		for (i=0; i<vines; i++) {
			seenReach[i] = 0;
			isInWaitlist[i] = 0;
		}
		seenReach[0] = dist[0];
		waitlistSize = 1;
		isInWaitlist[0] = 1;
		waitlist[0] = 0;
		
		while (waitlistSize) {
			v = waitlist[--waitlistSize];
			isInWaitlist[v] = 0;
			reach = seenReach[v];
			if (reach+dist[v] >= finalDistance) {
				printf("Case #%d: YES\n", caseNum);
				goto bypass;
			}
			//try to swing forward
			for (i=v+1; i<vines; i++) {
				if (dist[v]+reach >= dist[i]) {
					newReach = dist[i]-dist[v];
					if (newReach > length[i]) newReach = length[i];
					if (newReach > seenReach[i]) {
						seenReach[i] = newReach;
						if (isInWaitlist[i]==0) {
							isInWaitlist[i] = 1;
							waitlist[waitlistSize++] = i;
						}
					}
				}
			}
			//try to swing backward
			for (i=v-1; i>=0; i--) {
				if (dist[v]+reach >= dist[i]) {
					newReach = dist[i]-dist[v];
					if (newReach > length[i]) newReach = length[i];
					if (newReach > seenReach[i]) {
						seenReach[i] = newReach;
						if (isInWaitlist[i]==0) {
							isInWaitlist[i] = 1;
							waitlist[waitlistSize++] = i;
						}
					}
				}
			}
		}
		printf("Case #%d: NO\n", caseNum);
		bypass:;
	}
	return 0;
}

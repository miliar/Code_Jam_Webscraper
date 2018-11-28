#include <queue>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;

const int M = 1000;
int s, n, cnt, mx;

int cmp(int x,int y){return x<y;}

string nms[M];
string srch[M];
priority_queue<int, vector<int>, greater<int> > when[M];


int findmax() {
	int m = 0;
	for (int i = 0; i<s; i++)
		if ((mx == -1 || nms[i] != nms[mx]) && when[i].top() > when[m].top())
			m = i;
	return m;
}

int main() {
	int c,k;
	char nm[101];
	bool koniec;
	scanf("%d",&c);
	k=c;
	while(c--) {
		for (int i = 0; i<M; i++){
			while (!when[i].empty())
			  when[i].pop();
			nms[i] = srch[i] = "";
		}
		koniec = false;
		scanf("%d\n",&s);
		for (int i = 0; i<s; i++) {
			fgets(nm, 100, stdin);
			nms[i].append(nm);
		}
		scanf("%d\n",&n);
		for (int i = 0; i<n; i++) {
			fgets(nm, 100, stdin);
			srch[i].append(nm);
		}
		//printf("===========\n");		
		cnt = 0;
		mx = -1;
		for (int i = 0; i<n; i++)
			for (int j = 0; j<s; j++)
				if (srch[i]== nms[j]){
					when[j].push(i);
					j = s;
				}
		// for (int i = 0; i<s; i++) 
		//    printf("%s --> %d\n",nms[i].data(), when[i].size());
		int crr = 0;
		while (crr <= s-1) {
		  for (int i = 0; i<s; i++)
			if(when[i].empty())
			  koniec= true;
		  if (koniec){
		    printf("Case #%d: %d\n",k-c,cnt);
		    crr = s;
		    continue;
		  }              	
		  mx = findmax();
		//  printf("Wybieram %s\n",nms[mx].data());
		  for (int i = 0; i<s; i++) {
		//    printf("Kasujemy pojawienie sie %s  ",nms[i].data());
		    while ((!when[i].empty()) && when[i].top() < when[mx].top()) {
		//	printf(" jako %d\t", when[i].top());
			when[i].pop();	        
		    }
		//    printf(" --> %d",when[i].empty()? -1 :when[i].top());
		   // printf("\n");
		  }
		  cnt++;
		  crr = mx;
		  for (int i = 0; i<s; i++)
			if(when[i].empty())
			  koniec= true;
		  if (koniec){
		    printf("Case #%d: %d\n",k-c,cnt);
		    crr = s;
		    continue;
		  } 
		}			
		if (!koniec) printf("Case #%d: %d\n",k-c,cnt);
    }
    return 0;
}

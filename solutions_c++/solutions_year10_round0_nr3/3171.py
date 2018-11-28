#include<iostream>
#include<map>
#include<string>
#include<vector>
#include<algorithm>
#include<cstdio>

using namespace std;
#define ps system("PAUSE")
//#define FORI(k) (int i=0;i<k;i++) 

int r,k,n;

int gc[1001];
int pc[1001];
int nexti[1001];


int main() {
	int t,cs,previ;
	freopen("C:/TestData/C-small-attempt8.in","r",stdin);freopen("C:/TestData/C-small-attempt8.out","w",stdout);
	scanf("%d",&t);
	for(int ti=1;ti<=t;ti++)  {
	
		scanf("%d%d%d",&r,&k,&n);
		
		int tp = 0 ;
		for(int gi=0;gi<n;gi++)  {
			scanf("%d",&gc[gi]);
			nexti[gi] = -1;
			pc[gi] = 0;
			tp+= gc[gi];
		
		}

		if( tp < k ) {
			printf("Case #%d: %d\n",ti,tp * r);continue;
		}

		cs = -1;
		int temp = 0 ; previ = 0;
		for(int i=0;;i++) {
			int ei = i % n;
			temp += gc[ei];
			if(temp > k ) {
				nexti[previ] = ei; 
				pc[previ] = temp - gc[ei];
				nexti[previ] = ei;
				previ = ei;
				cs = ei;
				temp = gc[ei];
				if(nexti[previ] >= 0 ) break; // cycle found 
			}
		}

		int total = 0 ;
		int curpos = 0 ;

		for(curpos =0;r > 0 && curpos != cs ; curpos = nexti[curpos],r--) { // enough rounds or reach cycle position 
			total += pc[curpos];
		}

		int cpc=0 ,crc=0; // cycle total count and round count
		
		int pos = cs;
		do {
			cpc += pc[pos];
			crc++;
			pos = nexti[pos];
		}while(pos != cs ) ;

		int bycycles = r /crc ;
		total += bycycles * cpc;
		if(bycycles > 0) 
			r -= bycycles * crc;

		for(curpos =cs ;r>0  ; curpos = nexti[curpos],r--) { // enough rounds or reach cycle position 
			total += pc[curpos];
		}

		printf("Case #%d: %d\n",ti,total);

	}
}


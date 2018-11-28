#include <cstdio>

using namespace std;

inline int max(int a, int b){
	return (a<b)?b:a;
}

inline int min(int a, int b){
	return (a<b)?a:b;
}

inline int abs(int a){
	return (a<0)?-a:a;
}

int main()
{
	int T, N;
	char r, lr;
	int n, c;
	int nB, nO;
	int t=0,ta;
	int O[1000];
	int B[1000];
	int s[1000];
	char sr[1000];
	int pO, pB;
	int iO, iB;
	int tO, tB;
	int nc, p;
	
	scanf("%d\n",&T);
	
	nc=1;
	while(T--){
		
		scanf("%d\n",&N);
		
		pO=pB=1;
		nO=nB=0;
		iO=iB=0;
		
		for(int i=0;i<N;i++){
			scanf("%c %d\n",&r,&c);
			//printf("%c %d ",r,c);
			sr[i]=r;
			s[i]=c;
			if(r=='B'){
				B[nB]=c; nB++;
			}else{
				O[nO]=c; nO++;
			}
			
		}
		//printf("\n");
		
		t=0;
		ta=0;
		iO=iB=1;
		lr=-1;
		p=0;
		
		while(p<N){
			if(sr[p]=='B'){
				
				if(lr!='B'){
					if(abs(s[p]-pB)>=ta){
						t+=abs(s[p]-pB)-ta+1;
						ta=abs(s[p]-pB)-ta+1;
					}else{
						t++;
						ta=1;
					}
					
					
				}else{
					t+=abs(s[p]-pB)+1;
					ta+=abs(s[p]-pB)+1;
				}
				
				pB=s[p];
				lr='B';
				iB++;
			}else{
				
				if(lr!='O'){
					if(abs(s[p]-pO)>=ta){
						t+=abs(s[p]-pO)-ta+1;
						ta=abs(s[p]-pO)-ta+1;
					}else{
						t++;
						ta=1;
					}
					
					
				}else{
					t+=abs(s[p]-pO)+1;
					ta+=abs(s[p]-pO)+1;
				}
				
				pO=s[p];
				
				lr='O';
				iO++;
			}
			
			p++;
			//printf("%d\n",t);
		}
		
		printf("Case #%d: %d\n",nc,t);
		
		
		nc++;
		
	}
	
	return 0;
}
#include <cstdio>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
using namespace std;

#define MAX 51
int m[MAX][MAX];
int calc[MAX][MAX][4];
char s[MAX];
int TC = 1, T, N, K;


int busca,R,B;
/* hor 0
 * vert 1
 * dia dir 2
 * dia esq 3
 */
int s0(int i,int j,int q){
	calc[i][j][0]=1;
	if(q==0){
		if(busca==1){
			R=1;
		}else B=1;
		return 1;
	}
	if(j>0 &&  !calc[i][j-1][0] && m[i][j-1]==busca)
		if(s0(i,j-1,q-1))return 1;

	if(j<(N-1) &&  !calc[i][j+1][0] && m[i][j+1]==busca)
		if(s0(i,j+1,q-1))return 1;
}

int s1(int i,int j,int q){
	calc[i][j][1]=1;
	if(q==0){
		if(busca==1){
			R=1;
		}else B=1;
		return 1;
	}
	if(i>0 &&  !calc[i-1][j][1] && m[i-1][j]==busca)
		if(s1(i-1,j,q-1))return 1;

	if(i<(N-1) &&  !calc[i+1][j][1] && m[i+1][j]==busca)
		if(s1(i+1,j,q-1))return 1;
}

int s2(int i,int j,int q){
	calc[i][j][2]=1;
	if(q==0){
		if(busca==1){
			R=1;
		}else B=1;
		return 1;
	}
	if(i>0 && j<(N-1) &&  !calc[i-1][j+1][2] && m[i-1][j+1]==busca)
		if(s2(i-1,j+1,q-1))return 1;

	if(i<(N-1) && j>0 && !calc[i+1][j-1][2] && m[i+1][j-1]==busca)
		if(s2(i+1,j-1,q-1))return 1;
}

int s3(int i,int j,int q){
	calc[i][j][3]=1;
	if(q==0){
		if(busca==1){
			R=1;
		}else B=1;
		return 1;
	}
	if(i>0 && j>0 && !calc[i-1][j-1][3] && m[i-1][j-1]==busca)
		if(s3(i-1,j-1,q-1))return 1;

	if(i<(N-1) && j<(N-1) && !calc[i+1][j+1][3] && m[i+1][j+1]==busca)
		if(s3(i+1,j+1,q-1))return 1;
}

int main ()
{
	int tam,i,j,k;
    for (scanf ("%d", &T); TC <= T; TC++)
    {
        scanf ("%d %d", &N, &K);
        memset(m,0,sizeof(m));
        memset(calc,0,sizeof(calc));
        for(i=0;i<N;i++){
        	scanf("%s",s);
        	for(j=N-1;j>=0;j--) if(s[j]!='.') break;
        	for(k=N-1;j>=0;j--){
        		if(s[j]=='.')continue;
        		if(s[j]=='R'){
        			m[k][N-i-1]=1;
        		}else{
        			if(s[j]=='B'){
        				m[k][N-i-1]=2;
        			}
        		}
        		k--;
        	}
        }

        /*for(i=0;i<N;i++){
        	for(j=0;j<N;j++){
        		printf("%d",m[i][j]);
        	}
        	printf("\n");
        }*/

        B=0;R=0;
        for(i=0;i<N;i++){
        	for(j=0;j<N;j++){
        		if(R && B) break;
        		if(!R && m[i][j]==1){
        			busca=1;
        			if(!calc[i][j][0]){
        				s0(i,j,K-1);
        			}
        			if(!calc[i][j][1]){
        				s1(i,j,K-1);
        			}
        			if(!calc[i][j][2]){
        				s2(i,j,K-1);
        			}
        			if(!calc[i][j][3]){
        				s3(i,j,K-1);
        			}
        		}else if(!B && m[i][j]==2){
        			busca=2;
        			if(!calc[i][j][0]){
        				s0(i,j,K-1);
        			}
        			if(!calc[i][j][1]){
        				s1(i,j,K-1);
        			}
        			if(!calc[i][j][2]){
        				s2(i,j,K-1);
        			}
        			if(!calc[i][j][3]){
        				s3(i,j,K-1);
        			}
        		}
        	}
        }

        printf ("Case #%d: ", TC);
        if(B && R){
        	printf("Both\n");
        }else{
        	if(B){
        		printf("Blue\n");
        	}else{
        		if(R){
        			printf("Red\n");
        		}else printf("Neither\n");
        	}
        }
    }
    return 0;
}

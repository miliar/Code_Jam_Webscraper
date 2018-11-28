#include<stdio.h>
#include<queue>
#define M 102
using namespace std;


int main()
{
	int i,j,k,K;
	int T,H,W;
	int n,w,e,s;
	int V[M][M][5], map[M][M];
	char sol[M][M], Pi[M][M];
	char N[M][M];
	char c;
	queue<int> Qu;

	scanf("%d", &T);
	
	for(K=1;K<=T;K++){
		
		c='a'-1;
		for(i=0;i<M;i++){
			for(j=0;j<M;j++){
				map[i][j]=20000;
				sol[i][j]=0;
				Pi[i][j]=0;
				N[i][j]=0;
				for(k=0;k<5;k++)
					V[i][j][k]=-1;
			}
		}

		scanf("%d%d", &H,&W);
		for(i=1;i<=H;i++){
			for(j=1;j<=W;j++){
				scanf("%d", &map[i][j]);
			}
		}
/*
		for(i=0;i<=H+1;i++){
			for(j=0;j<=W+1;j++){
				printf("%d ", map[i][j]);
			}
			printf("\n");
		}
*/


		for(i=1;i<=H;i++){
			for(j=1;j<=W;j++){
				n=map[i-1][j];
				w=map[i][j-1];
				e=map[i][j+1];
				s=map[i+1][j];

				if( map[i][j]>n || map[i][j]>w || map[i][j]>e || map[i][j]>s ){
					if( n<=w && n<=e && n<=s ){
						V[i][j][ N[i][j]++ ] = M*(i-1)+j;
						V[i-1][j][ N[i-1][j]++ ] = M*i+j;
					}
					else if( w<=n && w<=e && w<=s ){
						V[i][j][ N[i][j]++ ] = M*i+(j-1);
						V[i][j-1][ N[i][j-1]++ ] = M*i+j;
					}
					else if( e<=n && e<=w && e<=s ){
						V[i][j][ N[i][j]++ ] = M*i+j+1;
						V[i][j+1][ N[i][j+1]++ ] = M*i+j;
					}
					else if( s<=n && s<=w && s<=e ){
						V[i][j][ N[i][j]++ ] = M*(i+1)+j;
						V[i+1][j][ N[i+1][j]++ ] = M*i+j;
					}
				}
			}
		}

/*
		for(i=1;i<=H;i++){
			for(j=1;j<=W;j++){
				printf("(%d,%d) -> ", i,j);
				for(k=0;k<N[i][j];k++){
					printf("(%d,%d), ", V[i][j][k]/M, V[i][j][k]%M);
				}
				printf("\n");
			}
		}
*/
		int d;
		for(i=1;i<=H;i++){
			for(j=1;j<=W;j++){
				if( Pi[i][j]==0){
					c++;

					Qu.push(M*i+j);

					while(!Qu.empty()){
						d=Qu.front();
						Qu.pop();
	//					printf("(i,j)=(%d,%d)\n", d/M,d%M);
	//					printf("size = %d   d=%d\n", Qu.size(), d);
	//					if(!Qu.empty()) printf("No~!\n");
	//					Qu.size()

						Pi[d/M][d%M]=1;
						sol[d/M][d%M]=c;

						for(k=0;k<N[d/M][d%M];k++){
							int i,j;
							i=V[d/M][d%M][k]/M;
							j=V[d/M][d%M][k]%M;

							if( Pi[i][j]==0)
								Qu.push( M*i+j );
						}
	//					printf("size = %d\n", Qu.size());
						
					}

					
				}
			}
		}

		printf("Case #%d:\n",K);
		for(i=1;i<=H;i++){
			for(j=1;j<=W;j++){
				printf("%c ", sol[i][j]);
			}
			printf("\n");
		}


	}

	return 0;
}
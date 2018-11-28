#include <cstdio>
#include <cstdlib>
int main(){
	 int T,N,M;
	 char **board;
	 int *x,*y;
	 bool fail;
	 int **color;
	 scanf("%d", &T);
	 for(int i=0;i<T;i++){
		 scanf("%d %d", &N, &M);
		 x=new int[N];
		 color=new int*[N];
		 for(int j=0;j<N;j++){x[j]=0;color[j]=new int[M];}
		 y=new int[M];
		 for(int j=0;j<M;j++)y[j]=0;
		 board=new char*[N];
		 getchar();
		 for(int j=0;j<N;j++){
			 board[j]=new char[M+1];
			 gets(board[j]);
			 for(int k=0;k<M;k++){
			    if(board[j][k]=='#'){
			       x[j]++;
			       y[k]++;
			    }
			    color[j][k]=0;
			 }
		 }
		 fail=0;
       printf("Case #%d:\n",i+1);
       for(int j=0;j<N&&!fail;j++)
          for(int k=0;k<M&&!fail;k++)
             if(board[j][k]!='.'&&color[j][k]==0){
	             if(j==N-1||k==M-1)fail=1;
				    if(!fail)if(board[j+1][k]!='#'||board[j+1][k+1]!='#'||board[j+1][k]!='#')fail=1;
					 else{ 
						 color[j][k]=color[j+1][k+1]=1;
						 color[j+1][k]=color[j][k+1]=2;
					 }
				 }
       if(fail)printf("Impossible\n");
       else
		    for(int j=0;j<N;j++){
		       for(int k=0;k<M;k++)
		          switch(color[j][k]){
			          case 0:printf(".");break;
			          case 1:printf("/");break;
			          case 2:printf("\\");break;
				    }
             printf("\n");
		    }
		 delete x;delete y;delete board; delete color;
    }
}

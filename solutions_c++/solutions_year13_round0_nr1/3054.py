#include <cstdio>
int t,board[4][4];
int main(){
   scanf("%d",&t);
   for(int testcase=0;testcase<t;++testcase){
      char c;
      int cmp=1;
      for(int x=0;x<4;++x)
	 for(int y=0;y<4;++y){
	    for(c=0;(c!='X')&&(c!='O')&&(c!='.')&&(c!='T');scanf("%c",&c));
	    if(c=='X') board[x][y]=1;
	    if(c=='O') board[x][y]=2;
	    if(c=='.'){board[x][y]=0;cmp=0;}
	    if(c=='T') board[x][y]=3;
	 }
      int flag=0;
      for(int i=0;i<4;++i){
	 flag=board[i][0];
	 for(int j=0;(j<4)&&(flag>0);++j){
	    if(flag==3) flag=board[i][j];
	    else if((flag!=board[i][j])&&(board[i][j]!=3)) flag=0;
	 }
	 if(flag>0) break;
      }
      if(flag==0){
	 for(int i=0;i<4;++i){
	    flag=board[0][i];
	    for(int j=0;(j<4)&&(flag>0);++j){
	       if(flag==3) flag=board[j][i];
	       else if((flag!=board[j][i])&&(board[j][i]!=3)) flag=0;
	    }
	    if(flag>0) break;
	 }
      }
      if(flag==0){
	 flag=board[0][0];
	 for(int i=0;i<4;++i){
	    if(flag==3) flag=board[i][i];
	    else if((flag!=board[i][i])&&(board[i][i]!=3)) flag=0;
	 }
      }
      if(flag==0){
	 flag=board[0][3];
	 for(int i=0;i<4;++i){
	    if(flag==3) flag=board[i][3-i];
	    else if((flag!=board[i][3-i])&&(board[i][3-i]!=3)) flag=0;
	 }
      }
      printf("Case #%d: ",testcase+1);
      if((flag==0)&&(cmp==1)) printf("Draw\n");
      if((flag==0)&&(cmp==0)) printf("Game has not completed\n");
      if(flag==1) printf("X won\n");
      if(flag==2) printf("O won\n");
   }
}

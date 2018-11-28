#include <cstdio>

int n;
int main(){
scanf("%d",&n);
for(int i=0;i<n;i++){
 scanf("\n");
 char tab[4][4];
 char tab2[4][4];
 char w = 'w';
 for(int j=0;j<4;j++)
  scanf("%c %c %c %c\n",&(tab[j][0]),&(tab[j][1]),&(tab[j][2]),&(tab[j][3]) );


 for(int j=0;j<4;j++){
  for(int k=0;k<4;k++) if(tab[k][j]=='T'){tab2[k][j]='O';tab[k][j]='X';}else tab2[k][j]=tab[k][j];
 }
//   for(int j=0;j<4;j++)for(int k=0;k<4;k++) printf("%c ",tab2[j][k]);
    
 for(int j=0;j<4;j++){
  if(tab[0][j]==tab[1][j] && tab[0][j]==tab[2][j] && tab[0][j]==tab[3][j] && tab[0][j]=='X') w=tab[0][j];
  if(tab2[0][j]==tab2[1][j] && tab2[0][j]==tab2[2][j] && tab2[0][j]==tab2[3][j]&& tab2[0][j]=='O') w=tab2[0][j];
  if(tab[j][0]==tab[j][1] && tab[j][0]==tab[j][2] && tab[j][0]==tab[j][3]&& tab[j][0]=='X') w=tab[j][3];
  if(tab2[j][0]==tab2[j][1] && tab2[j][0]==tab2[j][2] && tab2[j][0]==tab2[j][3]&& tab2[j][0]=='O') w=tab2[j][3];
 }  
 
  if(tab[0][0]==tab[1][1] && tab[2][2]==tab[0][0] && tab[0][0]==tab[3][3]&& tab[0][0]=='X') w=tab[0][0];
  if(tab2[0][0]==tab2[1][1] && tab2[0][0]==tab2[2][2] && tab2[0][0]==tab2[3][3]&& tab2[0][0]=='O') w=tab2[0][0];
  if(tab[0][3]==tab[1][2] && tab[2][1]==tab[0][3] && tab[0][3]==tab[3][0]&& tab[0][3]=='X') w=tab[0][3];
  if(tab2[0][3]==tab2[1][2] && tab2[0][3]==tab2[2][1] && tab2[0][3]==tab2[3][0]&& tab2[0][3]=='O') w=tab2[0][3];
  
  if(w=='w'){
  bool draw=true;
   for(int j=0;j<4;j++){for(int k=0;k<4;k++) if(tab[j][k]=='.')draw=false;
 }
 if(draw) printf("Case #%d: Draw\n",i+1); else printf("Case #%d: Game has not completed\n",i+1);

  }
  else printf("Case #%d: %c won\n",i+1,w);
  
}
return 0;
}

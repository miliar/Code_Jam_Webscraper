#include <stdio.h>
int main(){
  char a[4][4];
  int t;
  scanf("%d",&t);
  for(int k=1;k<(t+1);k++){
    bool done=false;
    for(int i=0;i<4;i++)
      for(int j=0;j<4;j++){
	char m=' ';
	while((m==' ')||(m=='\n'))m=getchar();
	a[i][j]=m;
      }
    //scanf("%c",&a[i][j]);
    /*    for(int i=0;i<4;i++){
      for(int j=0;j<4;j++)
	printf("%c",a[i][j]);
      printf("\n");
      }*/
    
    for(int i=0;i<4;i++){
      char who='.';
      if(((a[i][0]=='T')||(a[i][0]==a[i][1])||(a[i][1]=='T'))&&((a[i][1]=='T')||(a[i][1]==a[i][2])||(a[i][2]=='T'))&&((a[i][2]=='T')||(a[i][2]==a[i][3])||(a[i][3]=='T')))
	who=a[i][0];
      who=((who=='T')?a[i][1]:who);
      if(who!='.'){
	printf("Case #%d: %c won\n",k,who);
	done=true;
	break;
      }
    }
    if(done)
      continue;

    for(int i=0;i<4;i++){
      char who='.';
      if(((a[0][i]=='T')||(a[0][i]==a[1][i])||(a[1][i]=='T'))&&((a[1][i]=='T')||(a[1][i]==a[2][i])||(a[2][i]=='T'))&&((a[2][i]=='T')||(a[2][i]==a[3][i])||(a[3][i]=='T')))
	who=a[0][i];
      who=((who=='T')?a[1][i]:who);
      if(who!='.'){
	printf("Case #%d: %c won\n",k,who);
	done=true;
	break;
      }
    }
    
    if(done)
      continue;
    
    bool flag=false;
    int num_match=0;int num_t=0;
    if(((a[0][0]=='T')||(a[0][0]==a[1][1])||(a[1][1]=='T'))&&((a[1][1]=='T')||(a[1][1]==a[2][2])||(a[2][2]=='T'))&&((a[2][2]=='T')||(a[2][2]==a[3][3])||(a[3][3]=='T')))
      flag=true;
    
    char who = (a[0][0]=='T')?a[1][1]:a[0][0];
    if(who!='.')
      if(flag){
	printf("Case #%d: %c won\n",k,who);
	done=true;
      }
    
    if(done)
      continue;

    flag=false;
    if(((a[0][3]=='T')||(a[0][3]==a[1][2])||(a[1][2]=='T'))&&((a[1][2]=='T')||(a[1][2]==a[2][1])||(a[2][1]=='T'))&&((a[2][1]=='T')||(a[2][1]==a[3][0])||(a[3][0]=='T')))
      flag=true;
    
    who = (a[0][3]=='T')?a[1][2]:a[0][3];
    if(who!='.')
      if(flag){
	printf("Case #%d: %c won\n",k,who);
	done=true;
      }
    if(done)
      continue;

    bool comp=true;
    for(int i=0;i<4;i++)
      for(int j=0;j<4;j++)
	if(a[i][j]=='.'){
	  comp=false;
	  break;
	}
    if(comp)
      printf("Case #%d: Draw\n",k);
    else
      printf("Case #%d: Game has not completed\n",k);
  }
  
}

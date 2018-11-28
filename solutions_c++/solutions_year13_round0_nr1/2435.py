#include<iostream>
#include<cstdio>
using namespace std;
char a[4][4];
int i,n;
void init(){
  int i,j;
  for(i=0;i<=3;i++){
	for(j=0;j<=3;j++)
	  scanf("%c",&a[i][j]);
	scanf("\n");
  }
  scanf("\n");
}
int complete(){
  int i,j;
  for(i=0;i<=3;i++)
	for(j=0;j<=3;j++)
	  if(a[i][j]=='.')return(0);
  return(1);
}
int checkwin(){
  int i,j,flag;
  char ch;
  //r
  for(i=0;i<=3;i++){
	ch=a[i][0];
	if(ch=='.')continue;
	flag=1;
	for(j=1;j<=3;j++)
	  if(a[i][j]!=ch&&a[i][j]!='T'){
		flag=0;
		break;
	  }
	if(flag){
	  printf("%c won\n",ch);
	  return(1);
	}
  }
  //c
  for(j=0;j<=3;j++){
	ch=a[0][j];
	if(ch=='.')continue;
	flag=1;
	for(i=1;i<=3;i++)
	  if(a[i][j]!=ch&&a[i][j]!='T'){
		flag=0;
		break;
	  }
	if(flag){
	  printf("%c won\n",ch);
	  return(1);
	}
  }
  //d1
  ch=a[0][0];
  if(ch!='.'){
	flag=1;
	for(i=1;i<=3;i++)
	  if(a[i][i]!=ch&&a[i][i]!='T'){
		flag=0;
		break;
	  }	
	  if(flag){
		printf("%c won\n",ch);
		return(1);
	  } 
  }
  //d2
  ch=a[0][3];
  if(ch!='.'){
	flag=1;
	for(i=1;i<=3;i++)
	  if(a[i][3-i]!=ch&&a[i][3-i]!='T'){
		flag=0;
		break;
	  }	
	  if(flag){
		printf("%c won\n",ch);
		return(1);
	  }
  }
}
void solve(){
  if(checkwin()==0){
	if(complete()==0)printf("Game has not completed\n");
	else printf("Draw\n");
  }
}
int main(){
  freopen("a.in","r",stdin);
  freopen("a.out","w",stdout);
  scanf("%d\n",&n);
  for(i=1;i<=n;i++){
	init();
	printf("Case #%d: ",i);
	solve();
  }
  fclose(stdin);
  fclose(stdout);
  return(0);
}

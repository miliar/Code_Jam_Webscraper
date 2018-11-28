#include<iostream>
using namespace std;
int main(){
  int i,k,j,T,N,K,kase,rl,tb,red,blue, flag;
  char str[100][100],rot[100][100];
  scanf("%d",&T);
  for(kase=1;kase<=T;kase++)
  {
	scanf("%d %d\n",&N,&K);
	for(i=0;i<N;i++)
	  scanf("%s\n",str[i]);
	
	//Rotation
	for(i=0;i<N;i++){
	  rl=N-1;tb=N-1;
	  while(rl>=0){
		while(rl>=0 && (str[i][rl] == '.')){
		  rl--;
		}
		if(rl>=0){
		  rot[tb][N-1-i] = str[i][rl];
		  tb--;
		  rl--;
		}
	  }
	  while(tb>=0){
		rot[tb][N-1-i] = '.';
		tb--;
	  }
	}
	for(i=0;i<N;i++)
	  rot[i][N] = 0;
	
	for(i=0;i<N;i++)
	  //cout<<rot[i]<<endl;
	
	red=blue=0;
	for(i=0;i<N;i++){
	  for(k=0;k<N;k++){
		if(rot[i][k] != '.'){
		  for(j=1, flag=1;j<K;j++){
			if((k+j==N) ||(rot[i][k+j] != rot[i][k])){
			  flag=0;
			  break;
			}
		  }
		  if(flag){
			//cout<<"h"<<i<<","<<k<<";";
			if(rot[i][k] == 'B')
			  blue++;
			else
			  red++;
		  }
		  
		  for(j=1, flag=1;j<K;j++){
			if((i+j==N) ||(rot[i+j][k] != rot[i][k])){
			  flag=0;
			  break;
			}
		  }
		  if(flag){
			//cout<<"v"<<i<<","<<k<<";";
			if(rot[i][k] == 'B')
			  blue++;
			else
			  red++;
		  }
		  
		  for(j=1, flag=1;j<K;j++){
			if((k+j==N) || (i+j==N) || (rot[i+j][k+j] != rot[i][k])){
			  flag=0;
			  break;
			}
		  }
		  if(flag){
			//cout<<"rd"<<i<<","<<k<<";";
			if(rot[i][k] == 'B')
			  blue++;
			else
			  red++;
		  }
		  for(j=1, flag=1;j<K;j++){
			
			if((k-j<0) || (i+j==N) || (rot[i+j][k-j] != rot[i][k])){
			  flag=0;
			  break;
			}
		  }
		  if(flag){
			//cout<<"ld"<<i<<","<<k<<";";
			if(rot[i][k] == 'B')
			  blue++;
			else
			  red++;
		  }
		}
	  }
	}
	//cout<<red<<","<<blue<<endl;
	printf("Case #%d: ",kase);
	if(red){
	  if(blue)
		printf("Both\n");
	  else
		printf("Red\n");
	}
	else{
	  if(blue)
		printf("Blue\n");
	  else
		printf("Neither\n");
	}
  }
  return 0;
}

	  
	
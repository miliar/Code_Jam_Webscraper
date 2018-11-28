#include<iostream>
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;

void main2(){
	int R = 0, C =0;
	scanf("%d %d",&R,&C);
	int i = 0, j = 0,flag =0;
	char graph[52][52], ctl= '/',ctr='\\',cdl='\\',cdr='/';
	for(i = 0;i<R;i++) scanf("%s",graph[i]);
	for(i = 0,flag = 0; (i< R) && (flag == 0); i++){
		for(j = 0;(j<C) && (flag == 0);j++){
			flag = 0;
			//cout<<i<<" "<<j<<" "<<graph[i][j]<<endl;
			if(graph[i][j]=='#'){
				//cout<<"Inside "<<i<<" "<<j<<" "<<graph[i][j]<<" "<<j+1<<" "<<C<<endl;
			if((j+1==C) || (i+1==R)|| (graph[i][j+1]!='#')||(graph[i+1][j]!='#')||(graph[i+1][j+1]!='#'))
				{	flag =1;
					break;
				}
				else{
					graph[i][j] = ctl, graph[i][j+1] = ctr,graph[i+1][j] = cdl, graph[i+1][j+1]= cdr;
				}
			}
		}
	}
	if(flag == 1) printf("Impossible\n");
	else{
		for(i=0;i<R;i++) printf("%s\n",graph[i]);
	}
}

int main(){
	int test = 0;
	int a = 0;
	scanf("%d",&test);
	for(a= 1; a<=test;a++){
		printf("Case #%d:\n",a);
		main2();
	}
	return(0);
}

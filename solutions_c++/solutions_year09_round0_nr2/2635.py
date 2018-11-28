#include <stdio.h>
#include <stdlib.h>
#include <stack>
#include <vector>
using std::stack;
using std::vector;
int map[100][100][2];
int wt,ht;
struct Kpoint{
	Kpoint(){}
	Kpoint(int _x,int _y):x(_x),y(_y){}
	int x,y;
};
stack<Kpoint> slist;
vector<char> ocol(26);
bool issliv(int y,int x){
	int h=map[y][x][0];
	if(x>0 && h>map[y][x-1][0]){return false;}
	if(y>0 && h>map[y-1][x][0]){return false;}
	if(y<ht-1 && h>map[y+1][x][0]){return false;}
	if(x<wt-1 && h>map[y][x+1][0]){return false;}
	return true;
}
void AddInList(int y,int x){
   	if(y>0 && map[y-1][x][1]==-1)
		slist.push(Kpoint(x,y-1));
	if(x<wt-1 && map[y][x+1][1]==-1)
		slist.push(Kpoint(x+1,y));
	if(x>0 && map[y][x-1][1]==-1)
		slist.push(Kpoint(x-1,y));
	if(y<ht-1 && map[y+1][x][1]==-1)
		slist.push(Kpoint(x,y+1));
}
int main(){
	int T;
	scanf("%d\n",&T);

	for(int ij=0;ij<T;ij++){
		//reading
		scanf("%d%d\n",&ht,&wt);
		for(int ih=0;ih<ht;ih++)
			for(int iw=0;iw<wt;iw++){
				scanf("%d",&map[ih][iw][0]);
				map[ih][iw][1]=-1;
			}
		//clear
		while(!slist.empty()) slist.pop();
		//analising
		int col=0;
		for(int i=0;i<ht;i++)
			for(int j=0;j<wt;j++){
				if(issliv(i,j)){
					AddInList(i,j);
					map[i][j][1]=col++;
				}
			}
		Kpoint tmp,tmp2;
		while(!slist.empty()){
			tmp=slist.top();
			slist.pop();
			if(map[tmp.y][tmp.x][1]==-1){
				int x=tmp.x,y=tmp.y;
				int h=map[y][x][0];
				if(y>0 && h>map[y-1][x][0]){h=map[y-1][x][0];tmp2.x=x;tmp2.y=y-1;}    //1
				if(x>0 && h>map[y][x-1][0]){h=map[y][x-1][0];tmp2.x=x-1;tmp2.y=y;}    //2
				if(x<wt-1 && h>map[y][x+1][0]){h=map[y][x+1][0];tmp2.x=x+1;tmp2.y=y;} //3
				if(y<ht-1 && h>map[y+1][x][0]){h=map[y+1][x][0];tmp2.x=x;tmp2.y=y+1;} //4
				if((tmp2.x!=tmp.x || tmp2.y!=tmp.y) && map[tmp2.y][tmp2.x][1]!=-1){
					map[tmp.y][tmp.x][1]=map[tmp2.y][tmp2.x][1];
					AddInList(tmp.y,tmp.x);
				}
			}
		}
		//writing
		printf("Case #%d:\n",ij+1);
		char simv='a';
		for(int i=0;i<26;i++) ocol[i]='?';
		for(int i=0;i<ht;i++){
			for(int j=0;j<wt;j++){
				if(ocol[map[i][j][1]]=='?')
					ocol[map[i][j][1]]=simv++;
				printf("%c ",ocol[map[i][j][1]]);
			}
			printf("\n");
		}
	}
	return 0;
}
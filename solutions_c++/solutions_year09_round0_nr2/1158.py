/*Watersheds - Google Code Jam*/
#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

struct punto{
	int x,y;
	punto(int a,int b){
		y=a;
		x=b;
	}
	punto(){}
};
struct estado{
	int x,y,altura,peso;
	estado(int a,int b,int  c,int d){
		y=a;
		x=b;
		altura=c;
		peso=d;
	}
	estado(){}
};

int X,Y;

bool valido(int y,int x){
	return y>=0&&x>=0&&y<Y&&x<X;
}
bool comp(estado a,estado b){
	if(a.altura==b.altura)
		return a.peso<b.peso;
	else
		return a.altura<b.altura;
}



void resuelva(){
	int x,y;

	scanf("%d %d",&Y,&X);
	int m[Y][X];
	char label[Y][X],c='a',flag;



	for(int i=0;i<Y;i++){
		for(int j=0;j<X;j++){
			scanf("%d",&m[i][j]);
			label[i][j]='@';
		}
	}

	for(int i=0;i<Y;i++){
		for(int j=0;j<X;j++){
			if(label[i][j]=='@'){
				flag='@';//Si encontro alguno que tenga etiqueta
				vector<punto> recorrido;
				queue<punto> q;

				q.push(punto(i,j));
				while(!q.empty()){
					y=q.front().y;
					x=q.front().x;
					q.pop();

					if(label[y][x]!='@'){
						flag=label[y][x];
						break;
					}

					recorrido.push_back(punto(y,x));
					vector<estado> posible;
					if(valido(y-1,x)&&m[y-1][x]<m[y][x])
						posible.push_back(estado(y-1,x,m[y-1][x],0));
					if(valido(y,x-1)&&m[y][x-1]<m[y][x])
						posible.push_back(estado(y,x-1,m[y][x-1],1));
					if(valido(y,x+1)&&m[y][x+1]<m[y][x])
						posible.push_back(estado(y,x+1,m[y][x+1],2));
					if(valido(y+1,x)&&m[y+1][x]<m[y][x])
						posible.push_back(estado(y+1,x,m[y+1][x],3));

					if(!posible.empty()){
						sort(posible.begin(),posible.end(),comp);
						q.push(punto(posible[0].y,posible[0].x));
					}
				}

				if(flag=='@')
					flag=c++;
				int sz=recorrido.size();
				for(int k=0;k<sz;k++){
					label[recorrido[k].y][recorrido[k].x]=flag;
				}
			}
		}
	}
	for(int i=0;i<Y;i++){
		printf("%c",label[i][0]);
		for(int j=1;j<X;j++)
			printf(" %c",label[i][j]);
		printf("\n");
	}
}
int main(){
	int n;
	scanf("%d",&n);
	for(int i=1;i<=n;i++){
		printf("Case #%d:\n",i);
		resuelva();
	}
}
/*
5
3 3
9 6 3
5 9 6
3 5 9
1 10
0 1 2 3 4 5 6 7 8 7
2 3
7 6 7
7 6 7
5 5
1 2 3 4 5
2 9 3 9 6
3 3 0 8 7
4 9 8 9 8
5 6 7 8 9
2 13
8 8 8 8 8 8 8 8 8 8 8 8 8
8 8 8 8 8 8 8 8 8 8 8 8 8


1
5 5
1 2 3 4 5
2 9 3 9 6
3 3 0 8 7
4 9 8 9 8
5 6 7 8 9

*/

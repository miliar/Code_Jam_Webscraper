#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;
char tab[10][10];
int main(){

	int n;
	scanf("%d",&n);

	for(int x=0;x<n;x++){
		for(int y=0;y<4;y++) scanf("%s",tab[y]);

		printf("Case #%d: ",x+1);

		int dec = 0;

		for(int y=0;y<4;y++){
			bool todo1=true;
			bool todo2=true;
			for(int z=0;z<4;z++){
				todo1 = todo1 && (tab[y][z]=='X' || tab[y][z]=='T');
				todo2 = todo2 && (tab[y][z]=='O' || tab[y][z]=='T');
				
			}
			if(todo1) dec=1;
			if(todo2) dec=2;
		}

		for(int z=0;z<4;z++){
			bool todo1=true;
			bool todo2=true;
			for(int y=0;y<4;y++){
				todo1 = todo1 && (tab[y][z]=='X' || tab[y][z]=='T');
				todo2 = todo2 && (tab[y][z]=='O' || tab[y][z]=='T');
				
			}
			if(todo1) dec=1;
			if(todo2) dec=2;
		}
	
		bool p1=true,p2=true;
		for(int y=0;y<4;y++){
			p1 = p1 && (tab[y][y]=='X' || tab[y][y]=='T');
			p2 = p2 && (tab[y][y]=='O' || tab[y][y]=='T');
		}

		if(p1) dec = 1;
		if(p2) dec = 2;

		p1=true;
		p2=true;
	
		for(int y=0;y<4;y++){
			p1 = p1 && (tab[y][3-y]=='X' || tab[y][3-y]=='T');
			p2 = p2 && (tab[y][3-y]=='O' || tab[y][3-y]=='T');
		}

		if(p1) dec = 1;
		if(p2) dec = 2;

		
		if(dec==0)
			for(int y=0;y<4;y++)
				for(int z=0;z<4;z++)
					if(tab[y][z]=='.') dec=3;

		switch(dec){
			case 0:
				printf("Draw");
			break;
			case 1:
				printf("X won");
			break;
			case 2:
				printf("O won");
			break;
			case 3:
				printf("Game has not completed");
		};

		if(x!=n-1)
			printf("\n");

	}


	return 0;
}

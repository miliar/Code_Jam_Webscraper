#include<cstdio>
#include<iostream>
int picture[50][50];

void result(){
  int ancho, alto;
  scanf("%d %d",&alto, &ancho);
  int numTilesBlue = 0;
  for(int row = 0; row < alto; row++)
    for(int column = 0; column < ancho; column++){
      char r;
      std::cin >> r;
      if(r == 35) numTilesBlue++;
      picture[row][column] = r;
    }

  for(int row = 0; row < alto; row++)
    for(int column = 0; column < ancho; column++){
      if(picture[row][column] == 35 && row + 1 < alto && column + 1 < ancho &&
	 picture[row+1][column] == 35 &&
	 picture[row][column+1] == 35 &&
	 picture[row+1][column+1] == 35
	 ){
	numTilesBlue -= 4;
	picture[row][column] = 47;
	picture[row][column + 1] = 92;
	picture[row + 1][column] = 92;
	picture[row + 1][column + 1] = 47;

      }
    }

  if(numTilesBlue != 0)
    printf("Impossible\n");
  else
    for(int row = 0; row < alto; row++){
      for(int column = 0; column < ancho; column++){
	printf("%c",picture[row][column]);
	
      }
      printf("\n");
    }
}


int main(){
  int cases;
  scanf("%d",&cases);
  for(int i = 1; i <= cases; i++){
    printf("Case #%d:\n",i);
    result();
  }
}

#include <cstdio>
#include <vector>
using namespace std;
int main(){
  int t;
  scanf("%d", &t);
  for(int i=0; i<t; i++){
    int Alt[150][150], Nr[150][150];
    int H, W;
    int NUMER=1;
    vector< pair<int, int> > Bufor;
    for(int j=0; j<150; j++){
      for(int k=0; k<150; k++){
	Alt[j][k]=Nr[j][k]=0;
      }
    }
    scanf("%d%d", &H, &W);
    for(int h=0; h<H; h++){
      for(int w=0; w<W; w++){
	scanf("%d", &Alt[h][w]);
      }
    }
    for(int h=0; h<H; h++){
      for(int w=0; w<W; w++){
	//printf("h: %d w: %d", h, w);
	if(Nr[h][w]==0){
	  //printf(" nV \n");
	  int a=h, b=w;
	  int C=0;
	  while((1)){
	    //printf("-> h: %d w: %d\n", a, b);
	    int min=2000000000, A, B;
	    Bufor.push_back(make_pair(a, b));
	    if(a-1 >=0 && Alt[a-1][b] < min){ min = Alt[a-1][b]; A = a-1; B = b; };//North
	    if(b-1 >=0 && Alt[a][b-1] < min){ min = Alt[a][b-1]; A = a; B = b-1; };//West
	    if(b+1 < W && Alt[a][b+1] < min){ min = Alt[a][b+1]; A = a; B = b+1; };//East
	    if(a+1 < H && Alt[a+1][b] < min){ min = Alt[a+1][b]; A = a+1; B = b; };//South
	    if(min>=Alt[a][b]){
	      break;//doszlismy do zlewu
	    }else if(Nr[A][B]!=0){
	      C=Nr[A][B];
	    }
	    a=A;
	    b=B;
	  }
	  
	  if(C==0){
	    C=NUMER++;
	  }
	  for(unsigned int k=0; k<Bufor.size(); k++)
	    Nr[ Bufor[k].first ][ Bufor[k].second ]=C;
	  Bufor.clear();
	}
      }
    }
    printf("Case #%d: \n", i+1);
    for(int h=0; h<H; h++){
      for(int w=0; w<W; w++){
	printf("%c ", (char)(Nr[h][w]+'a'-1));
      }
      printf("\n");
    }
  }
  return 0;
}

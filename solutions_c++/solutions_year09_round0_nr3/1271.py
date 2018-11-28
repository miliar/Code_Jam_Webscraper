#include<iostream>
#include<string.h>
using namespace std;

#define M 501
#define N 20

char line[] = "welcome to code jam";

int pal[M][N];

void init(){
  for(int i = 0; i < M; i++)
    for(int j = 0; j < N; j++)
      pal[i][j] = 0;

  for(int i = 0; i < M; i++)
    pal[i][0] = 1;

  for(int i = 1; i < N; i++)
    pal[0][i] = 0;


}

const char * text;
int len = 0;

void calc(){

  for(int i = 1; i <= len; i++){
    for(int j = 1 ;  j< N; j++){
      pal[i][j] = pal[i-1][j];
      if(text[i-1] == line[j-1])
	pal[i][j] += pal[i-1][j-1];
      pal[i][j] %= 10000;
      //      cout<<pal[i][j]<<" ";
    }
    //    cout<<endl;
  }

}

int main(){
  int nooftest = 0;
  cin>>nooftest;
  string str;
  getline(cin, str);
  for(int i = 0; i < nooftest; i++){
    getline(cin, str);
    text = str.data();
    len = strlen(text);
    //  cout<<text<<" "<<len<<endl;
    init();
    calc();
    char res[5];
    sprintf(res, "%4d", pal[len][N-1]);
    for(int x = 0; res[x] - '0' <= 0 && x < 4; x++){
      //   cout<<res[x]<<" "<<(int)res[x]<<endl;
      res[x] = '0';
    }
    printf("Case #%d: %s\n", (i+1),res);// pal[len][N-1]);
  }
}

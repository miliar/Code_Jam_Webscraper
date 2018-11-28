#include <cstdio>
#include <cstring>
#include <string>

using namespace std;

const int MXVAL = 10000000+10;
int bio[MXVAL];


char temp[20];
int flag = 0;
int count(int n, int upper){
  flag++;

  sprintf(temp, "%d", n);
  string N(temp);

  int len = (int)N.size(), ret = 0;

  char rotated[20];
  memset(rotated, '\0', sizeof(rotated));
  int rotatedValue;

  char left[20]; int leftLen = 0;

  for(int i = 1; i < len; i++){
    left[leftLen] = N[leftLen]; leftLen++;
    
    memcpy(rotated, temp+i, len-i);
    memcpy(rotated+len-i, temp, i);

    //    rotated = N.substr(i) + N.substr(0,i);
    sscanf(rotated, "%d", &rotatedValue);

    if(rotated[0] != '0' && bio[rotatedValue] != flag && rotatedValue <= upper && rotatedValue > n){
      bio[rotatedValue] = flag;
      ret++;
    }
  }
  
  return ret;
}

void solve(int T){
  int A, B;
  scanf("%d %d", &A, &B);

  int ret = 0;
  for(int n = A; n < B; n++){
    ret += count(n,B);
  }

  printf("Case #%d: %d\n", T+1, ret);
}

int main(){
  int T;
  scanf("%d", &T);

  for(int i = 0; i < T; i++)
    solve(i);

  return 0;
}

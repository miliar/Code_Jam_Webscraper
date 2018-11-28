#include<cstdio>
#include<cstring>

int dp[600][50];
char s[600];
char ori[600]={"welcome to code jam"};
int tc;

int process (int charke, int suit){

  if (dp[charke][suit] != -1) return dp[charke][suit];
  if (suit == 19) {dp[charke][suit] = 1; return 1;}
  if (charke == strlen(s)) return 0;
   
  int temp = 0;
  if (s[charke] == ori[suit]){
     temp += process(charke+1, suit+1);
  } 
  temp += process(charke+1, suit);
  dp[charke][suit] = temp % 100000;
  return temp % 100000;
}


int main(){
 scanf("%d\n",&tc);
 for (int ti = 1; ti <= tc; ti++){
     gets(s);    
     memset(dp,-1,sizeof(dp));
     process(0,0);
     printf("Case #%d: ",ti);
     dp[0][0]= dp[0][0] % 10000;
     if (dp[0][0] >= 1000) {}
     else if (dp[0][0] >= 100) {printf("0");}
     else if (dp[0][0] >= 10) {printf("00");}
     else  printf("000");
     
     printf("%d\n",dp[0][0]);

 }
}

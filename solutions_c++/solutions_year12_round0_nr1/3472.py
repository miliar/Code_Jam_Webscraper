#include<iostream>
#include<iomanip>
#include<algorithm>
#include<vector>
#include<cstring>
#include<cstdio>

using namespace std;

#define FOR(i,a,b) for(int i = a ; i < b ; ++i)

char arr[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
char str[110];

int main(){
  
  int T;
  
  cin>>T;
  gets(str);
  FOR(j,0,T){
    gets(str);
    FOR(i,0,strlen(str))
      if((str[i] >= 'a')&&(str[i] <= 'z'))
	str[i] = arr[str[i]-'a'];
    printf("Case #%d: %s\n", j+1, str);
  }
  
  return 0;
  
}
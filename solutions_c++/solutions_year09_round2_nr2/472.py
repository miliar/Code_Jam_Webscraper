#include<iostream>
#include<algorithm>
#include<string>
using namespace std;

const int N = 25;
int tab[N];
string temp;

main(){
  int t;
  scanf("%d",&t);
  for(int q=1;q<=t;q++){  
    cin >> temp;
    int y = temp.size();
    for(int i=0;i<y;i++)
      tab[i+1] = temp[i] - '0';
    if(!next_permutation(tab+1,tab+1+y)){
      y++;
      tab[y] = 0;
      sort(tab+1,tab+y+1);
      int c = 1;
      while(tab[c] == 0) c++;
      printf("Case #%d: ",q);
      printf("%d",tab[c]);
      for(int i=1;i<=c-1;i++) printf("0");
      for(int j=c+1;j<=y;j++) printf("%d",tab[j]);
      printf("\n");
    }
    else{
      printf("Case #%d: ",q);
      for(int i=1;i<=y;i++) printf("%d",tab[i]);
      printf("\n");
    }
  }
}

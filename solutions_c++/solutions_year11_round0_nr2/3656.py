#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <map>

using namespace std;

typedef map<int, char> CONV;

int etoi2(char e){
   if(e == 'Q')return 1;
   if(e == 'W')return 2;
   if(e == 'E')return 3;
   if(e == 'R')return 5;
   if(e =='A') return 7;
   if(e == 'S')return 11;
   if(e== 'D') return 13;
   if(e=='F') return 17;
return -1;
}


int etoi(char e){
   if(e == 'Q')return 0;
   if(e == 'W')return 1;
   if(e == 'E')return 2;
   if(e == 'R')return 3;
   if(e =='A') return 4;
   if(e == 'S')return 5;
   if(e== 'D') return 6;
   if(e== 'F') return 7;
   return -1;
}
   
int main()
{
   int t;
   
   scanf("%d", &t);
   for(int i =0;i < t;i++){
	int c,d,n;
      CONV conv;
      bool b_op[8][8];
      int i_op[8];
      char str[128];
      string ans = "";
      for(int x=0;x<8;x++){
	 i_op[x] = 0;
	 for(int y=0;y<8;y++)
	    b_op[x][y]=false;
      }

      scanf("%d", &c);
      for(int j=0;j<c;j++){
	 char comb[4];
	 scanf("%s", comb);
	 conv.insert(CONV::value_type(etoi2(comb[0]) * etoi2(comb[1]), comb[2]));
      }
      scanf("%d", &d);
      for(int j=0;j<d;j++){
	 char op[3];
	 int a,b;
	 scanf("%s", op);
	 a = etoi(op[0]);
	 b = etoi(op[1]);
	 b_op[a][b] = true;
	 b_op[b][a] = true;
      }
      scanf("%d %s", &n, str);
      ans +=str[0];
	  i_op[etoi(str[0])]++;
      for(int j=1; j<n;j++){
	 CONV::iterator it;
	 if(!ans.empty())
		 it = conv.find(etoi2(ans[ans.size()-1])*etoi2(str[j]));
	 else
		it = conv.end();
	 if(it != conv.end()){
		 i_op[etoi(ans[ans.size()-1])]--;
	    ans.erase(--ans.end());
	    ans += it->second;
	 }
	 else{
	    bool clear =false;
	    int check = etoi(str[j]);
	    for(int k=0;k<8;k++){
	       if(b_op[check][k]&&i_op[k]>0){
		  clear = true;
		  ans.clear();
	       }
	    }
	    if(clear){
	       for(int x=0;x<8;x++)
		  i_op[x]=0;
	    }else{
	       ans += str[j];
	       i_op[check]++;
	    }
	 }
      }
      printf("Case #%d: [", i+1);
	  if(ans.empty()){
		  printf("]\n");
	  }
	  else{
	      for(int r=0;r<ans.size()-1;r++)
		 printf("%c, ", ans[r]);
		 printf("%c]\n", ans[ans.size()-1]);
	  }
   }
   return 0;
}

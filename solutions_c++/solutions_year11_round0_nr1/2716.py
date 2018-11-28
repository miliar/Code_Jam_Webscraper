#include <cstdio>
#include <vector>

using namespace std;

vector<char> list;
vector<int> bluel,oranl;
int blue,orange,bpos,opos,lpos,time;
int T,n,number;
char color[16];


int main(){

  scanf("%d",&T);
  for(int t=0;t<T;t++){
    scanf("%d",&n);
    list.clear();
    bluel.clear();
    oranl.clear();
    for(int i=0;i<n;i++){
      scanf("%s %d",color,&number);
      list.push_back(color[0]);
      if(color[0]=='B') bluel.push_back(number);
      else              oranl.push_back(number);
    }
    blue=0; orange=0;
    bpos=1; opos=1;
    char next=list[0];
    lpos=0; time=1;
    while(true){
      // both walk
      if(blue<(int)bluel.size() and bluel[blue]!=bpos and
         orange<(int)oranl.size() and oranl[orange]!=opos){
        if(orange<(int)oranl.size() and oranl[orange]<opos) opos--;
        if(orange<(int)oranl.size() and oranl[orange]>opos) opos++;
        if(blue<(int)bluel.size() and bluel[blue]<bpos) bpos--;
        if(blue<(int)bluel.size() and bluel[blue]>bpos) bpos++;
        time++; continue;
      }
      // blue push
      if(next=='B' and bluel[blue]==bpos){
        blue++;
        next=list[++lpos];
        if(orange<(int)oranl.size() and oranl[orange]<opos) opos--;
        if(orange<(int)oranl.size() and oranl[orange]>opos) opos++;
        time++;
        if(lpos>=(int)list.size()) break;
        continue;
      // orange push
      } else if(next=='O' and oranl[orange]==opos){
        orange++;
        next=list[++lpos];
        if(blue<(int)bluel.size() and bluel[blue]<bpos) bpos--;
        if(blue<(int)bluel.size() and bluel[blue]>bpos) bpos++;
        time++;
        if(lpos>=(int)list.size()) break;
        continue;
      } else {
        if(orange<(int)oranl.size() and oranl[orange]<opos) opos--;
        if(orange<(int)oranl.size() and oranl[orange]>opos) opos++;
        if(blue<(int)bluel.size() and bluel[blue]<bpos) bpos--;
        if(blue<(int)bluel.size() and bluel[blue]>bpos) bpos++;
      }
      time++;
    }
    printf("Case #%d: %d\n",t+1,time-1);
  }

  return 0;
}

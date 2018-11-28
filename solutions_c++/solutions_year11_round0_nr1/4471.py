#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <algorithm>
#include <numeric>
#include <functional>
#include <limits>
#include <utility>
#include <cstdlib>
#include <cstdio>
#include <cmath>

using namespace std;

int TC = 1;
int step_count;
const int big_num=200;

int next_value(int next_button,int x){
   if(next_button>=x){return 1;}else{return -1;}
}

struct button_pair{
int point;
int order_num;
};

class Robot{
   public:
   queue<button_pair> buttons;
   int x;
   int nb;
   int b_order;
   void init_robot(){
      x=1;
      nb=buttons.front().point;
      b_order=buttons.front().order_num;
      buttons.pop();
   }
   bool is_move(){
      return (x != nb);
   }
   void move_step(){
      x += next_value(nb,x);
   }
   void push_step(){
      if(buttons.empty()){nb =0;b_order=big_num;}
      else{
         nb=buttons.front().point;
         b_order=buttons.front().order_num;
         buttons.pop();
      }
   }
};


int main (){
   int T,N,P;
   char R;

    for(scanf ("%d", &T); TC <= T; TC++){
        
        scanf ("%d", &N);
        Robot ro;
        Robot rb;
        
        for(int i=0;i<N;i++){
            scanf("%s %d",&R,&P);
            if(R=='O'){struct button_pair bp={P,i+1}; ro.buttons.push(bp);}
            else{struct button_pair bp={P,i+1};rb.buttons.push(bp);}
        }

        step_count=0;
//start counting

        //single case
        if(rb.buttons.empty()){
           ro.init_robot();
           while(ro.nb != 0){
              step_count++;
              if(ro.is_move()){ro.move_step();}
              else{ro.push_step();}
           }
           printf("Case #%d: %d", TC,step_count);
           cout << endl;
           continue;
        }
           
        if(ro.buttons.empty()){
           rb.init_robot();
           while(rb.nb != 0){
              step_count++;
              if(rb.is_move()){rb.move_step();}
              else{rb.push_step();}
           }
           printf("Case #%d: %d", TC,step_count);
           cout << endl;
           continue;
        }
          
        //general case
        ro.init_robot();
        rb.init_robot();
        while( ro.nb != 0 || rb.nb != 0 ){
        step_count++;
        bool is_push_ro=false;
        bool is_push_rb=false;
        if(ro.is_move()){ro.move_step();}
        else{
           if(ro.b_order < rb.b_order){is_push_ro=true;}
        }
        if(rb.is_move()){rb.move_step();}
        else{
           if(rb.b_order < ro.b_order){is_push_rb=true;}
        }
        if(is_push_ro){ro.push_step();}
        if(is_push_rb){rb.push_step();}
        
        }
        printf("Case #%d: %d\n", TC,step_count);
    }
    return 0;
}
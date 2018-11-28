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
#include <bitset>
#include <cstdlib>
#include <cstdio>
#include <cmath>

using namespace std;

int TC = 1,T,N;

const int MAX_B=40;

int max_bit_num(long long a){
   int result =0;
   bitset<MAX_B> a_bit=a;
   if(a_bit.none()){return 0;}
   while(true){
      result++;
      a_bit >>=1;
      if(a_bit.none()){return result;}
   }
}

int max_index(int A){
int num=(int) pow(2.0,(double)A)-1;
   return num;
}

long long patrick_add(long long a,long long b){
   int clear_index =max(max_bit_num(a),max_bit_num(b));
   bitset<MAX_B> a_bit=a;
   bitset<MAX_B> b_bit=b;
   a_bit ^= b_bit;
   a_bit.set(clear_index,0);
   long long result =  a_bit.to_ulong();
   return result;
}

bool is_select_candy(int i,int k){
  bitset<MAX_B> bs;
  bs.flip();
  bs &= i;
  if(bs[k]==1){return true;}else{return false;}
}

int main(){
   for(scanf("%d", &T); TC <= T; TC++){
      scanf("%d", &N);
      vector<int> candy_bag;
      long long  result=0;
      int temp;
      for(int i=0;i<N;i++){
         scanf("%d", &temp);
         candy_bag.push_back(temp);
      }
      
      //priority_queue<long long> q1;
      int max_index_num = max_index(N);

      
      for(int i=1;i<max_index_num;i++){
         //cout << "i:" << i << endl;
         bool is_find_ans = false;
         

         long long real_sum_front=0;
         long long real_sum_back=0;
         long long sum_front=0;
         long long sum_back=0;
         for(int k=0;k<candy_bag.size();k++){

            if(is_select_candy(i,k)){
               real_sum_front += candy_bag[k];
               sum_front = patrick_add(sum_front,candy_bag[k]);
            }else{
               real_sum_back += candy_bag[k];
               sum_back = patrick_add(sum_back,candy_bag[k]);
            }

         }
        //if(sum_front == sum_back  ){q1.push(result);}
         if(sum_front == sum_back && result < max(real_sum_front,real_sum_back) ){
            is_find_ans=true;result = max(real_sum_front,real_sum_back);
         }
      }
      //if(!q1.empty()){
      //cout << q1.top() << endl;
      //} 
   if(result!=0){
      printf("Case #%d: %lld\n", TC,result);
   }else{
      printf("Case #%d: NO\n", TC);}      
   }
return 0;
}
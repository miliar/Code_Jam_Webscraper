#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <string>

#define _odjazd 0
#define _przyjazd 1

#define _A 0
#define _B 1

using namespace std;

class data{
private:
          int time;
          bool action; //0 - odjazd 1 - przyjazd
          bool train; // 0 - A 1 - B
public:
       void setTime(int t){ time = t; }
       int getTime() { return time; }
       void setAction(bool a) { action = a; }
       bool getAction() { return action; }
       void setTrain(bool t) { train = t; }
       bool getTrain() { return train; }
       void set(int ti, bool ac, bool tr){ setTime(ti); setAction(ac); setTrain(tr); }
       void operator=(data a){
            time = a.time;
            action = a.action;
            train = a.train;     
       }
       bool operator<(data a){
            if(time == a.time && action == 1) return 1;
            if(time < a.time) return 1;
            return 0;
       }
       //bool operator>(data a){
       //     return (a < this);     
       //}
       void print(){
            printf("Time: %d, Action: %s, Train: %c\n", time, action==0?"odjazd":"przyjzad", train==0?'A':'B');     
       }
       data(){}      
};

int HHMMtoInt(string sTime){
  int time = (int)(sTime[0]-'0')*10 + (int)(sTime[1]-'0');
  time *= 60;
  time += (int)(sTime[3]-'0') * 10 + (int)(sTime[4]-'0');
  return time;   
}

char buffor1[8], buffor2[8];

bool cmp(data a, data b){
     return a<b;     
}

int main(){
 int N;
 scanf("%d", &N);
 for(int n = 0; n < N; n++){
         vector<data> po;
         int T;
         scanf("%d", &T);
         int A, B;
         scanf("%d%d", &A, &B);
         for(int i = 0; i < A; i ++){
                 string a, b;
                 scanf("%s%s", buffor1, buffor2);
                 a = buffor1; b = buffor2;
                 data c, d;
                 c.set(HHMMtoInt(a), 0, 0);
                 d.set(HHMMtoInt(b) + T, 1, 0);
                 po.push_back(c); 
                 po.push_back(d);       
         }
         for(int i = 0; i < B; i ++){
                 string a, b;
                 scanf("%s%s", buffor1, buffor2);
                 a = buffor1; b = buffor2;
                 data c, d;
                 c.set(HHMMtoInt(a), 0, 1);
                 d.set(HHMMtoInt(b) + T, 1, 1);
                 po.push_back(c); 
                 po.push_back(d);       
         }
         sort(po.begin(), po.end(), cmp);
         int stA = 0, stB = 0;
         int wA = 0, wB = 0;
         for(int i = 0; i < po.size(); i++){
              //   printf("sta: %d stb: %d wA: %d wb: %d\n", stA, stB, wA, wB);
                 if(po[i].getAction() == _odjazd)
                   if(po[i].getTrain() == _A)
                     if(stA == 0) wA++;
                     else stA--;             
                   else if(po[i].getTrain() == _B)
                    if(stB == 0) wB++;
                    else stB--; 
                 if(po[i].getAction() == _przyjazd)
                   if(po[i].getTrain() == _A)
                     stB++;
                   else if(po[i].getTrain() == _B)
                     stA++;      
         }
         /*for(int i = 0; i < po.size(); i++){
                 po[i].print();
         }*/
         printf("Case #%d: %d %d\n", n+1, wA, wB);
 }
// system("pause");
 return 0;   
}

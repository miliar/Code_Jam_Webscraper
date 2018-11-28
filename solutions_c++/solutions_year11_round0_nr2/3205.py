#include <iostream>
#include <vector>
#include <string>
#include <stack>
using namespace std;
vector<char> inter;
stack<char> ch;
int T,D,C,N;
bool match_opp(string opp[], int t1, int t2, int D){
     for (int i=0;i<D;i++)
              if ((t1==opp[i][0] && t2==opp[i][1]) || (t1==opp[i][1] && t2==opp[i][0])) return 1;
     return 0;
}
bool match_com(string com[],char t1, char t2, int &tar, int D){
     for (int i=0;i<D;i++)
              if ((t1==com[i][0] && t2==com[i][1]) || (t1==com[i][1] && t2==com[i][0])){
                   tar = i;
                   return 1;
              }
     return 0;
}

int main(){
    cin >> T;
    for (int q=1;q<=T;q++){
        cin >> C;
        string com[C];
        for (int r=0;r<C;r++){
            cin >> com[r];
        }
        cin >> D;
        string opp[D];
        for (int r=0;r<D;r++){
            cin >> opp[r];
        }
        cin >> N;
        for (int i=0;i<N;i++){
            vector<char> watch;
            while (!watch.empty()) watch.pop_back();
            char in;
            cin >> in;
            ch.push(in);
            
            if (ch.size()>1){
                int t1 = ch.top();
                ch.pop();
                int t2 = ch.top();
                ch.pop();
                int tar;
                if (match_com(com,t1,t2,tar,C)){
                     ch.push(com[tar][2]);                  
                }
                else{
                     ch.push(t2);
                     ch.push(t1);
                }
            }
            stack<char>s2;
            while (!s2.empty()) s2.pop();
            char ttt=ch.top();
            ch.pop();
            int opposed = 0;
            while (!ch.empty()){
                  if (match_opp(opp,ch.top(),ttt,D)) opposed = 1;
                  s2.push(ch.top());
                  ch.pop();
            }
            if (!opposed){
               while (!s2.empty()){
                     ch.push(s2.top());
                     s2.pop();
               }
               ch.push(ttt);
            }
        }
        stack<char> temp;
        while (!temp.empty()) temp.pop();
        while (!ch.empty()){
              temp.push(ch.top());
              ch.pop();
        }
        printf("Case #%d: [",q);
        while (temp.size()>1){
              printf("%c, ", temp.top());
              temp.pop();
        }
        if (!temp.empty())
           printf("%c]\n",temp.top());
        else
            printf("]\n");
    }
}

#include<iostream>
#include<vector>
#include<stdio.h>
using namespace std;

int main(){
    int N,cases;
    scanf("%d\n",&N);
    for(cases=0;cases<N;cases++){
    int no_se,no_q;
    vector<string> seng;
    vector<int> flag;
    scanf("%d\n",&no_se);
    for(int i=0;i<no_se;i++)
    {
    char sas[1000];
    gets(sas);
    string str(sas);
    seng.push_back(str);
    flag.push_back(0);
    }
    scanf("%d\n",&no_q);
    int c=0,curr=0,sw=0,p;
    
    for(int j=0;j<no_q;j++){
    char sss[100];
    gets(sss);
    string str1(sss);
    for(p=0;p<no_se;p++)
    if(seng[p]==str1)
    break;
    if(flag[p]==curr){
                      c++;
                      if(c==no_se)
                      {
                                  c=1;
                                  curr=!curr;
                                  sw++;
                                  }
                                  else
                                  flag[p]=!flag[p];
                      }
    }
    printf("Case #%d: %d\n",(cases+1),sw);
    }
}

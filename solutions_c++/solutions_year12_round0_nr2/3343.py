#include<iostream>
#include<cstdio>
#include<string>
#include<fstream>
using namespace std;
int main()
{
    int t,i,j,n,s,p,ct;
    float score;
    ofstream istr;
    istr.open("demo.txt");
    scanf("%d",&t);
    for(i=1;i<=t;i++){
                      ct=0;
                         scanf("%d%d%d",&n,&s,&p);
                         for(j=0;j<n;j++){
                                  scanf("%f",&score);
                                  score-=p;
                                  if(score>=0){
                                  score/=2.00;
                                  if(score>=p-1)
                                                ct++;
                                  else if(score>=p-2){
                                                     s--; 
                                                     ct++;
                                  }
                                  }       
                         }
        istr<<"Case #"<<i<<": ";
        if(s>=0)
        istr<<ct<<"\n";
        else
        istr<<ct+s<<"\n";
    }
    istr.close();
    system("pause");
    return 0;
}

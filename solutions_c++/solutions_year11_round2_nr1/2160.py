/*
This program is develpoed by Ratan Dhorawat.
*/

#include <algorithm>
#include <iostream>
#include <iterator>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include<stdio.h>
using namespace std;

int main()
{

 int T,cas=0;
 cin>>T;
 while(T--)
 {cas++;
 int N;
 cin>>N;
 string tmp;
 string s[N];
 double a[N][N];
 double rp[N];
 double wn[N];
 double tt[N];
 for(int i=0;i<N;i++)
 {
         cin>>tmp;
         s[i]=tmp;
         double t=0,w=0;
         for(int j=0;j<N;j++)
         {
                 if(s[i][j]=='1')
                 {
                                 t+=1;w+=1;a[i][j]=1;
                 }
                 else if(s[i][j]=='0')
                 {
                      t+=1;a[i][j]=0;
                 }
                 else{a[i][j]=2;
                 continue;                 
                 }
         }
         rp[i]=w/t;
         wn[i]=w;
         tt[i]=t;
 }
 double owp[N];
 double owptmp;
 for(int i=0;i<N;i++)
 {
        // cout<<"inside\n";
         owptmp=0;double tmpw=0,cur=0,ttpp=0;
         for(int j=0;j<N;j++)
         {//cout<<"inside\n";
                 if(i==j)continue;
                 if(a[j][i]==1)
                 {
                            tmpw=wn[j]-1;cur=tt[j]-1;ttpp+=1;;
                 }        
                 else if(a[j][i]==0)
                 {
                      tmpw=wn[j];cur=tt[j]-1;ttpp+=1;
                 }
                 else
                 continue;
              //   cout<<tmpw<<" :"<<cur<<endl;
//                 cout<<owptmp<<endl;
                 owptmp +=(tmpw/cur); 
         }

         owp[i]=owptmp/ttpp;
 } 
 double oowp[N];
 for(int i=0;i<N;i++)
 {
         owptmp=0;double ttpp=0;
         for(int j=0;j<N;j++)
         {//cout<<owptmp<<":>"<<endl;
                 if(i==j)continue;
                 if(a[j][i]==0||a[j][i]==1){
                 owptmp+=(owp[j]);ttpp+=1;
                 }
                 
         }
         oowp[i]=owptmp/ttpp;
 }
// for(int i=0;i<N;i++)
// cout<<rp[i]<<" :: "<<owp[i]<<" :: "<<oowp[i]<<endl;
 cout<<"Case #"<<cas<<":\n";
 for(int i=0;i<N;i++)
 {
         owptmp=0;
         owptmp+= (0.25*rp[i])+(0.5*owp[i])+(0.25*oowp[i]);
         printf("%0.9lf\n",owptmp);
 }
 }
 return 0;
}

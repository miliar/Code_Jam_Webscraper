#include <stdio.h>
#include <conio.h>
#include <list>

using namespace std;

int main(){
    int t,t2,n,k,s,wR,wB;
    scanf("%d",&t);
    list<char> l[51];
    list<char>::iterator it;
    list<char>::iterator it2;    
    char c;
    for (int t2=1;t2<=t;t2++){
        scanf("%d %d\n",&n,&k);
        for (int i=0;i<n;i++){
             l[i].clear();
             for (int j=0;j<n;j++){
                 scanf("%c",&c);
                 if (c=='.')
                    l[i].push_front(c);
                    else
                        l[i].push_back(c);
                 }
             scanf("%c",&c);
             }
        wR=0;
        wB=0;
        for (int i=0;i<n;i++){
            for (int j=0;j<n;j++){
                it=l[i].begin();
                advance(it,j);
//                printf("%c",*it);
                if (*it!='.'){
                    //checo E
                    s=0;          
                    it2=it;
                    for (int a=i,b=j;a<n&&b<n&&*it2==*it;a++){
                        s++;
                        it2=l[a+1].begin();
                        advance(it2,b);
                        }
                    if (s>=k){
                       if (*it=='R')
                          wR=1;
                          else
                              wB=1;
                       }
                    //fin E
                    //checo SE
                    s=0;          
                    it2=it;                    
                    for (int a=i,b=j;a<n&&b<n&&*it2==*it;a++,b++){
                        s++;
                        it2=l[a+1].begin();
                        advance(it2,b+1);
                        }
                    if (s>=k){
                       if (*it=='R')
                          wR=1;
                          else
                              wB=1;
                       }
                    //fin SE
                    //checo S
                    s=0;          
                    it2=it;                    
                    for (int a=i,b=j;a<n&&b<n&&*it2==*it;b++){
                        s++;
                        it2=l[a].begin();
                        advance(it2,b+1);                       
                        }
                    if (s>=k){
                       if (*it=='R')
                          wR=1;
                          else
                              wB=1;
                       }
                    //fin S
                    //checo SW
                    s=0;          
                    it2=it;                    
                    for (int a=i,b=j;a<n&&b>=0&&*it2==*it;a++,b--){
                        s++;
                        it2=l[a+1].begin();
                        advance(it2,b-1);
                        }
                    if (s>=k){
                       if (*it=='R')
                          wR=1;
                          else
                              wB=1;
                       }
                    //fin SW       
                    }
                    if (wR==1&&wB==1)
                       break;                                                                                    
                 }        
             if (wR==1&&wB==1)
                break;
//             printf("\n");                       
             }
        if(wR==0&&wB==0)
           printf("Case #%d: Neither\n",t2);
        else if (wR==1&&wB==1)
           printf("Case #%d: Both\n",t2);
        else if (wR==1)
           printf("Case #%d: Red\n",t2);
        else if (wB==1)
           printf("Case #%d: Blue\n",t2);           
        }
//    printf("listo");
    getch();
    }

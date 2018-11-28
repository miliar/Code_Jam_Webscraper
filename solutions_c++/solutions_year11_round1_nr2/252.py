#include<stdio.h>
#include<stdlib.h>
#include<list>
#include<string>
#include<iostream>
#include<vector>
#include<string.h>
using namespace std;
struct node{
    char word[40];
    int num;
    vector<int> pos[30];
    node(){};
};

void solve(int test){
    printf("Case #%d:",test);
    int n,m;
    scanf("%d %d",&n,&m);
    list<node> wordList[11];
    node allList[n];
    for(int i=0;i<n;i++){
        node tmp;
        scanf("%s",tmp.word);
        //strcpy(allList[i],tmp.word);
        tmp.num=i;
        for(int j=0;tmp.word[j]!='\0';j++){
            tmp.pos[tmp.word[j]-'a'].push_back(j);
        }
        allList[i]=tmp;
        wordList[strlen(tmp.word)].push_back(tmp);
    }
    char guessList[30];

    for(int i=0;i<m;i++){
        scanf("%s",guessList);
        int answer=0,answernum=0;
        for(int j=0;j<n;j++){
            // choose word j
            //printf("j=%d\n",j);
            list<node> tmp =wordList[strlen(allList[j].word)];
            int score=0;
            for(int k=0;guessList[k]!='\0';k++){
                //printf("k=%d\n",k);
                // going to guess guess[k]
                bool hasK=0;
                if(tmp.size()==1)break;
                //printf("tmp size = %d\n",tmp.size());
                for(list<node>::iterator it=tmp.begin();it!=tmp.end();it++)if( (*it).pos[guessList[k]-'a'].size()!=0){
                    hasK=1;
                    break;
                }
                if(hasK==0)continue;
                if(allList[j].pos[guessList[k]-'a'].size()==0)score++;
                for(list<node>::iterator it=tmp.begin();it!=tmp.end();){
                    if( (*it).pos[guessList[k]-'a']!=allList[j].pos[guessList[k]-'a']){
                        list<node>::iterator it2=it;
                        it++;
                        tmp.erase(it2);
                    }
                    else it++;
                }
            }
            if(score>answer){
                answer=score;
                answernum=j;
            }
        }
        printf(" %s",allList[answernum].word);
    }
    printf("\n");
}
int main(){
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        solve(i);
    }
}

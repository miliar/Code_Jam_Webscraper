#include <iostream>
#include <vector>
using namespace std;

void vectorOR(vector<int>* src, vector<int>* dest){
    vector<int>::iterator p,q;
    for(p=dest->begin();p!=dest->end();p++){
        bool flag = true;
        for(q=src->begin();q!=src->end();q++){
            if(*p==*q)
                flag=false;
        }
        if(flag)
            src->push_back(*p);
    }     
}

void vectorAND(vector<int>* src, vector<int>* dest){
    vector<int>::iterator p,q;
    for(p=src->begin();p!=src->end();p++){
        bool flag = true;
        for(q=dest->begin();q!=dest->end();q++){
            if(*p==*q){
                flag=false;
                break;
            }
        }
        if(flag){
            src->erase(p,p+1);
            p--;
        }
    }
}

vector<int> dp[16][123];
int main(){
    int L,D,N;
    scanf("%d%d%d",&L,&D,&N);
    char word[L+1],pattern[256],ans[500][20];
    
    for(int i=0;i<D;i++){
        scanf("%s",word);
        for(int j=0;j<L;j++){
            dp[j][word[j]].push_back(i);   
        }
    }
    
    for(int i=0;i<N;i++){
        scanf("%s",pattern);
        vector<int> tmp1;
        int len=0;
        for(int j=0;j<strlen(pattern);j++){
            if(pattern[j]=='('){
                vector<int> tmp2;
                j++;
                while(pattern[j]!=')'){   
                    vectorOR(&tmp2,&dp[len][pattern[j]]);
                    j++;
                }
                if(len==0)
                    vectorOR(&tmp1,&tmp2);
                else
                    vectorAND(&tmp1,&tmp2);
            }else{
                if(len==0)
                    vectorOR(&tmp1,&dp[len][pattern[j]]); 
                else
                    vectorAND(&tmp1,&dp[len][pattern[j]]);
            }
            if(tmp1.size()==0)
                break;            
            len++;            
        }
        sprintf(ans[i],"Case #%d: %d\n",i+1,tmp1.size());
    } 
    
    for(int i=0;i<N;i++)
        printf("%s",ans[i]);
    system("pause");
}

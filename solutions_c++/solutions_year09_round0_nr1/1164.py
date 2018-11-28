#include <stdio.h>
#include <list>
using namespace std;

char temp[500];
char dict[5001][17];
bool c[27];
void setFalse(){
    int i;
    for(i=0;i<26;i++)
        c[i]=false;
}    
int main(){
    list <int> index;
    list <int>::iterator it;
    int l,d,n, i, j, k, word;
    /*for(i=0;i<10;i++)
        index.push_back(i);
    for(it=index.begin();it!=index.end();it++)
        printf("%d\n", (*it));*/
    scanf("%d %d %d", &l, &d, &n);
    for(i=0;i<d;i++)
        scanf("%s", dict[i]);
    for(i=0;i<n;i++){
        index.clear();
        for(j=0;j<d;j++)
            index.push_back(j);

        scanf("%s", temp);
        for(j=0,k=0;temp[j]!='\0';j++){
            setFalse();
            if(temp[j]=='('){
                //printf("set true: ");
                while(temp[++j]!=')'){
                    c[temp[j]-'a']=true;
                    //printf("%c ", temp[j]);
                }
                //printf("\n");     
            }    
            else{
                c[temp[j]-'a']=true;
                //printf("set true: %c\n", temp[j]);
            }    
            for(it=index.begin();it!=index.end();){
                if(!c[dict[(*it)][k]-'a'])
                    it=index.erase(it);
                else
                    it++;
            }
            /*for(it=index.begin();it!=index.end();it++)
                printf("%d, ", *it);            
            printf("\n");/**/
            k++;                    
        }    
        printf("Case #%d: %d\n", i+1, index.size());
    }    
    return 0;
}    

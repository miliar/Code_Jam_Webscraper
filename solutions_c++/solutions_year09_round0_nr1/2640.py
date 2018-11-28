#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char list[5000][12],list2[16][30],tmp[20],input[1000];
int total;

struct node{
       node *next[26];
       node (){
            int i;
            for (i=0;i<26;i++)next[i] = NULL;
       }
};

struct tree{
       node *root;
       tree (){
            node *n;
            n = new node();
            root = n;
       }
       void insert(char c[]){
            node *tmp, *tmp2;
            int i;
            tmp = root;
            for (i=0;i<strlen(c);i++){
                if (tmp->next[c[i]-'a'] == NULL){
                   tmp2 = new node();
                   tmp->next[c[i]-'a'] = tmp2;
                }
                tmp = tmp->next[c[i]-'a'];
            }
       }
};

void find(int l,int d,node *t){
     if (d == l){
        total++;
     }
     else {
          int i;
          for (i=0;i<strlen(list2[d]);i++){
              if (t->next[list2[d][i] - 'a'] != NULL){
                 find(l,d+1,t->next[list2[d][i] - 'a']);
              }
          }
     }
}

int main (){
    int l,d,n,i,j,k,m,o,p;
    tree *t;
    
    t = new tree();
    fgets(input,1000,stdin);
    input[strlen(input)-1]='\0';
    sscanf(input,"%d %d %d",&l,&d,&n);
    for (i=0;i<d;i++){
        fgets(input,1000,stdin);
        input[strlen(input)-1]='\0';
        t->insert(input);
    }
    for (i=0;i<n;i++){
        fgets(input,1000,stdin);
        input[strlen(input)-1]='\0';
        m=0;
        k=0;j=0;p=0;
        for (j=0;j<strlen(input);j++){
            if (input[j] == '(' || input[j] == ')'){
               p++;
               p = p % 2;
               if (input[j] == ')'){
                  list2[k][m] = '\0';
                  k++;
                  m=0;
               }
            }
            else if (p == 0){
                 list2[k][0] = input[j];
                 list2[k][1] = '\0';
                 k++;
                 m=0;
            }
            else if (p == 1){
                 list2[k][m] = input[j];
                 m++;
            }
        }
        total=0;
        find(l,0,t->root);
        printf("Case #%d: %d\n",i+1,total);
    }
    
    while (getchar()!=EOF);
    return 0;
}

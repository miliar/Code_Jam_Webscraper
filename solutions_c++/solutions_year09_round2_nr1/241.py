#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctype.h>
struct node {
    char s[200];
    double f;
    struct node *left,*right;
}t[1000];
int used ;
char s[10000];

node * creat(int i)
{
    node *T = &t[++used];
    T->f = atof(s+i);
    while(isdigit(s[i]) || s[i]=='.') i++;
    if(s[i] == ')')
        T->left = T->right =NULL;
    else {
        int j = 0;
        while(isalpha(s[i])){
            T->s[j] = s[i];
            i++,j++;
        }
        T->s [j] = '\0';
        T->left = creat(i+1);
        int p = 1;
        while(p){
            i++;
            if(s[i] == ')') p --;
            else if(s[i] == '(') p++;
        }
        T->right = creat(i+2);
    }
    return T;
}

void clear()
{
    int i,j;
    i = j = 0;
    while(s[i]) {
        if(isalnum(s[i]) || s[i] =='(' || s[i]==')' ||s[i] =='.'){
            s[j] = s[i];
            j ++;
        }
        i++;
    }
    s[j] = '\0';
}

node * input()
{
    int n;
    scanf("%d\n",&n);
    int len = 0;
    for(int k=0;k<n;k++){
        gets(s+len);
        while(s[len]) len++;
    }
    clear();
    return creat(1);
}

void search(node * tree)
{
    int n;
    char animal[100],ch[100][100];
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        scanf("%s",animal);
        int k = 0;
        scanf("%d",&k);
        for(int j=0;j<k;j++){
            scanf("%s",ch[j]);
        }
        node *T = tree ;
        double f = 1;
        while(T){
            f = T->f * f;
            bool find = false ;
            for(int j=0;j<k && !find;j++)if(strcmp(T->s,ch[j])==0){
                find = true;
            }
            if(find) T= T->left;
            else T= T->right;
        }
        printf("%.7lf\n",f);
    }
}
int main()
{
    int T;
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    node * tree;
    scanf("%d",&T);
    for(int t=1;t<=T;t++){
        used = 0;
        tree = input();
        printf("Case #%d:\n",t);
        search(tree);
    }
}

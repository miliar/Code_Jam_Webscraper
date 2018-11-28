
#include<iostream>
#include<cstring>
#include<ctime>
#include<cstdlib>
#include<map>
using namespace std;

struct SNode
{
    double w;
    char cute[20];
    SNode *left,*right;
};

int K;

void  creat(SNode * &root)
{

    char in[100];
    K--;
    gets(in);
    int i=0;

          root=new SNode; 
          root->cute[0]='\0';
         for(; in[i];i++)if(in[i]==')')break;
         if( in[i]){
                sscanf(in," (%lf)",&root->w);
         }
         else{
             sscanf(in," (%lf %s",&root->w,root->cute);
            creat(root->left);
             creat(root->right);
            gets(in);

         }

}

char A[110][20];
   int N,M;





double dfs(SNode *root)
{

    if(root->cute[0]=='\0')return root->w;

    for(int i=0;i<M;i++)
        if(strcmp(root->cute,A[i])==0){
            return root->w*dfs(root->left);
        }

     return root->w*dfs(root->right);


}




int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    int C=1;

    while(T--){
        SNode *root;
        scanf("%d",&K);getchar();

        creat(root);
        char tmp[200];
//        while(--K>=0)gets(tmp);
        printf("Case #%d:\n",C);
        C++;
        scanf("%d",&N);
        for(int i=0;i<N;i++){
            scanf("%s %d",A[0],&M);
            for(int j=0;j<M;j++)scanf("%s",A[j]);
//            printf("***");
            printf("%.6lf\n",dfs(root));
        }
    }
}











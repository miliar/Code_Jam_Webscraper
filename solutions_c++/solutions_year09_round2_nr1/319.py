#include <stdio.h>
#include <string>
#include <iostream>
using namespace std;

struct Tree
{
       double prob;
       string property;
       int left, right;
       Tree() {property=""; left = -1, right = -1; prob = -1;}
} nodes[100*80];

int table[100*80];
int cnt;

int n;
string F[100];

double dfs(int k)
{
     //cout << "k" << k << endl;
     if (nodes[k].left == -1) return nodes[k].prob;
     
     bool flag = 0;
     for (int i = 0; i < n; i++) if (nodes[k].property == F[i]) {flag = 1; break; }
     if (flag) return nodes[k].prob*dfs(nodes[k].left);
     else return nodes[k].prob*dfs(nodes[k].right);
}

int buildTree()
{
    nodes[cnt] = Tree();
    int save = cnt++;
    
    
    bool left = 1;
    while (1)
    {
          //aa++;
          //if (aa==20) exit(0);
   
          char c;
          scanf("%c", &c);
          //printf("%c\n", c);
          
          if (c == ')') return save;
          
          if (c >= 'a' && c <= 'z') nodes[save].property+=c;
          else if (c == '1' && nodes[save].prob == -1) nodes[save].prob = 1;
          else if (c == '0' && nodes[save].prob == -1) scanf("%lf", &nodes[save].prob);//, printf("%lf\n", nodes[save].prob);
          else if (c == '(')
          {
               if (left) nodes[save].left = buildTree(), left = 0;
               else nodes[save].right = buildTree();
          }
    }
    return -1;
}

int main()
{
    int T;
    scanf("%d\n", &T);
    for (int qqq = 0; qqq < T; qqq++)
    {
        //printf("%d\n", qqq);
        int qq;
        scanf("%d", &qq);
        
        memset(table, -1, sizeof(table));
        cnt = 0;
        char c;
        while (1)
        {
              scanf("%c", &c);
              if (c == '(') { buildTree(); break; }
        }
        
        int N;
        scanf("%d\n", &N);

        printf("Case #%d:\n", qqq+1);
        for (int i = 0; i < N; i++)
        {
            char ss[11];
            scanf("%s", ss);
            scanf("%d", &n);
            
            for (int j = 0; j < n; j++)
             cin >> F[j];
             
            printf("%.10lf\n", dfs(0));
        }
    }
}

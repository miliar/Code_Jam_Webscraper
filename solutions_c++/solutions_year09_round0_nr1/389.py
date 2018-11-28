/*
Program:
Author: ldl
Method:
DataStructure:
Date: 2009-7-16
Status:
Remark:
*/
#include<iostream>
#include<algorithm>
#include<queue>
#include<cstring>
#include<string>

using namespace std;

#define MaxSize 26 

struct TreeNode
{
    bool flag;
    TreeNode *next[MaxSize];
    TreeNode()
    {
        for (int i = 0; i < MaxSize ; i++)
            next[i] = NULL;
        flag = false;
    }
    void insert(char *word);
}root;

void TreeNode::insert(char *word)
{
    TreeNode * loca = this;
    while (*word)
    {
        int k = *word - 'a';
        if (!loca->next[k]) loca->next[k] = new TreeNode();
        loca = loca->next[k];
        word++;
    }
    loca->flag = true;
}

int L,D,N,ans,now,next;
char x[100];
char s[100000];
bool can[30];
queue<TreeNode *> q[2];

void work()
{
    while (!q[now].empty())
    {
        TreeNode* cur = q[now].front();
        q[now].pop();
        for (int i = 0; i < 26 ; i++)
        if (can[i])
        {
           TreeNode* ret = cur->next[i];
           if (ret)
           {
               if (ret->flag) ans++;
                 else q[next].push(ret);
           }
        }
    }
}

void solve()
{
     scanf("%s", s);
     int len = strlen(s);
     ans = 0;
     int i = 0;
     now = 0, next = 1; 
     while (!q[0].empty()) q[0].pop();
     while (!q[1].empty()) q[1].pop();
     q[now].push(&root);
     while (i < len)
     {
         memset(can,false,sizeof(can));
         if (s[i] == '(')
         {
             int j = i + 1;
             while (j < len && s[j] != ')')
                can[s[j++] - 'a'] = true;
             i = j;
         } else can[s[i] - 'a'] = true; 
         work();
         swap<int>(now,next);
         i++;
     }
}

void init()
{
    scanf("%d%d%d", &L , &D , &N);
    for (int i = 0; i < D ; i++)
    {
        scanf("%s", x);
        root.insert(x);
    }
}

int main()
{
//    freopen("test.in","r",stdin);
//    freopen("test.out","w",stdout);
    init();     
    for (int i = 1; i <= N ; i++)
    {
        printf("Case #%d: ",i);
        solve();
        printf("%d\n", ans);
    }
    return 0;
}


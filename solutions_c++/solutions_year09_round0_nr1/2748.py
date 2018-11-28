#include<iostream>
#include<cstdio>
#include<string>
#include<vector>
using namespace std;
struct node{
       node*next[26];
};
node *root =new node;
int l,d,n;
int cnt=0;
vector<char> v[20];
void init(node *t)
{
     for(int i=0;i<26;i++)t->next[i]=NULL;
}
void insert(string s)
{
     node *cur=root;
     for(int i=0;i<s.size();i++)
     {
       int d=s[i]-'a';
       if(cur->next[d]==NULL)
       {
         cur->next[d]=new node;
         init(cur->next[d]);
       }
       cur=cur->next[d];
     }
}
        
void get(int k)//v[k]
{
     
      char ch;
      l1:scanf("%c",&ch);
      //printf("here:%c",ch);
      if(ch!='('&&!(ch>='a'&&ch<='z'))goto l1;
      if(ch=='(')
      {
         scanf("%c",&ch);
         while(ch!=')')
         {
            v[k].push_back(ch);
            scanf("%c",&ch);
         }
      }
      else v[k].push_back(ch);
} 
void cal(node *p,int k)
{
      if(k==l)
      {
          cnt++;
      }
      else
      {
        for(int i=0;i<v[k].size();i++)
        {
           int d=v[k][i]-'a';
           if(p->next[d])cal(p->next[d],k+1);
        }
      }
}    
int main()
{
   freopen("A-small-attempt2.in","r",stdin);
    freopen("out.txt","w+",stdout);
      cin>>l>>d>>n;
      init(root);
      for(int i=0;i<d;i++)
      {
         string str;
         cin>>str;
         insert(str);
      }
      for(int i=0;i<n;i++)
      {  
         for(int j=0;j<l;j++)v[j].clear();
         for(int j=0;j<l;j++)get(j);
        /* for(int j=0;j<l;j++)
         {
           for(int f=0;f<v[j].size();f++)printf("%c ",v[j][f]);
           printf("\n");
         }*/
         cnt=0;
         cal(root,0);
         printf("Case #%d: %d\n",i+1,cnt);
      }
      return 0;
    }
      
         
      
      
      
      

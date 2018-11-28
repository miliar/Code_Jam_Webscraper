#include<cstdio>
#include<vector>
#include<string>
using namespace std;

typedef float num;

struct node
{
 num p;
 string fet;
 node * y;
 node * n;
};

void readtree(node * a)
{
 char trash;
 a->y=NULL;
 a->n=NULL;
 do {scanf("%c", &trash);} while(trash!='(');
  /*printf("D%cD", trash);*/
 scanf("%f", &a->p);
  /*printf("D%fD", a->p);*/
 do { scanf("%c", &trash); /*printf("D%cD", trash);*/} while(trash!=')' && !(trash>='a' && trash<='z'));
 if(trash==')') return;
 do { a->fet+=trash; scanf("%c", &trash); /* printf("D%cD\n", trash); */} while(trash>='a' && trash<='z');
 a->y=new node;
 readtree(a->y);
 a->n=new node;
 readtree(a->n);
 do {scanf("%c", &trash);} while(trash!=')');
}

void printtree(node * a)
{
 printf("%f", a->p);
 if(a->y != NULL && a->n != NULL)
 {
  printf("(%s?", a->fet.c_str());
   printtree(a->y);
  printf(":");
   printtree(a->n);
  printf(")");
 }
}

node * root;

int main()
{
 int t,l,a,n;
 bool has;
 num p;
 node * act;
 char lol[20];
 string str;
 vector<string> ani[101];
 scanf("%d", &t);
 for(int q=0;q<t;++q)
 {
  for(int k=0;k<101;++k) ani[k].clear();
  root=new node;
  scanf("%d", &l);
  readtree(root);
  // printtree(root);
  scanf("%d", &a);
  for(int i=0;i<a;++i)
  {
   scanf("%s", &lol);
   scanf("%d", &n);
   for(int j=0;j<n;++j)
   {
    scanf("%s", &lol);
    ani[i].push_back(lol);
   }
  }
  // for(int i=0;i<a;++i) { for(int j=0;j<ani[i].size();++j) printf("^%s$", ani[i][j].c_str()); printf("\n"); }
  printf("Case #%d:\n",q+1);
  for(int i=0;i<a;++i)
  {
   act=root;
   p=1;
   while(true)
   {
    p*=act->p;
    if(act->fet.empty()) break;
    has=0;
    for(int j=0;j<ani[i].size();++j)  if(ani[i][j]==act->fet) {has=1; break;}
    if(has) act=act->y;
    else act=act->n;
   }
   printf("%f\n", p);
  }
 }
}

#include <iostream>
#include <cstdio>
#include <string>

using std::cout ;

struct trie {
  trie *next[26];
  int v;       
} *root;

int l,d,n,cases=0;
char S[5000];
int add(char t[]){
 int i ;
 trie *tmp =root;
 for(i=0;t[i];i++){
   if(tmp->next[t[i]-'a']==NULL){
     tmp->next[t[i]-'a']=new trie;
     memset(tmp->next[t[i]-'a']->next,0,sizeof(tmp->next[t[i]-'a']->next));
     tmp->next[t[i]-'a']->v=0;                              
   }                
   tmp=tmp->next[t[i]-'a'];
   if(!t[i+1])
   tmp->v=1;
 }   
}
int input (){
 int i ;
 char STR[50];
 root = new trie ;
 memset(root->next,0,sizeof(root->next));
 root->v=0;
 for(i=0;i<d;i++){
   scanf("%s",STR);
   add(STR);                 
 }
}
int go(int lv,trie *t){
 if(!S[lv])
 return 1;
 int i,ans=0 ;
 int CHA[26]={0};
 if(S[lv]=='('){
   lv++;
   while(S[lv]!=')')
   CHA[S[lv]-'a']=1,lv++;
   lv++;               
 }
 else 
 CHA[S[lv]-'a']=1,lv++;
 for(i=0;i<26;i++)
   if(CHA[i]&&t->next[i]){
   ans+=go(lv,t->next[i]);             
   }
  return ans;
}
int sol(){
 gets(S);
 int i ,ans;
 for(i=0;i<n;i++){
   ans=0;
   gets(S);
   ans+=go(0,root);   
 cases++;
 printf("Case #%d: %d\n",cases,ans);              
 } 

}
int main (){
 while(scanf("%d %d %d",&l,&d,&n)==3){
   input();
   sol();                
 }   
}

/*
PROB: problemA
CONT: google code jam qualification 2009
KEYW: trie
*/

#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct node
{
 int words;
 int have['z'-'a'+2];
 node() { memset(have,-1,sizeof(have)); words=0; }      
};

int l,d,n,res;
int ts=1;
vector<node> trie;
string t;
int sizet;
int next[1001];

void addWord(int index,int pos)
{
 if(pos==l) { trie[index].words++; return; }
 
 if(trie[index].have[t[pos]-'a']!=-1) { addWord(trie[index].have[t[pos]-'a'],pos+1); }
 else { trie.push_back(node()); trie[index].have[t[pos]-'a']=ts; ts++;  addWord(trie[index].have[t[pos]-'a'],pos+1); }
}

void countWords(int index,int pos)
{
 if(pos==sizet) { res+=trie[index].words; return; }
 
 if(next[pos]==0) {
                    if(trie[index].have[t[pos]-'a']!=-1) countWords(trie[index].have[t[pos]-'a'],pos+1);              
                  }
 else
   {
    for(int k=pos+1;k<next[pos]-1;k++)
       if(trie[index].have[t[k]-'a']!=-1) countWords(trie[index].have[t[k]-'a'],next[pos]);              
   }  
}

int main()
{
 trie.push_back(node());
 scanf("%d %d %d",&l,&d,&n);
 
 int i,j,last;
 for(i=0;i<d;i++)
   { cin>>t; addWord(0,0); }
 
 for(i=0;i<n;i++)
   {
    cin>>t; sizet=t.size();
    
    for(j=0;j<sizet;j++)
       {
        if(t[j]!='(' && t[j]!=')') next[j]=0;
        if(t[j]=='(') last=j;
        if(t[j]==')') { next[j]=-1; next[last]=j+1; }                 
       }
    
    res=0;
    countWords(0,0);
    printf("Case #%d: %d\n",i+1,res);
   }
 
 //system("pause");
 return 0;   
}

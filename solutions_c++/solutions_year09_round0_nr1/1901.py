#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>

using namespace std;

int L, D, T;

char str[5001][20];

typedef struct trie Trie;


struct trie{
    trie(){
        mp.clear();
    }
    map<char,Trie> mp;
};

Trie t;

int cnt=0;

void insert(char *s,int len){
    Trie *Next=&t;
    for(int i=0;i<len;i++){
        if(Next->mp.count(s[i])){
            Next=&(Next->mp[s[i]]);
        }
        else{
            Next->mp[s[i]]=Trie();
            Next=&(Next->mp[s[i]]);
            cnt++;
        }
    }
}

string pattern;
int pLen;
int result=0;

void solve(int index, Trie *t) {
 if(index==pLen) {
   result++;
   return ;
 }
 char chars[50];
 int i=0;
 if(pattern[index]=='(') {
   index++;
   while(pattern[index]!=')') {
     chars[i++]=pattern[index++];
   }
 } else {
  chars[i++]=pattern[index];
 }
 for(int j=0;j<i;j++) {
   if(t->mp.count(chars[j])) {
    solve(index+1, &(t->mp[chars[j]]));
   }
 }
}

int main() {
  cin>>L>>D>>T;
  t = Trie();
  for(int i=0;i<D;i++) {
    scanf("%s",str[i]);
    insert(str[i], L);
  }
  for(int i=0;i<T;i++) {
    cin>>pattern;
    result=0;
    pLen=pattern.length();
    solve(0,&t);
    printf("Case #%d: %d\n", (i+1), result);
  }
}
#include<iostream>
#include<string>
#include<vector>
using namespace std;
struct node{
       bool exist;
       node* a[26];
       node(){
              exist=0;
              memset(a,0,sizeof(a));
              }
       };
node* head;
int l,d,n;
vector<char> b[20];
string r;
char t[20];
int ans;
void insert(char str[]){
     int i;
     node* temp=head;
     for(i=0;i<l;i++){
                      if(temp->a[str[i]-'a']==0)temp->a[str[i]-'a']=new node();
                      temp=temp->a[str[i]-'a'];
                      }
     temp->exist=true;
     }
int find(char str[],int l1){
     int i;
     node* temp=head;
     for(i=0;i<l1;i++){
                      if(temp->a[str[i]-'a']==0)return -1;
                      temp=temp->a[str[i]-'a'];
                      }
     if(temp->exist)return 1;
     return 0;
     }
void del(node* temp){
     int i;
     for(i=0;i<26;i++){
                       if(temp->a[i]!=0)del(temp->a[i]);
                       }
     delete temp;
     }
void dfs(int i){
     if(i>=l){
              if(find(t,l)==1)ans++;
              return ;
              }
     int j;
     int l1=b[i].size();
     for(j=0;j<l1;j++){
                      t[i]=b[i][j];
                      int k=find(t,i+1);
                      if(k!=-1)dfs(i+1);
                      }
     }
int solve(){
     int i;
     int k=0;
     int l1=r.size();
     bool p=false;
     for(i=0;i<l;i++)b[i].clear();
     for(i=0;i<l1;i++){
                      if(r[i]=='(')p=true;
                      else {
                           if(r[i]!=')'){
                                         if(p)b[k].push_back(r[i]);
                                         else b[k++].push_back(r[i]);
                                         }
                           else {
                                p=false;
                                k++;
                                }
                           }
                      }
     ans=0;
     dfs(0);
     return ans;
     }
int main(){
    head=new node();
    scanf("%d%d%d",&l,&d,&n);
    char str[30];
    int i;
    for(i=0;i<d;i++){
                     scanf("%s",str);
                     insert(str);
                     }
    int count=1;
    for(i=0;i<n;i++){
                     cin>>r;
                     printf("Case #%d: %d\n",count,solve());
                     count++;
                     }
    del(head);
    return 0;
}

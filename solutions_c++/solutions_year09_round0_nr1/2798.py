#include<iostream>
#include<cstring>
using namespace std;
struct steven
{
 int sum;       
 int child[26];      
}trie[2000000];

int sum1,all;
char str[200000];
char helloworld[20][26];
int top[20];
int N,l;
char substr[2000];


void buildTrie(int num,int now,int len)
{
 trie[num].sum++;
 if(now==len)return;
 if(trie[num].child[str[now+1]-'a']==0)     
 {
  trie[num].child[str[now+1]-'a']=N;
  trie[N].sum=0;
  for(int i=0;i<26;i++)
   trie[N].child[i]=0;
  N++;                                           
 }
 buildTrie(trie[num].child[str[now+1]-'a'],now+1,len);    
}

int findTrie(int num,int now,int len)
{
     if(now==len-1)return trie[num].sum;
     if(trie[num].child[substr[now+1]-'a']==0)return 0;
     return findTrie(trie[num].child[substr[now+1]-'a'],now+1,len);
}

void dfs(int now)
{
   int i;
   if(now==l)
   {
    all+=findTrie(substr[0]-'a',0,l);
    return ;          
   }
   for(i=0;i<top[now];i++)
   {
    substr[now]=helloworld[now][i];
    if(findTrie(substr[0]-'a',0,now+1)!=0)
      dfs(now+1);
   }   
}


int main()
{
   // freopen("a.in","r",stdin);
  //  freopen("a.out","w",stdout);
    int d,n;
    int i,j,k;
    int cc=1;
    N=26;
    scanf("%d%d%d",&l,&d,&n);
    
    for(i=0;i<26;i++)
    {
     trie[i].sum=0;
     for(j=0;j<26;j++)
      trie[i].child[j]=0;                 
    }
    
    for(k=0;k<d;k++)
    {
      cin>>str;
      buildTrie(str[0]-'a',0,l);              
    }
    
    
   // cout<<l<<" "<<d<<" "<<n<<endl;
    while(n--)
    {
       //cout<<"asdf"<<endl;
       cin>>str;
       int num=0;
       for(i=0;i<l;i++)
         top[i]=0;
       for(i=0;i<strlen(str);i++)
       {
        if(str[i]=='(')
        {
          i++;
          int len=0;
          while(str[i]!=')')
          {
           helloworld[num][len++]=str[i]; 
           i++;                 
          }
          top[num]=len;
          num++;        
        }
        else if(str[i]>='a'&&str[i]<='z')
        {
         helloworld[num][0]=str[i];
         top[num]=1;
         num++;    
        }                                     
       }  
       /*for(i=0;i<num;i++)
       {
        for(j=0;j<top[i];j++)
           printf("%c ",helloworld[i][j]);
        printf("\n");                  
       } */
       all=0;
       dfs(0);
       printf("Case #%d: %d\n",cc++,all);     
    }
    return 0;    
}

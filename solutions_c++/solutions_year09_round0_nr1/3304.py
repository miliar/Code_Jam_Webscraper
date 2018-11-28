#include<iostream>
#include<cstring>
//#include<fstream>
using namespace std;

int len,cnt;
int n,l,d;
bool flag;
char list[5010][20],str[2000],tmp[2000];
/*void cmpare(char *tmp1)
{  
     tmp1[strlen(tmp1)]='\0';
     int len1=strlen(tmp1);
     for(int k=1;k<=d;k++)
     {
        if(l!=len1)continue; 
        if (strcmp(tmp1,list[k])==0)cnt++;
     }
 }*/
bool cheak(char *tmp1,int j)
{
     for(int k=1;k<=d;k++){
             for(int i=0;i<=j;i++){
             if(list[k][i]!=tmp1[i])
             break;
             if(i==j) return 1;}
             }
      return 0; 
 }
void dfs(int i,int j)
{
     int start=i,end=-1;
     if((i+1)==len)//注意一个字符情况，还没解决 
     {
               cnt++;
                return ;   
     }
     //没有括号的字符 
     //if(i!=0&&str[i+1]!='('&&str[i]!='('&&str[i]!=')')
     /*if(i!=0&&str[i+1]!='('&&str[i]!='(') 
     {
        for(;i<len;i++)
        if(str[i]=='(')
        {start=i-1;}
        else
        {
             tmp[j++]=str[i];
             if(!cheak(tmp,j-1)){
             return ;}
        }
        dfs(i,j);
        return ;
     }*/
    // printf("%d\n",i);
      if(i!=0&&str[i+1]!='('&&str[i]==')') 
     {
        i++;
        for(;i<len;i++)
        if(str[i]=='(')
        {break;}
        else
        {
             tmp[j++]=str[i];
             if(!cheak(tmp,j-1)){
             return ;}
        }
        //printf("%d\n",i);
        if(i==len){dfs(i-1,j);}
        
        else dfs(i-1,j);
        return ;
     }
    
     //扫描下一个’)' ,确定将要枚举的范围 
     for(i=start+1;i<len;i++)
     {
        if(str[i]==')'){
        end=i;
        break;
        }
     }
     if(end==-1)
     {
        for(i=start+1;i<len;i++)
        {
         tmp[j++]=str[i];
         if(!cheak(tmp,j-1)){return ;}
         }
         cnt++;
     }
     if(str[start-1]==')') i=start+1;
     else i=start+2;
     if(str[start]=='(')i=start+1; 
     for(;i<end;i++)//()范围内枚举 
     {
         tmp[j]=str[i];
         if(cheak(tmp,j)){
          dfs(end,j+1);
         }
     }
 }
 
int main()
{
    //freopen("out.txt","w",stdout);
    while(scanf("%d%d%d",&l,&d,&n)!=EOF)
    {
        int i,j;
        getchar();
        for(i=1;i<=d;i++){
        scanf("%s",&list[i]);
        }
        int t=0;
        while(n--)
        {
            flag=true;
           scanf("%s",&str);
           len=strlen(str);
           cnt=0;
          i=0,j=0;
             if(str[0]!='(') //第一个位置不为'(' 
             {
               for(i=0,j=0;i<len;i++)
               if(str[i]=='(')
               break;
               else 
               {
                    tmp[j++]=str[i];
                    if(!cheak(tmp,j-1)) {flag=false;break;}
                }
             }
             //printf("%s\n",tmp);
             if(i==len)i--;
          if(flag)
          dfs(i,j);//j表示空位 
           t++;
           printf("Case #%d: %d\n",t,cnt);
        }
    }
    return 0;
}
 

#include<stdio.h>
#include<vector>
#include<iostream>
#include<map>
#include<utility>
#include<string>
#include<conio.h>
using namespace std;

int t=1,tests,c,d,n,i,k;

int main()
{
    freopen("B-small-attempt2.in","r",stdin);
    freopen("magicka_third.out","w",stdout);    
    scanf("%d\n",&tests);
    while(t<=tests)
    {
        scanf("%d ",&c);
        map<char,char> opp;
        map<pair<char,char>,char> comb;
        map<char,int> present;        
        for(i=0;i<c;i++)
        {
            char temp[5];
            scanf("%s ",temp);            
            comb[make_pair(temp[0],temp[1])]=temp[2];
            comb[make_pair(temp[1],temp[0])]=temp[2];            
        }
        scanf("%d ",&d);
        for(i=0;i<d;i++)
        {
            char temp[5];
            scanf("%s ",temp);
            opp[temp[0]]=temp[1];
            opp[temp[1]]=temp[0];
        }
        scanf("%d ",&n);
        char str[120];     
        string ans;   
        gets(str);
        i=0;
        k=0;                
        ans.resize(n);        
        while(i<n)
        {             
             ans[k]=str[i];             
             if(k>0)
             {
                  if(comb[make_pair(ans[k-1],ans[k])]!='\0')
                  {                                             
                       //printf("comb\n");
                       if(present[ans[k]]!=0){present[ans[k]]--;}
                       if(present[ans[k-1]]!=0){present[ans[k-1]]--;}
                       ans[k-1]=comb[make_pair(ans[k-1],ans[k])];                       
                       k--;
                  }                                                        
                  if(opp[ans[k]]!='\0')
                  {
                       //printf("opp\n");
                       present[ans[k]]++;
                       if(present[opp[ans[k]]]>=1)
                       {   
                           ans.clear();
                           present.clear();                           
                           k=-1;
                       }
                  }
             }
             else
             {
                 if(opp[ans[k]]!='\0')
                 {present[ans[k]]++;}
             }
             //printf("%s\n",ans.c_str());
             k++;
             i++;
        }        
        ans[k]='\0';
        printf("Case #%d: [",t);        
        if(ans[0]!='\0')
        {
            printf("%c",ans[0]);
            i=1;
            while(ans[i]!='\0')
            {
                printf(", %c",ans[i]);
                i++;
            }
        }
        printf("]\n");              
        t++;
    }
    getch();
}  
        
        

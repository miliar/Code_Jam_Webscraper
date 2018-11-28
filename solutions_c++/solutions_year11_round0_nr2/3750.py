#include<iostream>
#include<fstream>
using namespace std;
int check(char t)
{
    if(t=='O')return 0;
    else return 1;
}
#define M ((1<<32)-1)
int main()
{
    fstream  fout;
    fout.open("1.txt",ios::out);
    int cas,N,l,i,j;
    char words[5];
    int link[26][26];
    char combin[26][26];
    char now[110];
    cin>>cas;
    for(l=1;l<=cas;l++)
    {
               fout<<"Case #"<<l<<": ";
             // cout<<"Case #"<<l<<": ";
               cin>>N;
               for(i=0;i<26;i++)
               for(j=0;j<26;j++){combin[i][j]='\0';link[i][j]=0;}
               for(i=0;i<N;i++)
               {
                               cin>>words;
                               combin[*words-'A'][*(words+1)-'A']=words[2];
                               combin[*(words+1)-'A'][*words-'A']=words[2];
                               }
               cin>>N;
               for(i=0;i<N;i++)
               {
                               cin>>words;
                               link[words[0]-'A'][words[1]-'A']=1;
                               link[words[1]-'A'][words[0]-'A']=1;
                               }
                               
               cin>>N>>now;
               char p[110],*x=now;
               p[0]=now[0];
               x++;
               int len=1;
               while(*x!='\0')
               {
                              if(len==0){p[0]=*x;len=1;}
                              else if(combin[p[len-1]-'A'][*x-'A']!='\0')
                                       p[len-1]=combin[p[len-1]-'A'][*x-'A'];
                              else
                              {
                                    for(i=0;i<len;i++)
                                    {
                                                      if(link[p[i]-'A'][*x-'A']!=0)
                                                              len=0;
                                                      }
                                    if(len>0)
                                    {
                                             p[len++]=*x;
                                             }
                             }
                             x++;
                             }
               if(len==0)fout<<"[]\n";
               else if(len==1)fout<<"["<<p[0]<<"]\n";
               else 
               {
                    fout<<'[';//cout<<'[';
                    for(i=0;i<len-1;i++){fout<<p[i]<<", "; }//cout<<p[i]<<", ";}
                    fout<<p[len-1]<<"]\n";//cout<<p[len-1]<<"]\n";
               }                
             //  cout<<"Case #"<<l<<": "<<res<<endl;
    }
    fout.close();
   // cin>>i;
    return 0;
    
}
 

#include<cstdlib>
#include<iostream>
#include<string>
using namespace std;

int main()
{
    FILE *fp;
    fp=fopen("A-small-attempt0.in","r");
    string code;
    code="abcdefghijklmnopqrstuvwxyz ";
    string decode;
    decode="yhesocvxduiglbkrztnwjpfmaq ";
    char G[200];
    FILE *wfp;
    int times;
    bool lock=false;
    wfp=fopen("A-small-attempt0.out","w");
    while(!feof(fp))
    {
       if(!lock)
       {             
          fscanf(fp,"%d",&times);
          lock = true;
          fgets(G,200,fp);
       }
       while(times>0)
       {
          fgets(G,200,fp);
          cout<<G;
          fprintf(wfp,"Case #%d: ",31-times);
          for(int idx=0;G[idx]!='\n';idx++)
          {
                  int x=0;                  
                  while(x<28)
                  {
                  if(G[idx]==code[x])
                  {                  
                   fprintf(wfp,"%c",decode[x]);
                   break;
                  }
                   x++;
                  }                  
          }
          fprintf(wfp,"\n");
          for(int y=0;G[y]!='\n';y++)
          G[y]=' ';
          times--;
       }  
    }
    system("pause");
    fclose(wfp);
    fclose(fp);
    return 0;
}

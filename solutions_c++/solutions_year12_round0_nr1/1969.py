#include<stdio.h>
#include<string.h>
int n,hash[27];
char str[31][101],out[31][101];
int main()
{
    int i,j;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d\n",&n);
    memset(hash,-1,sizeof(hash));
    for(i=1;i<=n;i++)gets(str[i]);
    char a,b;
hash['e'-'a']='o';
hash['j'-'a']='u';
hash['p'-'a']='r';
hash['m'-'a']='l';
hash['y'-'a']='a';
hash['s'-'a']='n';
hash['l'-'a']='g';
hash['j'-'a']='u';
hash['c'-'a']='e';
hash['k'-'a']='i';
hash['d'-'a']='s';
hash['x'-'a']='m';
hash['v'-'a']='p';
hash['n'-'a']='b';
hash['r'-'a']='t';
hash['i'-'a']='d';
hash['b'-'a']='h';
hash['t'-'a']='w';
hash['a'-'a']='y';
hash['h'-'a']='x';
hash['w'-'a']='f';
hash['f'-'a']='c';
hash['u'-'a']='j';
hash['g'-'a']='v';
hash['o'-'a']='k';
hash['z'-'a']='q';
hash['q'-'a']='z';
      for(i=1;i<=n;i++)
        for(j=0;j<strlen(str[i]);j++)
        {
          if(str[i][j]==' ')
          {
            out[i][j]=' ';
            continue;
          }
          if(hash[str[i][j]-'a']==-1)out[i][j]='*';
          else out[i][j]=hash[str[i][j]-'a'];
        }
      for(i=1;i<=n;i++)
      {
        printf("Case #%d: ",i);
        puts(out[i]);
      }
    return 0;
}

#include<iostream>
int main()
{
    int T, C, D, N, flag[100], tos, i;
    char fuse[100][100], s[150], destroy[100], stack[110];
    scanf("%d",&T);
    for( int tc=1; tc<=T; tc++)
    {
         tos=-1;
         memset(fuse,0,sizeof(fuse));
         memset(destroy,0,sizeof(destroy));
         memset(flag,0,sizeof(flag));
         scanf("%d",&C);
         for( i=0;i<C;++i)
         {
              scanf("%s",s);
              fuse[s[0]][s[1]]=fuse[s[1]][s[0]]=s[2];
         }
         scanf("%d",&D);
         for( i=0;i<D;++i)
         {
              scanf("%s",s);
              destroy[s[0]]=s[1];
              destroy[s[1]]=s[0];
         }
         scanf("%d %s",&N,s);
         i=0;
         while( i<N)
         {
                if( tos==-1)
                {
                    stack[++tos]=s[i];
                    ++flag[s[i]];
                }
                else if( fuse[s[i]][stack[tos]]!=0)
                {
                     ++flag[fuse[s[i]][stack[tos]]];
                     --flag[stack[tos]];
                     stack[tos]= fuse[s[i]][stack[tos]];
                }
                else if( flag[destroy[s[i]]])
                {
                     memset(flag,0,sizeof(flag));
                     tos=-1;
                }
                else
                {
                    stack[++tos]=s[i];
                    ++flag[s[i]];
                }
                ++i;
         }
         printf("Case #%d: [",tc);
         for( i=0;i<tos;++i)
              printf("%c, ",stack[i]);
         if( tos!=-1)
             printf("%c",stack[tos]);
         printf("]\n");
    }
    return 0;
}

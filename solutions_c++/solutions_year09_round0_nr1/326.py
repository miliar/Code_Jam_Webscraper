#include<iostream>
using namespace std;

const int maxL = 16;
const int maxD = 5001;
const int maxN = 501;

int L,D,N;
int s[maxD][maxL];
int exist[maxL][26];

void init()
{
     scanf("%d%d%d",&L,&D,&N);
     getchar();
     for (int i=0; i<D; getchar(),i++ )
         for (int j=0; j<L; j++ ) s[i][j]=getchar()-97;
}

int match(int i )
{
     for (int j=0; j<L; j++ ) if (!exist[j][s[i][j]]) return 0;
     return 1;
}

void work()
{
     for (int i=0; i<N; getchar(),i++ )
     {
         memset(exist,0,sizeof(exist));
         int ans=0,ch;
         for (int j=0; j<L; j++ )
         {
             ch=getchar()-97;
             if (ch==-57)
                while (1)
                {
                      ch=getchar()-97;
                      if (ch==-56) break;
                      exist[j][ch]=1;
                }
             else exist[j][ch]=1;
         }
         for (int j=0; j<D; j++ ) if (match(j)) ans++;
         printf("Case #%d: %d\n",i+1,ans);
     }
     //system("pause");
}

int main()
{
    //freopen("a2.out","w",stdout);
     init();
     work();
    //fclose(stdout);
}

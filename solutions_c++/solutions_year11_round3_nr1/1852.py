#include <iostream>
#include <string>
#include<map>

using namespace std;

char t[51][51];

int T,r,c,impossible,R,C;

void print_tiles()
{
    for (int i=0; i<r; i++)
        {
            for (int j=0; j<c; j++)
            printf("%c",t[i][j]);
            printf("\n");
        }
    
    
}

int main ()
{
    scanf("%d",&T);
    int cnt=0;
    while(cnt<T)
    {
        cnt++;
        impossible=0;
        scanf("%d %d",&r,&c);
        int i=0;
        while(i<r)
        {
            cin>>t[i];
            i++;
        }
        //print_tiles();
        for (int R=0;R<r;R++)
        {
            for(int C=0; C<c; C++)
            {
                if(t[R][C]=='#')
                {
                    if(C==(c-1)||R==(r-1))
                    {
                        //printf("found %d %d\n",R,C);
                        impossible=1;
                        break;
                    }
                    else
                    {
                        //printf("checking grid %d %d\n",R,C);
                        if(t[R+1][C]=='#'&&t[R][C+1]=='#'&&t[R+1][C+1]=='#')
                        {
                            
                            t[R][C]='/';
                            t[R+1][C]='\\';
                            t[R][C+1]='\\';
                            t[R+1][C+1]='/';
                        }
                        else
                        {
                            impossible=1;
                            break;
                        }
                    }
                        
                }
                //print_tiles();
            }
            if(impossible)
                break;
        }
        printf ("Case #%d: \n", cnt);
        if(impossible)
            printf("Impossible\n");
        else
        print_tiles();
         
    }
    
    return 0;
}

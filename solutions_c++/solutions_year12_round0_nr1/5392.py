#include<cstdio>
#include<cstring>
#include<iostream>

using namespace std;

int main()
{

    freopen ("A-small-attempt2.in","r",stdin);
    freopen ("out.txt","w",stdout);

    int T,i,j,k,l,NL;
    char in[120],dummy;

    char innn[]= {"ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv"};
    char outt[]= {"ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup"};
    int iL=strlen(innn);

    scanf("%d%c",&T,&dummy);

    for(i=1; i<=T; i++)
    {
        gets(in);
        NL=strlen(in);

        for(j=0; j<NL; j++)
        {
           // cout << j <<endl;
            if(in[j] == 'q')
            {
                in[j]='z';
                continue;
            }
            if(in[j] == 'z')
            {
                in[j]='q';
                continue;
            }

            for(k=0; k<iL; k++)
            {
                //cout << k <<endl;
                if(in[j] == innn[k])
                {
                    in[j]=outt[k];
                    break;
                }
            }

        }

        //printf("Case #%d: %s\n",i,in);
        printf("Case #%d: ",i);
        puts(in);

    }
    fclose(stdin);
    fclose(stdout);

    return 0;
}

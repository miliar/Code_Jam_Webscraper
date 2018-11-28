#include<iostream>
#include<cstdio>
#include<cstdlib>
//#define MYDEBUG
using namespace std;

int check(int row[],int col[],int cor1, int cor2, int tx, int ty)
{
    for(int i=0; i<4; i++)
    {
        if(row[i]==4||(row[i]==3&&tx==i))
            return 0;
        if(row[i]==-4||(row[i]==-3&&tx==i))
            return 1;
    }
    for(int i=0; i<4; i++)
    {
        if(col[i]==4||(col[i]==3&&ty==i))
            return 0;
        if(col[i]==-4||(col[i]==-3&&ty==i))
            return 1;
    }
    if(cor1==4||(cor1==3&&tx+ty==3))
        return 0;
    if(cor1==-4||(cor1==-3&&tx+ty==3))
        return 1;
    if(cor2==4||(cor2==3&&tx==ty))
        return 0;
    if(cor2==-4||(cor2==-3&&tx==ty))
        return 1;
    return -1;
}


int main()
{
    freopen("A.in.txt","r",stdin);
    freopen("A.out.txt","w",stdout);
    int C;
    char nl;
    cin >> C;
    getchar();

    int r=0;
    while(r<C)
    {
        r++;
        string line;
        int gameR[4]={0},gameC[4]={0},cor1=0,cor2=0;
        int tx,ty;
        bool done = true;
        for(int i=0; i<4; i++)
        {
            getline(cin,line);
            for(int j=0; j<4; j++)
            {
                switch(line[j])
                {
                    case 'O':
                        gameR[i]++;
                        gameC[j]++;
                        if(i+j==3)
                            cor1++;
                        if(i==j)
                            cor2++;
                        break;
                    case 'X':
                        gameR[i]--;
                        gameC[j]--;
                        if(i+j==3)
                            cor1--;
                        if(i==j)
                            cor2--;
                        break;
                    case '.':
                        done = false;
                        break;
                    case 'T':
                        tx=i;
                        ty=j;
                        break;
                }
            }
        }
        //if(r<C)
            getline(cin,line);

        #ifdef MYDEBUG

        for(int i=0; i<4; i++)
            printf("[%2d]",gameR[i]);
        cout << endl;
        for(int i=0; i<4; i++)
            printf("[%2d]",gameC[i]);
        cout << endl;

        printf("[%2d]",cor1);
        printf("[%2d]",cor2);
        printf("[%2d]",tx);
        printf("[%2d]",ty);
        cout << endl;
        #endif

        int ans = check(gameR,gameC,cor1,cor2,tx,ty);
        //printf("%d\n",ans);
        switch(ans)
        {
            case 0:
                printf("Case #%d: O won\n",r);
                break;
            case 1:
                printf("Case #%d: X won\n",r);
                break;
            case -1:
                if(done)
                    printf("Case #%d: Draw\n",r);
                else
                    printf("Case #%d: Game has not completed\n",r);
                break;
        }

    }



}

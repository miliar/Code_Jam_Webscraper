#include<iostream>
#include<cstdio>

using namespace std;

typedef struct move
{
    char ch;
    int button;
} move;
int sign(int a)
{
    if(a<0)
        return -1;
    else
    {
       if(a==0)
         return 0;
       else return 1;
    }

}



int main()
{

    int T;
    scanf("%d",&T);
    for(int t=1;t<=T; t++)
    {
        int N;
        scanf("%d",&N);
        getchar();
        move moves[N];
        move blue[N];
        move orange[N];
        int bind=0;
        int oind=0;
        for(int i=0;i<N ;i++)
        {
            move m;
            scanf("%c%d",&m.ch,&m.button);
            getchar();
            switch(m.ch)
            {
                case 'O':
                    orange[oind++]=m;
                    break;
                case 'B':
                    blue[bind++]=m;
                    break;
            }
            moves[i]=m;
        }
        int currO=1;
        int currB=1;
        int nextO=0;
        int nextB=0;
        int j=0;
        int todo=0;
        for(;todo != N ;j++)
        {
            bool pressedO=false;
            bool pressedB=false;
            switch(moves[todo].ch)
            {
                case 'O':
                    if (currO == moves[todo].button)
                    {
                        nextO++;
                        todo++;
                        pressedO=true;
                    }

                    break;
                case 'B':
                    if(currB==moves[todo].button)
                    {
                        nextB++;
                        todo++;
                        pressedB=true;
                    }

            }
            if(nextO<oind && !pressedO)
                currO = currO + sign(orange[nextO].button - currO);
            if(nextB<bind && !pressedB)
               currB = currB + sign(blue[nextB].button - currB);
        }
        printf("Case #%d: %d\n",t, j);
    }

}

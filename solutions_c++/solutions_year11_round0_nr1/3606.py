#include<stdio.h>
#include<iostream>
#include<queue>
using namespace std;

int main()
{
    int N;
    scanf("%d",&N);

    int i;

    for(i=0; i<N ; i++ )
    {
        queue<char> order;
        queue<int> orange;
        queue<int> blue;

        int temp;
        char garbage;
        int T;
        scanf("%d",&T);

        scanf("%c",&garbage);
        int j;
        char turnOf;
        for (j=0;j<T;j++)
        {

            scanf("%c",&turnOf);
            scanf("%c",&garbage);
            order.push(turnOf);
            //printf("GOT %c\n",turnOf);
            scanf("%d",&temp);
            scanf("%c",&garbage);

            if (turnOf=='O')
            {
                orange.push(temp);
            }
            else if (turnOf=='B')
            {
                blue.push(temp);
            }
        }
        int remainder=0;
        int total=0;
        char last='N'; //USING N as null;
        int currentO=1;
        int currentB=1;
        for ( j=0;j< T ; j++)
        {
            char current=order.front();
            if( current== 'O' )
            {  
                int diff=abs(orange.front()-currentO);
                if(last=='O')
                {
                    remainder+=diff+1;
                    total+=diff+1;
                }
                else 
                {
                    int cval=0;
                    cval=diff-remainder;
                    if(cval<0)
                        cval=0;
                    total+=cval+1;
                    remainder=cval+1;
                }
                currentO=orange.front();
                orange.pop();
                last='O';

            }
            if( current== 'B' )
            {   

                int diff=abs(blue.front()-currentB);
                if(last=='B')
                {
                    remainder+=diff+1;
                    total+=diff+1;
                }
                else 
                {
                    int cval=0;
                    cval=diff-remainder;
                    if(cval<0)
                        cval=0;
                    total+=cval+1;
                    remainder=cval+1;
                }
                currentB=blue.front();
                blue.pop();
                last='B';
            }
            order.pop();

            //printf("Curent = %c, total = %d remainder= %d \n",current,total, remainder     );
        }
        printf("Case #%d: %d\n",i+1,total);
    }
    return 0;
}

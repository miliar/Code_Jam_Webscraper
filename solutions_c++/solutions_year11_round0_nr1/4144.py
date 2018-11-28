#include<iostream>
#define abs(a,b) (a)>(b)?(a)-(b):(b)-(a)
void getnum( int &x)
{
     x=0;
     char ch=getchar();
     while( ch<'0' || ch>'9')
            ch=getchar();
     while( ch>='0' && ch<='9')
     {
            x= 10*x+ ch-'0';
            ch=getchar();
     }
}
void getch( char &ch)
{
     ch=getchar();
     while( ch!='B' && ch!='O')
            ch=getchar();
}

int Blue[110], Orange[110], bp, op;
int main( int argc, char *argv[])
{
    int T, N, Bpos, Opos, button, i, time, waitsinceO, waitsinceB, j, k, move;
    char ch, turn[110];
    getnum(T);
    for( int Tcase=1;Tcase<=T;++Tcase)
    {
         getnum(N);
         Bpos=Opos=1;
         i=0;
         bp=op=0;
         while( i<N)
         {
                getch(ch);getnum(button);
                if( ch=='O')
                    Orange[++op]=button;
                else
                    Blue[++bp]=button;
                turn[i++]=ch;
         }
         turn[i]=0;
         j=k=1;
         waitsinceO=waitsinceB=0;
         time=0;
         i=-1;
         while( turn[++i]!=0)
         {
                if( turn[i]=='O')
                {
                    move = abs(Orange[j],Opos);
                    if( waitsinceO+move >  time)
                        time= move+waitsinceO+1;
                    else
                        ++time;
                    waitsinceO= time;
                    Opos=Orange[j++];    
                }
                else
                {
                    move= abs(Blue[k],Bpos);
                    if( waitsinceB+ move >  time)
                        time= move +waitsinceB+1;
                    else
                        ++time;
                    waitsinceB= time;
                    Bpos=Blue[k++];    
                }
         }
         printf("Case #%d: ",Tcase);
         printf("%d\n",time);
    }
    return 0;
}
                    

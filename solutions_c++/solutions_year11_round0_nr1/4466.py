#include <cstdio>
#include <math.h>
#include <conio.h>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
using namespace std;

int TC = 1, T, N;
int minimize(char robots[],int buttons[],int N);
int main ()
{
    std::ofstream os("text_file.txt");
    for (scanf ("%d", &T); TC <= T; TC++)
    {

        scanf ("%d", &N);
        char robots[N];
        int buttons[N];
        int button;
        char robot;
        for (int i = 0; i < N; i++)
        {
            scanf ("%s %d", &robot, &button);
            robots[i]=robot;
            buttons[i]=button;
        }
        os<<"Case #"<<TC<<": ";
        //printf ("Case #%d: ", TC);
        char ausgabe[10];
        itoa(minimize(robots,buttons,N),ausgabe,10);
        //puts (ausgabe);
        os<<ausgabe<<"\n";
    }
    
    //char robots[]="OOB";
    //int buttons[3]={5,8,100};
    //printf("%d",minimize(robots,buttons,3));
    //printf("Fertig");
    getch();
    return 0;
}

int minimize(char robots[],int buttons[],int N)
{
    bool solved=false;
    int zeit=0;
                  int nextbuttono=0;
              int nextbuttonb=0;
    int buttonpos=0;
    int positiono=1,positionb=1;
    while (!solved)
    {
          if (robots[buttonpos]=='O'&&positiono==buttons[buttonpos]){buttonpos++;for (int i=buttonpos;i<N;i++)
              {if (robots[i]=='B'){nextbuttonb=buttons[i];if (nextbuttonb>positionb)positionb++;else if (nextbuttonb<positionb)positionb--;break;}}}
          else if (robots[buttonpos]=='B'&&positionb==buttons[buttonpos]){buttonpos++;for (int i=buttonpos;i<N;i++)
              {if (robots[i]=='O'){nextbuttono=buttons[i];if (nextbuttono>positiono)positiono++;else if (nextbuttono<positiono)positiono--;break;}}}
          else
          {

              for (int i=buttonpos;i<N;i++)
              {if (robots[i]=='O'){nextbuttono=buttons[i];if (nextbuttono>positiono)positiono++;else if (nextbuttono<positiono)positiono--;break;}}
              for (int i=buttonpos;i<N;i++)
              {if (robots[i]=='B'){nextbuttonb=buttons[i];if (nextbuttonb>positionb)positionb++;else if (nextbuttonb<positionb)positionb--;break;}}
          }
          zeit++;
          //printf("Zeit %d, Position %d, Orange bei %d, Blau bei %d\n",zeit,buttonpos,positiono,positionb);getch();
          if (buttonpos==N)solved=true;
    }
    return zeit;
}

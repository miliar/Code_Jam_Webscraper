/*
Luis Eduardo Oliveira Lizardo
lizardo.luis@gmail.com
Brazil
*/

#include <stdio.h>

using namespace std;

int main()
{
    int T, N, button;
    char robot;

    scanf("%d", &T);
    for(int t=1; t<=T; t++)
    {
        int time=0, BPos=1, OPos=1, dB, dO, ltimeB=0, ltimeO=0;
        char lRobot;
        scanf("%d", &N);

        for(int i=0; i<N; i++){
            scanf(" %c %d", &robot, &button);

            if(robot == 'B'){

                if(button > BPos)
                    dB = button-BPos+1;
                else
                    dB = BPos-button+1;

                if( lRobot == 'O' ){
                    if(time-ltimeB < dB)
                        time += dB - (time-ltimeB);
                    else
                        time += 1;
                }
                else
                    time += dB;

                ltimeB = time;
                BPos = button;
                dO = 0;
                lRobot = 'B';
            }
            else{

                if(button > OPos)
                    dO = button-OPos+1;
                else
                    dO = OPos-button+1;

                if( lRobot == 'B' ){
                    if(time-ltimeO < dO)
                        time += dO - (time-ltimeO);
                    else
                        time += 1;
                }
                else
                    time += dO;

                ltimeO = time;
                OPos = button;
                dB = 0;
                lRobot = 'O';
            }
        }

        printf("Case #%d: %d\n", t, time);
    }

}

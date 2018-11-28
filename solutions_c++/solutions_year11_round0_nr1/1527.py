#include <stdio.h>
#include <stdlib.h>
#define BLUE 0
#define ORANGE 1

int taskguy[100]; //1 = Orange, 0 = Blue
int tasks[2][101]; //guarda o botão
int totaltask[2];
int currpos[2];
int currtask[2];

int main (void)
{
    int test, i,j, task, button, counter, curr;
    bool complete;
    char guy;
    scanf ("%d", &test);
    for (i = 1; i <= test; i++)
    {
        currpos[0] = currpos[1] = 1;
        counter = totaltask[0] = totaltask[1] = currtask[0] = currtask[1] = 0;
        scanf ("%d ", &task);
        for (j = 0; j < task-1; j++)
        {
            scanf ("%c%d ", &guy, &button);
            taskguy[j] = guy=='O';
            tasks[guy=='O'][totaltask[guy=='O']] = button;
            totaltask[guy=='O']++;
        }
        scanf ("%c%d", &guy, &button);
        taskguy[j] = guy=='O';
        tasks[guy=='O'][totaltask[guy=='O']] = button;
        totaltask[guy=='O']++;
        //printf ("terminou de ler\n");
        tasks[0][totaltask[0]] = tasks[0][totaltask[0]-1];
        tasks[1][totaltask[1]] = tasks[1][totaltask[1]-1];
        for (j = 0; j < task; j++)
        {
            curr = taskguy[j];
            while (currpos[curr] != tasks[curr][currtask[curr]])//enquanto a posição não for igual à do botão da task atual
            {
                counter++;
                //printf ("%d   Blue: %d Orange: %d\n", counter, currpos[0], currpos[1]);
                if (currpos[curr^1] != tasks[curr^1][currtask[curr^1]]) //anda o outro se a posição não estiver certa
                    currpos[curr^1] += currpos[curr^1]>tasks[curr^1][currtask[curr^1]]?-1:1;
                currpos[curr] += currpos[curr]>tasks[curr][currtask[curr]]?-1:1;
            }
            counter++; //aperta o botão
            currtask[curr]++;
            if (currpos[curr^1] != tasks[curr^1][currtask[curr^1]]) //anda o outro se a posição não estiver certa
                    currpos[curr^1] += currpos[curr^1]>tasks[curr^1][currtask[curr^1]]?-1:1;
            //printf ("%d   Blue: %d Orange: %d\n", counter, currpos[0], currpos[1]);
        }
        printf ("Case #%d: %d\n",i, counter);
    }
}

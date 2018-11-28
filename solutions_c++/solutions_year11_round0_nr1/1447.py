#include <stdio.h>

typedef struct robotsActions
{
    char robot;
    int button;
}robotsActions;

int solve(FILE *f);

int main()
{
    FILE *f=fopen("d:/Google_codejam/task1/data/input.txt","r");
    FILE *fOut=fopen("d:/Google_codejam/task1/data/output.txt","w");
    if(f==NULL)
        return 1;
    int total=4;
    fscanf(f,"%d",&total);
    for(int h=0; h<total; h++)
    {
        fprintf(fOut,"Case #%d: %d\n", h+1, solve(f));
    }
    fclose(f);
    fclose(fOut);
}


int solve(FILE *f)
{
    int count;
    int totalTime=0;
    int robotO=1;
    int robotB=1;
    robotsActions actions[128];

    fscanf(f,"%d ",&count);
    for(int h=0; h<count; h++)
    {
        fscanf(f,"%c %d ",&actions[h].robot, &actions[h].button);
    }


    for(int h=0; h<count; h++)
    {
        int x;
        if(actions[h].robot=='O')
        {
            int nextB=-1;
            for(x=h+1; x<count; x++)
                if(nextB==-1 && actions[x].robot=='B')
                    nextB=actions[x].button;


            while(robotO != actions[h].button)
            {
                if(robotO > actions[h].button)
                    robotO--;
                else
                    robotO++;

                if(robotB != nextB)
                {
                    if(robotB > nextB)
                        robotB--;
                    else
                        robotB++;
                }

                totalTime++;
            }

            totalTime++;
            if(robotB != nextB)
            {
                if(robotB > nextB)
                    robotB--;
                else
                    robotB++;
            }
        }


        if(actions[h].robot=='B')
        {
            int nextO=-1;
            for(x=h+1; x<count; x++)
                if(nextO==-1 && actions[x].robot=='O')
                    nextO=actions[x].button;

            while(robotB != actions[h].button)
            {
                if(robotB > actions[h].button)
                    robotB--;
                else
                    robotB++;

                if(robotO != nextO)
                {
                    if(robotO > nextO)
                        robotO--;
                    else
                        robotO++;
                }

                totalTime++;
            }



            totalTime++;
            if(robotO != nextO)
            {
                if(robotO > nextO)
                    robotO--;
                else
                    robotO++;
            }
        }
    }

    return totalTime;
}

#include<cstdio>

#define _in "A-large.in"
#define _out "out.txt"

int main(int argc, void** argv)
{
    FILE *fin, *fout;

    fin = fopen(_in, "r");
    fout = fopen(_out, "w");
    
    int nCases;
    fscanf(fin,"%d", &nCases);
    for(int i = 1; i<=nCases; i++)
    {
        int nSteps;
        fscanf(fin,"%d ", &nSteps);
        
        int newPos, oSum=0, oShift=0, bShift=0, bSum=0, oPos=1, bPos=1;
        char robot='-', lastRobot='-';
        for(int j=0; j<nSteps; j++)
        {
            fscanf(fin," %c %d", &robot ,&newPos);
            if(robot=='O')
            {
                int shift = oPos - newPos;
                oPos = newPos;
                shift = shift > 0?shift: -shift;
                oSum += shift + 1;
                if(lastRobot=='B')
                {
                    //maybe have to wait
                    if(oSum <=bSum)
                        // wait until finish then press the button
                        oSum = bSum+1;
                }

            }
            else if (robot=='B')
            {
                int shift = bPos - newPos;
                bPos = newPos;
                shift = shift > 0?shift: -shift;
                bSum += shift + 1;
                if(lastRobot=='O')
                {
                    //maybe have to wait
                    if(bSum <=oSum)
                        // wait until finish then press the button
                        bSum = oSum+1;
                }
            }
            lastRobot=robot;
        }
        fprintf(fout,"Case #%d: %d\n", i, oSum>bSum?oSum:bSum);
    }
    fclose(fin);
    fclose(fout);
}
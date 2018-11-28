#include <stdio.h>

using namespace std;

FILE *fi;
FILE *fo;
int main()
{
    int T,counter;
    fi=fopen("input.txt","r");
    fo=fopen("output.txt","w");
    fscanf(fi,"%d\n",&T);
    for(counter=1;counter<=T;counter++)
    {
        int i,j,xflag,oflag,dot=0,T,X=0,O=0;
        char arr[4][4],ch;
        for(i=0;i<4;i++)
        {
            xflag=oflag=T=0;
            for(j=0;j<4;j++)
            {
                fscanf(fi,"%c",&arr[i][j]);
                if(arr[i][j]=='X')
                xflag++;
                else if(arr[i][j]=='O')
                oflag++;
                else if(arr[i][j]=='T')
                T=1;
                else
                dot=1;
            }
            fscanf(fi,"%c",&ch);
            if(xflag==4||(xflag==3&&T))
            X=1;
            else if(oflag==4||(oflag==3&&T))
            O=1;
        }
        fscanf(fi,"%c",&ch);

        if(X==1)
        {
            fprintf(fo,"Case #%d: X won\n",counter);
            continue;
        }
        if(O==1)
        {
            fprintf(fo,"Case #%d: O won\n",counter);
            continue;
        }

        for(i=0;i<4;i++)
        {
            xflag=0;oflag=0;T=0;
            for(j=0;j<4;j++)
            {
                if(arr[j][i]=='X')
                xflag++;
                else if(arr[j][i]=='O')
                oflag++;
                else if(arr[j][i]=='T')
                T=1;
            }
            if(xflag==4||(xflag==3&&T))
            X=1;
            else if(oflag==4||(oflag==3&&T))
            O=1;

        }

        if(X==1)
        {
            fprintf(fo,"Case #%d: X won\n",counter);
            continue;
        }
        if(O==1)
        {
            fprintf(fo,"Case #%d: O won\n",counter);
            continue;
        }

        xflag=0;oflag=0;T=0;
        for(i=0;i<4;i++)
        {
            if(arr[i][i]=='X')
            xflag++;
            else if(arr[i][i]=='O')
            oflag++;
            else if(arr[i][i]=='T')
            T=1;
        }
            if(xflag==4||(xflag==3&&T))
            X=1;
            else if(oflag==4||(oflag==3&&T))
            O=1;

        if(X==1)
        {
            fprintf(fo,"Case #%d: X won\n",counter);
            continue;
        }
        if(O==1)
        {
            fprintf(fo,"Case #%d: O won\n",counter);
            continue;
        }

        xflag=0;oflag=0;T=0;
        for(i=0;i<4;i++)
        {
            if(arr[i][3-i]=='X')
            xflag++;
            else if(arr[i][3-i]=='O')
            oflag++;
            else if(arr[i][3-i]=='T')
            T=1;
        }
            if(xflag==4||(xflag==3&&T))
            X=1;
            else if(oflag==4||(oflag==3&&T))
            O=1;

        if(X==1)
        {
            fprintf(fo,"Case #%d: X won\n",counter);

            continue;
        }
        if(O==1)
        {
            fprintf(fo,"Case #%d: O won\n",counter);

            continue;
        }
        if(dot)
        fprintf(fo,"Case #%d: Game has not completed\n",counter);
        else
        fprintf(fo,"Case #%d: Draw\n",counter);



    }
    return 0;
}

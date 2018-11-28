//
//  main.cpp
//  TicTacToeTomek
//
//  Created by PeterChoi on 13. 4. 13..
//  Copyright (c) 2013년 summerpool. All rights reserved.
//

#include <stdio.h>
#include <string.h>

#define INPUTFILENAME "./A-large.in.txt"
#define OUTPUTFILENAME "./resultA2.txt"

#define INPUTSTR "%[^\n]s"
#define OUTPUTSTR "Case #%d: %s\n"

#define OPEN_FILE_READ(X) X=fopen(INPUTFILENAME,"r");
#define OPEN_FILE_WRITE(X) X=fopen(OUTPUTFILENAME,"w");
int main(int argc, const char * argv[])
{

    FILE * inputF, *outputF;
    
    OPEN_FILE_READ(inputF)
    OPEN_FILE_WRITE(outputF)
    
    int n;
    
    fscanf(inputF, "%d", &n);
    
    for(int i=0 ; i<n ; i++)
    {
        char temp;
        
        char Map[4][5];
        
        fscanf(inputF, "%c", &temp);
        
        for(int j=0 ; j<4 ; j++)
        {
            for(int k=0 ; k<5 ; k++)
            {
                fscanf(inputF, "%c", &Map[j][k]);
            }
        }
        
        bool bO, bX, bD;
        bO = bX = bD = false;
        
        for(int j=0 ; j<4 ; j++)
        {
            if(bO == false)
            for(int k=0 ; k<4 ; k++)
            {
                if(Map[j][k] == 'O' || Map[j][k] == 'T')
                {
                    if(k == 3)
                    {
                        bO = true;
                    }
                    else
                        continue;
                }
                else
                {
                    break;
                }
            }
        }
        if(!bO)
        for(int j=0 ; j<4 ; j++)
        {
            if(bO == false)
            for(int k=0 ; k<4 ; k++)
            {
                if(Map[k][j] == 'O' || Map[k][j] =='T')
                {
                    if(k == 3)
                    {
                        bO = true;
                    }
                    else
                        continue;
                }
                else
                {
                    break;
                }
            }
        }
        if(!bO)
            for(int j=0 ; j<4 ; j++)
            {
                if(Map[j][j] == 'O' || Map[j][j] == 'T')
                {
                    if(j==3)
                    {
                        bO = true;
                    }
                    else
                    {
                        continue;
                    }
                }
                else
                    break;
            }
        if(!bO)
            for(int j=0 ; j<4 ; j++)
            {
                if(Map[j][3-j] == 'O' || Map[j][3-j] == 'T')
                {
                    if(j==3)
                    {
                        bO = true;
                    }
                    else
                    {
                        continue;
                    }
                }
                else
                    break;
            }
        if(!bO)
        {
            for(int j=0 ; j<4 ; j++)
            {
                if(bX == false)
                    for(int k=0 ; k<4 ; k++)
                    {
                        if(Map[j][k] == 'X' || Map[j][k] == 'T')
                        {
                            if(k == 3)
                            {
                                bX = true;
                            }
                            else
                                continue;
                        }
                        else
                        {
                            break;
                        }
                    }
            }
            if(!bX)
                for(int j=0 ; j<4 ; j++)
                {
                    if(bX == false)
                        for(int k=0 ; k<4 ; k++)
                        {
                            if(Map[k][j] == 'X' || Map[k][j] =='T')
                            {
                                if(k == 3)
                                {
                                    bX = true;
                                }
                                else
                                    continue;
                            }
                            else
                            {
                                break;
                            }
                        }
                }
            if(!bX)
                for(int j=0 ; j<4 ; j++)
                {
                    if(Map[j][j] == 'X' || Map[j][j] == 'T')
                    {
                        if(j==3)
                        {
                            bX = true;
                        }
                        else
                        {
                            continue;
                        }
                    }
                    else
                        break;
                }
            if(!bX)
                for(int j=0 ; j<4 ; j++)
                {
                    if(Map[j][3-j] == 'X' || Map[j][3-j] == 'T')
                    {
                        if(j==3)
                        {
                            bX = true;
                        }
                        else
                        {
                            continue;
                        }
                    }
                    else
                        break;
                }
        }
        if(bO)
        {
            fprintf(outputF, "Case #%d: O won\n", i+1);
        }
        else if(bX)
        {
            fprintf(outputF, "Case #%d: X won\n", i+1);
        }
        else
        {
            for(int j=0 ; j<4 ; j++)
            {
                if(!bD)
                for(int k=0 ; k<4 ; k++)
                {
                    if(Map[j][k] == '.')
                    {
                        bD = true;
                        break;
                    }
                }
            }
            if(!bD)
                fprintf(outputF, "Case #%d: Draw\n", i+1);
            else
                fprintf(outputF, "Case #%d: Game has not completed\n", i+1);
        }
    }
    
    
    
    
    
    fclose(inputF);
    fclose(outputF);
    

    return 0;
}


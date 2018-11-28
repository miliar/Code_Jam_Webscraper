//
//  main.cpp
//  Code_Jam
//
//  Created by 용 최 on 12. 4. 13..
//  Copyright (c) 2012년 soaryong.c@gmail.com. All rights reserved.
//

#include <stdio.h>
#include<stdlib.h>
#include<string.h>

int main(int argc, const char * argv[])
{
    FILE *in = fopen("/Users/soaryong/dev/Code_Jam/Code_Jam/sample.in","rt");
    FILE *out = fopen("/Users/soaryong/dev/Code_Jam/Code_Jam/sample.out","wt");
    int n,t,s,p,arr[101],i,j,player;
    fscanf(in,"%d",&t);
    for(i=0;i<t;i++)
    {
        fscanf(in,"%d",&n);
        fscanf(in,"%d",&s);
        fscanf(in,"%d",&p);
        player=0;
        for(j=0;j<n;j++)
        {
            fscanf(in, "%d",&arr[j]);
        }
        for(j=0;j<n;j++)
        {
            if(arr[j]==0){
                if (p == 0) {
                    player++;
                }
            } else if(arr[j]%3==0)
            {
                if(arr[j]/3>=p) {
                    player++;
                }
                else {
                    if(s>0 && arr[j]/3+1 >= p)
                    {
                        s--;
                        player++;
                    }
                }
            } else if(arr[j]%3==1)
            {
                if(arr[j]/3+1>=p) {
                    player++;
                }

            } else
            {
                if(arr[j]/3+1>=p) {
                    player++;
                } else {
                    if(s>0 && arr[j]/3+2 >=p)
                    {
                        s--;
                        player++;
                    }
                }
            }
        }
        fprintf(out, "Case #%d: %d\n",i+1,player);
    }
    return 0;
}



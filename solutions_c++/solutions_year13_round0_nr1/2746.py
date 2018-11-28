//
//  main.cpp
//  GCJ_1
//
//  Created by Yutian Liu on 13-4-13.
//  Copyright (c) 2013年 Yutian Liu. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;


int check(char pattern[][4])
{
    int i,j;
    //check row
    for(i=0;i<4;i++)
    {
        int flag = 0;
        for(j=0;j<4;j++)
        {
            if(pattern[i][j]=='.')
            {
                flag = -1;
                break;
            }
            else if(pattern[i][j]=='X')
            {
                if(flag==0)
                    flag = 1;
                else if(flag==2)
                {
                    flag = -1;
                    break;
                }

            }
            else if(pattern[i][j]=='O')
            {
                if(flag==0)
                    flag = 2;
                else if(flag==1)
                {
                    flag = -1;
                    break;
                }
            }
        }
        if(flag==1)
        {
            return 1;
        }
        else if(flag==2)
        {
            return 2;
        }
        else if(flag==0)
            cout << "Error_1" <<endl;
    }
    
    
    //check col
    for(i=0;i<4;i++)
    {
        int flag = 0;
        for(j=0;j<4;j++)
        {
            if(pattern[j][i]=='.')
            {
                flag = -1;
                break;
            }
            else if(pattern[j][i]=='X')
            {
                if(flag==0)
                    flag = 1;
                else if(flag==2)
                {
                    flag = -1;
                    break;
                }
                
            }
            else if(pattern[j][i]=='O')
            {
                if(flag==0)
                    flag = 2;
                else if(flag==1)
                {
                    flag = -1;
                    break;
                }
            }
        }
        if(flag==1)
        {
            return 1;
        }
        else if(flag==2)
        {
            return 2;
        }
        else if(flag==0)
            cout << "Error_2" <<endl;
    }
    
    //check diog
    int flag = 0;
    for(i=0;i<4;i++)
    {
        if(pattern[i][i]=='.')
        {
            flag = -1;
            break;
        }
        else if(pattern[i][i]=='X')
        {
            if(flag==0)
                flag = 1;
            else if(flag==2)
            {
                flag = -1;
                break;
            }
        }
        else if(pattern[i][i]=='O')
        {
            if(flag==0)
                flag = 2;
            else if(flag==1)
            {
                flag = -1;
                break;
            }
        }
    }
    if(flag==1)
        return 1;
    else if(flag==2)
        return 2;
    else if(flag==0)
        cout << "Error_3" <<endl;
    
    
    flag = 0;
    for(i=0;i<4;i++)
    {
        if(pattern[i][3-i]=='.')
        {
            flag = -1;
            break;
        }
        else if(pattern[i][3-i]=='X')
        {
            if(flag==0)
                flag = 1;
            else if(flag==2)
            {
                flag = -1;
                break;
            }
        }
        else if(pattern[i][3-i]=='O')
        {
            if(flag==0)
                flag = 2;
            else if(flag==1)
            {
                flag = -1;
                break;
            }
        }
    }
    if(flag==1)
        return 1;
    else if(flag==2)
        return 2;
    else if(flag==0)
        cout << "Error_4" <<endl;
    
    return 0;    
}

int main(int argc, const char * argv[])
{

    // insert code here...
    int numOfSample;
    char pattern[4][4];
    ifstream infile;
    infile.open("input.txt",ios::in);
    if(!infile)
        cout << "oend" <<endl;
    ofstream outfile;
    outfile.open("output.txt",ios::out);
    
    infile >> numOfSample;
    
    int i,m,n;
    
    for(i=0;i<numOfSample;i++)
    {
        bool full = true;
        for(m=0;m<4;m++)
        {
            for(n=0;n<4;n++)
            {
                infile >> pattern[m][n];
                if(pattern[m][n] == '.')
                    full = false;
            }
                
        }
        int res = check(pattern);
        outfile << "Case #" << i+1;
        if(res == 0)
        {
            if(full)
                outfile << ": Draw" << endl;
            else
                outfile << ": Game has not completed" <<endl;
        }
        else if(res == 1)
            outfile << ": X won" << endl;
        else if(res == 2)
            outfile << ": O won" << endl;
        
    }
    infile.close();
    outfile.close();
    
    
    
    return 0;
}


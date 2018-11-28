#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
#include<string>
#include<stack>
#include<queue>

using namespace std;

string a[4];


string chkstat()
{
    //row checking
    int cntd=0;
    for(int i=0;i<4;i++)
    {
        int cntx=0,cnto=0;
        for(int j=0;j<4;j++)
        {
            if(a[i][j] == 'X')
                cntx++;
            else if(a[i][j] == 'O')    
                cnto++;
            else if(a[i][j] == 'T')
            {
                cnto++;
                cntx++;    
            }    
            else if(a[i][j] == '.')
                cntd++;
        } 
        if(cntx == 4)
            return "X won";
        else if(cnto == 4)
            return "O won";   
    } 
    //column checking
    for(int j=0;j<4;j++)
    {
        int cntx=0,cnto=0;
        for(int i=0;i<4;i++)
        {
            if(a[i][j] == 'X')
                cntx++;
            else if(a[i][j] == 'O')    
                cnto++;
            else if(a[i][j] == 'T')
            {
                cnto++;
                cntx++;    
            }    
        } 
        if(cntx == 4)
            return "X won";
        else if(cnto == 4)
            return "O won";   
    }
    // trailing diagonal checking
    int cntx=0,cnto=0;
    for(int i=0;i<4;i++)
    {
        if(a[i][i] == 'X')
            cntx++;
        else if(a[i][i] == 'O')    
            cnto++;
        else if(a[i][i] == 'T')
        {
            cnto++;
            cntx++;    
        }    
        if(cntx == 4)
            return "X won";
        else if(cnto == 4)
            return "O won";   
    }
    // leading diagonal checking
     cntx=0;
     cnto=0;
    for(int i=0;i<4;i++)
    {
        if(a[i][3-i] == 'X')
            cntx++;
        else if(a[i][3-i] == 'O')    
            cnto++;
        else if(a[i][3-i] == 'T')
        {
            cnto++;
            cntx++;    
        }    
        if(cntx == 4)
            return "X won";
        else if(cnto == 4)
            return "O won";   
    }  
    if(cntd ==0)
        return "Draw";
    else 
        return "Game has not completed";
}


int main()
{
    int T;
    cin >> T;
    for(int t=0;t<T;t++)
    {
        for(int i=0;i<4;i++)
                cin >> a[i];
        cout << "Case #" << t+1<< ": "<<chkstat()<<endl;    
    }    
    return 0;    
}


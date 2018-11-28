#include <iostream>
using namespace std; 

int testGame();
bool add(int* player, int i);

int main()
{
    int numTest;
    cin>>numTest;

    for(int i=0;i<numTest;++i)
    {
        int result=testGame();
        cout<<"Case #"<<i+1<<": "; 
        switch(result)
        {
            case 1:
                cout<<"X won"<<endl;
                break;
            case 2:
                cout<<"O won"<<endl;
                break;
            case 3:
                cout<<"Draw"<<endl;
                break;
            case 4:
                cout<<"Game has not completed"<<endl;
                break;
        }
    }
    return 0;
}

int testGame()
{
    int playerX[10]={0,0,0,0,0,0,0,0,0,0};
    int playerO[10]={0,0,0,0,0,0,0,0,0,0};
    bool empty=false;
    int result = 0;

    char input;
    for(int i=0;i<16;++i)
    {
        cin>>input;
        if(result!=0)
            continue;

        if(input=='X')
        {
            bool cur=add(playerX, i);
            if(cur==true)
            {
                result = 1;
            }
        }
        else if(input=='O')
        {
            bool cur=add(playerO, i);
            
            if(cur==true)
            {
                result=2;
            }
        }
        else if(input == 'T')
        {
            bool cur=add(playerX, i);
            if(cur==true)
            {
                result = 1;
            }
            
            cur=add(playerO, i);
            if(cur==true)
            {
                result = 2;
            }
        }
        else
        {
            empty=true;
        }
    }

    if(result==0)
    {
        if(empty==false)
            result = 3;
         else    
           result = 4;
    }
    
    return result;
}

bool add(int* player, int i)
{
    player[i/4]++;
    if(player[i/4]==4)
        return true;

    player[4+i%4]++;
    if(player[4+i%4]==4)
        return true;

    if(i==0 || i==5 || i==10 || i==15)
    {
        player[8]++;
        if(player[8]==4)
            return true;
    }
    else if(i==3 ||i==6 || i==9 || i==12)
    {
        player[9]++;
        if(player[9]==4)
            return true;
    }

    return false;
}

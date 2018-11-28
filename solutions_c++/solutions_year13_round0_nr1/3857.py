
#include <fstream>
using namespace std;
int check(char [][4]);
int main()
{
    int t,y;
    ifstream cin;
    ofstream cout;
    cin.open("input.txt");
    cout.open("output.txt");
    cin>>t;
    char tik[4][4];
    for(int i=0;i<t;i++)
    {
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++) cin>>tik[j][k];
        }
        y=check(tik);
        cout<<"Case #"<<i+1<<": ";
        switch(y)
        {
            case 0:
                   cout<<"X won"<<endl;
                   break;
            case 1:
                   cout<<"O won"<<endl;
                   break;
            case 2:
                   cout<<"Draw"<<endl;
                   break;
            default:
                   cout<<"Game has not completed"<<endl;
                   break;
        }
    }
    cin.close();
    cout.close();
    return 0;
}

int check(char tik[4][4])
{
    //checking rows
    int x,o,t;
    for(int i=0;i<4;i++)
    {
        x=0; o=0; t=0;
        for(int j=0;j<4;j++)
        {
            if(tik[i][j]=='X') x++;
            else if(tik[i][j]=='O') o++;
            else if(tik[i][j]=='T') t++;
        }
        if((x==4)||((x==3)&&(t==1))) return 0;
        if((o==4)||((o==3)&&(t==1))) return 1;
    }
    //checking columns
    for(int j=0;j<4;j++)
    {
        x=0; o=0; t=0;
        for(int i=0;i<4;i++)
        {
            if(tik[i][j]=='X') x++;
            else if(tik[i][j]=='O') o++;
            else if(tik[i][j]=='T') t++;
        }
        if((x==4)||((x==3)&&(t==1))) return 0;
        if((o==4)||((o==3)&&(t==1))) return 1;
    }
    //checking diagonals
    int i=0,j=0;
    x=0; o=0; t=0;
    while(i<4)
    {
        if(tik[i][j]=='X') x++;
        else if(tik[i][j]=='O') o++;
        else if(tik[i][j]=='T') t++;
        i++; j++;
    }
    if((x==4)||((x==3)&&(t==1))) return 0;
    if((o==4)||((o==3)&&(t==1))) return 1;
    x=0; o=0; t=0;
    i=0; j=3;
    while(i<4)
    {
        if(tik[i][j]=='X') x++;
        else if(tik[i][j]=='O') o++;
        else if(tik[i][j]=='T') t++;
        i++; j--;
    }
    if((x==4)||((x==3)&&(t==1))) return 0;
    if((o==4)||((o==3)&&(t==1))) return 1;
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
            if(tik[i][j]=='.') return 3;
        }
    }
    return 2;

}

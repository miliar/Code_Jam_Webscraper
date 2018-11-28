#include <iostream>
#include <fstream>

using namespace std;

fstream file;
char matrix[4][4];

void read(char matrix[4][4])
{
    for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                char temp=file.get();
                matrix[i][j]=temp;
            }
            file.get();
        }
        file.get();
}

bool check(char item)
{
    for(int i=0;i<4;i++)
    {
        if((matrix[i][0]==item||matrix[i][0]=='T')&&(matrix[i][1]==item||matrix[i][1]=='T')&&(matrix[i][2]==item||matrix[i][2]=='T')&&(matrix[i][3]==item||matrix[i][3]=='T'))
        return true;

        if((matrix[0][i]==item||matrix[0][i]=='T')&&(matrix[1][i]==item||matrix[1][i]=='T')&&(matrix[2][i]==item||matrix[2][i]=='T')&&(matrix[3][i]==item||matrix[3][i]=='T'))
        return true;
    }

    if((matrix[0][0]==item||matrix[0][0]=='T')&&(matrix[1][1]==item||matrix[1][1]=='T')&&(matrix[2][2]==item||matrix[2][2]=='T')&&(matrix[3][3]==item||matrix[3][3]=='T'))
    return true;

    if((matrix[0][3]==item||matrix[0][3]=='T')&&(matrix[1][2]==item||matrix[1][2]=='T')&&(matrix[2][1]==item||matrix[2][1]=='T')&&(matrix[3][0]==item||matrix[3][0]=='T'))
    return true;

    return false;
}

bool draw ()
{

    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
        {
            if(matrix[i][j]=='.')
            return false;
        }
    }
    return true;
}

int main()
{

    ofstream answer;
    file.open("A-large.in");
    answer.open("answer.txt");

    int n=0;
    while(int temp=file.get())
    {
        if(temp==10)break;
        temp-=48;
        n=(n*10)+temp;
    }
    cout<<n<<endl;
    char output;

    for(int i=1;i<=n;i++)
    {
        read(matrix);

        if(check('X'))
        {
            cout<<"Case #"<<i<<": "<<"X won"<<endl;
            answer<<"Case #"<<i<<": "<<"X won"<<endl;
            continue;
        }

        if(check('O'))
        {
            cout<<"Case #"<<i<<": "<<"O won"<<endl;
            answer<<"Case #"<<i<<": "<<"O won"<<endl;
            continue;
        }

        bool flag=draw();
        if(flag)
        {
            cout<<"Case #"<<i<<": "<<"Draw"<<endl;
            answer<<"Case #"<<i<<": "<<"Draw"<<endl;
            continue;
        }
        else
        {
            cout<<"Case #"<<i<<": "<<"Game has not completed"<<endl;
            answer<<"Case #"<<i<<": "<<"Game has not completed"<<endl;
            continue;
        }
    }
}

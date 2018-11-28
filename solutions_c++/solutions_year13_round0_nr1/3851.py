#include<fstream>
#include<iostream>
#include<string>
#include<cstring>
using namespace std;
int main()
{
int N;
char str[30];
cin>>str;
fstream fi,fo;
fi.open(str,fstream::in);
fo.open("output.out",fstream::out);
fi>>N;
char A[4][5];
for(int k=0;k<N;k++)
{

    for (int i=0;i<4;i++)
    {
        fi>>A[i];

    }

    bool x1,x2,o1,o2;bool x3=true;bool o3=true;int i=0;bool draw=true;bool o4=true;bool x4=true;
    fo<<"Case #"<<(k+1)<<": ";
    for(i=0;i<4;i++)
    {
        x1=true;x2=true;o1=true;o2=true;
        for(int j=0;j<4;j++)
        {
            x1&=(A[i][j]=='X'||A[i][j]=='T');
            x2&=(A[j][i]=='X'||A[j][i]=='T');
            o1&=(A[i][j]=='O'||A[i][j]=='T');
            o2&=(A[j][i]=='O'||A[j][i]=='T');
            draw&=(A[i][j]=='X'||A[i][j]=='O'||A[i][j]=='T');
        }
        x3&=(A[i][i]=='X'||A[i][i]=='T');
        o3&=(A[i][i]=='O'||A[i][i]=='T');
        x4&=(A[i][3-i]=='X'||A[i][3-i]=='T');
        o4&=(A[i][3-i]=='O'||A[i][3-i]=='T');
        if(x1||x2){fo<<"X won"<<endl;break;}
        else if(o1||o2){fo<<"O won"<<endl;break;}
    }
    if(i==4)
    {
        if(x3||x4){fo<<"X won"<<endl;}
        else if(o3||o4){fo<<"O won"<<endl;}
        else if(draw){fo<<"Draw"<<endl;}
        else{fo<<"Game has not completed"<<endl;}
    }
}
fi.close();
fo.close();
return (0);
}

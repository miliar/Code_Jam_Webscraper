#include<iostream>
using namespace std;
int wincase[10]={15,
        240,
        3840,
        61440,
        34952,
        17476,
        8738,
        4369,
        33825,
        4680};
int pow2(int i)
{
    return 1<<i;
}
int checkCase(int c)
{
    int i;
    for(i=0;i<10;i++)
    {
        if ((c&wincase[i])==wincase[i])
        {
            return 1;
        }
    }
    return 0;
}
int main()
{
    int n,c,j,i,isEnd,caseX,caseO,p;
    char t[5][5];
    cin >> n;
    for(c=1;c<=n;c++)
    {
        isEnd=1;
        caseX=0;
        caseO=0;
        for(i=0;i<4;i++) cin >> t[i];
        for(j=0;j<4;j++)
        {
            for(i=0;i<4;i++)
            {
                p = j*4+i;
                if (t[j][i]=='.')isEnd=0;
                else if (t[j][i]=='X')caseX+=pow2(p);
                else if (t[j][i]=='O')caseO+=pow2(p);
                else
                {
                    caseO+=pow2(p);
                    caseX+=pow2(p);
                }

            }
        }
        cout << "Case #"<<c<<": ";
        if (checkCase(caseX))cout <<"X won"<<endl;
        else if (checkCase(caseO))cout << "O won"<<endl;
        else
        {
            if(isEnd) cout << "Draw"<<endl;
            else cout << "Game has not completed" <<endl;

        }
    }
}


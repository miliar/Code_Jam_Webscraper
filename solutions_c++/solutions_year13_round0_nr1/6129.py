#include <iostream>
#include <fstream>
using namespace std;

int main()
{
     ofstream write;
    write.open ("file.out");

    ifstream read("A-large.in");
    int t;
    read>> t;
    for(int k=1;k<=t;k++)
    {
        char arr[4][4];
        int sumMainX=0;
        int sumSpamX=0;
        int sumMainO=0;
        int sumSpamO=0;
        int sumRowX=0;
        int sumRowO=0;
        int sumColX=0;
        int sumColO=0;
        bool dotfound=false;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                read>>arr[i][j];
                if(arr[i][j]=='.')
                {
                    dotfound=true;
                }

            }
        }
        sumMainX=0;
        sumSpamX=0;
        sumMainO=0;
        sumSpamO=0;
         bool flag=false;
            for(int i=0;i<4&&flag==false;i++)
            {
            if(arr[i][i]=='X'||arr[i][i]=='T')
            {
                sumMainX++;
            }
            if(arr[i][3-i]=='X'||arr[i][3-i]=='T')
            {
                sumSpamX++;
            }
             if(arr[i][i]=='O'||arr[i][i]=='T')
            {
                sumMainO++;
            }
             if(arr[i][3-i]=='O'||arr[i][3-i]=='T')
            {
                sumSpamO++;
            }

            sumRowX=0;
            sumRowO=0;
            sumColX=0;
            sumColO=0;
            for(int j=0;j<4&&flag==false;j++)
            {
                if(arr[i][j]=='O'||arr[i][j]=='T')
                {
                    sumRowO++;
                }
                if(arr[i][j]=='X'||arr[i][j]=='T')
                {
                    sumRowX++;
                }
                if(arr[j][i]=='X'||arr[j][i]=='T')
                {
                    sumColX++;
                }
                if(arr[j][i]=='O'||arr[j][i]=='T')
                {
                    sumColO++;
                }
            }
            if(sumRowO==4||sumColO==4||sumMainO==4||sumSpamO==4)
            {
                flag=true;
                write<< "Case #"<<k<<": O won";
            }
            else if(sumRowX==4||sumColX==4||sumMainX==4||sumSpamX==4)
            {
                flag=true;
                write <<"Case #"<<k<<": X won";
            }
        }
            if(dotfound==true&&flag==false)
            {
                flag=true;
                write <<"Case #"<<k<<": Game has not completed";
            }
            else if(flag==false)
            {
                flag=true;
                write<<"Case #"<<k<<": Draw";
            }
            write<<endl;
    }
     write.close();
    return 0;
}

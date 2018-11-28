#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main()
{
    ifstream file("A-large.in");
    ofstream file2("output.txt");
    string line;
    int n;
    file>>n;
    //cout<<n;
    for(int i=0;i<n;++i)
    {
        //cout<<i<<endl;
        char arr[4][4];
        file>>arr[0]>>arr[1]>>arr[2]>>arr[3];
        //char c;
        //file>>c;
        int flag=0;
        int flagg=0;
        int flagd=0;
        int no=0,nx=0;
        for(int j=0;j<4;++j)
        {
            for(int k=0;k<4;++k)
            {
                if(arr[j][k]=='X')
                    nx++;
                else if(arr[j][k]=='O')
                    no++;
                else if(arr[j][k]=='T')
                    flag=1;
                else if(arr[j][k]=='.')
                    flagd=1;
            }
            if(nx==4 || (nx==3&&flag==1))
            {
                file2<<"Case #"<<i+1<<": X won\n";
                flagg=1;
                break;
                //goto g;
            }
            else if(no==4 || (no==3&&flag==1))
            {
                file2<<"Case #"<<i+1<<": O won\n";
                flagg=1;
                break;
                //goto g;
            }
            
            //cout<<nx<<" "<<no<<" "<<flag<<endl;
            flag=0;
            no=0;
            nx=0;
        }
        if(flagg==1)
        {
            //cout<<"hi";
        	continue;
        }
        //cout<<"bye";
        for(int j=0;j<4;++j)
        {
            for(int k=0;k<4;++k)
            {
                if(arr[k][j]=='X')
                    nx++;
                else if(arr[k][j]=='O')
                    no++;
                else if(arr[k][j]=='T')
                    flag=1;
                else if(arr[j][k]=='.')
                    flagd=1;
            }
            if(nx==4 || (nx==3&&flag==1))
            {
                file2<<"Case #"<<i+1<<": X won\n";
                flagg=1;
                break;
                //goto g;
            }
            if(no==4 || (no==3&&flag==1))
            {
                file2<<"Case #"<<i+1<<": O won\n";
                flagg=1;
                break;
                //goto g;
            }
            flag=0;
            no=0;
            nx=0;
        }
        if(flagg==1)
            continue;
        for(int j=0;j<4;++j)
        {
            if(arr[j][j]=='X')
                nx++;
            else if(arr[j][j]=='O')
                no++;
            else if(arr[j][j]=='T')
                flag=1;
            else if(arr[j][j]=='.')
                    flagd=1;
        }
        if(nx==4 || (nx==3&&flag==1))
        {
            file2<<"Case #"<<i+1<<": X won\n";
            flagg=1;
            //goto g;
        }
        if(no==4 || (no==3&&flag==1))
        {
            file2<<"Case #"<<i+1<<": O won\n";
            flagg=1;
            //goto g;
        }
        flag=0;
        no=0;
        nx=0;
        if(flagg==1)
            continue;
        int p=3;
        for(int j=0;j<4;++j)
        {
            if(arr[j][p]=='X')
                nx++;
            else if(arr[j][p]=='O')
                no++;
            else if(arr[j][p]=='T')
                flag=1;
            else if(arr[j][p]=='.')
                    flagd=1;
            p--;
        }
        if(nx==4 || (nx==3&&flag==1))
        {
            file2<<"Case #"<<i+1<<": X won\n";
            flagg=1;
            //goto g;
        }
        if(no==4 || (no==3&&flag==1))
        {
            file2<<"Case #"<<i+1<<": O won\n";
            flagg=1;
        }
        if(flagg==1)
            continue;
        if(flagd==1)
        file2<<"Case #"<<i+1<<": Game has not completed\n";
        else
        file2<<"Case #"<<i+1<<": Draw\n";
    }
    file.close();
    file2.close();
    system("Pause");
    return 0;
}


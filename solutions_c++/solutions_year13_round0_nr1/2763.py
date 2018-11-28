#include<iostream>
#include<fstream>

using namespace std;
int main()
{
    int t;

    string s1;
    string s2;
    string s3;
    string s4;
    ifstream ifs;
    ifs.open("input.txt");
    ofstream ofs;
    ofs.open("output.txt");
    int cs=0;
    int flag,inc;
    ifs>>t;
    while(cs<t)
    {
        ifs>>s1;
        if(s1=="")
        {
            //cout<<endl<<endl;
            continue;

        }ifs>>s2;
        ifs>>s3;
        ifs>>s4;
        //cout<<s1<<endl;
        //cout<<s2<<endl;
        //cout<<s3<<endl;
        //cout<<s4<<endl;

        cs++;
        flag=0;
        inc=0;
        if(s1=="OOOO"||s1=="OOOT"||s1=="OOTO"||s1=="OTOO"||s1=="TOOO"
           ||s2=="OOOO"||s2=="OOOT"||s2=="OOTO"||s2=="OTOO"||s2=="TOOO"
           ||s3=="OOOO"||s3=="OOOT"||s3=="OOTO"||s3=="OTOO"||s3=="TOOO"
           ||s4=="OOOO"||s4=="OOOT"||s4=="OOTO"||s4=="OTOO"||s4=="TOOO")
           {
               ofs<<"Case #"<<cs<<": O won\n";flag=1;
           }
        else if(s1=="XXXX"||s1=="XXXT"||s1=="XXTX"||s1=="XTXX"||s1=="TXXX"
           ||s2=="XXXX"||s2=="XXXT"||s2=="XXTX"||s2=="XTXX"||s2=="TXXX"
           ||s3=="XXXX"||s3=="XXXT"||s3=="XXTX"||s3=="XTXX"||s3=="TXXX"
           ||s4=="XXXX"||s4=="XXXT"||s4=="XXTX"||s4=="XTXX"||s4=="TXXX")
           {
               ofs<<"Case #"<<cs<<": X won\n";flag=1;
           }
        if(flag==1)
            continue;
        for(int i=0;i<4;i++)
        {
            if(s1[i]=='.'||s2[i]=='.'||s3[i]=='.'||s4[i]=='.')
            inc=1;
            if((s1[i]=='O'||s1[i]=='T')&&(s2[i]=='O'||s2[i]=='T')&&(s3[i]=='O'||s3[i]=='T')&&(s4[i]=='O'||s4[i]=='T'))
            {
                ofs<<"Case #"<<cs<<": O won\n";
                flag=1;
                break;
            }
            if((s1[i]=='X'||s1[i]=='T')&&(s2[i]=='X'||s2[i]=='T')&&(s3[i]=='X'||s3[i]=='T')&&(s4[i]=='X'||s4[i]=='T'))
            {
                ofs<<"Case #"<<cs<<": X won\n";
                flag=1;
                break;
            }

        }
        if(flag==1)

            continue;
        else if((s1[0]=='O'||s1[0]=='T')&&(s2[1]=='O'||s2[1]=='T')&&(s3[2]=='O'||s3[2]=='T')&&(s4[3]=='O'||s4[3]=='T'))
        {
                ofs<<"Case #"<<cs<<": O won\n";
                continue;
        }
        else if((s1[3]=='O'||s1[3]=='T')&&(s2[2]=='O'||s2[2]=='T')&&(s3[1]=='O'||s3[1]=='T')&&(s4[0]=='O'||s4[0]=='T'))
        {
                ofs<<"Case #"<<cs<<": O won\n";
                continue;
        }
        else if((s1[0]=='X'||s1[0]=='T')&&(s2[1]=='X'||s2[1]=='T')&&(s3[2]=='X'||s3[2]=='T')&&(s4[3]=='X'||s4[3]=='T'))
        {
                ofs<<"Case #"<<cs<<": X won\n";
            continue;
        }
        else if((s1[3]=='X'||s1[3]=='T')&&(s2[2]=='X'||s2[2]=='T')&&(s3[1]=='X'||s3[1]=='T')&&(s4[0]=='X'||s4[0]=='T'))
        {
                ofs<<"Case #"<<cs<<": X won\n";
            continue;
        }
        else if(inc==1)
        {
          //      cout<<"%%%%%%%%%%%%%%%%%%%%\n";
                ofs<<"Case #"<<cs<<": Game has not completed\n";
                continue;
        }
        else
            ofs<<"Case #"<<cs<<": Draw\n";


    }
}

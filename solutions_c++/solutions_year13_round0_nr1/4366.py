#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int args, char* arg[])
{
    if(args<2) return 1;
    ifstream fin(arg[1],ifstream::in);
    ofstream fou("Aout.txt",ofstream::out);

    int tc,t,i,j; fin>>t; fin.ignore(100,'\n');
    char row,k,d1,d2,s[5];

    for(tc=1;tc<=t;tc++)
    {
        char state[]="TTTT"; int dots=0; row='.'; d1='T';d2='T';
        for(i=0;i<4;i++)
        {
            fin.getline(s,sizeof(s)); k='T';
            if(d1=='T') d1=s[i]; if(d1!=s[i]&&s[i]!='T') d1='.';
            if(d2=='T') d2=s[3-i]; if(d2!=s[3-i]&&s[3-i]!='T') d2='.';
            for(j=0;j<4;j++)
            {
                if(k=='T') k=s[j]; if(k!=s[j]&&s[j]!='T') k='.';
                if(state[j]=='T') state[j]=s[j];
                if(state[j]!=s[j]&&s[j]!='T') state[j]='Z';
                if(s[j]=='.') dots++;
            }
            if(k=='X'||k=='O') row=k;
        }
        cout<<row<<" "<<d1<<" "<<d2<<" "<<"dots="<<dots<<" "<<state<<endl;
        fou<<"Case #"<<tc<<": ";
        if(row=='X'||d1=='X'||d2=='X'||state[0]=='X'||state[1]=='X'||state[2]=='X'||state[3]=='X') fou<<"X won";
        else if(row=='O'||d1=='O'||d2=='O'||state[0]=='O'||state[1]=='O'||state[2]=='O'||state[3]=='O') fou<<"O won";
        else if(dots==0) fou<<"Draw";
        else fou<<"Game has not completed";
        fou<<endl;
        fin.ignore(100,'\n');
    }


    return 0;
}

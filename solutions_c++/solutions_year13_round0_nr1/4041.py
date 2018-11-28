#include<iostream>
#include<fstream>
#include<string>
#include<sstream>
using namespace std;

int main()
{
    fstream fin,fout;
    fin.open("a.in");
    fout.open("b.txt");
    int t;
    fin>>t;
    //cout<<t;
    for(int z=1;!fin.eof() && z<=t;z++)
    {

            string tmp,s[4];
            for(int i=0;i<4;i++)
            {
                fin>>tmp;
                s[i]=tmp;
            }

            int st;
            int ans=-1;

            for(int i=0;i<4;i++)
                {
                    int x,o,t;
                    x=o=t=0;
                    for(int j=0;j<4;j++)
                        if(s[i][j]=='X')
                            x++;
                        else if(s[i][j]=='O')
                            o++;
                        else if(s[i][j]=='T')
                            t++;
                        else if(s[i][j]=='.')
                           {
                             ans=0;
                             break;
                           }

                    if(x==4 || (x==3 && t==1))
                    {
                        ans=1;
                        break;
                    }
                    if(o==4 || (o==3 && t==1))
                    {
                        ans=2;
                        break;
                    }

                    o=x=t=0;
                    for(int j=0;j<4;j++)
                        if(s[j][i]=='X')
                            x++;
                        else if(s[j][i]=='O')
                            o++;
                        else if(s[j][i]=='T')
                            t++;
                    else if(s[i][j]=='.')
                           {
                             ans=0;
                             break;
                           }
                    if(x==4 || (x==3 && t==1))
                    {
                        ans=1;
                        break;
                    }
                    if(o==4 || (o==3 && t==1))
                    {
                        ans=2;
                        break;
                    }
                }

                if(ans==0  || ans==-1)
                {

                int x,o,t;
                x=o=t=0;
                for(int i=0;i<4;i++)
                {
                        if(s[i][i]=='X')
                            x++;
                        else if(s[i][i]=='O')
                            o++;
                        else if(s[i][i]=='T')
                            t++;
                        else if(s[i][i]=='.')
                           ans=0;

                }
                    if(x==4 || (x==3 && t==1))
                        ans=1;
                    if(o==4 || (o==3 && t==1))
                        ans=2;
                    if(ans==0 || ans==-1)
                    {
                     x=o=t=0;

                    for(int i=0;i<4;i++)
                    {
                        if(s[3-i][i]=='X')
                            x++;
                        else if(s[3-i][i]=='O')
                            o++;
                        else if(s[3-i][i]=='T')
                            t++;
                        else if(s[3-i][i]=='.')
                            ans=0;
                    }
                    if(x==4 || (x==3 && t==1))
                        ans=1;
                    if(o==4 || (o==3 && t==1))
                        ans=2;

                    }
                    }

                string ns;
                ns="Case #";
                stringstream ss;
                ss<<z;
                ns+=ss.str();
                ns+=": ";
            if(ans==1)
                ns+="X won";
            else if(ans==2)
                ns+="O won";
            else if(ans==0)
                ns+="Game has not completed";
            else
                ns+="Draw";
        fout<<ns;
        fout<<endl;

    }
    fin.close();
    fout.close();
   // cout<<"l";
 return 0;
}

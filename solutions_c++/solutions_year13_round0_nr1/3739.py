#include<fstream>
using namespace std;
ifstream cin ("temp.in");
ofstream cout ("temp.out");
int main ()
{
    int t;
    cin>>t;
    int i;
    char save[4][4];
    for (i=0;i<t;i++)
    {
        cout<<"Case #"<<i+1<<": ";
        int x,y;
        for (x=0;x<4;x++)
            for (y=0;y<4;y++)
                cin>>save[x][y];
        bool find=true;
        for (x=0;x<4&&find;x++)
        {
            bool can=true;
            for (y=0;y<4&&can;y++) 
                if (save[x][y]!='X'&&save[x][y]!='T')can=false; 
            if (can==true) {cout<<"X won"<<endl;find=false;}
        }
        for (y=0;y<4&&find;y++)
        {
            bool can=true;
            for (x=0;x<4&&can;x++) 
                if (save[x][y]!='X'&&save[x][y]!='T')can=false; 
            if (can==true) {cout<<"X won"<<endl;find=false;}
        }
        if (find)
        {
            bool can=true;
            for (y=0;y<4&&can;y++) 
                if (save[y][y]!='X'&&save[y][y]!='T')can=false; 
            if (can==true) {cout<<"X won"<<endl;find=false;}
        }
        if (find)
        {
            bool can=true;
            for (y=0;y<4&&can;y++) 
                if (save[3-y][y]!='X'&&save[3-y][y]!='T')can=false; 
            if (can==true) {cout<<"X won"<<endl;find=false;}
        }
         for (x=0;x<4&&find;x++)
        {
            bool can=true;
            for (y=0;y<4&&can;y++) 
                if (save[x][y]!='O'&&save[x][y]!='T')can=false; 
            if (can==true) {cout<<"O won"<<endl;find=false;}
        }
        for (y=0;y<4&&find;y++)
        {
            bool can=true;
            for (x=0;x<4&&can;x++) 
                if (save[x][y]!='O'&&save[x][y]!='T')can=false; 
            if (can==true) {cout<<"O won"<<endl;find=false;}
        }
        if (find)
        {
            bool can=true;
            for (y=0;y<4&&can;y++) 
                if (save[y][y]!='O'&&save[y][y]!='T')can=false; 
            if (can==true) {cout<<"O won"<<endl;find=false;}
        }
        if (find)
        {
            bool can=true;
            for (y=0;y<4&&can;y++) 
                if (save[3-y][y]!='O'&&save[3-y][y]!='T')can=false; 
            if (can==true) {cout<<"O won"<<endl;find=false;}
        }
        if (find)
        {
                 int number=0;
                 for (x=0;x<4;x++)
                     for (y=0;y<4;y++)
                         if (save[x][y]!='.') number++;
                 if (number==16) {cout<<"Draw"<<endl;}
                 else cout<<"Game has not completed"<<endl;
        }
    }
    return 0;
}

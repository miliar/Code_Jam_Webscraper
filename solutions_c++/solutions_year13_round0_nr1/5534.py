# include<iostream>
# include<cstdio>
# include<fstream>
# include<sstream>
using namespace std;
int main()
{
    int t,x,y,d,css=0,i,j,c;
    char a[4][4];
    freopen("A-small-attempt0.in","r",stdin);
    cin>>t;
    cin.ignore();
    ofstream m;
    m.open("ou.txt");
    while(t--)
    {
              c=0;
              x=0;
              y=0;
              d=0;
              for(i=0;i<4;++i)
              for(j=0;j<4;++j)
              {
                              cin>>a[i][j];
                              if(a[i][j]=='.')
                              ++d;
              }
              for(i=0;i<4;++i)
              {
                              if((a[i][0]=='X' || a[i][0]=='T') && (a[i][1]=='X' || a[i][1]=='T') && (a[i][2]=='X' || a[i][2]=='T') && (a[i][3]=='X' || a[i][3]=='T'))
                              {
                                                    x=1;
                                                    break;
                              }
                              if((a[i][0]=='O' || a[i][0]=='T') && (a[i][1]=='O' || a[i][1]=='T') && (a[i][2]=='O' || a[i][2]=='T') && (a[i][3]=='O' || a[i][3]=='T'))
                              {
                                                    y=1;
                                                    break;
                              }
              }
              //m<<x<<" "<<y<<endl;
              if(!x && !y)
              {
                    for(i=0;i<4;++i)
                    {
                              if((a[0][i]=='X' || a[0][i]=='T') && (a[1][i]=='X' || a[1][i]=='T') && (a[2][i]=='X' || a[2][i]=='T') && (a[3][i]=='X' || a[3][i]=='T'))
                              {
                                                    x=1;
                                                    break;
                              }
                              if((a[0][i]=='O' || a[0][i]=='T') && (a[1][i]=='O' || a[1][i]=='T') && (a[2][i]=='O' || a[2][i]=='T') && (a[3][i]=='O' || a[3][i]=='T'))
                              {
                                                    y=1;
                                                    break;
                              }
                    }
                    //m<<x<<" "<<y<<endl;
                    if(!x && !y)
                    {
                          i=0;
                          
                                          if((a[i][i]=='X' || a[i][i]=='T') && (a[i+1][i+1]=='X' || a[i+1][i+1]=='T') && (a[i+2][i+2]=='X' || a[i+2][i+2]=='T') && (a[i+3][i+3]=='X' || a[i+3][i+3]=='T'))
                                          x=1;
                                          if((a[i][i]=='O' || a[i][i]=='T') && (a[i+1][i+1]=='O' || a[i+1][i+1]=='T') && (a[i+2][i+2]=='O' || a[i+2][i+2]=='T') && (a[i+3][i+3]=='O' || a[i+3][i+3]=='T'))
                                          y=1;
                          i=3;
                                          if((a[0][i]=='X' || a[0][i]=='T') && (a[1][i-1]=='X' || a[1][i-1]=='T') && (a[2][i+2]=='X' || a[2][i-2]=='T') && (a[3][i-3]=='X' || a[3][i-3]=='T'))
                                          x=1;
                                          if((a[0][i]=='O' || a[0][i]=='T') && (a[1][i-1]=='O' || a[1][i-1]=='T') && (a[2][i-2]=='O' || a[2][i-2]=='T') && (a[3][i-3]=='O' || a[3][i-3]=='T'))
                                          y=1;
                    } 
              }
              m<<"Case #"<<++css<<": ";
              if(x)
              m<<"X won";
              if(y)
              m<<"O won";
              if(!x && !y)
              {
                    if(d)
                    m<<"Game has not completed";
                    else
                    m<<"Draw";
              }
              m<<endl;
              cin.ignore();
    }
    m.close();
    return 0;
}

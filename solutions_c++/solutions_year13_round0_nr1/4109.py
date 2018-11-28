#include<iostream>
#include<cstdlib>
#include<string>
#include<cstdio>

using namespace std;

int main()
{
  int game[17];
  string line;
  int tcases, print, row, pos, col, noto, beg, tot, xwin, owin;

  game[17]='\0';
  print = 1;

  cin>>tcases;

  while(tcases--)
  {
    noto = xwin = owin = pos =0;

    cout<<"Case #"<<print<<": ";
    print++;

    for(row=0;row<4;row++)
    {
      cin>>line;

      for(col=0;col<4;col++,pos++)
      {
        if(line[col] == 'X')
          game[pos] = -1;
        else if(line[col] == 'O')
          game[pos] = 1;
        else if(line[col] == 'T')
          game[pos] = 100;
        else if(line[col] == '.')
        {
          game[pos] = 0;
          noto = 1;
        }
        else cout<<"?????"<<endl;
      }
    }

    for(beg=0;beg<13;beg+=4)
    {
      tot = 0;
      for(row=beg;row<(beg+4);row++)
        tot += game[row];
      if(tot == 103 || tot == 4)      owin = 1;
      else if(tot == 97 || tot == -4) xwin = 1;
    }

    for(beg=0;beg<4;beg++)
    {
      tot = 0;
      for(row=beg;row<(beg+13);row+=4)
        tot += game[row];
      if(tot == 103 || tot == 4)      owin = 1;
      else if(tot == 97 || tot == -4) xwin = 1;
    }

    tot = 0;
    for(row=0;row<16;row+=5)
      tot += game[row];
    if(tot == 103 || tot == 4)      owin = 1;
    else if(tot == 97 || tot == -4) xwin = 1;
    tot = 0;
    for(row=3;row<13;row+=3)
      tot += game[row];
    if(tot == 103 || tot == 4)      owin = 1;
    else if(tot == 97 || tot == -4) xwin = 1; 

    if(xwin)
      cout<<"X won"<<endl;
    else if(owin)
      cout<<"O won"<<endl;
    else if(!noto)
      cout<<"Draw"<<endl;
    else
      cout<<"Game has not completed"<<endl;
  }
  return 0;
}


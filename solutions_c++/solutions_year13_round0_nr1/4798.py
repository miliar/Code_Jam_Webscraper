#include <stdio.h>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <math.h>
#include <string>
#include <vector>
#include <map>
using namespace std;

FILE *fin=freopen("input.txt","r",stdin);
FILE *fout=freopen("output.txt","w",stdout);

int t,tt,i,j,k,cT,cX,cO;
bool room,winX,winO;
vector <string> v;
string tmp,s[4],answer;

main()
{
 cin>>tt;
 for ( t=1;t<=tt;t++ )
  {
   v.clear();
   room=winX=winO=false;

   for ( i=0;i<4;i++ )
    {
     cin>>s[i];
     v.push_back(s[i]);
    }

   for ( j=0;j<4;j++ )
    {
     tmp="";
     for ( i=0;i<4;i++ )
      tmp+=s[i][j];
     v.push_back(tmp);
    }

   tmp=""; tmp+=s[0][0]; tmp+=s[1][1]; tmp+=s[2][2]; tmp+=s[3][3];
   v.push_back(tmp);

   tmp=""; tmp+=s[0][3]; tmp+=s[1][2]; tmp+=s[2][1]; tmp+=s[3][0];
   v.push_back(tmp);

   for ( i=0;i<4;i++ )
    for ( j=0;j<4;j++ )
     if ( s[i][j]=='.' )
      room=true;

   for ( k=0;k<v.size();k++ )
    {
  //   cout<<"-> "<<v[k]<<endl;
     cX=0;
     cO=0;
     cT=0;
     for ( i=0;i<v[k].size();i++ )
      if ( v[k][i]=='T' ) cT++;
      else if ( v[k][i]=='X' ) cX++;
           else if ( v[k][i]=='O' ) cO++;

     if ( cX+cT == 4 ) winX=true;
     if ( cO+cT == 4 ) winO=true;
    }

   if ( winX ) answer="X won";
   else if ( winO ) answer="O won";
   else if ( room ) answer="Game has not completed";
   else answer="Draw";

   cout<<"Case #"<<t<<": "<<answer<<endl;
  }
}

#include <fstream>
#define rep(x,y,z) for (int x=y;x<=z;x++)
using namespace std;
ifstream fin("A.in");
ofstream fout("A.out");
string s[6];
int n,r,k,tr;
char c,r1;

int main()
{
    fin>>n;
    getline(fin,s[1]);
    rep(t,1,n)
    {
              tr=0;
              r=0;
              rep(i,0,4)
                        getline(fin,s[i]);
              fout<<"Case #"<<t;
              rep(i,0,3)
              rep(j,0,3)
              if (s[i][j]=='.') {r=1; break;}
              if (r==1) tr=1; 
              r=0;
              rep(i,0,3)
              {
                        k=1;
                        c=s[i][0];
                        if (c=='T') c=s[i][1];
                        if (c!='.') rep(j,1,3)
                        if (s[i][j]!=c && s[i][j]!='T')  {k=1; break;} else k=0;
                        if (k==0) {r=1;r1=c;break;} 
                        c=s[0][i];
                        k=1;
                        if (c=='T') c=s[1][i];
                        if (c!='.')rep(j,1,3)
                        if (s[j][i]!=c && s[j][i]!='T')  {k=1; break;} else k=0;
                        if (k==0) {r=1;r1=c;break;}
                        }
              c=s[0][0];
              k=1;
              if (c=='T') c=s[1][1];
              if (c!='.')rep(j,1,3)
              if (s[j][j]!=c && s[j][j]!='T')  {k=1; break;} else k=0;
              if (k==0) {r=1;r1=c;}
              c=s[0][3];
              k=1;
              if (c=='T') c=s[1][1];
              if (c!='.') rep(j,1,3)
              if (s[j][3-j]!=c && s[j][3-j]!='T')  {k=1; break;} else k=0;
              if (k==0) {r=1;r1=c;}
              if (r==1) fout<<": "<<r1<<" won"; else if (tr) fout<<": Game has not completed"; else fout<<": Draw";

              fout<<"\n";
              }
    return 0;
}

              
              
                        

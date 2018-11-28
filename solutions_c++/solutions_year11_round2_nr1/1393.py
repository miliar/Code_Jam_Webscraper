#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

double wp[100];
double owp[100];
double oowp[100];
char ch[100][100];
bool team[100][100];

void cal_wp(int n)
{
     for (int i=0; i<n; i++)
     {
         int w=0;
         int siz =0;
         for (int j=0; j<n; j++)
         { if (team[i][j])
           {
                     siz++;
                     if (ch[i][j]=='1') { w++; }
           }
         }
         wp[i] = double(w)/double(siz);
         //cout<<wp[i]<<endl;
     }
     //cout<<"wp\n";
}

void cal_oowp(int n)
{
     for (int i=0; i<n; i++)
     {
         double towp=0;
         int siz =0;
         for (int j=0; j<n; j++)
         { if (team[i][j])
           {
                     siz++;
                     towp+=owp[j];
           }
         }
         oowp[i] = towp/double(siz);
         //cout<<oowp[i]<<endl;
     
     }
//cout<<"oowp\n";
}

void cal_oop(int n)
{
     for (int i=0; i<n; i++)
     {
         double toop=0;
         int siz =0;
         for (int j=0; j<n; j++)
         { if (team[i][j])
           {
                     siz++;
                     double b= wp[j];
                     int p_s =0;
                     for (int k=0; k<n; k++)
                     {
                         if (ch[j][k]!='.') {p_s++;} }
                     double c = b*p_s;
                     if (ch[i][j]=='0') { c--; }
                     toop+= c/(p_s-1);
           }
         }
         owp[i] = toop/siz;
         //cout<<owp[i]<<endl;
     }
     //cout<<"owp\n";
}

void convert(int n)
{
   for (int i=0; i<n; i++)
   {
       for (int j=i+1; j<n;j++)
       {
           if ((ch[i][j]=='0') || (ch[i][j]=='1'))
           {
                             team[i][j] = true;
                             team[j][i] = true;
           }
       }
}
}          


int main(){
    ifstream fin;
    ofstream fout;
    
    fin.open("a.in");
    fout.open("output.txt");
    int test=0;
    int t;
    fin>>t;
    while (test!=t)
    {
          test++;
          memset(wp,0,sizeof(wp));
          memset(team,0,sizeof(team));
          memset(ch,0,sizeof(ch));
          memset(owp,0,sizeof(owp));
          memset(oowp,0,sizeof(oowp));
          
          int n;
          fin>>n;
          for (int i=0; i<n; i++)
          {
              for (int j=0; j<n; j++)
              {
                  fin>>ch[i][j];
              }
          }
          convert(n);
          cal_wp(n);
          cal_oop(n);
          cal_oowp(n);          
          
          fout<<"Case #"<<test<<":\n";
          cout<<"Case #"<<test<<":\n";
          for (int i=0; i<n; i++)
          {
              fout<<setprecision (6)<<0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]<<endl;
              cout<<setprecision (6)<<0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]<<endl;
          }
    }
    
    fin.close();
    fout.close();
    system("pause");
    return 0;
}

#include<iostream>
#include<fstream>
using namespace std;
ifstream fin("A-large.in");
ofstream fout("A-large.out");
char A[101][101];
double WP[101];
double OWP[101];
double OOWP[101];
int N;

double wp(int index)
{
    int n = 0;
    int w = 0;
    for(int i=1;i<=N;i++)
       if(A[index][i]!='.')
       {
           n++;
           if(A[index][i]=='1')
              w++;
       }
    return w*1.0/n;
}

double owp(int index)
{
    int n = 0;
    double wp = 0;
    double WPP[101];
        
    for(int i=1;i<=N;i++)
       if(i!=index)
       {
           int n = 0;
           int w = 0;
           for(int j=1;j<=N;j++)
              if(j!=index&&A[i][j]!='.')
              {
                  n++;
                  if(A[i][j] == '1')
                     w++;
              }
           WPP[i] = w*1.0/n;
       }
    for(int i=1;i<=N;i++)
       if(A[i][index]!='.')
       {
          n++;
          wp += WPP[i]; 
       }
    return wp/n;
}

double oowp(int index)
{
    int n = 0;
    double owp = 0;
    for(int i=1;i<=N;i++)
       if(A[i][index]!='.')
       {
           n++;
           owp += OWP[i];
       }
    return owp/n;
}

void process(int t)
{
    fout<<"Case #"<<t<<":\n";
    fin>>N;
    for(int i=1;i<=N;i++)
       for(int j=1;j<=N;j++)
           fin>>A[i][j];
    for(int i=1;i<=N;i++)
        WP[i] = wp(i);

    for(int i=1;i<=N;i++)
        OWP[i] = owp(i);
    for(int i=1;i<=N;i++)
        OOWP[i] = oowp(i);
    for(int i=1;i<=N;i++)
        fout<<0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]<<endl;
}

int main()
{
    int T;
    fin>>T;
    for(int i=1;i<=T;i++)
       process(i);
    //system("pause");
    return 0;
}

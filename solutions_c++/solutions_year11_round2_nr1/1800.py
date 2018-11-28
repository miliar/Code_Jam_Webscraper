#include<iostream>


using namespace std;


int main(){

  int T, N;
  int i,j,t=0,k;
  double mp, mw;
  double oc, swp;

  char ch;

  int mat[101][101];
  double owp[101];
  double wp[101];
  double oowp[101];
  double rpi;

  cin>>T;


  t=0;
  while(t++<T){

    cin>>N;

    for(i=0;i<N;i++)
    {
      for(j=0;j<N;j++)
      {
        cin>>ch;
        if(ch=='0')
          mat[i][j] = 0;
        else if (ch=='1')
          mat[i][j] = 1;
        else mat[i][j]=-1;
      }
    }

    /*WP*/
    for(i=0;i<N;i++)
    {
      mp=0;mw=0;

      for(j=0;j<N;j++)
      {
        if(mat[i][j] != -1)
        {
          mp++;
          if(mat[i][j])
            mw++;
        }
      }
      wp[i]= mw/mp; 
    }

    /* OWP */

    for(k=0;k<N;k++)
    {
      oc=0;
      swp=0;

      for(i=0;i<N;i++)
      {
        if(mat[i][k] == -1) continue;

        oc++;
        mp=0;mw=0;

        for(j=0;j<N;j++)
        {
          if(j==k) continue;

          if(mat[i][j] != -1)
          {
            mp++;
            if(mat[i][j])
              mw++;
          }
        }
        swp += mw/mp; 
      }
      owp[k] = swp/oc;
    }

    /* OOWP */

    for(i=0;i<N;i++)
    {
      oc=0;
      swp=0;
      for(j=0;j<N;j++)
      {
        if(mat[i][j] != -1)
        {
          oc++;
          swp += owp[j];
        }
        oowp[i]= swp/oc;
      }
    }

    cout<<"Case #"<<t<<":"<<endl;
    for(i=0;i<N;i++)
    {
      rpi = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
      printf("%0.12lf\n",rpi);
    }

  }
  return 0;
}

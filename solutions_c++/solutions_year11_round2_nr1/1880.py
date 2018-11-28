#include<iostream>

using namespace std;



class games
{
      private:
      int M[105][105];
      float WP[101], OWP[101], OOWP[101], RPI[101];
      int T,N,i,j,k,l,count,mat;
      float sum;
      char str[205];
      
      public:
      void control();
      void wp();
      void owp();
      void oowp();
      void rpi();
      void output();
             
};



void games::control()
{
     cin>>T;
     
     for(i=1;i<=T;++i)
     {
                      
                      cin>>N;
                      
                      for(j=0;j<N;++j)
                      {
                                      l=0;
                                      count=0;
                                      mat=0;
                                      cin>>str;
                                      
                                      for(k=0;str[k]!='\0';k++)
                                      {
                                        if(str[k]=='0')
                                        {M[j][l++] = 0; mat++;}
                                        else if(str[k]=='1')
                                        {M[j][l++] = 1; count++; mat++;}
                                        else if(str[k]=='.')
                                        {M[j][l++] = -1;}
                                      }
                                      
                                      M[j][l++] = count;
                                      M[j][l++] = mat;
                      }
                      
     
                     for(j=0;j<N;++j)
                     wp();
                     
                     for(j=0;j<N;++j)
                     owp();
                     
                     for(j=0;j<N;++j)
                     oowp();
                     
                     for(j=0;j<N;++j)
                     rpi();
     
     output();
     }
}



void games::wp()
{
     WP[j] = ((float)M[j][N]) / M[j][N+1];
}


void games::owp()
{
     sum=0;
     
     for(k=0;k<N;++k)
     {
                     if(M[j][k] == 0 || M[j][k] == 1)
                     {
                                if(M[k][j] == 1)
                                sum += ((float)(M[k][N] - 1))/(M[k][N+1] - 1);
                                
                                else
                                sum += ((float)(M[k][N]))/(M[k][N+1] - 1);
                     }
     }
     
     OWP[j] = sum/M[j][N+1];
}


void games::oowp()
{
     sum=0;
     
     for(k=0;k<N;++k)
     {
                     if(M[j][k] == 0 || M[j][k] == 1)
                     {
                                sum += OWP[k];
                     }
     }
     
     OOWP[j] = sum/M[j][N+1];
}


void games::rpi()
{
     RPI[j] = 0.25 * WP[j] + 0.50 * OWP[j] + 0.25 * OOWP[j];
}



void games::output()
{
     cout<<"Case #"<<i<<":"<<'\n';
     
     for(j=0;j<N;++j)
     {
                     cout.precision(12);
                     
                     cout<<RPI[j]<<'\n';
     }
}



int main()
{
    games obj;
    obj.control();
    
    return 0;
}

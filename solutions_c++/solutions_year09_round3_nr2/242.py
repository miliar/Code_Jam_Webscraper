# include<iostream>
# include<cmath>
# include<cstdio>

using namespace std;

int main ()
{
    int test;
    cin>>test;
    int j=1;
    while (test--)
    {
          int N;
          double x,y,z,vx,vy,vz;
          double mx=0.0,my=0.0,mz=0.0,mvx=0.0,mvy=0.0,mvz=0.0;
          cin>>N;
          for (int i=0;i<N;i++)
          {
              cin>>x>>y>>z;
              cin>>vx>>vy>>vz;
              mx+=x;
              my+=y;
              mz+=z;
              mvx+=vx;
              mvy+=vy;
              mvz+=vz;    
          }
          mx/=N;
          my/=N;
          mz/=N;     
          mvx/=N;
          mvy/=N;
          mvz/=N;
          double first=(double)((mvx*mvx)+(mvy*mvy)+(mvz*mvz));
          double second=(double)((mvx*mx)+(mvy*my)+(mvz*mz));
          double time=0.0;
          double dist=0.0;
          //cout<<first<<" "<<second<<endl;
          if (first==0.0)
          {
              time=0.0;
              //cout<<"MAN"<<endl;
              dist=sqrt ((pow((double) (mx),2))+(pow((double) (my),2))+(pow((double) (mz),2)));
          } 
          else
          {             
                        //cout<<"Here"<<endl;
          time=-(second)/(first);
          dist=0.0;
          if (time<0.0)
          {
             time=0.0;
             dist=sqrt ((pow((double) (mx),2))+(pow((double) (my),2))+(pow((double) (mz),2)));
          }
          else
          {
              double mx1=mx+mvx*time;
              double my1=my+mvy*time;
              double mz1=mz+mvz*time;
              dist=sqrt ((pow((double) (mx1),2))+(pow((double) (my1),2))+(pow((double) (mz1),2)));
          }
          }
          cout<<"Case #"<<j<<": ";  
          printf ("%f %f\n",dist,time);
          j++;
    }
    return 0;
}            
               

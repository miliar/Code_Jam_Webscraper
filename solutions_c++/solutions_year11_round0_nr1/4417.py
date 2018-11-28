//bot trust

#include<iostream>

using namespace std;

int main()
{
  int t,time[101],i,poso=1,posb=1,p[101],n,j,tim,tim2;
  //int flago,flagb;
  //int m;
  char r[101];


  cin>>t;//test cases

    for(i=0;i<t;i++)
    time[i]=0;


  for(i=0;i<t;i++)
  {
    cin>>n; //length of arrays p and r

    poso=1;
    posb=1;
    //flago=0;
    //flagb=0;
    //m=0;
    //tim=0;

    for(j=0;j<n;j++)
    {
        cin>>r[j];
        cin>>p[j];
    }

    for(j=0;j<n;j++)
    {
        if(r[j]=='O')
        {
            //flago=1;
            tim=poso-p[j];
            if(tim<0)
                tim=0-tim;
            time[i]+=tim;
            for(int k=j+1;k<n;k++)
            {
                if(r[k]=='B')
                {
                    tim2=posb-p[k];
                    if(tim2<0)
                        tim2=0-tim2;
                    else{}
                    if(tim2<=tim+1)
                        posb=p[k];
                    else
                    {
                        if(posb<p[k])
                            posb+=tim+1;
                        else
                            posb=posb-tim-1;
                    }
                    break;
                }
            }
            time[i]++;//to push button
            poso=p[j];
            //flago=0;
        }
        else
        {
            //flagb=1;
            tim=posb-p[j];
            if(tim<0)
                tim=0-tim;
            time[i]+=tim;
            for(int k=j+1;k<n;k++)
            {
                if(r[k]=='O')
                {
                    tim2=poso-p[k];
                    if(tim2<0)
                        tim2=0-tim2;
                    else{}
                    if(tim2<=tim+1)
                        poso=p[k];
                    else
                    {
                        if(poso<p[k])
                            poso+=tim+1;
                        else
                            poso=poso-tim-1;
                    }
                    break;
                }
            }
            time[i]++;
            posb=p[j];
            //flagb=0;
        }
    }



  }

    for(i=0;i<t;i++)
    {
        cout<<"Case #"<<i+1<<": "<<time[i]<<endl;
    }

  return 0;
}

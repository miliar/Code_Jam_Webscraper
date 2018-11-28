#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;

int main()
{
    int t,n;
    int btn[100];
    char bot[100];
    int p1,p2,t1,t2,time;
    
    fstream fin,fout;
    fin.open("a.in",ios::in);
    fout.open("a.out",ios::out);
    
    fin >> t;
    for(int i=0;i<t;i++)
    {
        fin >> n;
        for(int j=0;j<n;j++)
        {
            fin >> bot[j] >> btn[j];
        }
        fout<<"Case #"<<i+1<<": ";
        p1=p2=1;
        time=t1=t2=0;
        
        for(int k=0;k<n;k++)
        {
            //cout<<bot[k];
            if(bot[k]=='O')
            {
                
                int temp=btn[k]-p1;
                if(temp<0) temp= -temp;
                
                if(t1<time && temp<(time-t1))
                    t1=time+1;
                else
                    t1+=temp+1;
                    
                p1=btn[k];
                if(t1==time)
                {
                    t1++;
                    time++;
                }
                else if(t1>time)
                    time=t1;
                
               // if(i==16) cout<<t1<<endl;
            }
            else
            {
                
                int temp=btn[k]-p2;
                if(temp<0) temp= -temp;
                
                if(t2<time && temp<(time-t2))
                    t2=time+1;
                else    
                    t2+=temp+1;
                    
                p2=btn[k];    
                if(t2==time)
                {
                    t2++;
                    time++;
                }
                else if(t2>time)
                    time=t2;
               // if(i==16) cout<<t2<<endl;
            }
        }
        //val=(t1>t2)?t1:t2;
        fout<<time<<endl;
    }
    int x;
    cin>>x;
    return 0;
}

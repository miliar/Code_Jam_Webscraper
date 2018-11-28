#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int max,i,j,num,minw,minwi,cnt,t,val,S,r12,r22;
    fstream fp;
    fp.open("input.txt");
    fp >> t;
    for(i=0;i<t;i++)
    {
            //total=0;
            fp >> num;
            fp >> S;
            fp >> max;
            minw=max+max-2+max-2;  //for str
         //   r12=max+max+2+max+2; //for str
           // r2=max+max+1+max+1;
            minwi=max+max-1+max-1;
            if(minw<0)
                minw=1;
            cnt=0;
            for(j=0;j<num;j++)
            {
                fp >> val;
                if(S==0)
                {
                    if(val>=minwi)
                    {
                        //cout<<"case "<<i+1<<"Val is "<<val<<endl;
                        cnt++;
                    }
                }
                else if(S>0)
                {
                    if(val>=minwi)
                    {
                      //  cout<<"case "<<i+1<<"Val is "<<val<<endl;
                        cnt++;
                        //S--;
                    }
                    else if(val>=minw)
                    {
                      //  cout<<"case "<<i+1<<"Val is "<<val<<endl;
                        cnt++;
                        S--;
                    }

                }

            }
             cout<<"Case #"<<i+1<<": "<<cnt<<endl;
    }
}

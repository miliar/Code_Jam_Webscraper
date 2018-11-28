#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
using namespace std;

int formnumber(string number)
{
    int len = number.size(); 
    //cout<<"\nthe length is "<<len;   
    int num=0;
    for(int i=0;i<len;i++)
    {
            num*=10;
            num+=number[i]-48;
    }
    //cout<<"inside the form number part.. return ing "<<num;
    return num;            
}


int formabstime(string time)
{
    int abstime;
    string hour,min;
    bool passedcolon=false;
    for(int i=0;i<time.size();i++)    
    {
            if(time[i]==':')
            {
               passedcolon=true;
               continue;
            }
            if(!passedcolon)
               hour=hour+time[i];
            else
                min=min+time[i];
    }
    abstime=formnumber(hour)*60+formnumber(min);
    return abstime;
    
}

int main(void)
{
    int N;
    fstream inp("B-large.in",ios::in);
    inp>>N;    
    for(int i=1;i<=N;i++)
    {
            int turnaroundtime;
            int NA,NB;
            inp>>turnaroundtime;
            inp>>NA>>NB;
            //cout<<"\nturaroundtime "<<turnaroundtime;
            //cout<<"\n\narrival from a "<<NA;
            //cout<<"\narrival from b "<<NB;
            //break;*/
            vector<int> adep,aarr,bdep,barr;
            for(int j=1;j<=NA;j++)
            {
               string dep,arr;
               inp>>dep>>arr;
               //cout<<"\n"<<arr<<" "<<dep;
               
               
               adep.push_back(formabstime(dep));
               aarr.push_back(formabstime(arr)+turnaroundtime);
              // cout<<"\n"<<adep.back()<<" "<<aarr.back();
            }            
            for(int j=1;j<=NB;j++)
            {
               string arr,dep;
               inp>>dep>>arr;
               //cout<<"\n"<<arr<<" "<<dep;                    
               bdep.push_back(formabstime(dep));
               barr.push_back(formabstime(arr)+turnaroundtime);
               //cout<<"\n"<<bdep.back()<<" "<<barr.back();
            }
            sort(adep.begin(),adep.end());
            sort(aarr.begin(),aarr.end());
            sort(bdep.begin(),bdep.end());
            sort(barr.begin(),barr.end());
            /*cout<<"\n\n";
            cout<<"\n a deperature times ";
            for(int j=0;j<adep.size();j++)
            cout<<"\n"<<adep[j];
            cout<<"\n a arrival times ";
            for(int j=0;j<aarr.size();j++)
            cout<<"\n"<<aarr[j];
            cout<<"\n b deperture times ";
            for(int j=0;j<bdep.size();j++)
            cout<<"\n"<<bdep[j];
            cout<<"\n b arrival times ";
            for(int j=0;j<barr.size();j++)
            cout<<"\n"<<barr[j];
            
            /******** Calculating atrains ************/
            int atrain=0;
            int bstart=0;            
            for(int j=0;j<adep.size();j++)
            {
                    if(!barr.empty() && bstart >=0 && barr[bstart]<=adep[j])
                    {
                       bstart++;                    
                       if(bstart>=barr.size())
                                              bstart=-1;
                    }
                    else
                       atrain++;
                    
            }            
            /*****************************************/
            
            /********** Calculating btrains ***********/
            int btrain=0;
            int astart=0;
            for(int j=0;j<bdep.size();j++)
            {
                    if(!aarr.empty() && astart >=0 && aarr[astart]<=bdep[j])
                    {
                       astart++;                    
                       if(astart>=aarr.size())
                                              astart=-1;
                    }
                    else
                       btrain++;
                    
            }
            cout<<"\nCase #"<<i<<": "<<atrain<<" "<<btrain;
            /******************************************/
    }    
    inp.close();    
    return 0;
}

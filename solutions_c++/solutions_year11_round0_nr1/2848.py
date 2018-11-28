#include<iostream>
#include<vector>
#include<cmath>

using namespace std;

int main()
{
    int t;
    cin>>t;
    int counter=0;
    while(t>0)
    {
        counter++;
        int n,i,b=0,o=0,time=0,pob=1,poo=1,k=0,l=0;
        cin>>n;
        vector <char> ro(n);
        vector <int> bu(n);
        vector <int>blue(n);
        vector<int> orange(n);
        for(i=0;i<n;i++)
       {
             cin>>ro[i]>>bu[i];
             if(ro[i]=='O')
             orange[o++]=bu[i];
             else
             blue[b++]=bu[i];
       }
       for(i=0;i<n;i++)
       {
              if(ro[i]=='O')
              {  
                          int ttime=abs(orange[l]-poo)+1;
                          time+=ttime;
                          poo=orange[l];
                          l++;
                          if(k<b)
                          {int temp=blue[k]-pob;
                          if(temp>=0)
                              pob=pob+min(ttime,temp);
                          else
                             pob=pob-min(ttime,abs(temp));}
              }
              else
              {
                            int ttime=abs(blue[k]-pob)+1;
                            time+=ttime;
                            pob=blue[k];
                            k++;
                            if(l<o)
                            {int temp=orange[l]-poo;
                            if(temp>=0)
                               poo=poo+min(ttime,temp);
                            else
                                poo=poo-min(ttime,abs(temp));}
       }}
       cout<<"Case #"<<counter<< ": "<<time<<endl;
       t--;
       }
    }

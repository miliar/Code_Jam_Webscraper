
#include <cstdio>
#include <iostream>
#include <conio.h>
#include <queue>
using namespace std;
    
class systime{
       public:
       int hr;
       int min;
       systime()
       {
           hr = 0;
           min = 0;
       }
       void incr()
       {
           if(min<59)
           {
               min++;
           }
           else
           {
               hr++;
               min=0;
           }
       }
};

int find_valid_min(vector <systime>, vector <int>);
int t_less(systime, systime, int);
    


int main()
{
    systime t;
    int no_of_cases, forp=1, d;
    scanf("%d", &no_of_cases);
    d = no_of_cases;
    while(no_of_cases--)
    {
        int turn_time;
        scanf("%d", &turn_time);
       // cout<<"tt"<<turn_time;
        int na, nb;
        scanf("%d", &na);
        scanf("%d", &nb);
        int nt = na+nb;
        nt=nt*2;
        int ta=0, tb=0;
        int ansa=0, ansb=0;                
        vector <systime> a;
        vector <int> entry;
        queue <systime>aq;
        queue <systime>bq;
        //cout<<"here3";
        while (nt--)
        {
            systime temp;
            scanf("%d:%d", &temp.hr, &temp.min);
            a.push_back(temp);
          //  cout<<temp.hr<<":"<<temp.min<<"\n";
            entry.push_back(1);
        }
     //   cout<<"-----------\n";
        systime gclock;
        int check=0;
 //       for(int i=0;i<a.size();i++)
 //               cout<<a[i].hr<<":"<<a[i].min<<"\n";
        while(gclock.hr<24)
        {
            int f;
            f = find_valid_min(a, entry); // one more check here
            if(!(aq.empty()))
            {
                systime t;
                t=aq.front();
     //           printf("partially ready to go from a");
      //          cout<<t.hr<<":"<<t.min;
      //          getch();
                if(t_less(t, gclock, turn_time))
                {
                    ta++;
                    aq.pop();
                  //  cout<<"ready to go from a";
                }
            } 
            if(!(bq.empty()))
            {
                systime t;
                t = bq.front();
                if(t_less(t, gclock, turn_time))
                {
                    tb++;
                    bq.pop();
                 //   cout<<"ready to go from b";
                }
            }
            if((gclock.hr>a[f].hr)||((gclock.hr==a[f].hr)&&(gclock.min>=a[f].min)))
            {   
                gclock.hr=a[f].hr;
                gclock.min=a[f].min;
           //     cout<<"f-"<<f;
              //  cout<<" "<<gclock.hr<<":"<<gclock.min<<"\n";
                if (f%2==0)      // leave
                {
                    if(f<na*2)      //station A
                    {
                        if(ta>0)     // train present??
                        {
                            ta--;
                        }
                        else
                        {
                       //     cout<<"now";
                            ansa++;
                      //      cout<<"ina";
                        }
                    }
                    else    //station b
                    {
                        if(tb>0)
                        {
                            tb--;        
                        }
                        else
                        {
                            ansb++;
                      //      cout<<"inb";
                        }
                    }   
                }
                else              // arrival
                {
                    if(f>na*2)    // station A
                    {
                        aq.push(a[f]);
                   //     cout<<"arrived at a";
                    }
                    else           //station b
                    {
                        bq.push(a[f]);
                   //     cout<<"arived at b";
                    }
                }
                entry[f] = 0;
            } // gclock check
            
            
            gclock.incr();
        }    // while gcclock   wont need it
    //cout<<"here2"<<no_of_cases;
    cout<<"Case #"<<forp<<": "<<ansa<<" "<<ansb;
    if(forp!=d)
        cout<<"\n";
    forp++;
    //getch();
    }// end of a test case

    return 0;
}

int find_valid_min(vector <systime> t, vector <int>e)
{
    int count=-1;
    systime temp;
    temp.hr = 25;
    temp.min = 65;
    for(int i=0;i<t.size();i++)
    {
        if ((t[i].hr<temp.hr)&&(e[i]==1))
        {
            count = i;
            temp.hr = t[i].hr;
            temp.min = t[i].min;
        }    
        if((t[i].hr == temp.hr)&&(e[i]==1))
        {
            if(t[i].min<temp.min)
            {
                temp.min = t[i].min;
                count = i;
            }
        }
        if((t[i].hr==temp.hr)&&(t[i].min==temp.min)&&(e[i]==1))
        {
            if(i%2!=0)
            {
                count=i;
            }
        }
    }
    return count;
}

int t_less(systime t, systime gclock, int tt)
{
    for(int i=0;i<tt;i++)
    {
        t.incr();
    }
//cout<<"-----------";
//cout<<t.hr<<":"<<t.min;
//cout<<gclock.hr<<":"<<gclock.min;
//cout<<"------------";
    if(t.hr<gclock.hr)
        return 1;
    else if((t.hr==gclock.hr)&&(t.min<=gclock.min))
        return 1;
    else
        return 0;
}

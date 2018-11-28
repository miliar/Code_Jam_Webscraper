#include<iostream>
#include<list>
using namespace std;
int main(){
    int t;
    scanf("%d",&t);
    int left=t;
    while(left--)
    {
    long long r,k,n,i,p,tempk,poped,count,count1=1,popedflag=0,division=0;
    long long profit=0;
    scanf("%lld %lld %lld",&r,&k,&n);
    list<long long> g;
    list<long long> flag;
    list<long long> cost;
    list<long long> counter;
    for(i=0;i<n;i++)
    {
        counter.push_back(0);
        cost.push_back(0);
        flag.push_back(0);
        scanf("%lld",&p);
        g.push_back(p);
       // cout<<i<<endl;
    }
    //cout<<"Input complete";
    while(r--)
    {
        tempk=0;
        count=0;
        while(tempk+*g.begin()<=k)
        {
            //cout<<
            //cout<<"count="<<count<<"size="<<g.size()<<endl;
            if(count==g.size())
                break;
            poped=*g.begin();
            popedflag=*flag.begin();
            //printf("%d\n",popedflag);
            if(popedflag==0 && count==0 && division==0)
            {
               // cout<<"m here"<<endl;
                popedflag=1;
                cost.pop_front();
                cost.push_front(profit);
                counter.pop_front();
                counter.push_front(r);
            }
            else if(count==0 && popedflag==1 && division==0)
            {
                //cout<<endl<<"g="<<*g.begin()<<endl;
                //cout<<endl<<"cb="<<*cost.begin()<<"profit="<<profit<<endl;
                if(*cost.begin()==0)
                {

                    cost.pop_front();
                    cost.push_front(profit);
                    counter.pop_front();
                    counter.push_front(r);
                }
                else
                {
                long long cyclecost=profit-*cost.begin();
                //cout<<endl<<"cyclecost="<<cyclecost<<endl;
                //cout<<endl<<*counter.begin()<<"   ";
                long long cyclespan=*counter.begin()-r;
               // cout<<"r="<<r<<" cyclespan="<<cyclespan<<endl;
                long long factor=(r+1)/cyclespan;
               // cout<<endl<<"factor="<<factor<<endl;
               // cout<<endl<<"old profit="<<profit<<endl;
               // cout<<endl<<"c*f"<<cyclecost*factor<<endl;
                profit+=cyclecost*factor;
              //  cout<<endl<<"new profit="<<profit<<endl;
                r=r-(cyclespan*factor);
               // cout<<endl<<"new r="<<r<<endl;
                if(r<0)
                    break;
                division=1;
                }

            }
            tempk+=poped;
            profit+=poped;
            poped=poped;
            g.pop_front();
            flag.pop_front();
            //cout<<"cb of g="<<poped<<" is="<<*cost.begin()<<" profit=";
            cost.push_back(*cost.begin());
            cost.pop_front();
            counter.push_back(*counter.begin());
            counter.pop_front();
            g.push_back(poped);
            flag.push_back(popedflag);
            count++;
           // cout<<"profit="<<profit<<endl;
            //cout<<" "<<poped<<"\n";
        }
        //cout<<endl;
        if(r<0)
        break;
    }
    printf("Case #%d: %lld\n",(t-left),profit);
    }
    return 0;
}

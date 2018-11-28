#include <iostream>
#include <string>
using namespace std;

struct list{
       list(int x,list* n){
              value=x;
              next=n;
       }
       int value;
       list* next;
};
class queue{
      list* head;
      public:queue(){
              head=new list(0,NULL);
      }
      public:
              void in(int a){
             list* item;
             list* temp=head;
             while(temp->next!=NULL&&temp->next->value<a)temp=temp->next;
             item=new list(a,temp->next);
             temp->next=item;
      }
      public: int first(){
             if(head->next==NULL)return -1;
             return head->next->value;       
      }
      public: void removefirst(){
             // if(head->next==NULL)return;
             list* temp=head;
             head=head->next;
             delete temp;      
      }
};

int convert(string s1){
    int time=0;
    time+=s1[0]*600;
    time+=s1[1]*60;
    time+=s1[3]*10;
    time+=s1[4]*1;
    return time;
}
int main()
{
    int N,Time,Na,Nb;
    cin>>N;
    for(int i=0;i<N;++i)
    {
            cin>>Time;
            cin>>Na>>Nb;
            queue a1,a2,b1,b2;
            string temp;
            for(int j=0;j<Na;++j)
            {
                    cin>>temp;
                    a1.in(convert(temp));
                    cin>>temp;
                    a2.in(convert(temp));
            }        
            for(int k=0;k<Nb;++k)
            {
                    cin>>temp;
                    b1.in(convert(temp));
                    cin>>temp;
                    b2.in(convert(temp));
            }
            int save1=0,save2=0;
            for(int j=0;j<Na;++j)
            {
                    if(b2.first()==-1)break;
                    if(a1.first()>=b2.first()+Time)
                    {
                            ++save1;
                            b2.removefirst();
                    }
                    a1.removefirst();
            }
            for(int j=0;j<Nb;++j)
            {
                    if(a2.first()==-1)break;
                    if(b1.first()>=a2.first()+Time)
                    {
                            ++save2;
                            a2.removefirst();
                    }
                    b1.removefirst();
            }
            cout<<"Case #"<<i+1<<": "<<Na-save1<<" "<<Nb-save2<<endl;
    }
    return 0;
}

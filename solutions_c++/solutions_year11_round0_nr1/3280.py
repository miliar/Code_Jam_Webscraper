#include<iostream>
using namespace std;

class bot
{
      private:
      int T,N,p,i,j,k,l,m,n, orange[101], blue[101], time, t;
      int ocur, bcur;
      char R, order[101];
      int x;
      
      public:
      void control();
      void init();
};


void bot::control()
{
     cin>>T;
     
     for(i=1;i<=T;++i)
     {        
        init();
        
        cin>>N;
        
        for(j=0;j<N;++j)
        {
          cin>>R;
          cin>>p;
          
          order[j] = R;
          
          if(R == 'O')
          {
               orange[k++] = p;
          }
          
          else if(R == 'B')
          {
               blue[l++] = p;
          }
        }
        //end of input for a  test case
        
        
        m=0;
        n=0;
        for(j=0;j<N;++j)
        {  
           if(order[j]=='O')
           {
               t = abs(orange[m] - ocur) + 1;
               time += t;
               ocur = orange[m];
               m++;
               
               if(n<l)
               {
                       if(abs(blue[n] - bcur) > t)
                       {
                                if(blue[n]>bcur)
                                    bcur += t;
                                else
                                    bcur -= t;
                       }
                       else
                       {
                           bcur = blue[n];
                       }
               }
           }
           
           else if(order[j]=='B')
           {
               t = abs(blue[n] - bcur) + 1;
               time += t;
               bcur = blue[n];
               n++;
               
               if(m<k)
               {
                       if(abs(orange[m] - ocur) > t)
                       {
                                if(orange[m]>ocur)
                                    ocur += t;
                                else
                                    ocur -= t;
                       }
                       else
                       {
                           ocur = orange[m];
                       }
               }               
           }
           
        }
        //end of evaluation of time
        
        //printing the output
        cout<<"Case #"<<i<<": "<<time<<'\n';
        
     }
     //end of a test case
}


void bot::init()
{
        k   = 0;
        l   = 0;
        time=0;
        ocur=1;
        bcur=1;
}

int main()
{
    bot obj;
    obj.control();
    return(0);
}

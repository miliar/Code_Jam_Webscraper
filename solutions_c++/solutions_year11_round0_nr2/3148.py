#include<iostream>

using namespace std;

class magicka
{
      private:
      int T,C,D,N,i,j,k,first;
      char list[11];
      int last, dest;
      char comb[3];
      char opp[2];
              
      public:
      void control();
      void only_comb();
      void only_opp();
      void both();
      void output();
};

void magicka :: control()
{
     cin>>T;
     for(i=1;i<=T;++i)
     {
                      
                      
                      last = -1;
                      dest = -1;
                      
                      cin>>C;
                      if(C==1)
                      cin>>comb;
                      
                      cin>>D;
                      if(D==1)
                      cin>>opp;
                      
                      cin>>N;
                      cin>>list;
                      
                      //if(C==0 && D==0)
                      //list will remain as it is
                      
                      if(C==1 && D==0)
                      {
                           only_comb();
                      }
                      
                      else if(C==0 && D==1)
                      {
                           only_opp();
                      }
                      
                      else if(C==1 && D==1)
                      {
                          both();
                      }
                      
                      
                      // if C or D or both are zero we won't have any problem of
                      // the opposing and combining chars of previous case getting
                      // used as we have different functions for every case
                      cout<<"Case #"<<i<<": ";
                      output();
                      cout<<'\n';
     }
}


void magicka :: only_comb()
{
     for(j=0;j<N;++j)
     {
      if(last!=-1) 
      { 
        if((list[j]==comb[0] && list[last]==comb[1]) || (list[j]==comb[1] && list[last]==comb[0]))
        {
           list[last] = comb[2];
           list[j]   = 0;
        }
        else
        {
           last = j;
        }
      }
       
      else
      {
          last = j;
      }
     }
}


void magicka :: only_opp()
{
     for(j=0;j<N;++j)
     {
      if(dest!=-1) 
      { 
           if((list[j]==opp[0] && list[dest]==opp[1]) || (list[j]==opp[1] && list[dest]==opp[0]))
           {
                               for(k=0;k<=j;++k)
                               list[k]=0;
                               dest = -1;
           }
      }
      
      else
      {
          if(list[j]==opp[0] || list[j]==opp[1])
          {
              dest = j;
          }
      }
     }
}


void magicka :: both()
{
     for(j=0;j<N;++j)
     {
      if(last!=-1) 
      { 
        if((list[j]==comb[0] && list[last]==comb[1]) || (list[j]==comb[1] && list[last]==comb[0]))
        {
           list[last] = comb[2];
           list[j]   = 0;
           
           
           if(dest == last)
           dest = -1;
        }
        else
        {
           last = j;
        }
      }
       
      else
      {
          last = j;
      }
       
       //////////
       
      if(dest!=-1) 
      { 
           if((list[j]==opp[0] && list[dest]==opp[1]) || (list[j]==opp[1] && list[dest]==opp[0]))
           {
                               for(k=0;k<=j;++k)
                               list[k]=0;
                               
                               dest = -1;
                               
                               last = -1;
           }
      }
      
      else
      {
          if(list[j]==opp[0] || list[j]==opp[1])
          {
              dest = j;
          }
      }
     }
}


void magicka :: output()
{
     first = 1;
     cout<<"[";
     
     for(j=0;j<N;++j)
     {
                     if(list[j]!=0 && first == 0)
                     cout<<", "<<list[j];
                     else if(list[j]!=0 && first == 1)
                     {
                          first = 0;
                          cout<<list[j];
                     }
     }
     
     cout<<"]";
}


int main()
{
    magicka object;
    object.control();
   
    return(0);
}

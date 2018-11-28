#include <fstream>
#include <iostream>
#include <cmath>
using namespace std;
main()
{
      ifstream in("1.in");
      ofstream out("1.out");
      int k=0,t;
      in>>t;
      while(k!=t)
      {
      int present=0,is;
      int abhitakb=0,abhitako=0,abhib=1,abhio=1;
      char abhi='k';
      in>>is;
      k++;
      while(is--)
      {
      char ch;
      in>>ch;
      if(ch=='O')
      {
      int f;
      in>>f;
      int la=abs(f-abhio)+1;
      abhio=f;
      if(abhi=='B')
      {
       if(abhitakb>=la)
       {
       present+=1;
       abhitako+=1;
       }
      
      else if(la>abhitakb)
      {
      present+=la-abhitakb;
      abhitako+=la-abhitakb;
      }
      abhitakb=0;
      }
      else
      {
          present+=la;
          abhitako+=la;
      }
      abhitakb=0;
      abhi='O';
      }
      if(ch=='B')
      {
      int f;
      in>>f;
      int la=abs(f-abhib)+1;
      abhib=f;
      if(abhi=='O')
      {
       if(abhitako>=la)
       {
       present+=1;
       abhitakb+=1;
       }
       //else if(abhitakb==abhitako);

       else if(la>abhitako)
       {
           present+=la-abhitako;
           abhitakb+=la-abhitako;
           //present+=1;
       }
      abhitako=0;
      }
      else
      {
      present+=la;
     abhitakb+=la;
      }
       abhitako=0;
       abhi='B';
       }
       //cout<<"Case #"<<k<<":"<<" "<<present<<endl;
      }
            out<<"Case #"<<k<<":"<<" "<<present<<endl;   
                }
                out.close();
                in.close();
                }
                

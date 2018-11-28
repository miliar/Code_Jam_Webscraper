#include <iostream>
#include <string>
#include <fstream>
#include <map>
#include <vector>
#include<conio.h>

#define foreach(it,c) for(typeof((c).begin()) it=(c).begin(); it != (c).end() ; it++ )
#define F(i,mi,ma) for(int i=mi;i<ma;i++)

#define vi vector< int >
#define vs vector< string >
#define bn begin()
#define en end()
#define sz size()
#define pb push_back

using namespace std;

class Time{
public:
      string t;
      Time(){
             t="0000";
      }
      Time(string s1){
                  t=s1.substr(0,2)+s1.substr(3,2);
      }
      string print(){
           return t.substr(0,2)+":"+t.substr(2,2) ;
      }
      friend bool operator<(const Time a,const Time b){
           if( a.t < b.t ) return true;
           return false;
      }
      Time operator+(int T){
           Time tp;
           int h = (t[0]-'0')*10+(t[1]-'0') ;
           int m = (t[2]-'0')*10+(t[3]-'0') ;
           m+=T;
           if(m>=60){
                     m-=60;
                     h+=1;
           }
          
           tp.t[0] = h/10 + '0' ;
           tp.t[1] = h%10 + '0' ;
           tp.t[2] = m/10 + '0' ;
           tp.t[3] = m%10 + '0' ;
           return tp;
      }
};
int main()
{
    int N,na,nb,T;

    ifstream in("bl.in");
    ofstream out("bl.out");
    
    in >> N ;
    
    F(i,0,N){
             in>>T;
             in >> na >> nb;
             
             vector<Time> ad,aa,bd,ba;
             
             F(j,0,na){
                       string t1,t2;
                       in >> t1 >> t2;
                       //cout<<t1<<" "<<t2<<endl;
                       Time tt1(t1),tt2(t2);
                       ad.pb(tt1);
                       aa.pb(tt2);
             }
             //F(j,0,na) cout<< ab[i].print();
             
             //getch();
             F(j,0,nb){
                       string t1,t2;
                       in >> t1 >> t2;
                       Time tt1(t1),tt2(t2);
                       bd.pb(tt1);
                       ba.pb(tt2);
             }
             
             if(ad.sz != 0) sort(ad.bn,ad.en);
             if(aa.sz != 0) sort(aa.bn,aa.en);
             if(bd.sz != 0) sort(bd.bn,bd.en);
             if(ba.sz != 0) sort(ba.bn,ba.en);
             
             int ta=0,tb=0,tba=0,taa=0;

             F(j,0,ad.sz){
                          if ( tba < ba.size() && !(ad[j] < (ba[tba]+T)) ) tba++;
                          else ta++;
             }
             F(j,0,bd.sz){
                          if ( taa < aa.size() && !(bd[j] < (aa[taa]+T)) ) taa++;
                          else tb++;
             }

             out << "Case #"<<i+1<<": "<<ta<<" "<<tb<<endl;
             //cout << "Case #"<<i+1<<": "<<ta<<" "<<tb<<endl;
             //getche();
    }
    
    
   out.close();
   in.close();

    cout<<"done";
    getch();

}




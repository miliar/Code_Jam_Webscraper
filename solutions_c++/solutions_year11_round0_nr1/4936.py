#include<iostream>
#include<vector>
#include <cstdio>
#include <stdlib.h>
using namespace std;


vector<pair<int,int> >o;
vector<pair<int,int> >b;
int t,n,cnt,z=0;

int main(){
    freopen("A-small-attempt1.in","r",stdin);
	freopen("output.txt","w",stdout);
    cin>>t;
    for(int i = 0 ; i < t;i++){
            cin>>n;
            z++;
            cnt = 0;
            o.clear();
            b.clear();
            for(int j = 0;j<n;j++){
                   int r;char c;
                   cin>>c>>r;
                   if(c== 'O')o.push_back(make_pair(r,j));
                   else b.push_back(make_pair(r,j));
            }
            int k=0,l=0,oo=1,bb=1;
            
            while(k<o.size() && l<b.size()){


                              while(b[l].first > bb && o[k].first > oo){
                                               oo++,bb++;
                                               cnt++;
                              }
                         
                            while(b[l].first < bb && o[k].first > oo){oo++,bb--;cnt++;}
                            
                         
                            

                            while(b[l].first < bb && o[k].first < oo)oo--,bb--,cnt++;
                            
                         
                            

                            while(b[l].first > bb && o[k].first < oo)oo--,bb++,cnt++;
                         
                         
                         
                            while (b[l].first==bb && b[l].second < o[k].second && o[k].first<oo){l++,cnt++,oo--;}
                            while (b[l].first==bb && b[l].second > o[k].second && o[k].first<oo){cnt++,oo--;}
                            while(b[l].first==bb && b[l].second < o[k].second  && o[k].first>oo){l++,cnt++,oo++;}
                            while(b[l].first==bb && b[l].second > o[k].second  && o[k].first>oo){cnt++,oo++;}
                            while(o[k].first==oo && o[k].second < b[l].second  && b[l].first<bb){bb--,k++,cnt++;}
                            while(o[k].first==oo && o[k].second > b[l].second  && b[l].first<bb){bb--,cnt++;}
                            while(o[k].first==oo && o[k].second < b[l].second  && b[l].first>bb){bb++,k++,cnt++;}
                            while(o[k].first==oo && o[k].second > b[l].second  && b[l].first>bb){bb++,cnt++;}
                            while (b[l].first==bb && b[l].second < o[k].second && o[k].first==oo){l++,cnt++;}
                            while(o[k].first==oo && o[k].second < b[l].second  && b[l].first==bb){k++,cnt++;}

            }
            while(l<b.size()){
                     while(b[l].first>bb){bb++,cnt++;}
                     while(b[l].first< bb)bb--,cnt++;
                     if(bb == b[l].first)cnt++;
  
                     l++;
                 
            }
            while(k<o.size()){
           
                           while(o[k].first< oo )oo--,cnt++;
                           while(o[k].first> oo)oo++,cnt++;
                           cnt++;
                                           k++;
            }
            cout<<"Case #"<<z<<": "<<cnt<<endl;
    }
//    system("pause");
}

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <ctime>

#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())
using namespace std;

struct node{
  
  int deph, depm, arrh, arrm;
  
  bool operator <(const node & n) const {
       
       if(deph == n.deph)
               return depm < n.depm;
       return deph < n.deph;     
  }
};
vector<node> A, B;
vector<node> arrA, arrB;

int t;
int na, nb;
string a, b;
int hh, mm;
int newA, newB;
int compare(const node &a, const node &b)
{
    //cout<<endl<<"Comparing : "<<a.deph<<":"<<a.depm<<"-"<<a.arrh<<":"<<a.arrm<<"     "<<b.deph<<":"<<b.depm<<"-"<<b.arrh<<":"<<b.arrm;
    if(a.arrh == b.deph && a.arrm <= b.depm) return 1;
    if(a.arrh < b.deph) return 1;
    return 2;    
}

int compare2(const node &a, const node &b)
{
    //cout<<endl<<"Comparing : "<<a.deph<<":"<<a.depm<<"-"<<a.arrh<<":"<<a.arrm<<"     "<<b.deph<<":"<<b.depm<<"-"<<b.arrh<<":"<<b.arrm;
    if(a.deph == b.arrh && a.depm >= b.arrm) return 1;
    if(a.deph > b.arrh) return 1;
    return 2;   
}

int compareDep(const node &a, const  node&b)
{
    //cout<<endl<<"Comparing : "<<a.deph<<":"<<a.depm<<"-"<<a.arrh<<":"<<a.arrm<<"     "<<b.deph<<":"<<b.depm<<"-"<<b.arrh<<":"<<b.arrm;
    if(a.deph == b.deph && a.depm <= b.depm) return 1;
    if(a.deph < b.deph) return 1;
    return 2;   
}




node delay(node &a)
{
     node n;
     n.deph = a.deph;
     n.depm = a.depm;
     n.arrm = (a.arrm + t) % 60;
     n.arrh = a.arrh + (a.arrm + t) / 60;
     return n;
}


int main()
{
    int cases;
    cin >> cases;
    int cnt = 1;
    int ans = 0;   


    int cnta, cntb;
    int cura, curb;
    while(cases--)
    {
        cin >> t;
        cin >> na >> nb;
        A.clear();
        B.clear();
        
        arrA.clear();
        arrB.clear();
        
       
    
      
        cnta = 0;
        cntb = 0;
        for(int i = 0; i < na; i++)
        {
            cin >> a >> b;
            sscanf(a.c_str(), "%d:%d", &hh, &mm);
            //cout<< hh << mm;        
            node n;
            n.deph = hh;
            n.depm = mm;
            sscanf(b.c_str(), "%d:%d", &hh, &mm);
            n.arrh = hh;
            n.arrm = mm;
            A.pb(n);
        }
        
        for(int i = 0; i < nb; i++)
        {
            cin >> b >> a;
            sscanf(a.c_str(), "%d:%d", &hh, &mm);
            //cout<< hh << mm;        
            node n;
            n.arrh = hh;
            n.arrm = mm;
            sscanf(b.c_str(), "%d:%d", &hh, &mm);
            n.deph = hh;
            n.depm = mm;
            B.pb(n);
        }
        
        sort(all(A));
        sort(all(B));
        //tr(A, itr) cout<<endl<<itr->deph<<" "<<itr->depm<<" "<<itr->arrh<<" "<<itr->arrm;
        //tr(B, itr) cout<<endl<<itr->deph<<" "<<itr->depm<<" "<<itr->arrh<<" "<<itr->arrm;
        
        cura = 0; 
        curb = 0;
        newA = 0;
        newB = 0;
        while(cura < na && curb < nb)
        {
            int send = compareDep(A[cura], B[curb]);
            if(send == 1)
            {
                bool found = false;
                //cout<<endl<<"Checking arrived trains at A.";
                for(int i = 0; i < sz(arrA); i++)
                {
                    
                    if(compare(arrA[i], A[cura]) == 1 && compare2(A[cura], delay(arrA[i])) == 1)
                    {
                         //cout<<endl<<"Found train to schedule at A.";               
                         found = true;
                         //remove(all(arrA), arrA[i]);
                         arrA.erase(arrA.begin() + i, arrA.begin() + 1 + i);
                         break;                    
                    }        
                      
                }   
                if(!found)
                {
                          //cout<<endl<<"No arrived train.";
                              newA++;
                              
                }
                arrB.pb(A[cura]);     
                cura++;
            }
            else
            {
                bool found = false;
                //cout<<endl<<"Checking arrived trains at B";
                for(int i = 0; i < sz(arrB); i++)
                {
                        if(compare(arrB[i], B[curb]) == 1 &&compare2(B[curb], delay(arrB[i])) == 1)
                        {
                            //cout<<endl<<"Found train to schedule at B.";
                            found = true;
                            arrB.erase(arrB.begin() + i, arrB.begin() + i + 1);
                            break;
                                                
                        }        
                }
                if(!found)
                {
                          //cout<<endl<<"No arrived train.";
                           newB++;
                }
                arrA.pb(B[curb]);
                curb++;
            }       
        }

        while(cura < na)
        {
             bool found = false;
                //cout<<endl<<"Checking arrived trains at A.";
                for(int i = 0; i < sz(arrA); i++)
                {
                    
                    if(compare(arrA[i], A[cura]) == 1 && compare2(A[cura], delay(arrA[i])) == 1)
                    {
                         //cout<<endl<<"Found train to schedule at A.";               
                         found = true;
                         //remove(all(arrA), arrA[i]);
                         arrA.erase(arrA.begin() + i, arrA.begin() + 1 + i);
                         break;                    
                    }        
                      
                }   
                if(!found)
                {
                          //cout<<endl<<"No arrived train.";
                              newA++;
                              
                }
                arrB.pb(A[cura]);     
                cura++;      
        }
        
        while(curb < nb)
        {
              bool found = false;
                //cout<<endl<<"Checking arrived trains at B";
                for(int i = 0; i < sz(arrB); i++)
                {
                        if(compare(arrB[i], B[curb]) == 1 &&compare2(B[curb], delay(arrB[i])) == 1)
                        {
                            //cout<<endl<<"Found train to schedule at B.";
                            found = true;
                            arrB.erase(arrB.begin() + i, arrB.begin() + i + 1);
                            break;
                                                
                        }        
                }
                if(!found)
                {
                          //cout<<endl<<"No arrived train.";
                           newB++;
                }
                arrA.pb(B[curb]);
                curb++;     
        }

        cout<<"Case #"<<cnt<<": "<<newA<<" "<<newB<<endl;
        cnt++;        
    }
    return 0;
}


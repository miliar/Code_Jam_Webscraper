#include <cstdio>
#include <cmath>
#include <map>
#include <vector>
#include <algorithm>
#include <iostream>
#include <string>
#include <set>
#include <sstream>
#include <cstdlib>
#include <stack>
#define FOR(i,j,n) for (int i=j;i<n;++i)
#define FORI(i,j,n) for (int i=j;i<=n;++i)
#define FORN(i,n) FOR(i,0,n)
#define sz size()
#define PB(a) push_back(a)
#define foreach(i, c) for( __typeof( (c).rbegin() ) i = (c).rbegin(); i != (c).rend(); ++i )
#define CPRESENT(container, element) (find(ALL(container),element) != container.end())
#define MIN(a,b) (a < b ? a : b)
#define MAX(a,b) (a > b ? a : b)
#define ALL(x) x.begin(), x.end()
#define INF 1<<30
using namespace std;

int N,t,n,m;
string dep,arr;

class sch{
   public:
      int dep;
      int arr;
   sch(){
      dep=0;
      arr=0;
   };
   sch(int x,int y){
      dep=x;
      arr=y;
   };

};
   bool operator<(const sch& a,const sch &b){
      if (a.dep!=b.dep)return a.dep<b.dep;
      return a.arr<b.arr;
   }


sch A[50],B[50];

int conv(string s){
   int h,m;
  sscanf(s.c_str(),"%d:%d",&h,&m);
  return h*60+m;
}

 int main(){
    
    cin >> N ;
    
    FORN(ca,N){
      
       cin >>t;
       cin >>n>>m;
       
       FORN(i,n){
	  cin>>dep>>arr;
	  A[i]=sch(conv(dep),conv(arr)+t);
       }
       FORN(i,m){
	  cin>>dep>>arr;
	  B[i]=sch(conv(dep),conv(arr)+t);
       }
       A[n]=sch(999999999,999999999);
       B[m]=sch(999999999,999999999);
       sort(A,A+n+1);
       sort(B,B+m+1);
       
       int a=0;
       int b=0;
       
       map<int,int> Wa,Wb;
       
       int posa=0;
       int posb=0;
       while(posa+posb!=n+m){
	  
// 	  printf("posa %d , posb %d, a=%d b=%d\n",posa,posb,a,b);
	  if (A[posa].dep<B[posb].dep){
// 	     printf("Min a con %d llegando a las %d \n",A[posa].dep,A[posa].arr);
	     bool found=0;
	     int px=0;
	     foreach(it,Wa){
// 		printf("chck %d\n",it->first);
		if (it->first<=A[posa].dep && Wa[it->first]>0){
		   Wa[it->first]--;
// 		   printf("FOUND CON %d\n",it->first);
		   found=1;
		   break;
		}
	     }
	     if (!found)a++;
	    
	     Wb[A[posa].arr]++;
	     posa++;
	  }
	  else {
// 	     printf("Min b con %d llegando a las %d \n",B[posb].dep,B[posb].arr);
	     bool found=0;
	     int px=0;
	     foreach(it,Wb){
		if (it->first<=B[posb].dep && Wb[it->first]>0){
		   Wb[it->first]--;
// 		   printf("FOUND CON %d\n",it->first);
		   found=1;
		   break;
		}
	     }
	     if (!found)b++;
	    
	     Wa[B[posb].arr]++;
	     posb++;
	  }
       }
       printf("Case #%d: %d %d\n",ca+1,a,b);
//        cout<< a <<" "<<b<<endl;
    }
    return 0;
 }

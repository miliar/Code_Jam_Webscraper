#include <string>
#include <iostream>
#include <list>
#include <map>
#include <algorithm>
#include <math.h>

using namespace std;


int main() 
{
    //--------------------------------
    int  t;
    cin >> t;
    int  _case = 1;
	for(;_case<=t;_case++)
	{     
       long long N,L,H;
       cin >> N >> L >> H;
       long otherfreq[10001];
       for(int i=0; i<N; i++) cin >> otherfreq[i];
       bool found = false;
       while(!found && L <=H)
       { 
         found = true;
         for(int i=0; i<N; i++) 
           if(otherfreq[i]%L!=0 && L%otherfreq[i]!=0)
             {found = false; break;}
         if (!found)L++;
         }
          
       
       //------------- o/p --------------
	   cout << "Case #" << _case << ": " ;
	   if (!found) cout << "NO"<< endl;
	   else
	     cout << L << endl;
	   
	}
	return 0;
}



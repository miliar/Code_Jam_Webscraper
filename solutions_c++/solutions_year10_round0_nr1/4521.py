	#include <iostream>
        #include <stdlib.h>
        #include <cstdio>
	#include <algorithm>
	#include <cstring>
	#include <string>
	#include <cctype>
	#include <stack>
	#include <queue>
	#include <vector>
	#include <map>
	#include <sstream>
	#include <set>
	#include <math.h>
	using namespace std;
	 
	struct snapper {
	    bool power;
	    bool on;
	} a [100000000 + 2];
	 
	void clear (int n)
	{
	    for ( int i = 0; i < n; i++ ) {
	        a [i].power = false;
	        a [i].on = false;
	    }
	    a [0].power = true;
	}
	 
	int main ()
	{
	  freopen ("A-small-attempt1.in", "r", stdin);
	  freopen ("A-small-attempt1.out", "w", stdout);	    
	    long Tests;
	    cin>>Tests;
	    if (Tests < 1 || Tests > 10000){
	      cout<<"Please eneter tests between 1 and 10000"<<endl;
	      exit(0);
	    }
	    long cases = 0;
	 
	    while ( Tests-- ) {
	        long n;
	        unsigned long k;
	        cin>>n>>k;
		if (n>30 || n<1 || k<0 || k>100000000){
		  cout<<"Numbers out or range"<<endl;
		  exit(0);
		}
	 
	        clear (n);
	 
	        for ( unsigned long i = 0; i < k; i++ ) {
	            for ( unsigned long j = 0; j < n; j++ ) {
	                if ( a [j].power )
	                    a [j].on = a [j].on ? false : true;
	            }
	            for ( unsigned long j = 0; j < n; j++ ) {
	                if ( a [j].power && a [j].on )
	                    a [j + 1].power = true;
	                else
	                    a [j + 1].power = false;
	            }
	        }
	 
	        if ( a [n - 1].power && a [n - 1].on ){		  
		  cout<<"Case #"<<++cases<<": ON"<<endl;
		}	    
	        else{		  
		    cout<<"Case #"<<++cases<<": OFF"<<endl;
		}
	    }
	 
	    return 0;
	}
	 



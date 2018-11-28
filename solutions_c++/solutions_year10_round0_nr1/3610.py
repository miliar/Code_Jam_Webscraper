#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
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
#include <ctime>

using namespace std;

int cases;
int main()
{
    cin>>cases;
    
    int snappers;
    int chasquidos;
    for(int i=0; i<cases ; i++)
    {
	cin>>snappers;
	cin>>chasquidos;
	
	if(chasquidos==0)
	cout<<"Case #"<<(i+1)<<": OFF"<<endl;	
	
	else
	{
	    if(chasquidos%2==0)
	    cout<<"Case #"<<(i+1)<<": OFF"<<endl;	
	    
	    else
	    {
	    	if((chasquidos+1)%(int)pow(2, snappers)==0)
		cout<<"Case #"<<(i+1)<<": ON"<<endl;	    
		
		else
		cout<<"Case #"<<(i+1)<<": OFF"<<endl;	
	    }
	}
    }
    return 0;
}

//Problem C. Perfect Harmony//
#include <iostream>
#include <fstream>
#include <inttypes.h>

using namespace std;

/*
Input
  	
Output
 
2
3 2 100
3 5 7
4 8 16
1 20 5 2

Case #1: NO
Case #2: 10

*/

int gcd(int a, int b)
{
    while(true)
    {
        a = a % b;
		if( a == 0 )
			return b;
		b = b % a;

        if( b == 0 )
			return a;
    }
}

int mod(int a,int b)
{
     if (a>b)
        return a%b;
        else return b%a;
}

int main()
{
    ifstream in;
    ofstream out;
    in.open("C-small-attempt0.in");
    out.open("output.txt");
    
    int cases=0;
    in>>cases;
    
    for (int i=0; i<cases; i++)
    {
        int p,l,h;
        in>>p>>l>>h;
        
        int arr[p];
        for (int j=0; j<p; j++)
            in>>arr[j];
            
        bool possible;    
            
        
        int min = h+1;
        for (int j=l; j<=h; j++)
        {
            possible = false;
            for (int k=0; k<p; k++)
            {
                if (mod(j,arr[k])==0)
                   {possible=true;}
                else {possible=false;break;}
            }
            if (possible && (min>j)) min=j;
        }
        
        cout<<"Case #"<<(i+1)<<": "; out<<"Case #"<<(i+1)<<": ";
        if ((min>=l)&&(min<=h)) {cout<<min<<endl;out<<min<<endl;}
        else {cout<<"NO\n";out<<"NO\n";}
    }
    
    in.close();
    out.close();
    system("pause");
}


//
//  main.cpp
//  Googlerese
//
//  Created by Lyamani Moulay on 14/04/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <string>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <sstream>

using namespace std;

map <string,string>  rules ;
int A, B ;
/*string changeline(string str)
 {
 string line = "" ;
 
 return line;
 }*/

int main (int argc, const char * argv[])
{
    freopen("/Users/lyamanimoulay/Desktop/RecycledNumbers/RecycledNumbers/output.in","w", stdout);
    freopen("/Users/lyamanimoulay/Desktop/RecycledNumbers/RecycledNumbers/input.in","r", stdin);
    
    
    int test,cases;
    
    // recycled between 10 ... 99     : 1 pair max for each number xy <--> yx if y!=0
    
    // recycled between 100 ... 999   : 2 pair max : xyz <-> zxy  or xyz <-> yzx

    cases=0;
    scanf("%d",&test);
    while (test){
        test--;
        cases++;
        
        scanf("%d",&A);
        scanf("%d",&B);
        
       // map<int, int> myMap ;
        
        int digitsA = floor( log10( abs( A != 0 ? A : 1 ) ) ) + 1;
        if(digitsA == 1)
            A = 10;
        
        int digitsB = floor( log10( abs( B != 0 ? B : 1 ) ) ) + 1;
        if(digitsB == 1)
            B = 10;
        // Here im sure that 10 <= A <= B <= 999 
        
        int n = A  ; 
        int m ;
        
        if(digitsA == digitsB && digitsA == 1 )
            cout<<"Case #"<<cases<<": "<< 0 <<endl;
        else if(digitsA == digitsB && digitsA == 4)
            cout<<"Case #"<<cases<<": "<< 0 <<endl;
        else if (digitsA == digitsB && digitsA == 2 )
        {
            int result = 0;
            
            for(n=A; n<=B; n++)
            {
                if(n%10 !=0 )
                {
                    std::ostringstream os;
                    
                    os << n;
                    std::string m_str = os.str();
                    m_str = m_str.substr(1, 1) + m_str.substr(0, 1) ;
                    m = atoi(m_str.c_str() ) ;
                    
                    if(n<m && m<=B)
                        result++ ;
                    
                }
                
            }
            
            cout<<"Case #"<<cases<<": "<< result <<endl;
            
        }
        else if (digitsA == digitsB && digitsA == 3 )
        {
            
            int result = 0;
            
            for(n=A; n<=B; n++)
            {

                    std::ostringstream os;
                    
                    os << n;
                    std::string m1_str = os.str();
                    m1_str = m1_str.substr( 2, 1) + m1_str.substr(0, 1) + m1_str.substr(1, 1) ;
                    int m1 = atoi(m1_str.c_str() ) ;
                    int digitsM1 = floor( log10( abs( m1 != 0 ? m1 : 1 ) ) ) + 1;
                
                    os << n;
                    std::string m2_str = os.str();
                    m2_str =  m2_str.substr(1, 1) + m2_str.substr( 2, 1) + m2_str.substr(0, 1) ;
                    int m2 = atoi(m2_str.c_str() ) ;
                    int digitsM2 = floor( log10( abs( m2 != 0 ? m2 : 1 ) ) ) + 1;
                
                
                
                    if(n<m1 && digitsM1==3 && m1<=B)
                        result++ ;
                    if(n<m2 && digitsM2==3 && m2<=B)
                        result++ ;
                    
                
            }
            
            cout<<"Case #"<<cases<<": "<< result <<endl;
            
        }
        
        else
            
        {
            // 2 and 3
            int result = 0;
            
            for(n=A; n<=99; n++)
            {
                if(n%10 !=0 )
                {
                    std::ostringstream os;
                    
                    os << n;
                    std::string m_str = os.str();
                    m_str = m_str.substr(1, 1) + m_str.substr(0, 1) ;
                    m = atoi(m_str.c_str() ) ;
                    
                    if(n<m && m<=B)
                        result++ ;
                    
                }
                
            }
            
            for(n=100; n<=B; n++)
            {
                
                std::ostringstream os;
                
                os << n;
                std::string m1_str = os.str();
                m1_str = m1_str.substr( 2, 1) + m1_str.substr(0, 1) + m1_str.substr(1, 1) ;
                int m1 = atoi(m1_str.c_str() ) ;
                int digitsM1 = floor( log10( abs( m1 != 0 ? m1 : 1 ) ) ) + 1;
                
                os << n;
                std::string m2_str = os.str();
                m2_str =  m2_str.substr(1, 1) + m2_str.substr( 2, 1) + m2_str.substr(0, 1) ;
                int m2 = atoi(m2_str.c_str() ) ;
                int digitsM2 = floor( log10( abs( m2 != 0 ? m2 : 1 ) ) ) + 1;
                
                
                
                if(n<m1 && digitsM1==3 && m1<=B)
                    result++ ;
                if(n<m2 && digitsM2==3 && m2<=B)
                    result++ ;
                
                
            }
            
            cout<<"Case #"<<cases<<": "<< result <<endl;
            
        }
            

    }
    return 0;
}




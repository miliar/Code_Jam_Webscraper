#include<iostream>
#include<stdio.h>
#include<stdlib.h>

using namespace std ;

int oPosition = 1 , bPosition = 1 , timeReq = 0 ;


int oCountTime ( int oValue , int bValue )
{

     if( bValue > bPosition )
        bPosition ++ ;

     else if ( bValue < bPosition )
        bPosition -- ;
            
     if (oValue == oPosition)
     {
         timeReq ++ ;
         return 1 ;
     }    
     else if( oValue > oPosition )
     {
        oPosition ++ ;
        timeReq ++ ;
       // cout<<oPosition ;
        return 0 ;
     }   
     else
     {
        oPosition -- ;
        timeReq ++ ;
         return 0 ;
     }

     
}

int bCountTime ( int bValue , int oValue )
{

     if( oValue > oPosition )
        oPosition ++ ;
   
     else if ( oValue < oPosition )
        oPosition -- ;
            
     if (bValue == bPosition)
     {
         timeReq ++ ;
         return 1 ;
     }    
     else if( bValue >bPosition )
     {
        bPosition ++ ;
        timeReq ++ ;
       // cout<<oPosition ;
        return 0 ;
     }   
     else
     {
        bPosition -- ;
        timeReq ++ ;
         return 0 ;
     }

     
}


int main ()
{
    int o[] = {1} , b[] = {} , i ,j, totalPush = 1 , flag ;
    int totalCases , i , totalSubCases , o[100] ,b[100];
    fstream fin ;
    string str ,temp ;    
    char sequence[100] , *ptrSequence;
    
    fin.open( "input.txt" , fstream::in ) ;
    getline (fin , str ) ;
    
    totalCases = atoi(str.c_str()) ;
    
    for(j = 0 ; j < totalCases ; j++ )
    {
        getline(fin , str ) ;
        getSequence ( str, sequence ) ;            
        totalSubCases = strlen(sequence) ;
        getO(str , o) ;
        getB(str , b) ; 
                       
   
        int oPos = 0 , bPos = 0 ;
        timeReq = 0 ;
        for ( i = 0 ; i < totalSubCases ; i++ )
        {
            flag = 0 ;
            if (sequence[i] == 'O')
            {   
                while(!flag)
                {
                    flag = oCountTime( o[oPos] , b[bPos] ) ;
                        
                }
                oPos ++ ;
            }
            else if (sequence[i] == 'B')
            {
               while (!flag)
                { 
                    flag = bCountTime(  b[bPos] , o[oPos] ) ;
                 }
                 bPos ++ ;
            }   
        } 
    
        cout<<"time:"<<timeReq<<endl ;
    
    }
}


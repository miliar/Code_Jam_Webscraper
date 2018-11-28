/*
First i make a c++ code to generate all the fundamental numbers to make the lamp 
on for different number of snappers

I deduce thatthe first lamp is onwhen the number of snaps by hand=2^(snappers number)-1
and the snappers time should verify the formula:

snappers by hand= (integer number)*(first time snappers number ) +( the same integer number-1)

  */
#include <stdio.h>
#include <iostream>
#include <math.h>
#include <stdio.h>
using namespace std;

#define rep(i,m) for( i=0;i<m;i++)
#define rep2(i,x,m) for(i=x;i<m;i++)
#define T_Max  10000
void toggle(int&x);

int main ()
{
 int i,ON;//,u;
	     
 int Snap_Num[T_Max];
 long double	 Fing_Num[T_Max],Fund,arr[31];    

    //rep(u,31)
    //arr[u]=(pow(2,Snap_Num[u])-1);
    arr[0]=0;
	arr[1]=1;
	arr[2]=3;
	arr[3]=7;
	arr[4]=15;
	arr[5]=31;
	arr[6]=63;
	arr[7]=127;
	arr[8]=255;
	arr[9]=511;
	arr[10]=1023;

	
	arr[11]=2047;
	arr[12]=4095;
	arr[13]=8191;
	arr[14]=16383;
	arr[15]=32767;
	arr[16]=65535;
	arr[17]=131071;
	arr[18]=262143;
	arr[19]=524287;
	arr[20]=1048575;

	
	arr[21]=2097151;
	arr[22]=4194303;
	arr[23]=8388607;
	arr[24]=16777215;
	arr[25]=33554431;
	arr[26]=67108863;
	arr[27]=134217727;
	arr[28]=268435455;
	arr[29]=536870911;
	arr[30]=1073741823;



      
                 freopen("A-large.in","rt",stdin);    
                 freopen("A-large.out","wt",stdout);    
      
                 int T;//test cases number    
                 cin>>T;    
    
                     rep(i,T)    
                                 cin>>Snap_Num[i]>>Fing_Num[i];    
					 

                  rep(i,T)    
                                                    
                  {   
					  //cout<<Snap_Num[i]<<endl;
					  Fund=arr[Snap_Num[i]];
					  //cout<<(long)Fund<<endl;

    
					        ON=0;
							if(Fund!=1)
							if( (long)(Fing_Num[i]+1)%(long)(Fund+1)==0  )
							ON=1;

							if(Fund==1)
								if(((long)Fing_Num[i]%2)==1)
								ON=1;


								
							if(ON==1)      
                            {cout<<"Case #"<<i+1<<": ON"<<endl;} 
							//rep(j,Snap_Num[i]+1)cout<<" "<<Snapper_Next[j];cout<<endl;}
                            else     
                            cout<<"Case #"<<i+1<<": OFF"<<endl; 
							



				  
				  
				  
				  
				  
				  }
    
       
  return 0;    
}    
    


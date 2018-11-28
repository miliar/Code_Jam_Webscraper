#include<iostream>
#include<string>
#include<fstream>
using namespace std ;

class Time
	{
	public :
		int _hour ;
		int _min ;
	public :
		void putin(string s){_hour=(s[0]-'0')*10+s[1]-'0'; _min=(s[3]-'0')*10+s[4]-'0';}
		Time operator+ (int ) ;
		bool operator> (Time) ;
		bool operator< (Time) ;
		int operator-(Time) ;
	} ;
Time Time::operator+ (int i )
{_min+=i ;
 if(_min>=60)
	{_hour+=1 ;
	 _min-=60 ;
	}
 return *this ;
}

bool Time::operator> (Time v)
{
 if(_hour>v._hour||(_hour==v._hour&&_min>v._min))
	return true ;
 else return false ;
}


bool Time::operator< (Time v)
{
 if(_hour>v._hour||(_hour==v._hour&&_min>v._min))
	return false ;
 else return true ;
}

int Time::operator-(Time v)
{
 return (_hour-v._hour)*60+_min-v._min ;
}


int main()
{ 
 ifstream pt_in ;
 ofstream pt_out ;
 pt_in.open("B-large.in") ;
 pt_out.open("out.txt") ;
 

 string s ;
 int n , i ,  k  , m2 , m , **x , t ;
 char turns ;
 int min , NA , NB ; 
 Time *A_begin , *B_begin ;
 Time *A_end , *B_end ;
 Time begin , end ;
 pt_in>>n ;
 x=new int*[n] ;
 for(k=0;k<n;k++)
	{x[k]=new int[2] ;
	 x[k][0]=x[k][1]=0 ;
	 pt_in>>min>>NA>>NB ;
	 A_begin=new Time[NA] ;
	 A_end=new Time[NA] ;
	 B_begin=new Time[NB] ;
	 B_end=new Time[NB] ;
	 for(i=0;i<NA;i++)
		{pt_in>>s ;
		 A_begin[i].putin(s);
		 pt_in>>s;
		 A_end[i].putin(s);
		}
	 for(i=0;i<NB;i++)
		{pt_in>>s ;
		 B_begin[i].putin(s);
		 pt_in>>s ;
		 B_end[i].putin(s);
		}
	 while(1)
		{for(m=0,begin=A_end[0],i=1;i<NA;i++)	
			if(begin>A_end[i])
				{begin=A_end[i] ;
				m=i ;
				}
		 for(m2=-1,i=0;i<NB;i++)
			if(begin>B_end[i])
				{begin=B_end[i] ;
				 m2=i ;
				}
		 if(begin._hour==24)break ;
		 if(m2==-1){turns='A' ;x[k][0]+=1 ;}
		 else {turns='B';m=m2 ;x[k][1]+=1 ;}
		 if(turns=='A'){A_begin[m]._hour=24 ;A_end[m]._hour=24 ;}
		 else	{B_begin[m]._hour=24 ;B_end[m]._hour=24 ;}
		 while(1)
			{end=begin ;
			 if(turns=='A')
				{for(t=2400,i=0;i<NB;i++)
					if(B_begin[i]._hour!=24&&B_begin[i]-begin>=min&&B_begin[i]-begin<t)
						{t=B_begin[i]-begin ;
						 m=i ;
						 end=B_begin[i] ;
						}
				 if(t==2400)break ;
				 begin=B_end[m] ;
				 B_begin[m]._hour=24 ;	
				 B_end[m]._hour=24 ;
				 turns='B' ;
				}
			 else	
				{for(t=2400,i=0;i<NA;i++)
					if(A_begin[i]._hour!=24&&A_begin[i]-begin>=min&&A_begin[i]-begin<t)
						{t=A_begin[i]-begin ;
						 m=i ;
						 end=A_begin[i] ;
						}
				 if(t==2400)break ;
				 begin=A_end[m] ;
				 A_begin[m]._hour=24 ;
				 A_end[m]._hour=24 ;
				 turns='A' ;
				}
			}
		}
	 delete[] A_begin ;
	 delete[] A_end ;
	 delete[] B_begin ;
	 delete[] B_end ;
	}
 for(k=0;k<n;k++)pt_out<<"Case #"<<k+1<<": "<<x[k][0]<<" "<<x[k][1]<<endl ;
 for(k=0;k<n;k++)delete[] x[k] ;
 delete[] x ;
 pt_in.close() ;
 pt_out.close() ;
 return 0 ;
}
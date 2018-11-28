#include<iostream>
#include<string>
#include<fstream>
using namespace std ;
int main()
{
 ifstream pt_in ;
 ofstream pt_out ;
 pt_in.open("A-large.in");
 pt_out.open("out.txt");
 
 
 string *search , *question ;
 bool *appear_s ;
 bool change ;
 int s , q ;
 int n , m , i , j , k ;
 int *y ;
 string temp ;
 pt_in>>n ;
 y=new int[n] ;
 for(k=0;k<n;k++)
	{y[k]=0 ;
	 pt_in>>s ;
	 search=new string[s] ;
	 appear_s=new bool[s] ;
	 getline(pt_in , temp) ;
	 for(i=0;i<s;i++)
		{getline(pt_in , search[i]);
		 appear_s[i]=false ;
		}
	 pt_in>>q ;
	 getline(pt_in , temp) ;
	 if(q<0)q=0;
	 question=new string[q] ;
	 for(i=0;i<q;i++)getline(pt_in , question[i]) ;
	 for(i=0;i<q;i++)
		{for(j=0;j<s;j++)
			if(question[i]==search[j])
				{appear_s[j]|=true ;
				 m=j ;
				}
		 for(change=true,j=0;j<s;j++)
			change&=appear_s[j] ;
		 if(true==change)
			{y[k]+=1 ;
			 for(j=0;j<s;j++)
				if(j!=m)appear_s[j]=false ;
			}
		}
	 delete[] search ;
	 delete[] appear_s ;
	 delete[] question ;
	}
 for(k=0;k<n;k++)
	pt_out<<"Case #"<<k+1<<": "<<y[k]<<endl ;
 delete[] y ;
 return 0 ;
}
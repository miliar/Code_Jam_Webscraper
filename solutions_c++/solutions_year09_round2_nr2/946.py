#include<iostream>
#include<fstream>
using namespace std;
int t;
char s[50],temp;

int minnow;
bool check()
 { 
  
   for (int  i = 0 ; i <= strlen(s)-2; i++)
    {
	  if (s[i]<s[i+1]) { 	return false;} 		 
    }	 
    
    return true;
 }
 
void strsort()
 {
  	 char temp;
  for (int i = 0; i <= strlen(s)-2; i++)
   for (int j = i +1 ;  j<=strlen(s)-1 ; j++)
    {
	  if (i==0 && s[j]=='0') continue; 		
	  if (s[i]>s[j])
	   {
	   	 			temp=s[i];
	   	 			s[i]=s[j];
	   	 			s[j]=temp;
	   }
	}	 
 }
 
void strsort1(int k)
 {
  	 char temp;
  for (int i = k; i <= strlen(s)-2; i++)
   for (int j = i +1 ;  j<=strlen(s)-1 ; j++)
    {
	  if (s[i]>s[j])
	   {
	   	 			temp=s[i];
	   	 			s[i]=s[j];
	   	 			s[j]=temp;
	   }
	}	 
 }
int main()
 {
  freopen("B.in","r",stdin);
  freopen("B.txt","w",stdout);		  
   ifstream fin;
   fin.open("B.in");
   ofstream fout;
   fout.open("B.txt");
   int  k;
  fin>>t ;
  for (int  test = 1 ; test <= t; test++)
   {
   	s[1]='\0';  
	memset(s,'\0',sizeof s);   		
   fin>>s;
   if (strlen(s)==1)  { fout<<"Case #"<<test<<": "<<s<<'0'<<endl;continue;}
	 if (check())
	  {	
	     strsort();
	     
		 for (int i = strlen(s)-1 ; i >= 1; i-- )
		  {
		   s[i+1] = s[i]; 
		  }		
		 s[1]='0';
		 fout<<"Case #"<<test<<": "<<s<<endl;
		 continue;   	 
	  }  		
	  
	for (int  i = strlen(s)-1; i>=0 ; i--)
	 {
	   minnow=10;		  
	   
	   for (int j = strlen(s)-1; j>=i+1; j--)
	    {
		   if (s[j]>s[i] && s[j]-48<minnow)
		    {
			  minnow=s[j]-48;		
			  k=j;	 
 			 }		
  		}		  
  	   if ( minnow!=10)
		  {
		   temp=s[i];
		   s[i]=(char)('0'+minnow);	
		   s[k]=temp;	
		    strsort1(i+1);  
		   // cout<<k<<endl;
		   	  break;
          }	
     
         
     }  
     fout<<"Case #"<<test<<": "<<s<<endl;  
	  
   }		  
 }

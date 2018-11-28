#include<iostream>
#include<fstream>
#include<cstring>
bool f[6000];
char s[6000][20],s1[600][1500];
using namespace std;
int l,d,n;
int ans;
bool check(char s[20],char s1[100])
    {
	 int i;
	 bool flag=true;
	 int temp=0;
	 int j;
	 bool kuohao=false;
	 for (i = 0; i <= strlen(s)-1; i++ )
	    {
		   flag=false;
		   if (temp==strlen(s1)) break; 
		   kuohao=false;
		   if (s1[temp]=='(') kuohao=true;	
		   if (kuohao) {
		   for (   j = temp+1; s1[j]!=')' ; j++)
		    {
			    if  (s1[j]==s[i]) flag=true;	 
	   	    }
	   	   temp=j+1; 
		   }	else  { if (s1[temp]==s[i]) flag=true; temp++;}   	
		     	
	   	   if  (flag==false ) break;
 	    } 			  
 	    return flag;
    }
int main()
 {
   ifstream fin;
   fin.open("a.in");
   ofstream fout;
   fout.open("a.out");		  
   fin>>l>>d>>n;
   for (int i = 1; i <= d; i++ )
    {
	   fin>>s[i];		
	}   		
	for  (int i = 1 ; i <=n ; i++)
	 {
	  	 fin>>s1[i];
	  	// memset(f,true,sizeof(f));
		 ans=0;
		 for (int  j = 1 ; j <=d ; j ++)
		  {	 	   
             if (check(s[j],s1[i])) ans++;
	      } 
	     fout<<"Case #"<<i<<": "<<ans<<endl; 
	 }  
  	system("pause");	  
 }

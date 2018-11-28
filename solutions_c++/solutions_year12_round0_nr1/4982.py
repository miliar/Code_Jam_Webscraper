
//  bismillahir rahmani rahim thanks Allah 4 everything

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
#include<math.h>

#include<string>
#include<queue>

#define vec vector<int>
#define m_i map<int,string>
 #define m_s map<string ,int >

 #define fo_(a,b) for((a)=1;(a)<=(b);(a++))
 #define fo_1(b,a) for((b)=(a);(b)>=0;(b--))
  #define fo_0(b,a) for((b)=0;(b)<=(a);(b++))
  #define fo(a,b,c) for( (a)=(b);(a)<=(c);(a++))
  #define max 205
  #define MAX 205
  #define inf 1000000
    #define filer() freopen("in.txt","r",stdin)
#define filew() freopen("out.txt","w",stdout)

  using namespace std;

 map<char,char > set;
 
 void make();

 int main() 
 
 { 
	   
	   
	   filer();
	   filew();
	 make();
	 
	 int T; 
	 
	 
	 
	 cin >> T;
	 char e;
	 scanf("%c",&e);
	 
	  int a;
	  fo(a,1,T)
	  {
		  
		  char s[109];
		  
		   gets(s);
		   
		  
		  char str[109] ={0};
		  int r=0;
		  
		  int b;
		  for(b=0;b<strlen(s);b++)
		  {
			char d=s[b];
			if(d==' ')
			 {  
				
				  str[r++]= ' '; 
		        }
			else 
			{
				char w=set[d];
				str[r++]=w;
			}
		}
		
		
		   str[r]='\0';
		   
		   printf("Case #%d: ",a);
		   puts(str);
			
			
			
			  
		  }
			  
		  
		  
	 
	 
	 
	 
	 return 0;
 }
 
 
   void make()
   
   {
	  set['a']='y';
	  set['b']='h';
	  set['c']='e';
	  set['d']='s';
	  set['e']='o';
	  set['f']='c';
	  set['g']='v';
	  set['h']='x';
	  set['i']='d';
	  set['j']='u';
	  set['k']='i';
	  set['l']='g';
	  set['m']='l';
	  set['n']='b';
	  set['o']='k';
	  set['p']='r';
	  set['q']='z';
	  set['r']='t';
	  set['s']='n';
	  set['t']='w';
	  set['u']='j';
	  set['v']='p';
	  set['w']='f';
	  set['x']='m';
	  set['y']='a';
	  set['z']='q';
  }
	   
	   
 
 
	 
	 

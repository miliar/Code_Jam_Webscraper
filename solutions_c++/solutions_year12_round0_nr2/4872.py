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

 
    vec v_a[40];
    vec v_s[40];
    int c_a[42];
    int c_s[42];
    
    void make_set();
    
    
 
 int main()
 { 
	 
	 memset(c_a,0,sizeof(c_a));
	 memset(c_s,0,sizeof(c_s));
	 memset(v_a,0,sizeof(v_a));
	 
	 memset(v_s,0,sizeof(v_s));
	 
	 make_set();
	 
	
	 
	 int z;
	 fo(z,1,30)
	 
	 {  
		 printf("\n number is %d \n",z);
		if(c_a[z]==0)
		cout <<"notsurprise  absent" <<endl;
		 else 
		  printf("%d %d %d  %d\n",v_a[z][0],v_a[z][1],v_a[z][2],c_a[z]);
		 
		 if(c_s[z]==0)
		cout <<" surprise absent" <<endl;
		else 
		 printf("%d %d %d   %d\n",v_s[z][0],v_s[z][1],v_s[z][2],c_s[z]);
		 
	 }
	
	 
	 
	 
	 filer();
	 filew();
	 
	 
	 int T;
	 
	 cin >> T;
	 
	 int x;
	 fo(x,1,T)
	 
	 {
		 
		 int n,sur_p,p;
		 
		 int sav[105];
		 memset(sav,0,sizeof(sav));
		 
		 cin >> n >> sur_p >> p;
		 //printf("%d %d %d",n,sur_p,p);
		 
		 int k;
		 int ans=0;
		 int hand=0;
		 int sur=sur_p; 
		 fo(k,1,n)
		 { 
			
		    int sam;
		    cin >> sam;
		  //  printf(" %d",sam);
		    
		    int ij;
		    
		    if(sam==0&&p==0)
		    {
				ans++;
				continue;
			}
			else if(sam==0&&p>0)
			{
				continue;
			}
		    
		    if(c_a[sam]>=p && c_s[sam]<p)
		    {
				 ij=n-k+hand;
				 if(ij>sur)
				 ans++;
			}
			
			else if (c_s[sam]>=p && c_a[sam]<p)
			{
				
				
				if(sur!=0)
				{
					sur--;
					ans++;
				}
			}
			
			else if (c_a[sam]>=p && c_s[sam]>=p)
			
			{ 
				
				
				ans++;
				hand++;
				
			}
			
		    
		  } 
		  
		 // printf("\n");  
		 
		 	
		   printf("Case #%d: %d\n",x,ans);	
			 
			 
	}
		 
		 
	 
	  
	 
	 
	 
	 
	 
	 return 0;
 }
 
 
 void make_set()
 {
	 int a,b,c;
	 
	   fo(a,0,30)
	   {
		   fo(b,0,30)
		   {
			   fo(c,0,30)
			   {   
				   
				   if( a-b>2||b-a>2||b-c>2||c-b>2||a-c>2||c-a>2) continue;
				   if(a+b+c>30) continue;
				   
				int s=a+b+c;
				if(s==0&&c_a[s]==1) continue;
				else  if(s==0)
				{
					c_a[0]=1;
					v_a[0].push_back(0);
					v_a[0].push_back(0);
					v_a[0].push_back(0);
					
					
				}
				else 
				
				{  
					 int m;
				   
				   if( a-b==2||b-a==2||b-c==2||c-b==2||a-c==2||c-a==2)  
				   {
					 
					  if(a>b&&a>c) m=a;
					  else if(b>a&&b>c) m=b;
					  else m=c;
					  if(c_s[s]>=m) continue ;
					  
					  v_s[s].clear();
					  v_s[s].push_back(a);
					v_s[s].push_back(b);
					v_s[s].push_back(c);
					
					c_s[s]=m;
					  
					  
					   
				   }
				   
				   else 
				   
				   
				   {
					   
					    if(a>b&&a>c) m=a;
					  else if(b>a&&b>c) m=b;
					  else m=c;
					  if(c_a[s]>=m) continue ;
					  
					    v_a[s].clear();
					  v_a[s].push_back(a);
					v_a[s].push_back(b);
					v_a[s].push_back(c);
					
					c_a[s]=m;
					   
					   
					   
				   }
				  	
					
					
					
				}
				
				
					
				 
				 
				   
				   
			   }
			   
		   }
		   
	   }
   }
 
	 
	 
	




/*
    anick saha
*/
 
#include <sstream>
#include <iostream>
#include <fstream>
#include<cstdlib>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<cassert>
#include<functional>
#include<numeric>
#include<bitset>
#include<utility>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<deque>
#include<list>
#include<map>
#include<set>
#include<iterator>
#include<ctime>
 
 
using namespace std;
 
 
#define MAX(A,B) (A)>(B)?(A):(B)
#define MIN(A,B) (A)<(B)?(A):(B)
#define lcm(a,b)  { return a*b/gcd(a,b);  }
 
 
typedef long long ll;
typedef long double ld;
typedef long long unsigned int llu;
 
 
#define SL(x) scanf("%lld",&x)
#define SLL(x) scanf("%llu",&x)
#define S(x) scanf("%d",&x)
#define SS(x) scanf("%s",s)
#define P(x) printf("%d",x)
#define PL(x) printf("%lld",x)
#define PLL(x) printf("%llu",x)
#define PS(x) printf("%s",x)
#define FOR(x) for(int i=1;i<=x;i++)
#define f_FOR(p,q,r) for(int p=q;p<=r;p++)
#define REV(x) for(int i=x;i>0;i--)
#define r_REV(p,q,r) for(int p=q;p<=r;p--)
#define W(x) while(x--)
#define TC int t;for(scanf("%d",&t);t>0;t--)
#define NL printf("\n")
 

#define M 1000000007


int main()
{
    //freopen("C:\\Users\\Anick\\Desktop\\in.txt","r",stdin);
    //freopen("C:\\Users\\Anick\\Desktop\\out.txt","w",stdout);
     
	 int t,cases=0;

	 char a[4][4];
	 scanf("%d",&t);
     
     for(cases=1;cases<=t;cases++)
     {
			for(int i=0;i<4;i++)
				for(int j=0;j<4;j++)
					cin>>a[i][j];
					
					
			printf("Case #%d: ",cases);
			
			bool win=false;
			bool complete=true;
			
			for(int i=0;i<4;i++)
				for(int j=0;j<4;j++)
					if(a[i][j]=='.')
						complete=false;
			
			
		
			for(int i=0;i<4;i++)
			{
				if(((a[i][0]=='X'||a[i][0]=='T')&&(a[i][1]=='X'||a[i][1]=='T')&&(a[i][2]=='X'||a[i][2]=='T')&&(a[i][3]=='X'||a[i][3]=='T'))
					||((a[0][i]=='X'||a[0][i]=='T')&&(a[1][i]=='X'||a[1][i]=='T')&&(a[2][i]=='X'||a[2][i]=='T')&&(a[3][i]=='X'||a[3][i]=='T'))
				    || ((a[0][0]=='X'||a[0][0]=='T')&&(a[1][1]=='X'||a[1][1]=='T')&&(a[2][2]=='X'||a[2][2]=='T')&&(a[3][3]=='X'||a[3][3]=='T'))
					||((a[0][3]=='X'||a[0][3]=='T')&&(a[1][2]=='X'||a[1][2]=='T')&&(a[2][1]=='X'||a[2][1]=='T')&&(a[3][0]=='X'||a[3][0]=='T')) )
				{    
					cout<<"X won"<<endl;
					win=true;
					break;
			    }
			}
			
			if(win)
				continue;
				
		for(int i=0;i<4;i++)
			{
				if(((a[i][0]=='O'||a[i][0]=='T')&&(a[i][1]=='O'||a[i][1]=='T')&&(a[i][2]=='O'||a[i][2]=='T')&&(a[i][3]=='O'||a[i][3]=='T'))
				    ||((a[0][i]=='O'||a[0][i]=='T')&&(a[1][i]=='O'||a[1][i]=='T')&&(a[2][i]=='O'||a[2][i]=='T')&&(a[3][i]=='O'||a[3][i]=='T'))
				    ||((a[0][0]=='O'||a[0][0]=='T')&&(a[1][1]=='O'||a[1][1]=='T')&&(a[2][2]=='O'||a[2][2]=='T')&&(a[3][3]=='O'||a[3][3]=='T'))
					||((a[0][3]=='O'||a[0][3]=='T')&&(a[1][2]=='O'||a[1][2]=='T')&&(a[2][1]=='O'||a[2][1]=='T')&&(a[3][0]=='O'||a[3][0]=='T')) )
				{    
					cout<<"O won"<<endl;
					win=true;
					break;
			    }
			}
			
			if(win)
				continue;
				
			if(!complete)
				cout<<"Game has not completed"<<endl;
			else
				cout<<"Draw"<<endl;
			   
            
			
			
			
			
               
			           
     
     } // TC 
     
     
     return 0;
}


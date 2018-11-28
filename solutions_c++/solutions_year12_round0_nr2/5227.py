#include<stdio.h>
#include<string.h>
#include<memory.h>
#include<math.h>
#include<iostream>
#include <vector>
#define fi(a,b) for( i = a; i < b ; i++ )
#define fj(a,b) for( j = a; j < b ; j++ )
#define fk(a,b) for( k = a; k < b ; k++ )

using namespace std;

int ri()
	{ int a; 
	  scanf( "%d", &a ); 
	  return a; 
	}

typedef vector<int> vi;

int main()
{
	
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );

	int i=0, t , j, k, tt, n, s, p, q, r,sol=0;

	scanf("%d",&tt);
	
	for(t=1;t<=tt;t++)
	{
		scanf("%d",&n); scanf("%d",&s); scanf("%d",&p);
		sol=0;
		vi v;	v.clear();
		fi(0,n)	{v.push_back(ri());}
		
		fi(0,n)
		{	if ((s==0)&&(p==0))
			sol = n; else {
			q = v[i]/3;
			r = v[i]%3;
			
			switch(r)
			{
			case 0 : if ((q >= p) && (v[i]!=0))
					 { sol++; }	else if(((q+1) >= p) && (s > 0) &&(v[i]!=0))
											{ sol++; s--;}	break;
			case 1 : if ((q >= p) || ((q+1) >=p))
					 {	sol ++; }	//else if((q+1) >= p) && (s > 0))
									//		{ sol++; s--;}	
					 break;
			case 2 : if ((q >= p) || ((q+1) >=p))
					 {	 sol++; }	else if(((q+2) >= p) && (s > 0))
											{ sol++; s--;}	break;
			default : cout<<"Mismatch"<<endl;
			}
		}
		}
		printf("Case #%d: %d\n",t,sol);
	}
}	
		

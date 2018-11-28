//Prateek Garg :Author

#include <cstdio>
#include <fstream>
#include <iostream>

using namespace std;

int main()
{
	ifstream in("B-small-attempt1.in");
	ofstream out("B-small-attempt1.out");
int i=0;
int count;
int t;
int max;
int a, b, c;
int exp;
int n;
int r;// total
//scanf("%d", &t);
in>>t;
while(t-->0)
{
i++;
count=0;
//scanf("%d", &n);
//scanf("%d", &exp);
//scanf("%d", &max);
in>>n;
in>>exp;
in>>max;
while(n-->0)
	{
		//scanf("%d", &r);
		in>>r;
		{	  
		  a=max;	b=max; 		c=max; 
		 if(a*3<=r && r<=30)
			{count++;continue;}                 
			{
				 c--;
				 if(a+b+c==r && c>=0 && b>=0){ count++;continue;}
					{
						 b--;			
						if(a+b+c==r && c>=0 && b>=0) {count++;continue;}
					}
			}	
		}

		if(exp>0)
		{
                   c--; 
			if(a+b+c==r && c>=0 && b>=0){ count++;exp--;continue;}
		   b--;
			if(a+b+c==r && c>=0 && b>=0) {count++;exp--;continue;}
		}	
	}
//printf("\nCase #%d: %d", i,count);
out<<"Case #"<<i<<": "<<count<<"\n";
}
in.close();
out.close();
return 0;

}

#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	ifstream in;
	ofstream out;
  	in.open ("A-large.in");
  	out.open("out.in");
  	int n,i,j,k,xc1,oc1,xc2,oc2,xc3,oc3,xc4,oc4,d;            // skip case 2 not complete
  	char x[4][4];
  	in>>n;
  	for(i=1;i<=n;i++)
  	{
		xc1=0;
		oc1=0;
		xc2=0;
		oc2=0;
		xc3=0;
		oc3=0;
		xc4=0;
		oc4=0;
		d=0;
		
		// fill array 
		
		for(j=0;j<4;j++)	
			for(k=0;k<4;k++)  
			{
				in>>x[j][k];
			}
							
			
			//////////////////////
			
			
				for(j=0,k=0;j<4;k++,j++)
			{
				if(x[j][k]=='X'||x[j][k]=='T')
				{
					xc1++;	
				}
				if(x[j][k]=='O'||x[j][k]=='T')
				{
					oc1++;	
				}
				
				if(x[j][k]=='.')
				{
					d=1;	
				}
				
				
				if(xc1==4)
				{
					break;	
				}
				if(oc1==4)
				{
				break;	
				}
			}
		
		
		////////////////////////////////////////
			
			
			for(j=0,k=3;j<4;k--,j++)
			{
				if(x[j][k]=='X'||x[j][k]=='T')
				{
					xc2++;	
				}
				if(x[j][k]=='O'||x[j][k]=='T')
				{
					oc2++;	
				}
				
				if(x[j][k]=='.')
				{
					d=1;	
				}
				
				if(xc2==4)
				{
					break;	
				}
				if(oc2==4)
				{
					break;	
				}
			}
			
			
			
			for(j=0;j<4;j++)
			{	
				xc3=0;
				oc3=0;
				for(k=0;k<4;k++)
				{
					if(x[j][k]=='X'||x[j][k]=='T')
					{
						xc3++;	
					}
					if(x[j][k]=='O'||x[j][k]=='T')
					{
						oc3++;	
					}
					
					if(x[j][k]=='.')
					{
						d=1;	
					}
					
				}
				if(xc3==4)
				{
					break;	
				}
				if(oc3==4)
				{
					break;	
				}
			}
			
			
			
			
			
			for(k=0;k<4;k++)
			{	
				xc4=0;
				oc4=0;
				for(j=0;j<4;j++)
				{
					if(x[j][k]=='X'||x[j][k]=='T')
					{
						xc4++;	
					}
					if(x[j][k]=='O'||x[j][k]=='T')
					{
						oc4++;	
					}
				
				
					if(x[j][k]=='.')
					{
						d=1;	
					}
				
				}
				if(xc4==4)
				{
					break;	
				}
				if(oc4==4)
				{
					break;	
				}
			}
			
			
		
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
				if(xc1==4||xc2==4||xc3==4||xc4==4)
				{
					out<<"Case #"<<i<<": X won"<<endl;	
					continue;
				}
				if(oc1==4||oc2==4||oc3==4||oc4==4)
				{
					out<<"Case #"<<i<<": O won"<<endl; 
					continue;
				}
				
				 if(!d)
				{
					out<<"Case #"<<i<<": Draw"<<endl; 
					continue;
				}
				
				
				
				 if(d)
				{
					out<<"Case #"<<i<<": Game has not completed"<<endl; 
					continue;
				}
				
				
				
				
				
				
	}
	return 0;
}

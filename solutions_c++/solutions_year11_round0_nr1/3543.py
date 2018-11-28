#include<iostream>
#include<cstdio>
#include<map>
#include<vector>
using namespace std;

int main()
{
 	FILE *f1,*f2;
 	f1=fopen("Input.txt","r");
 	f2=fopen("Output.txt","w+");
 	int t;
 	fscanf(f1,"%d",&t);
 	for(int i=1;i<=t;i++)
 	{
	 		int n;
	 		fscanf(f1,"%d",&n);
	 		int opos,oval,bpos,bval,val;
	 		opos=1;bpos=1;oval=0;bval=0;val=0;
			 		//cout<<n<<endl;
	 		while(n--)
	 		{
			 		char* c = new char[10];
			 		int x,y;
			 		fscanf(f1,"%s",c);
			 		fscanf(f1,"%d",&x);
			 		if(c[0]=='O')
			 		{
					 		  //cout<<val;
					 		  y=val-oval;
					 		  opos=x-opos;
					 		  if(opos<0) opos=0-opos;
					 		  y=opos-y;
					 		  if(y<0) y=0;
					 		  opos=x;
					 		  oval=y+val+1;
					 		  //cout<<"\n"<<y<<"  "<<val<<" "<<oval<<"\n"; 
					 		  val=oval;
	 		  		}
	 		  		else if(c[0]=='B')
	 		  		{
					 		  //cout<<val;
					 		  y=val-bval;
					 		  bpos=x-bpos;
					 		  if(bpos<0) bpos=0-bpos;
					 		  y=bpos-y;
					 		  if(y<0) y=0;
					 		  bpos=x;
					 		  bval=y+val+1;
					 		  //cout<<"\n"<<y<<"  "<<val<<" "<<bval<<"\n";
					 		  val=bval;
					 }
	 		}
	 		//cout<<val<<endl<<endl;
	 		fprintf(f2,"Case #%d: %d\n",i,val);
	}
	fclose(f1);
	fclose(f2);
	system("pause");
}

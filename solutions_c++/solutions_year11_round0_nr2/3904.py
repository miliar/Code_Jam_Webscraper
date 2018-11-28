#include <iostream>
#include<string>
#include<fstream>
using namespace std;
#ifndef NULL
#define NULL 0
#endif


bool check(string*& input,int E0,int E1,string*& Com);
int main ()
{   
	ofstream fout ("Sol12345.txt");
    ifstream fin ("B-small-attempt6.in");
	int T;
	fin>>T;
	for(int i=0;i<T;i++)
	{
		fout<<"Case #"<<(i+1)<<": [";
		//Taking inputs
		std::string::size_type k = 0; 

		int C;
		fin>>C;
		string *Combine;

		Combine =NULL;
		for(int j=0;j<C;j++)
		{   Combine=new string;
		    
			fin>>*Combine;
			(*Combine).resize(101);
		}
		int D;
		fin>>D;
		string *Erase;
		Erase=NULL;
		for(int j=0;j<D;j++)
		{   Erase=new string;
		   
			fin>>*Erase;
			(*Erase).resize(101);
		}
		int N;
		fin>>N;
		string *input;
		input=NULL;
		for(int j=N-1;j<N;j++)
		{   input=new string;
		
			fin>>*input;
			(*input).resize(101);
		}
		
		
		//End
	
	
			for(int i=0;i<N-1;i++)
			{  
				if(Erase!=NULL)
			  {
				for(int j=i+1;j<N;j++)
				{
					if((*input)[i]==(*Erase)[0])
					{
						if((*input)[j]==(*Erase)[1])
							{   
								bool check1=true;
						if(Combine != NULL)
						{
						        check1=check(input,j,i,Combine);
						}		
								if(check1)
								{
								  for(int mnb=0;mnb<=j;mnb++)
									 {
										 (*input)[mnb]='0';
									 }
								}
						    
					        }
					}
					else if((*input)[i]==(*Erase)[1])
					{
						if((*input)[j]==(*Erase)[0])
							{   bool check1=true;
						        if(Combine != NULL)
								{
						        check1=check(input,j,i,Combine);
								}
								if(check1)
								{
								   for(int mnb=0;mnb<=j;mnb++)
									 {
										 (*input)[mnb]='0';
									 }
								}
						    }
					}
				
			 }
			

	      			
			

			
			
	        }
			    
			
			}
			k=0;
			while((k=(*input).find('0',k))!=(*input).npos)
			           {
                          (*input).erase(k, 1);
                       }
			
			if(Combine!=NULL)
			    {   //Remove NULL IN inputs
			    							
					

					 //check for Comine
					for(int mn=0;mn<(*input).length()-1;mn++)
					{
						check(input,mn,mn,Combine);
					}
					 k = 0; 

					while((k=(*input).find('0',k))!=(*input).npos)
			           {
                          (*input).erase(k, 1);
                       }
					

			    }

			 //Print
			
			for(int h=0;h==0 ||(*input)[h]!=0;h++)
			{    if((*input)[0]==0)
					fout<<"]"<<endl;
			else	if((*input)[h+1]==0)
			    
			{
					fout<<(*input)[h]<<"]"<<endl;
					break;
			}  
			
			else
				fout<<(*input)[h]<<", ";
			}


		
	}
	return 0;
}

	
bool check(string*& input,int E1,int E0,string*& Com)
{  
	bool check1=true;
	int x=1;
	int y=1;
	while((E0-x)>=0&&(*input)[E0-x]=='0' )
	{
		x--;
	}
	while( (E0+y)!=E1 && (*input)[E0+y]=='0')

	{
		y++;
	}
	int z=1;
	while((E1-z)>0 && (E1-z)!=E0 &&(*input)[E1-z]=='0' )
	{
		z--;
	}
   if((*input)[E0]==(*Com)[0])
	{ 
		if((E0-x)>=0&&(*input)[E0-x]==(*Com)[1])
		{  
			check1 =false;
			(*input)[E0]=(*Com)[2];
			(*input)[E0-x]='0';
		}

	}
	else if((*input)[E0]==(*Com)[1])
	{ 
		if((E0-x)>=0 &&(*input)[E0-x]==(*Com)[0])
		{    check1=false;
			(*input)[E0]=(*Com)[2];
			(*input)[E0-x]='0';
		}

	}
	 if((*input)[E0]==(*Com)[0])
	{ 
		if((E0+y)<=E1&&(*input)[E0+y]==(*Com)[1])
		{   check1 =false;
			(*input)[E0]=(*Com)[2];
			(*input)[E0+y]='0';
		}

	}
	else if((*input)[E0]==(*Com)[1])
	{ 
		if((E0+y)<=E1 && (*input)[E0+y]==(*Com)[0])
		{   check1 =false;
			(*input)[E0]=(*Com)[2];
			(*input)[E0+y]='0';
		}

	}

	
	if((*input)[E1]==(*Com)[0])
	{ 
		if((E1-z)>=E0 && (*input)[E1-z]==(*Com)[1])
		{   check1 =false;
			(*input)[E1]=(*Com)[2];
			(*input)[E1-z]='0';
		}

	}
	else if((*input)[E1]==(*Com)[1])
	{ 
		if((E1-z)>=E0 &&(*input)[E1-z]==(*Com)[0])
		{   check1 =false;
			(*input)[E1]=(*Com)[2];
			(*input)[E1-z]='0';
		}

	}
	return check1;
}

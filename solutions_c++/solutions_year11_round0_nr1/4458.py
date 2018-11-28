#include<iostream>
#include<string>
#include<cstring>
#include<fstream>

using namespace std;


class Robot
{
public:

int current;
int next;


Robot()
	{
	current = 1;
	next = 0;
	}


}orange, blue;

int main()
{
int onext = 0;
int bnext = 0;
int ocurrent = 1;
int bcurrent = 1;
char currentRob = 'X';		// 0-Orange 1-Blue


int t=0;
int k=1;

int oArr[100] = {0};
int bArr[100] = {0};
char robArr[100] = {'X'};
int oa = 0;
int ba = 0;
int ra = 0;

ifstream fi;
fi.open("A-small-attempt0.in");

ofstream fo;
fo.open("output.txt");

string str;
int j=0;
int n=0;
string nstr = "";
string ostr = "";
string bstr = "";
int opos = 0;
int bpos = 0;

int steps = 0;

if(fi.good())
	{
	getline(fi,str);
	t = atoi(&str[0]);
	//cout<<"\nT = "<<t<<endl;
	
	
	for(int i=0; i<t; i++)
		{
		getline(fi,str);
		//cout<<"\nstr = "<<str<<endl;
		j=0;
		nstr = "";
		
		for(int i2=0; i2<100; i2++)
			{
			bArr[i2] = oArr[i2] = 0;
			robArr[i2] = 'X';
			}
		ba = oa = ra = 0;
		
		while(str[j]==' ')
			{j++;}
		
		while(str[j]!=' ')
			{
			nstr = nstr + str[j];
			j++;
			}
		n = atoi(&nstr[0]);
		//cout<<"\nn = "<<n<<endl;
		
		
		for(int i1=0; i1<n; i1++)
			{
			ostr = bstr = "";
			opos = bpos = 0;
			
			while(str[j]==' ') j++;
			
			if( str[j]=='O' )
				{
				robArr[ra] = 'O'; ra++;
				
				j =  j+2;
				
				while(str[j]!=' ')
					{
					ostr = ostr + str[j];					
					j++;
					}
				opos = atoi(&ostr[0]);
				oArr[oa] = opos;
				oa++;
				
				continue;
				
				}
			else
			if( str[j]=='B' )
				{
				robArr[ra] = 'B'; ra++;
				
				j =  j+2;
				
				while(str[j]!=' ')
					{
					bstr = bstr + str[j];					
					j++;
					}
				bpos = atoi(&bstr[0]);
				bArr[ba] = bpos;
				ba++;
				
				continue;
				}
			
			
			
			}
		
		
			
		// cout<<endl<<endl;
		
		// for(int i=0; i<100; i++)
			// cout<<oArr[i]<<" ";
			// cout<<endl<<endl;
		
		// for(int i=0; i<100; i++)
			// cout<<bArr[i]<<" ";
			// cout<<endl<<endl;
		
		// for(int i=0; i<100; i++)
			// cout<<robArr[i]<<" ";
			// cout<<endl<<endl;
		
		
		
		
		ra = oa = ba =0;
		
		currentRob = robArr[ra];
		onext = oArr[ra];
		bnext = bArr[ra];
		ocurrent = bcurrent = 1;
		
		steps = 0;
		
		while(currentRob == 'O' || currentRob == 'B')
			{
			if(currentRob == 'O')
				{
				while(ocurrent != onext)
					{
					if(ocurrent < onext) ocurrent++;
					else if(ocurrent > onext) ocurrent--;
					
					if(bcurrent < bnext) bcurrent++;
					else if(bcurrent > bnext) bcurrent--;
					
					steps++;
					
					}
				if(ocurrent == onext)
					{
					if(bcurrent < bnext) bcurrent++;
					else if(bcurrent > bnext) bcurrent--;
					
					steps++;
					
					oa++; ra++;
					onext = oArr[oa];
					currentRob = robArr[ra];
					continue;
					}
				
				
				}
			
			else
			if(currentRob == 'B')
				{
				while(bcurrent != bnext)
					{
					if(ocurrent < onext) ocurrent++;
					else if(ocurrent > onext) ocurrent--;
					
					if(bcurrent < bnext) bcurrent++;
					else if(bcurrent > bnext) bcurrent--;
					
					steps++;
					
					}
				if(bcurrent == bnext)
					{
					if(ocurrent < onext) ocurrent++;
					else if(ocurrent > onext) ocurrent--;
					
					steps++;
					
					ba++; ra++;
					bnext = bArr[ba];
					currentRob = robArr[ra];
					continue;
					}
				
				
				}
			
			
			
			
			
			
			
			
			}
		cout<<"\nSTEPS = "<<steps<<endl;
		fo<<"Case #"<<k<<": "<<steps<<endl;
		k++;
		}
		
		
		
	
	

	
	
	
	
	}
fi.close();
fo.close();


return 0;
}



#include<iostream>
#include<string>
#include<cstring>
#include<fstream>


using namespace std;

class row
{
public:

char *col;
string st;





};




int main()
{

int t,r,c;
string str;
row* rr;
bool check=0;

ifstream fi;
fi.open("inp.txt");

ofstream fo;
fo.open("out.txt");



fi>>t;


for(int i=0; i<t; i++)
	{
	fo<<"Case #"<<i+1<<":"<<endl;
	
	fi>>r>>c;
	cout<<"\nr="<<r<<"   c="<<c<<endl;
	
	rr = new row[r];
	
	for(int i2=0; i2<r; i2++)
		{
		
		}
	
	
	
	for(int i1=0; i1<r; i1++)
		{
		
		fi>>str;
		
		//cout<<"\nstr = "<<str;
		
		rr[i1].st = str;
		
		cout<<"\nrow"<<i1<<" string = "<<rr[i1].st;
		
		
				
		}
	
	check = 0;
	
	
	for(int i1=0; i1<r; i1++)
		{
		
		for(int i2=0; i2<c; i2++)
			{
			
			if(rr[i1].st[i2]=='#')
				{
				if(i2+1<c && i1+1<r  && rr[i1].st[i2+1]=='#' && rr[i1+1].st[i2]=='#' && rr[i1+1].st[i2+1]=='#')
					{
					rr[i1].st[i2] = '/';
					rr[i1].st[i2+1] = '\\';
					rr[i1+1].st[i2] = '\\';
					rr[i1+1].st[i2+1] = '/';
					
									
					}
				else
				{
				
				check = 1;
				break;
				}
				}
			else continue;
			
			
			
			
			}
		
		 if(check==1)
			{
			//fo<<"Impossible"<<endl;
			break;
			}
		else
			{
			//fo<<rr[i1].st<<endl;
			continue;
			} 
		}
	
	if(check!=1)
		{
		for(int i1=0; i1<r; i1++)
			{
			fo<<rr[i1].st<<endl;
			
			
			}
		
		
		}
	else fo<<"Impossible"<<endl;
	
		
	
	
	
	
	}







fi.close();
fo.close();

return 0;
}



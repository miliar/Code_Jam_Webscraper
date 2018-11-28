#include<iostream>
using namespace std;
int main()
{
	int o[100],b[100],T,N,button,i,j,x,y,sec,o_pos,b_pos;
	char seq[101],r;
	
	cin>>T;
	for(i=0;i<T;i++)
	{
		cin>>N;
		for(j=0,x=0,y=0;j<N;j++)
		{
			cin>>r;
			cin>>button;
			
			seq[j] = r;
			
			switch(r)
			{
				case 'O':
					o[x++]=button;
					break;
				case 'B':
					b[y++]=button;
					break;
			}
		}
		for(sec=0,o_pos=1,b_pos=1,x=0,y=0,j=0; j<N ;sec++)
		{
			r=seq[j];
			switch(r)
			{
				case 'O':
					if(o_pos<o[x])
						o_pos++;
					else if(o_pos>o[x])
						o_pos--;
					else
					{
						seq[j]=0;
						j++;
						o[x]=-1;
						x++;
					}
					
					if(b_pos < b[y])
						b_pos ++;
					else if(b_pos >b[y])
						b_pos --;					
					break;
				
				case 'B':
					if(b_pos<b[y])
						b_pos++;
					else if(b_pos > b[y])
						b_pos --;
					else
					{
						seq[j] = 0;
						j ++ ;
						b[y] = -1;
						y++;
					}
					
					if(o_pos< o[x])
						o_pos ++;
					else if(o_pos > o[x])
						o_pos --;
					break;
			}
		}
		cout<<"Case #"<<i+1<<": "<<sec<<endl;
	}
}
						
				
						

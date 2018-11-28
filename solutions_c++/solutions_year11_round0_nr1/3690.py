#include<iostream>

using namespace std;

int main()
{
	int n,N,t,T,i,j,k,b_dest,o_dest,move,o_pos,b_pos,push_flag;
	char ch;
	
	int *O,*B;
	char *order;
	cin>>T;
	for(t=0;t<T;t++)
	{
		cin>>N;
		
		O = new int[N];
		B = new int[N];
		order = new char[N];
		
		for(n=0,i=0,j=0;n<N;n++)
		{
			cin>>order[n];
			//cout<<order[n]<<" ";
			
			if(order[n] == 'O')
			{
				cin>>O[i];
				//cout<<O[i]<<" ";
				i++;
			}
			else
			{
				cin>>B[j];
				//cout<<B[j]<<" ";
				j++;
			}
		}		
		
		o_dest = O[0];
		b_dest = B[0];
		o_pos = 1;
		b_pos = 1;
 		i=j=k=0;
		
		move = 0;
		//int l;
		//for(l=0;l<N;l++)
			//cout<<order[l];
			
		while(k<N)
		{
			//cout<<"\n"<<move+1<<"("<<order[k]<<":\n";
			push_flag = 0;
			if(order[k] == 'O' && o_pos == o_dest)
			{
				//cout<<"\nOrange pushes "<<o_dest;
				o_dest = O[i+1];
				//cout<<"\nNew dest"<<o_dest;
				i++;
				k++;
				push_flag = 1;
			}
			else
			{
				if(o_pos > o_dest)
				{
					o_pos--;
					//cout<<"\nOrange to "<<o_pos;
				}
				
				if(o_pos < o_dest)
				{
					o_pos++;
					//cout<<"\nOrange to "<<o_pos;
				}
			}
			
			if(order[k] == 'B' && b_pos == b_dest && push_flag == 0)
			{
				//cout<<"\nBlue pushes "<<b_dest;
				b_dest = B[j+1];
				j++;
				k++;
			}
			else
			{
				if(b_pos > b_dest)
				{
					b_pos--;
					//cout<<"\nBlue to "<<b_pos;
				}
				
				if(b_pos < b_dest)
				{
					b_pos++;
					//cout<<"\nBlue to "<<b_pos;
				}
			}
			move++;
		}
		
		cout<<"Case #"<<t+1<<": "<<move<<"\n";
		delete O;
		delete B;
		delete order;
	}

}

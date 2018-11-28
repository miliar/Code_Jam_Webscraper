#include<iostream>

using namespace std;

template <class T>
void myswap(T &a , T &b)
{
	T temp;
	temp=a;
	a=b;
	b=temp;
	
}

int hash(char ch)
{
	//Q, W, E, R, A, S, D, F
	switch(ch)
	{
		case 'Q': return 0;
		case 'W': return 1;
		case 'E': return 2;
		case 'R': return 3;
		case 'A': return 4;
		case 'S': return 5;
		case 'D': return 6;
		case 'F': return 7;
		default :return -1;
	}
	
}

int main()
{
	string temp,oppose[8],invk_list,stack;
	int genX[8][8],i,j,r,c,N,C,t,T,D,cast,top_int;
	char gen[8][8];
	cin>>T;
	
	for(t=0;t<T;t++)
	{
		cin>>C;
		
		for(i=0;i<8;i++)
			for(j=0;j<8;j++)
				genX[i][j]=0;
		
		for(i=0;i<C;i++)
		{
			cin>>temp;
			
			r = hash(temp[0]);
			c = hash(temp[1]);

			genX[r][c] = 1;
			genX[c][r] = 1;

			gen[r][c] = temp[2];
			gen[c][r] = temp[2];	
		}
		
			
		cin>>D;
		
				
		for(i=0;i<D;i++)
		{
			cin>>temp;
			oppose[hash(temp[0])].append(temp.substr(1,1));
			oppose[hash(temp[1])].append(temp.substr(0,1));
		}
		
		cin>>N;
		
		cin>>invk_list;
				
		while(invk_list.length() != 0)
		{
			cast = hash(invk_list[0]); 
			//cout<<"\nstack:"<<stack;
			//cout<<"\ninvoking"<<invk_list[0];
						
			if(stack.length() != 0)
			{
				top_int = hash(stack[stack.length()-1]);
				
				if( top_int != -1 && cast != -1 && genX[top_int][cast] == 1 )
				{
					//for(i=0;i<8;i++)
						//for(j=0;j<8;j++)
							//cout<<gen[i][j];
					stack[stack.length()-1] = gen[top_int][cast];
					invk_list.erase(0,1);
					continue;
				}
			}
			
			if(stack.find_first_of(oppose[cast]) != string::npos)
			{
				stack.clear();
				invk_list.erase(0,1);
				continue;
			}	
				
			stack.append(invk_list.substr(0,1));	
			invk_list.erase(0,1);
			
		}
		
		cout<<"Case #"<<t+1<<": [";
		
		
		if(stack.length() != 0)
		{
			cout<<stack[0];
			
			for(i=1;i<stack.length();i++)
			{
				cout<<", "<<stack[i];
			}	

		}
		cout<<"]\n";
		
		for(i=0;i<8;i++)
			oppose[i].clear();
			
		stack.clear();
	}

}

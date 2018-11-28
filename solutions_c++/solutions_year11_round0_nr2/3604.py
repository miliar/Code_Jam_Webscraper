#include<iostream>
#include<cstring>
using namespace std;

struct comb
{
	char base1;
	char base2;
	char nbase;
};
struct oppose
{
	char base3;
	char base4;
};
int main(void)
{
	int t;
	cin>>t;
	
	for(int i=0;i<t;i++)
	{
		int c,d,n;
		cin>>c;
		if(c!=0)
		{
			comb combine[c];
		
			for(int l=0;l<c;l++)
			{
				cin>>combine[l].base1;
				cin>>combine[l].base2;
				cin>>combine[l].nbase;
			}
			cin>>d;
			if(d!=0)
			{
				oppose check[d];
				
				for(int l=0;l<d;l++)	
				{
					cin>>check[l].base3;
					cin>>check[l].base4;
				}
				cin>>n;
			
				char list[n];
				memset(list,'\0',sizeof(list));
				int m=0;
				for(int l=0;l<n;l++)//invoke loop
				{	
					cin>>list[m];
					if(m==0)
					{
						m++;
						continue;
					}
					int rem =0;
					for(int q=0;q<c;q++)//combine
					{
						if(list[m]==combine[q].base1 )
						{
							if(list[m-1]==combine[q].base2)
							{
								list[m-1]=combine[q].nbase;
								list[m]='\0';
								m--;
								rem=1;
								break;
							}
						}
						else if (list[m]==combine[q].base2)
						{
							if(list[m-1]==combine[q].base1)
							{
								list[m-1]=combine[q].nbase;
								list[m]='\0';
								m--;	
								rem=1;
								break;
							}				
						}
					}
					
					if(rem!=1 )//oppose
					{
						for(int q=0;q<d;q++)
						{
							if(list[m]==check[q].base3)
							{
								int u=0;
								while(u<=m)
								{
									if(list[u]==check[q].base4)
										break;
									u++;
								}
										
								if(u<m)
								{
									for(int y=0;y<=m;y++)
										list[y]='\0';
								
									m=-1;
									break;
								}	
							}
							else if(list[m]==check[q].base4)
							{
								int u=0;
								while(u<=m)
								{
									if(list[u]==check[q].base3)
										break;
									u++;						
								}
								if(u<m)
								{
									for(int y=0;y<=m;y++)
										list[y]='\0';
								
									m=-1;
									break;									
								}						
							}
						
						}
					}
				
					m++;
				}
				
				cout<<"Case #"<<i+1<<": [";
				int p=0;
				while(list[p]!='\0')
				{
					if(p!=0)
						cout<<" ";
					cout<<list[p];
					p++;
					if(list[p]!='\0')
						cout<<",";
				}	
				cout<<"]\n";
			}
			
			else
			{
				cin>>n;
				char list[n];
				memset(list,'\0',sizeof(list));
				int m=0;
				for(int l=0;l<n;l++)//invoke loop
				{	
					cin>>list[m];
					if(m==0)
					{
						m++;
						continue;
					}
					for(int q=0;q<c;q++)//combine
					{
						if(list[m]==combine[q].base1 )
						{
							if(list[m-1]==combine[q].base2)
							{
								list[m-1]=combine[q].nbase;
								list[m]='\0';
								m--;
								break;
							}
						}
						else if (list[m]==combine[q].base2)
						{
							if(list[m-1]==combine[q].base1)
							{
								list[m-1]=combine[q].nbase;
								list[m]='\0';
								m--;
								break;								
							}				
						}
					}
					m++;
				}
				
				cout<<"Case #"<<i+1<<": [";
				int p=0;
				while(list[p]!='\0')
				{
					if(p!=0)
					cout<<" ";
					cout<<list[p];
					p++;
					if(list[p]!='\0')
						cout<<",";
				}	
				cout<<"]\n";
			}
			continue;
		}
		cin>>d;
		if(d!=0)
		{
			oppose check[d];
			
			for(int l=0;l<d;l++)	
			{
				cin>>check[l].base3;
				cin>>check[l].base4;
			}
				cin>>n;
			
			char list[n];
			memset(list,'\0',sizeof(list));
			int m=0;
			for(int l=0;l<n;l++)//invoke loop
			{	
				cin>>list[m];
				if(m==0)
				{
					m++;
					continue;
				}
				
				for(int q=0;q<d;q++)
				{
					if(list[m]==check[q].base3)
					{
						int u=0;
						while(u<=m)
						{
							if(list[u]==check[q].base4)
								break;
							u++;
						}
								
						if(u<m)
						{
							for(int y=0;y<=m;y++)
								list[y]='\0';
							
							u--;
							m=-1;
							break;
						}	
					}
					else if(list[m]==check[q].base4)
					{
						int u=0;
						while(u<=m)
						{
							if(list[u]==check[q].base3)
								break;
							u++;						
						}
						if(u<m)
						{
							for(int y=0;y<=m;y++)
								list[y]='\0';
						
							u--;
							m=-1;
							break;							
						}						
					}
				
				}
				m++;
			}
			
			cout<<"Case #"<<i+1<<": [";
			int p=0;
			while(list[p]!='\0')
			{
				if(p!=0)
					cout<<" ";
				cout<<list[p];
				p++;
				if(list[p]!='\0')
					cout<<",";
			}	
				
			cout<<"]\n";	
		}
		else
		{
			cin>>n;
		
			char list[n];
			for(int l=0;l<n;l++)
				cin>>list[l];
			cout<<"Case #"<<i+1<<": [";
			int l=0;
			while(l<n)
			{
				if(l!=0)
					cout<<" ";
				cout<<list[l];
				l++;
				if(l<n)
					cout<<",";
			}		
			cout<<"]\n";		
		}	
	
	}
	return 0;
}

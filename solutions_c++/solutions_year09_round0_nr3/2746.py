#include<iostream>
#include<cstdio>
#define N 550
void printarray(int *arr);
using namespace std;
int main()
{
int cases;
int case_counter=0;
FILE *fp;
int w_pos[N];
int e_pos[N];
int l_pos[N];
int c_pos[N];
int o_pos[N];
int m_pos[N];
int t_pos[N];
int d_pos[N];
int j_pos[N];
int a_pos[N];
int space_pos[N];
int COUNTER=0;

int w_count=0;
int e_count=0;
int l_count=0;
int c_count=0;
int o_count=0;
int m_count=0;
int t_count=0;
int d_count=0;
int j_count=0;
int a_count=0;
int space_count=0;
int position=0;
for(int i=0;i<N;i++)
{

w_pos[i]=0;
e_pos[i]=0;
l_pos[i]=0;
c_pos[i]=0;
o_pos[i]=0;
m_pos[i]=0;
t_pos[i]=0;
d_pos[i]=0;
j_pos[i]=0;
a_pos[i]=0;
space_pos[i]=0;
}
char filename[50];

cin>>filename;
fp=fopen(filename,"r+");
fscanf(fp,"%d\n",&cases);
char ch;
while(cases>0)
{case_counter++;
int w_count=0;
int e_count=0;
int l_count=0;
int c_count=0;
int o_count=0;
int m_count=0;
int t_count=0;
int d_count=0;
int j_count=0;
int a_count=0;
int space_count=0;
position=0;	
	FILE *buffer;
	buffer=fp;
	do
	{
	
	ch=getc(fp);
	//cout<<ch;
	if(ch=='w')
	{
	w_pos[w_count]=position;
	w_count++;
	}
	if(ch=='e')
	{
	e_pos[e_count]=position;
	e_count++;
	}
	
	if(ch=='l')
	{
	l_pos[l_count]=position;
	l_count++;
	}
	
	if(ch=='c')
	{
	c_pos[c_count]=position;
	c_count++;
	}
	
	if(ch=='o')
	{
	o_pos[o_count]=position;
	o_count++;
	}
	
	if(ch=='m')
	{
	m_pos[m_count]=position;
	m_count++;
	}
	
	if(ch=='t')
	{
	t_pos[t_count]=position;
	t_count++;
	}
	
	if(ch=='d')
	{
	d_pos[d_count]=position;
	d_count++;
	}
	
	if(ch=='j')
	{
	j_pos[j_count]=position;
	j_count++;
	}
	
	if(ch=='a')
	{
	a_pos[a_count]=position;
	a_count++;
	}
	
	if(ch==' ')
	{
	space_pos[space_count]=position;
	space_count++;
	}
	
	position++;
	}while(ch!='\n');
	
	/*printarray(w_pos);
	printarray(e_pos);
	printarray(l_pos);
	printarray(c_pos);
	printarray(o_pos);
	printarray(m_pos);
	
	printarray(space_pos);
	
	printarray(t_pos);
	printarray(d_pos);
	printarray(j_pos);
	printarray(a_pos);
	*/
	
	for(int j=0;j<w_count;j++)
	{
		
		for(int k=0;k<e_count;k++)
		{
			if(w_pos[j]<e_pos[k])
				{
					for(int b=0;b<l_count;b++)
					{
						if(e_pos[k]<l_pos[b])
						{
							for(int cc=0;cc<c_count;cc++)
							{
								if(l_pos[b]<c_pos[cc])
								{
									for(int oo=0;oo<o_count;oo++)
									{
										if(c_pos[cc]<o_pos[oo])
										{
											for(int mm=0;mm<m_count;mm++)
											{
												if(o_pos[oo]<m_pos[mm])
												{
													for(int ee=0;ee<e_count;ee++)
													{
														if(m_pos[mm]<e_pos[ee])
														{
															for(int sss=0;sss<space_count;sss++)
															{
																if(e_pos[ee]<space_pos[sss])
																{
																	for(int tt=0;tt<t_count;tt++)
																	{
																		if(space_pos[sss]<t_pos[tt])
																		{
																			for(int ooo=0;ooo<o_count;ooo++)
																			{
																				if(t_pos[tt]<o_pos[ooo])
																				{
																					for(int ssss=0;ssss<space_count;ssss++)
																					{
																						if(o_pos[ooo]<space_pos[ssss])
																						
																						{
																							for(int ccc=0;ccc<c_count;ccc++)
																							{
																							if(space_pos[ssss]<c_pos[ccc])
																							
																								{
																									for(int oooo=0;oooo<o_count;oooo++)
																									{
																										if(c_pos[ccc]<o_pos[oooo])
																										{
																											for(int dd=0;dd<d_count;dd++)
																											{
																												if(o_pos[oooo]<d_pos[dd])
																												{
																													for(int eee=0;eee<e_count;eee++)
																													{
																														if(d_pos[dd]<e_pos[eee])
																														{
																															for(int sssss=0;sssss<space_count;sssss++)
																															{
																																if(e_pos[eee]<space_pos[sssss])
																																{
																																	for(int jj=0;jj<j_count;jj++)
																																	{
																																		if(space_pos[sssss]<j_pos[jj])
																																		{
																																			for(int aaa=0;aaa<a_count;aaa++)
																																			{
																																				if(j_pos[jj]<a_pos[aaa])
																																				{
																																					for(int mmmm=0;mmmm<m_count;mmmm++)
																																					{
																																						if(a_pos[aaa]<m_pos[mmmm])
																																						{
																																						COUNTER++;
																																						if(COUNTER==10000)
																																						{
																																						COUNTER=0;
																																						}
																																						}
																																					}
																																				}
																																			}
																																		}
																																	}
																																}
																															}
																														}
																													}
																												}
																											}
																										}
																									}
																								
																								}
																							}
																						}
																					}
																				}
																			}
																		}
																	}
																}
															}
														}
													
													}
												}
												
											}
										
										}
									}
								
								}
							
							
							}
							
							
						}
						
					
					
					
					}
				
				
				
				}
		}
	}
	
	cout<<"Case #"<<case_counter<<": ";
	printf("%04d",COUNTER);
	cout<<endl;
	COUNTER=0;
	cases--;
	
	
	
	
}
return 0;
}

void printarray(int *arr)
{cout<<"Printing array\n";
for(int i=0;i<N && arr[i]!=0;i++)
{
cout<<arr[i]<<" ";
}
cout<<endl;
}


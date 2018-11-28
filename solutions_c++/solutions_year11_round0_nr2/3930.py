#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

int main( void )
{
	int test_cases, C,D,N,t, temp_calc,count=0;
	scanf("%d",&test_cases);
	cin.ignore();
	char common[6] = {'C','a','s','e',' ','#'};
	//char result[10];
	string result;
	char inp[2500];
	char inpC[3], inpD[2], inpN[10];
	int blocks = fread(inp, 1, 2500, stdin);
	//cout<<"blocks::::::"<<blocks<<endl;
	for(unsigned int i=0; i<blocks; i++)
	{
		++count;
		C=-1;
		D=-1;
		N=-1;
		result = "";
		//for C
		for(;;++i)
		{
			if(inp[i] == 32 )
			{
				C = t;
				t=0;
				break;
			}
			else
			{	t = t*10 +(inp[i] - '0');	}	
		}
		++i;
	//	cout<<"i after reading C"<<i<<"   c is:::"<<C<<endl;
		for(unsigned int j=0; j<C; ++j)
		{
			temp_calc = (j-1)*3;
			inpC[temp_calc] = inp[i++];
			inpC[temp_calc+1] = inp[i++];
			inpC[temp_calc+2] = inp[i++];
		}
		if(C!=0)
		{++i;}
		//for D
		for(;;++i)
		{
			if(inp[i] == 32 )
			{
				D = t;
				t=0;
				break;
			}
			else
			{	t = t*10 +(inp[i] - '0');	}	
		}
		++i;
	//	cout<<"i after reading D"<<i<<"   d is:::"<<D<<endl;
		for(unsigned int j=0; j<D; ++j)
		{
			temp_calc = (j-1)*2;
			inpD[temp_calc] = inp[i++];
			inpD[temp_calc+1] = inp[i++];
		}
		if(D!=0)
		{++i;}
		//for N
		for(;;++i)
		{
			if(inp[i] == 32 )
			{
				N = t;
				t=0;
				break;
			}
			else
			{	
	//			cout<<"in here"<<endl;
				t = t*10 +(inp[i] - '0');	}	
		}
		++i;
	//	cout<<"i after reading N"<<i<<"   N is:::"<<N<<endl;
		for(unsigned int j=0; j<N; ++j)
		{
			inpN[j] = inp[i++];
		}

		//cout<<C<<"   "<<N<<"    "<<D<<"  i is::"<<i<<endl;
		int xx = 0;
		char q, transfer;
		bool check, check2;
	
	
		for(unsigned int k=1; k<N; ++k)
		{
			check = true;
			q = inpN[k];
		//	cout<<"from start	inpN[k]:::: "<<inpN[k]<<"        inpN[k+1]::  "<<inpN[k-1]<<endl;
			//combination
			for(unsigned int j=0; j<C; ++j)
			{
				temp_calc = (j-1)*3;
				if( inpC[temp_calc] == q )
				{
					if(inpC[temp_calc+1] == inpN[k-1])
					{
	//					cout<<"combining:::"<<inpC[temp_calc+2]<<endl;
						for(int z=k-2; z>=xx; --z)
						{inpN[z+1] = inpN[z];}
						inpN[k] = inpC[temp_calc+2];
						++xx;
	/*
		printf("%d: [", count);
		for(unsigned int dd=xx; dd<N; ++dd)
		{
			if(dd!=N-1)
			{printf("%c, ", inpN[dd]);}
			else
			{printf("%c", inpN[dd]);}
		}
		printf("]\n");
						
	*/
	
//						cout<<"xx is  "<<xx<<endl;
						check = false;
					}
				}
				else if( inpC[temp_calc+1] == q )
				{
					if(inpC[temp_calc] == inpN[k-1])
					{
					//	cout<<"combininghhhh:::"<<inpC[temp_calc+2]<<endl;
				//		cout<<" K is :  "<<k<<xx<<endl;
						for(int z=k-2; z>=xx; --z)
						{inpN[z+1] = inpN[z];}
						inpN[k] = inpC[temp_calc+2];
						++xx;
						
			/*			
		printf("%d: [", count);
		for(unsigned int dd=xx; dd<N; ++dd)
		{
			if(dd!=N-1)
			{printf("%c, ", inpN[dd]);}
			else
			{printf("%c", inpN[dd]);}
		}
		printf("]\n");
						
						
			*///			cout<<"xx is  "<<xx;
		//				check = false;
					}
				}
			}
			
			//clearing
			if(check)
			{
				check2 =false;
			//	cout<<"entering clearing and now on:::  "<<inpN[k]<<"   K is::::  "<<k<<endl;
				q = inpN[k];
				for(unsigned int j=0; j<D; ++j)
				{
					int z;
					temp_calc = (j-1)*2;
					if( inpD[temp_calc] == q )
					{
						//for(z=k-1; z>=xx; --z)
						for(z=xx; z<k; ++z)
						{
							if(inpN[z] == inpD[temp_calc+1])
							{
		//						cout<<"in here proudly"<<endl;
								xx = k+1;
								++k;
								//check2 = true;
								break;
							}
						}
						/*if(check2)
						{
			//				cout<<"found at"<<z<<""<<endl;
							if(z!=0)
							{
		//					cout<<endl<<"checking shifting "<<endl;
						//	cout<<"z is  "<<z<<"  k is   "<<k<<endl;
								for(int w=z-1,g=k; w>=xx; --w,--g )
								{
									inpN[g] = inpN[w];
					
					//				cout<<"w is  "<<w<<"  g is   "<<g<<endl;
								}
				//				cout<<"here"<<endl;
								xx = xx + k - z + 1;
			//					cout<<"XXX"<<xx<<endl;
							}
							else
							{
								xx = k+1;
								++k;
		//						cout<<"xx is hh::"<<xx<<"  K is   "<<k<<endl;
							}
							
							
							
	/*						
							
							
								
		printf("%d: [", count);
		for(unsigned int dd=xx; dd<N; ++dd)
		{
			if(dd!=N-1)
			{printf("%c, ", inpN[dd]);}
			else
			{printf("%c", inpN[dd]);}
		}
		printf("]\n");
						

							
							
							
							
							
							
							//++k;
						}*/
					}
					else if( inpD[temp_calc+1] == q )
					{
						//for(z=k-1; z>=xx; --z)
						for(z=xx; z<k; ++z)
						{
							if(inpN[z] == inpD[temp_calc])
							{
								xx = k+1;
								++k;
								//check2 = true;
								break;
							}
						}/*
						if(check2)
						{
							if(z!=0)
							{
								for( int w=z-1,g=k; w>=xx; --w,--g )
								{	inpN[g] = inpN[w];	}
								xx = xx + k - z + 1;
						//		cout<<"xx is ::"<<xx<<endl;
							}
							else
							{	
								xx = k+1;	
								++k;
					//		cout<<"xx is ::"<<xx<<endl;
							}
							
							
							
							
				/*			
								
		printf("%d: [", count);
		for(unsigned int dd=xx; dd<N; ++dd)
		{
			if(dd!=N-1)
			{printf("%c, ", inpN[dd]);}
			else
			{printf("%c", inpN[dd]);}
		}
		printf("]\n");
						

							
							
							
							
							
							
							
							//++k;
						}*/
					}	
				}
			}
		}
		fwrite(common,1 ,6, stdout);
		printf("%d: [", count);
		for(unsigned int dd=xx; dd<N; ++dd)
		{
			if(dd!=N-1)
			{printf("%c, ", inpN[dd]);}
			else
			{printf("%c", inpN[dd]);}
		}
		printf("]\n");
	}
	return 0;
}

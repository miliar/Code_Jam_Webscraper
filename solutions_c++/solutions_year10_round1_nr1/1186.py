#include <iostream>
#include <fstream>
#include <string>

using namespace std;


string filename = "A-small-attempt0.in";
string outname = "A-small-attempt0.out";

int main()
{
	ifstream input;
	input.open(filename.c_str());
	
	ofstream output;
	output.open(outname.c_str());
	
	int T,K,N;
	
	input>>T;
	
	for(int t=1; t<=T; t++)
	{
		input>>N>>K;
		//cou<<N<<" "<<K<<endl;
		char** mat = new char* [N];
		
		for(int n=0; n<N; n++)
		{
			mat[n] = new char[N];
			for(int j=0; j<N;j++)
			{
				input>>mat[n][j];
			}
		}
		
	/*	for(int n=0; n<N; n++)
		{
			
			for(int j=0; j<N;j++)
			{
				cou<<mat[n][j]<<" ";
			}
			cou<<endl;
		}*/
		
		
		
		int increment = 0;
		for(int n=N-1; n>=0; n--)
		{
			 increment = 0;
			for(int j=N-1; j>=0; j--)
			{
				if(mat[n][j] == '.')
					{
						increment++;
					}
				else if(increment != 0)
				{
					mat[n][j+increment] = mat[n][j];
					
					mat[n][j] = '.';
				}
				
			}
			
			if(increment == N)
			{
				goto AAA;
			}
			
		}
		
		
		
		
		AAA:
	/*	for(int n=0; n<N; n++)
		{
			
			for(int j=0; j<N;j++)
			{
				cou<<mat[n][j]<<" ";
			}
			cou<<endl;
		}*/
		bool isred = false; 
		bool isblue = false;
		
		int r_count=0;
		int b_count=0;
		
		for(int n= N-1; n>=0; n--)
			{
				for(int j=N-1; j>=0; j--)
				{
					if(mat[n][j] == 'R')
					{
						r_count++;
						b_count =0;
						if(r_count == K)
							{
								isred = true;
								if(isblue)
									goto BBB;
							}
					}
					else if(mat[n][j]=='B')
					{
						b_count++;
						r_count =0;
						if(b_count == K)
							{
								isblue = true;
								if(isred)
									goto BBB;
							}
					}
					else
						break;
				}	
				b_count =0;
				r_count =0;
			}
			
			for(int j=N-1; j>=0; j--)
			{
				for(int n=N-1; n>=0; n--)
				{
					if(mat[n][j] == 'R')
					{
						r_count++;
						b_count =0;
						if(r_count == K)
							{
								isred = true;
								if(isblue)
									goto BBB;
							}
					}
					else if(mat[n][j]=='B')
					{
						b_count++;
						r_count =0;
						if(b_count == K)
							{
								isblue = true;
								if(isred)
									goto BBB;
							}
					}
					else
					{
						break;
					}
				}
				b_count =0;
				r_count =0;
			}
			
					
		
			/*	for(int n=0; n<N; n++)
		{
			
			for(int j=0; j<N;j++)
			{
				cou<<mat[n][j]<<" ";
			}
			cou<<endl;
		}*/
		
					for(int n=N-1; n>=0; n--)
					{
						int a= n; 
						int b=N-1;
						while(a>=0 && b>=0)
						{
								if(mat[a][b] == 'R')
								{
									r_count++;
									b_count =0;
									if(r_count == K)
										{
											isred = true;
											if(isblue)
												goto BBB;
										}
								}
								else if(mat[a][b]=='B')
								{
									b_count++;
									r_count =0;
									if(b_count == K)
										{
											isblue = true;
											if(isred)
												goto BBB;
										}
								}
								else
								{
									break;
								}
								
								a--;
								b--;
							
							
						}
						b_count =0;
						r_count =0;
											
						
					}
					
		// cou<<isred<<" "<<isblue<<endl;

		
					for(int j=N-1; j>=0; j--)
					{
						int a= N-1; 
						int b=j;
						while(a>=0 && b>=0)
						{
								if(mat[a][b] == 'R')
								{
									r_count++;
									b_count =0;
									if(r_count == K)
										{
											isred = true;
											if(isblue)
												goto BBB;
										}
								}
								else if(mat[a][b]=='B')
								{
									b_count++;
									r_count =0;
									if(b_count == K)
										{
											isblue = true;
											if(isred)
												goto BBB;
										}
								}
								else
								{
									break;
								}
								
								a--;
								b--;
							
							
						}
						b_count =0;
						r_count =0;
											
						
					}
					
		// cou<<isred<<" "<<isblue<<endl;

					
					
					for(int j=0; j<N; j++)
					{
						int a= N-1; 
						int b=j;
						while(a>=0 && b<N)
						{
								if(mat[a][b] == 'R')
								{
									r_count++;
									b_count =0;
									if(r_count == K)
										{
											isred = true;
											if(isblue)
												goto BBB;
										}
								}
								else if(mat[a][b]=='B')
								{
									b_count++;
									r_count =0;
									if(b_count == K)
										{
											isblue = true;
											if(isred)
												goto BBB;
										}
								}
								else
								{
									break;
								}
								
								a--;
								b++;
							
							
						}
						b_count =0;
						r_count =0;					
						
					}
					
		// cou<<isred<<" "<<isblue<<endl;

						for(int n=0; n<N; n++)
						{
							int a= n; 
							int b=N-1;
							while(a<N && b>=0)
							{
									if(mat[a][b] == 'R')
									{
										r_count++;
										b_count =0;
										if(r_count == K)
											{
												isred = true;
												if(isblue)
													goto BBB;
											}
									}
									else if(mat[a][b]=='B')
									{
										b_count++;
										r_count =0;
										if(b_count == K)
											{
												isblue = true;
												if(isred)
													goto BBB;
											}
									}
									else
									{
										break;
									}

									a++;
									b--;


							}
							b_count =0;
							r_count =0;

						}
						
//		cou<<isred<<" "<<isblue<<endl;

		
			if(!isred && !isblue)
			output<<"Case #"<<t<<": Neither"<<endl;
			else if(isred && !isblue)
			output<<"Case #"<<t<<": Red"<<endl;
			else if(!isred && isblue)
			output<<"Case #"<<t<<": Blue"<<endl;
			else
			{
				BBB:
					output<<"Case #"<<t<<": Both"<<endl;
			}
		
			
		for(int n=0; n<N; n++)
		{
			delete [] mat[n];
		}
		delete [] mat;
		
			
			
		
		
		
	}
	
	
	
	return 0;
}
#include<iostream>
#include<string>
#include<string.h>
#include<fstream>
using namespace std;
	

int gmin(double It,double N,double W,double E,double S)
{
	if((It<=N)&&(It<=W)&&(It<=E)&&(It<=S))
	{
		return 0;
	}
	else {
		if((N<=W)&&(N<=E)&&(N<=S))
			return 1;
		else if((W<=E)&&(W<=S))
			return 2;
		else if (E<=S)
			return 3;
		else
			return 4;

	}
	
}

int main(void)
{
	char* pch;
	int ** map;

	char ** OO;

	int N,H,W;
	const char*aa;

	string str;
	fstream text2;
	text2.open("ABCD");

	getline(text2,str);
	N = atoi(str.c_str());

	int i;
	for(i =0;i<N;i++)
	{
		getline(text2,str);
		sscanf(str.c_str(),"%d%d%d",&H,&W);
		
		int k;
		map = new int*[H];
		for(k=0;k<H;k++)
			map[k]=new int[W];

		OO = new char*[H];
		for(k=0;k<H;k++)
			OO[k]=new char[W];

		for(k=0;k<H;k++)
		{
			int a=0;
			getline(text2,str);
			pch = strtok((char*)str.c_str()," ");

			while(pch!=NULL)
				{
					map[k][a] = atoi( pch);
					a++;
					pch=strtok(NULL," ");
				}	
		}		

		int l;int f;
		


		for(k=0;k<H;k++)
			for(l=0;l<W;l++)
				OO[k][l]=k*W+l;
		
	
		for(k=0;k<H;k++)
			for(l=0;l<W;l++){
			f = gmin(map[k][l],k>0?map[k-1][l]:100000,l>0?map[k][l-1]:100000,l<W-1?map[k][l+1]:100000,k<H-1?map[k+1][l]:100000);
			
				if(f==1){
					int mina=OO[k][l]<OO[k - 1][l]?OO[k][l]:OO[k - 1][l];
					
							for(int k2=0;k2<H;k2++)
								for(int l2=0;l2<W;l2++)
									if((OO[k2][l2]==OO[k][l])||(OO[k2][l2]==OO[k - 1][l]))
										OO[k2][l2]=mina;
					}
				else if(f==2){
					int mina=OO[k][l]<OO[k][l - 1]?OO[k][l]:OO[k][l - 1];
	   						for(int k2=0;k2<H;k2++)
								for(int l2=0;l2<W;l2++)
									if((OO[k2][l2]==OO[k][l])||(OO[k2][l2]==OO[k][l-1]))
										OO[k2][l2]=mina;
}
				else if(f==3){
					int mina=OO[k][l]<OO[k][l +1]?OO[k][l]:OO[k][l+1];
							for(int k2=0;k2<H;k2++)
								for(int l2=0;l2<W;l2++)
									if((OO[k2][l2]==OO[k][l])||(OO[k2][l2]==OO[k][l+1]))
										OO[k2][l2]=mina;
					}
				else if(f==4){
					int mina=OO[k][l]<OO[k+1][l]?OO[k][l]:OO[k+1][l]; 
							for(int k2=0;k2<H;k2++)
								for(int l2=0;l2<W;l2++)
									if((OO[k2][l2]==OO[k][l])||(OO[k2][l2]==OO[k + 1][l]))
										OO[k2][l2]=mina;}
				}

	
		for(k=H-1;k>0;k--)
			for(l=W-1;l>0;l--){
			f = gmin(map[k][l],k>0?map[k-1][l]:100000,l>0?map[k][l-1]:100000,l<W-1?map[k][l+1]:100000,k<H-1?map[k+1][l]:100000);
			
				if(f==1){
					int mina=OO[k][l]<OO[k - 1][l]?OO[k][l]:OO[k - 1][l];
					
							for(int k2=0;k2<H;k2++)
								for(int l2=0;l2<W;l2++)
									if((OO[k2][l2]==OO[k][l])||(OO[k2][l2]==OO[k - 1][l]))
										OO[k2][l2]=mina;
					}
				else if(f==2){
					int mina=OO[k][l]<OO[k][l - 1]?OO[k][l]:OO[k][l - 1];
	   						for(int k2=0;k2<H;k2++)
								for(int l2=0;l2<W;l2++)
									if((OO[k2][l2]==OO[k][l])||(OO[k2][l2]==OO[k][l-1]))
										OO[k2][l2]=mina;
}
				else if(f==3){
					int mina=OO[k][l]<OO[k][l +1]?OO[k][l]:OO[k][l+1];
							for(int k2=0;k2<H;k2++)
								for(int l2=0;l2<W;l2++)
									if((OO[k2][l2]==OO[k][l])||(OO[k2][l2]==OO[k][l+1]))
										OO[k2][l2]=mina;
					}
				else if(f==4){
					int mina=OO[k][l]<OO[k+1][l]?OO[k][l]:OO[k+1][l]; 
							for(int k2=0;k2<H;k2++)
								for(int l2=0;l2<W;l2++)
									if((OO[k2][l2]==OO[k][l])||(OO[k2][l2]==OO[k + 1][l]))
										OO[k2][l2]=mina;}
				}


		for(k=0;k<H;k++)
			for(l=0;l<W;l++){
			f = gmin(map[k][l],k>0?map[k-1][l]:100000,l>0?map[k][l-1]:100000,l<W-1?map[k][l+1]:100000,k<H-1?map[k+1][l]:100000);
			
				if(f==1){
					int mina=OO[k][l]<OO[k - 1][l]?OO[k][l]:OO[k - 1][l];
					
							for(int k2=0;k2<H;k2++)
								for(int l2=0;l2<W;l2++)
									if((OO[k2][l2]==OO[k][l])||(OO[k2][l2]==OO[k - 1][l]))
										OO[k2][l2]=mina;
					}
				else if(f==2){
					int mina=OO[k][l]<OO[k][l - 1]?OO[k][l]:OO[k][l - 1];
	   						for(int k2=0;k2<H;k2++)
								for(int l2=0;l2<W;l2++)
									if((OO[k2][l2]==OO[k][l])||(OO[k2][l2]==OO[k][l-1]))
										OO[k2][l2]=mina;
}
				else if(f==3){
					int mina=OO[k][l]<OO[k][l +1]?OO[k][l]:OO[k][l+1];
							for(int k2=0;k2<H;k2++)
								for(int l2=0;l2<W;l2++)
									if((OO[k2][l2]==OO[k][l])||(OO[k2][l2]==OO[k][l+1]))
										OO[k2][l2]=mina;
					}
				else if(f==4){
					int mina=OO[k][l]<OO[k+1][l]?OO[k][l]:OO[k+1][l]; 
							for(int k2=0;k2<H;k2++)
								for(int l2=0;l2<W;l2++)
									if((OO[k2][l2]==OO[k][l])||(OO[k2][l2]==OO[k + 1][l]))
										OO[k2][l2]=mina;}
				}

	
		for(k=H-1;k>0;k--)
			for(l=W-1;l>0;l--){
			f = gmin(map[k][l],k>0?map[k-1][l]:100000,l>0?map[k][l-1]:100000,l<W-1?map[k][l+1]:100000,k<H-1?map[k+1][l]:100000);
			
				if(f==1){
					int mina=OO[k][l]<OO[k - 1][l]?OO[k][l]:OO[k - 1][l];
					
							for(int k2=0;k2<H;k2++)
								for(int l2=0;l2<W;l2++)
									if((OO[k2][l2]==OO[k][l])||(OO[k2][l2]==OO[k - 1][l]))
										OO[k2][l2]=mina;
					}
				else if(f==2){
					int mina=OO[k][l]<OO[k][l - 1]?OO[k][l]:OO[k][l - 1];
	   						for(int k2=0;k2<H;k2++)
								for(int l2=0;l2<W;l2++)
									if((OO[k2][l2]==OO[k][l])||(OO[k2][l2]==OO[k][l-1]))
										OO[k2][l2]=mina;
}
				else if(f==3){
					int mina=OO[k][l]<OO[k][l +1]?OO[k][l]:OO[k][l+1];
							for(int k2=0;k2<H;k2++)
								for(int l2=0;l2<W;l2++)
									if((OO[k2][l2]==OO[k][l])||(OO[k2][l2]==OO[k][l+1]))
										OO[k2][l2]=mina;
					}
				else if(f==4){
					int mina=OO[k][l]<OO[k+1][l]?OO[k][l]:OO[k+1][l]; 
							for(int k2=0;k2<H;k2++)
								for(int l2=0;l2<W;l2++)
									if((OO[k2][l2]==OO[k][l])||(OO[k2][l2]==OO[k + 1][l]))
										OO[k2][l2]=mina;}
				}

	
		int ind = 0;int cc;
		for(k=0;k<H;k++)
			for(l=0;l<W;l++)
					if(OO[k][l]>ind){
						ind++;
						cc = OO[k][l];		
						if(OO[k][l]>ind)
							for(int k2=0;k2<H;k2++)
								for(int l2=0;l2<W;l2++)
									if(cc==OO[k2][l2])
										OO[k2][l2]=ind;
					

					}

	//	if(OO[H-1][W-1]>ind)
	//		OO[H-1][W-1]=ind++;
		cout<<"Case #"<<i+1<<":"<<endl;
		for(k=0;k<H;k++){
			for(l=0;l<W-1;l++)
				cout<<(char)(97+OO[k][l])<<" ";

			cout<<(char)(97+OO[k][W-1]);

			cout<<endl;
		}

		for(k=0;k<H;k++)
			delete [] OO[k];
		delete [] OO;

		for(k=0;k<H;k++)
			delete [] map[k];
		delete [] map;

		
					
	}
	
}


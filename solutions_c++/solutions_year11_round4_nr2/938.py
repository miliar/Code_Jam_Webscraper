#include<iostream>
#include<fstream>
#include<cstdio>
#include<map>

using namespace std;

#define REP(i,a,b) for(int i=a;i<b;++i)
#define RESET(v,t,s) memset(v,0,s*sizeof(t))

int main()
{
	ifstream fin("B-small-attempt1.in");
	FILE* fp=fopen("B.o","w+");
	
	char input;
	int T,R,C,D;
	int w[600][600];
	long long size,tr,tc,ans,total;
	bool found;
	
	fin>>T;
	REP(i,0,T)
	{
cout<<"case start "<<i+1<<"\n";

		fin>>R>>C>>D;
		
cout<<R<<" "<<C<<" "<<D<<endl;;		

		REP(j,0,R)
		{
			REP(k,0,C)
			{
				fin>>input;
				w[j][k]=input-'0';
				
			}
		}
		size=(R<C)?R:C;
		
cout<<size<<endl;

		found=0;
		for(;size>=3;--size)
		{
cout<<size<<endl;
			
			for(int j=0;j+size<=R;++j)
			{
				
				for(int k=0;k+size<=C;++k)
				{
					total=0;
					if(k==0)
					{
						tr=tc=0;
						REP(p,0,size)
						{
							REP(q,0,size)
							{
								cout<<w[j+p][k+q];
								
								tr+=w[j+p][k+q]*(j+p); tc+=w[j+p][k+q]*(k+q);
								total+=w[j+p][k+q];
							}
							cout<<endl;
						}
						tr-=w[j+0][k+0]*(j+0); tc-=w[j+0][k+0]*(k+0); total-=w[j+0][k+0];
						tr-=w[j+size-1][k+0]*(j+size-1); tc-=w[j+size-1][k+0]*(k+0); total-=w[j+size-1][k+0];
						tr-=w[j+0][k+size-1]*(j+0); tc-=w[j+0][k+size-1]*(k+size-1); total-=w[j+0][k+size-1];
						tr-=w[j+size-1][k+size-1]*(j+size-1); tc-=w[j+size-1][k+size-1]*(k+size-1); total-=w[j+size-1][k+size-1];
					}
					else
					{
						/*
						tr-=w[j+0][k+0]*(j+0); tc-=w[j+0][k+0]*(k+0);
						tr-=w[j+size-1][k+0]*(j+size-1); tc-=w[j+size-1][k+0]*(k+0);
						
						tr+=w[j+0][k+size-2]*(j+0); tc+=w[j+0][k+size-2]*(k+size-2);
						tr+=w[j+size-2][k+size-2]*(j+size-2); tc+=w[j+size-2][k+size-2]*(k+size-2);
						
						REP(p,1,size-1)
						{
							tr-=w[j+p][k-1]*(j+p); tc-=w[j+p][k-1]*(k-1);
							tr+=w[j+p][k+size-1]*(j+p); tc+=w[j+p][k+size-1]*(k+size-1);
						}*/
						tr=tc=0;
						REP(p,0,size)
						{
							REP(q,0,size)
							{
								cout<<w[j+p][k+q];
								
								tr+=w[j+p][k+q]*(j+p); tc+=w[j+p][k+q]*(k+q);
								total+=w[j+p][k+q];
							}
							cout<<endl;
						}
						tr-=w[j+0][k+0]*(j+0); tc-=w[j+0][k+0]*(k+0); total-=w[j+0][k+0];
						tr-=w[j+size-1][k+0]*(j+size-1); tc-=w[j+size-1][k+0]*(k+0); total-=w[j+size-1][k+0];
						tr-=w[j+0][k+size-1]*(j+0); tc-=w[j+0][k+size-1]*(k+size-1); total-=w[j+0][k+size-1];
						tr-=w[j+size-1][k+size-1]*(j+size-1); tc-=w[j+size-1][k+size-1]*(k+size-1); total-=w[j+size-1][k+size-1];
					}
					
cout<<size<<" "<<j<<" "<<k<<" "<<2*tr<<" "<<total*(j+size-1)<<" "<<2*tc<<" "<<total*(k+size-1)<<" "<<total<<endl;
					
					if( 2*tr-j*total==total*(j+size-1) && 2*tc-k*total==total*(k+size-1) )
					{
						found=1;
						ans=size;
						break;
					}
				}
				
				if(found)break;
			}
			
			if(found)break;
		}
		
		if(found)
		{
			printf("Case #%d: %d\n",i+1,ans);
			fprintf(fp,"Case #%d: %d\n",i+1,ans);
		}
		else
		{
			printf("Case #%d: IMPOSSIBLE\n",i+1);
			fprintf(fp,"Case #%d: IMPOSSIBLE\n",i+1);
		}
	}
	
	fclose(fp);
	return 0;
}

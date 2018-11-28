#include<iostream>
#include<fstream>
#include<cstdio>
#include<map>

using namespace std;

#define REP(i,a,b) for(int i=a;i<b;++i)
#define RESET(v,t,s) memset(v,0,s*sizeof(t))

int main()
{
	ifstream fin("A-large.in");
	FILE* fp=fopen("A.o","w+");
	
	int T;
	double X,S,R,t,N;
	double B[1050],E[1050],w[1050];
	
	double walk,ans;
	
	multimap<double,double> Q;
	multimap<double,double>::iterator ite;
	
	fin>>T;
	REP(i,0,T)
	{
		Q.clear();
		
		fin>>X>>S>>R>>t>>N;
		
		walk=0;
		REP(j,0,N)
		{
			fin>>B[j]>>E[j]>>w[j];
			
			if(j==0)
				walk+=B[j];
			else
				walk+=B[j]-E[j-1];
				
			Q.insert(make_pair( w[j],E[j]-B[j] ));
			
			if(j==N-1)
				walk+=X-E[j];
		}
		Q.insert(make_pair(0,walk));
		
		ans=0;
		ite=Q.begin();
		while(t>0 && ite!=Q.end())
		{
cout<<t<<"\\"<<ite->second/R<<"\\"<<ans<<endl;
			
			if(t>ite->second/(R+ite->first))
			{
				t-=ite->second/(R+ite->first);
				ans+=ite->second/(R+ite->first);
			}
			else
			{
				ans+=t+(ite->second-t*(R+ite->first))/(S+ite->first);
				t=0;
			}
			

cout<<ite->first<<" "<<ite->second<<" "<<ans<<endl;
			
			++ite;
		}
		
cout<<"R\n";
		
		while(ite!=Q.end())
		{
			ans+=ite->second/(S+ite->first);
			
cout<<ite->first<<" "<<ite->second<<" "<<ans<<endl;
			
			++ite;
		}

		printf("Case #%d: %.8f\n",i+1,ans);
		fprintf(fp,"Case #%d: %.8f\n",i+1,ans);
	}
	
	fclose(fp);
	return 0;
}

#include<iostream>
#include<fstream>
#include<cstdio>
#include<cstring>
#include<string>
#include<vector>

using namespace std;

int comb[30][30];
int opp[30][30];
int conv[300];
char rev[300];

void pre()
{
     for(int i='A';i<='Z';++i)
     {
             conv[i]=i-'A'+1;
             rev[i-'A'+ 1]= (char)i;
     }
}

main()
{
    pre();
	ifstream fin;ofstream fout;
	fin.open("C:\\Data\\B-large.in");
//    fin.open("C:\\Data\\A-large.in");
	fout.open("C:\\Data\\B-large.out");
//	fout.open("C:\\Data\\A-large.out");
	
	int tests;
	
	fin>>tests;
	
	for(int cas=1;cas<=tests;++cas)
	{
      memset(comb,0,sizeof(comb));
      memset(opp,0,sizeof(opp));
      
      int C,D,N;
      fin>>C;
      for(int i=0;i<C;++i)
      {
       char a,b,c;
       fin>>a>>b>>c;
       comb[conv[a]][conv[b]]=conv[c];    
       comb[conv[b]][conv[a]]=conv[c];
      }
      fin>>D;
      for(int i=0;i<D;++i)
      {
       char a,b;
       fin>>a>>b;
       opp[conv[a]][conv[b]]=1;    
       opp[conv[b]][conv[a]]=1;
      }
      fin>>N;      
      int ret[300],cnt=0;
      for(int i=0;i<N;++i)
      {
       char a;
       fin>>a;
       int temp=conv[a];
       if(cnt==0){ret[cnt++]=temp;continue;}
       if(comb[ret[cnt-1]][temp]!=0) { ret[cnt-1]=comb[ret[cnt-1]][temp]; continue;}
       int op=0;
       for(int i=0;i<cnt;++i) if(opp[ret[i]][temp]) { cnt=0;op=1;break; }
       if(op)continue;
       ret[cnt++]=temp;
      }
     fout<<"Case #"<<cas<<": [";
     for(int i=0;i<cnt;++i)
     {
      if(i)fout<<", ";
      fout<<rev[ret[i]];
     }
     fout<<"]"<<endl;
    }
 
	fin.close();
	fout.close();
	cin>>tests;
}

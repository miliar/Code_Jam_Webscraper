#include<iostream>
#include<fstream>
#include<cstdio>
#include<cstring>
#include<string>
#include<vector>

using namespace std;

int a[60][60];
int conv[512];
char rconv[5];
main()
{
    conv['.']=0;rconv[0]='.';
    conv['#']=1;rconv[1]='#';
    conv['/']=2;rconv[2]='/';
    conv['\\']=3;rconv[3]='\\';
	ifstream fin;ofstream fout;
//	fin.open("D:\\A-small-attempt0.in");
    fin.open("D:\\A-large.in");
//	fout.open("D:\\A-small.out");
	fout.open("D:\\A-large.out");
	
	int tests;
	
	fin>>tests;
	
	for(int cas=1;cas<=tests;++cas)
	{
            memset(a,0,sizeof(a));
     int poss=1,r,c;
     fin>>r>>c;    
     int total=0;
     for(int i=0;i<r;++i)
             for(int j=0;j<c;++j)
             {
              char ab;
              fin>>ab;
              a[i][j]=conv[ab];
              total+=a[i][j];
             }
     if(total%4==0)
     {
         for(int i=0;i<r && poss==1;++i)
                 for(int j=0;j<c && poss==1;++j)
                 {
                  if(a[i][j]!=1)continue;
                  if(j>=c-1){ poss=0; continue;}
                  if(i>=r-1){poss=0;continue;}
                  if(a[i][j+1]!=1 || a[i+1][j]!=1 || a[i+1][j+1]!=1){poss=0;continue;}
                  a[i][j]=a[i+1][j+1]=2;
                  a[i+1][j]=a[i][j+1]=3;
                 }
     }
     else poss=0;
     
     fout<<"Case #"<<cas<<":"<<endl;
     if(poss==0)fout<<"Impossible"<<endl;
     else
     {
      for(int i=0;i<r;++i)
      {
      for(int j=0;j<c;++j)
      {
              fout<<rconv[a[i][j]];
      }
      fout<<endl;
      }    
     }
    }
 
	fin.close();
	fout.close();
	cin>>tests;
}

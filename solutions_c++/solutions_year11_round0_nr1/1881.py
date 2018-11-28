#include<iostream>
#include<fstream>
#include<cstdio>
#include<cstring>
#include<string>
#include<vector>

using namespace std;

main()
{
	ifstream fin;ofstream fout;
//	fin.open("C:\\Data\\A-small-attempt0.in");
    fin.open("C:\\Data\\A-large.in");
//	fout.open("C:\\Data\\A-small.out");
	fout.open("C:\\Data\\A-large.out");
	
	int tests;
	
	fin>>tests;
	
	for(int cas=1;cas<=tests;++cas)
	{
     int ret=0,N;
     vector<int> O,B,retO,retB,inp;
     fin>>N;
     char bot;
     int button;
     for(int i=0;i<N;++i)
     {
      fin>>bot>>button; 
      if(bot=='O')
      {
       O.push_back(button);
       inp.push_back(0);
      }
      else
      {
       B.push_back(button);
       inp.push_back(1);
      }
     }
     
     int cur=1;
//     retO.push_back(0);
//cout<<"retO ";
     for(int i=0;i<O.size();++i)
     {
      int temp=O[i]-cur;
      if(temp<0)temp=-temp;
      retO.push_back(temp+1);
//cout<<temp+1<<" ";
      cur=O[i];
     }
//cout<<endl;
//cout<<"retB ";
     cur=1;
//     retB.push_back(0);
     for(int i=0;i<B.size();++i)
     {
      int temp=B[i]-cur;
      if(temp<0)temp=-temp;
      retB.push_back(temp+1);
//cout<<temp+1<<" ";      
      cur=B[i];
     }     
//cout<<endl;     
     int o=0,b=0,other=0,c=0;
     cur=1;
     for(int i=0;i<inp.size();++i)
     {
       if(inp[i]==0)
       {
         if(c==0)
         {
          ret+=retO[o];
          other+=retO[o];
//cout<<"inp 0 c 0 ret "<<ret<<" other "<<other<<endl;
         }
         else
         {
          int add=retO[o]-1;
          if(other>=add){add=1;}
          else {add-=other-1;}
          ret+=add;
//cout<<"inp 0 c 1 ret "<<ret<<" other "<<other<<" add "<<add<<endl;                    
          other=add;    
         }
         o++;
         c=0;
       }
       else
       {
        if(c==1)
        {
         ret+=retB[b];
         other+=retB[b];
//cout<<"inp 1 c 1 ret "<<ret<<" other "<<other<<endl;                   
         }
         else
         {
          int add=retB[b]-1;
          if(other>=add){add=1;}
          else {add-=other-1;}
          ret+=add;
//cout<<"inp 1 c 0 ret "<<ret<<" other "<<other<<" add "<<add<<endl;                    
          other=add;    
         }         
         b++;
         c=1;
       }
     }
     fout<<"Case #"<<cas<<": "<<ret<<endl;
    }
 
	fin.close();
	fout.close();
	cin>>tests;
}

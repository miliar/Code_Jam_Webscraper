#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
typedef struct int2
{ int start;int end;
} int2;
bool comp(int2& a,int2&b)
{ return (a.start<b.start);
}
using namespace std;
int main(int argc,char* argv[])
{
	ifstream ifs(argv[1]);
	ofstream ofs(strcat(argv[1],".out"));
	int N;
	ifs>>N;
	int i,j;
	for(i=0;i<N;i++)
	{int T;
		int NA,NB;
	  ifs>>T>>NA>>NB;
	  vector<int2> va;
	  vector<int2> vb;
	  

      for(j=0;j<NA;j++)
	  {int a,b; char c;
	  ifs>>a>>c>>b; int2 tmp;
	  tmp.start=60*a+b;
	  printf("%d ",60*a+b);
	  ifs>>a>>c>>b;
	  tmp.end=60*a+b+T;
	  printf("%d \n",60*a+b+T);
	  va.push_back(tmp);
	  }

	  for(j=0;j<NB;j++)
	   {int a,b; char c;
	  ifs>>a>>c>>b; int2 tmp;
	  tmp.start=60*a+b;
	  printf("%d ",60*a+b);
	  ifs>>a>>c>>b;
	  tmp.end=60*a+b+T;
	  printf("%d \n",60*a+b+T);
	  vb.push_back(tmp);
	  }
	  int na_color=0;
	  int nb_color=0;
	  int a_pivot=0;
	  int b_pivot=0;
	 
	  sort(va.begin(),va.end(),comp);
	  sort(vb.begin(),vb.end(),comp);
	  vector <int> train;
	  vector <int> atA;
	  while(a_pivot+b_pivot!=NA+NB){
	  if(b_pivot==NB||((a_pivot!=NA)&&(va[a_pivot].start<vb[b_pivot].start))) 
	  {
	  for (j=0;j<train.size();j++)
		  if((atA[j]==1)&&(train[j]<=va[a_pivot].start))
		  { train[j]=va[a_pivot].end;atA[j]=0;break;}
		  if(j==train.size()) {na_color++;train.push_back(va[a_pivot].end);atA.push_back(0);}
	    a_pivot++;
	  }
	  else
	  {
		for (j=0;j<train.size();j++)
			if((atA[j]==0)&&train[j]<=vb[b_pivot].start)
		  { train[j]=vb[b_pivot].end;atA[j]=1;break;}
		  if(j==train.size()) {nb_color++;train.push_back(vb[b_pivot].end);atA.push_back(1);}
	    b_pivot++;
	  }
	  }
	  ofs<<"Case #"<<i+1<<": "<<na_color<<" "<<nb_color<<endl;




	}
	ifs.close();
	ofs.flush();
	ofs.close();
	cout<<"OK"<<endl;
return 0;
}
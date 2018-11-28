#include <stdio.h>
#include <string.h>
#include <math.h>
#include <iostream>
#include <queue>

using namespace std;

//struct elem{
//  long num;
//  bool used;
//};

//typedef struct elem Elem;

int main()
{
  int i=0,j=0;
  int T=0, N=0;
  long R=0, k=0;
  long r=0;
  long long money=0;
  long tmpElem;
  queue<long> q;
  queue<long> tmpQueue;
  long tmpGroupSize=0;
  long tmpGuestsSum=0;

  char filename[32]="C-small-attempt0";
  //   char filename[32]="test";

  char infile[32], outfile[32];
  strcpy(infile, filename); strcpy(outfile, filename);
  strcat(infile, ".in"); strcat(outfile, ".out");
  FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
  
  cout<<outfile<<endl; //for delete
  fscanf(fp, "%d", &T);
  cout<<"T="<<T<<endl;  //for delete
 
  for(i=1;i<=T;i++) 
    {
      tmpGuestsSum=0;
      money=0;
      //empty the q and tmpQueue
      while(!q.empty())
	q.pop();
      while(!tmpQueue.empty())
	tmpQueue.pop();


      cout<<"i="<<i<<endl; //for delete
      fscanf(fp, "%ld%ld%d", &R, &k, &N);
      
      cout<<"R="<<R<<" k="<<k<<" N="<<N<<endl; //for delete
      for (j=1; j<=N; j++)
	{
	  fscanf(fp, "%ld", &tmpGroupSize);
	  cout<<" GroupSize="<<tmpGroupSize<<endl; //for delete
	  tmpElem=tmpGroupSize;
	  
	  q.push(tmpElem);
	}
      
      for (r=1; r<=R; r++)
	{
	  cout<<"r="<<r<<endl; //for delete
	  cout<<"tmpElem="<<tmpElem<<endl;
	  while (tmpGuestsSum<=k && !q.empty())
	    {
	      tmpElem=q.front();
	      if (tmpGuestsSum+tmpElem<=k)
		{
		  cout<<"q.size()="<<q.size()<<endl; // for delete
		  q.pop();
		  cout<<"  q.pop("<<tmpElem<<")"<<endl;
		  tmpGuestsSum+=tmpElem;
		  money+=tmpElem;
		  tmpQueue.push(tmpElem);
		  cout<<"  tmpQueue.push("<<tmpElem<<")"<<endl;
		  cout<<"  tmpGuestsSum="<<tmpGuestsSum<<" money="<<money<<endl; //for delete
		}
	      else
		break;
	    }
	  
	  //one round finished
	  tmpGuestsSum=0;
	  while (!tmpQueue.empty())
	    {
	      long tmp1=tmpQueue.front();
	      q.push(tmpQueue.front());
	      tmpQueue.pop();
	      cout<<"q.push("<<tmp1<<")"<<endl;
	      cout<<"tmpQueue.pop("<<tmp1<<")"<<endl;

	    }
	}//loop the rounds
      
      
      fprintf(ofp, "Case #%d: %lld\n", i, money);

    }//T 

  fclose(fp);
  fclose(ofp);

  return 0;
}

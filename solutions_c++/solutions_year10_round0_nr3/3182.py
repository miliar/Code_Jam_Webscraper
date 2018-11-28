#include <fstream>
#include <iostream>
using namespace std;

int main(int argc, char** argv)
{
  ifstream fin;
  fin.open(argv[1]);
  ofstream fout;
  fout.open(argv[2]);

  int num_case;
  fin>>num_case;
  for (int i=0; i<num_case; ++i)
    {
      int R, k, N;
      fin>>R>>k>>N;

      int* cost = new int[N];
      int* group_size = new int[N];
      int* group_eidx = new int[N];
      memset(cost, 0, N*sizeof(int));
      for (int j=0; j<N; ++j)
	{
	  fin>>group_size[j];
	}
      
      int sidx = 0;
      int count = 0;
      int total_cost = 0;
      while (count < R)
	{
	  if ( cost[sidx] == 0 )
	    {
	      int offset = 0;
	      int curr_idx = sidx;
	      while ( offset<N )
		{
		  if ( cost[sidx] + group_size[(sidx+offset)%N] > k )
		    break;
		  else 
		    {
		      curr_idx = (sidx+offset)%N;
		      cost[sidx] += group_size[curr_idx];
		      ++offset;
		    }
		}
	      group_eidx[sidx] = curr_idx;
	    }
	  total_cost += cost[sidx];
	  sidx = (group_eidx[sidx] + 1)%N;
	  ++count;
	}
      fout<<"Case #"<<i+1<<": "<<total_cost<<endl;
      cout<<"Case #"<<i+1<<": "<<total_cost<<endl;
    }

  fin.close();
  fout.close();
}

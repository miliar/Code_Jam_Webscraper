#include <iostream>
#include <string>
#include <vector>
#include <cstdio>


using namespace std;

struct tour
{
  long capacite;
  int suivant;
  long R_backup;
  long long sous_backup;
};

vector<tour> distribution;
    
void preproc(vector<long> groupes, long k)
{
    distribution.clear();
    long N = groupes.size();
    
    for (long i = 0; i < N; ++i) {
      long gi = groupes.at(i);
      
      long j = (i+1) % N;
      int sum = gi;
      while (sum + groupes.at(j) <= k && j != i)
      {
	sum += groupes.at(j);
	j = (j+1) % N;
      }
      
      tour pass;
      pass.capacite = sum;
      pass.suivant = j;
      pass.R_backup = 0;
      pass.sous_backup = 0;
      distribution.push_back(pass);
      //printf("%d : capa:%d, suiv: %d\n", i, sum, j);
    }
  
}


int main(int argc, char **argv) {
  
    int nbtests;
    cin >> nbtests;

    long R, k, N;
    
    for (int test = 0; test<nbtests; test++)
    {
      cin >> R;
      cin >> k;
      cin >> N;
      
      vector<long> groupes;
      groupes.reserve(N);
      long gi = 0;
      for (long i = 0 ; i < N; ++i) {
	cin >> gi;
	groupes.push_back(gi);
      }
      
      preproc(groupes, k);
      
      long pos = 0;
      long long sousous = 0;
      while (R > 0)
      {
	tour passage = distribution.at(pos);
	
	if(passage.R_backup != 0)
	// Already seen that :p
	{
	  long delta_R = passage.R_backup - R;
	  long long delta_sous = sousous - passage.sous_backup;
	  
// 	  cerr << "[" << test << "] R, delta_R: "  << R << " " << delta_R << endl;
// 	  cerr << "    sous, delta_sous: " << sousous << " " << delta_sous << endl;
	  if (R >= delta_R)
	  {
	    long nbfois = R / delta_R;
	    R = R % delta_R;
	    sousous += delta_sous * nbfois;
// 	    cerr << "[" << test << "] --> R, sous: "  << R << " " << sousous << endl;
	  }
	  else
	  {
// 	    cerr << "[" << test << "] R < delta_R: " << R << " " << delta_R << endl;
// 	    distribution[pos].sous_backup = sousous;
// 	    distribution[pos].R_backup = R;
	    
	    R--;
	    sousous += passage.capacite;
	    pos = passage.suivant;
	  }
	}
	else
	{
	  //Back up
	  distribution[pos].sous_backup = sousous;
	  distribution[pos].R_backup = R;
	  
	  R--;
	  sousous += passage.capacite;
	  pos = passage.suivant;
	}
      }
      
      cout << "Case #" << test+1 <<": " << sousous << endl;
      cerr << test+1 << "/" << nbtests << endl;
    }
    
    return 0;
}

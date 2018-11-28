#include <iostream>
#include <fstream>
#include <vector>


using namespace std; 

int main(int argc, char* argv[])
{
  std::ifstream input(argv[1]);
  int cases;
  input>> cases;
  for(int iter=1; iter<=cases; iter++)
  {
    int nteams;
    input >> nteams;
    int* result = new int[nteams*nteams];
    for(int i=0; i<nteams; i++)
    {
       string rs;
       input >> rs;
       int leng = rs.size();
       for(int j=0; j<nteams; j++)
       {
          switch(rs[j]) {
            case '1': result[i*nteams + j] = 1; break;
            case '0': result[i*nteams + j] = 0; break;
            case '.': result[i*nteams + j] = -1; break;
            default: ;
           }
       } 
      }
      double* wp = new double[nteams];
      double* owp = new double[nteams];
      double* oowp = new double[nteams];
      double* adjwp = new double [ nteams*nteams];
      int* matchs = new int[nteams];
      int* scores = new int[nteams];

      for(int j=0; j<nteams; j++)
      {
          matchs[j]=0; 
          scores[j]=0;
      }
      for(int j=0; j<nteams; j++)
      {
          for(int k=0; k<nteams; k++)
          {
             if(result[j*nteams +k] >=0)
             {
                matchs[j]++;
                scores[j] += result[j*nteams +k];
             }
          }
          wp[j] = (double)scores[j]/(double)matchs[j];
      }
      for(int j=0; j<nteams; j++)
      {
        // calculate owp
        for(int k=0; k<nteams; k++)
        {
            int nmatch;
            int nscore;
            if(result[j*nteams+k] >=0)
            { // games between the two
               nmatch = matchs[j] -1;
               nscore = scores[j]-result[j*nteams+k];
               adjwp[j*nteams + k] = (double)nscore/(double)nmatch;
            } 
            else
               adjwp[j*nteams + k] = 0.0;
        }
        
       } // for int j

       for(int j=0; j<nteams; j++)
       {

        double sum=0.0;
        for(int k=0; k<nteams; k++)
           sum += adjwp[k*nteams+j];
        owp[j] = sum/matchs[j];
       }
      
       for(int j=0; j<nteams; j++)
       {
         //calculate oowp
         double sum=0.0;
         for(int k=0; k<nteams; k++)
         {
            if(result[j*nteams+k] >=0) 
              sum += owp[k];
         }
         oowp[j] = sum/matchs[j];
       }

    cout<<"Case #"<<iter<<":" << endl;
    for(int j=0; j<nteams; j++)
    {
    //   cout << "wp=" << wp[j] << " owp=" << owp[j] << " oowp= " << oowp[j];
    //   cout << " score=" << scores[j] << " matches=" << matchs[j]<< endl;
       cout.precision(12);
       double res = 0.25*wp[j]+0.50*owp[j]+0.25*oowp[j];
       cout << res <<endl;
    }
    // cleanup temporary data
    delete[] result;
    delete[] wp;
    delete[] owp;
    delete[] oowp;
    delete[] adjwp;
    delete[] matchs;
    delete[] scores;
 
    }    

}

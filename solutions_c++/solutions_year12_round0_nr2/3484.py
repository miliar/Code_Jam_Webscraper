#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream infile;
    infile.open("B-large.in", ifstream::in);
    ofstream outfile;
    outfile.open("output_2.txt", ofstream::out);
    
    int t = 0;
    infile >> t;
    
    int n = 0;
    int s = 0;
    int p = 0;
    
    int* score = NULL;
    int minSupScore = 0;
    int minNormScore = 0;
    int cntSup = 0;
    int cntSupPlus = 0;
    int cntNormPlus = 0;
    int* cnt = new int[t];
    
    //cout << t << endl;
    for (int i = 1; i < t+1; i++)
    {
       cntSup = 0;
       cntSupPlus = 0;
       cntNormPlus = 0;
        
       infile >> n;
       infile >> s;
       infile >> p;
       
       //cout << n << "\t" << s << "\t" << p << "\t";
       
       score = new int[n];
       minSupScore = p + p-2 + p-2;
       if (p - 2 < 0)
          minSupScore = p;
       minNormScore = p + p-1 + p-1;
       if (p - 1 < 0)
          minNormScore = p;
          
       for (int j = 1; j < n+1; j++)
       {
           infile >> score[j-1];
           cout << score[j-1] << "\t";
           
           if (score[j-1] >= minNormScore)
              cntNormPlus++;
           else if (score[j-1] >= minSupScore)
              cntSupPlus++;
       }
       if (cntSupPlus <= s)
          cnt[i-1] = cntNormPlus + cntSupPlus;
       else
          cnt[i-1] = cntNormPlus + s;
       //cout << "\t" << cnt[i-1] << endl;
       outfile << "Case #" << i << ": " << cnt[i-1] << endl; 
       delete []score;     
    }
    
    delete []cnt;
    
    return 0;
}

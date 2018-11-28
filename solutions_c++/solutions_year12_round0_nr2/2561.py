#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    string in("B-large.in");
    ifstream infile;
    infile.open(in.c_str(), ifstream::in);
    
    size_t found = in.find_last_of(".in");
    string out = in.replace(found-1, 2, "out");    
    ofstream outfile;
    outfile.open(out.c_str(), ofstream::out);
    
    int t = 0;
    infile >> t;
    
    int n = 0;
    int s = 0;
    int p = 0;
    
    int* score = NULL;
    int minSScore = 0;
    int minNScore = 0;
    int cntS = 0;
    int cntSP = 0;
    int cntNP = 0;
    int* cnt = new int[t];
    
    //cout << t << endl;
    for (int i = 1; i < t+1; i++)
    {
       cntS = 0;
       cntSP = 0;
       cntNP = 0;
        
       infile >> n;
       infile >> s;
       infile >> p;
       
       //cout << n << "\t" << s << "\t" << p << "\t";
       
       score = new int[n];
       minSScore = p + p-2 + p-2;
       if (p - 2 < 0)
          minSScore = p;
       minNScore = p + p-1 + p-1;
       if (p - 1 < 0)
          minNScore = p;
          
       for (int j = 1; j < n+1; j++)
       {
           infile >> score[j-1];
           //cout << score[j-1] << "\t";
           
           if (score[j-1] >= minNScore)
              cntNP++;
           else if (score[j-1] >= minSScore)
              cntSP++;
       }
       if (cntSP <= s)
          cnt[i-1] = cntNP + cntSP;
       else
          cnt[i-1] = cntNP + s;
       //cout << "\t" << cnt[i-1] << endl;
       outfile << "Case #" << i << ": " << cnt[i-1] << endl; 
       delete []score;     
    }
    
    delete []cnt;
    infile.close();
    outfile.close();
    
    return 0;
}

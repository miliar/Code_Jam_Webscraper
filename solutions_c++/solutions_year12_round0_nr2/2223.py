#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    int testcases;
    int j;
    int googlers;
    int maxSurprising;
    int bestScore;
    int googlerScore;
    int count;
    int b,c;
    int sum, diff;
    
    ifstream fin;
    ofstream fout;
    
    fin.open("B-large.in", ios::in);
    fout.open("B-large.out", ios::out);
    fin>>testcases;
    
    for(j=1; j<=testcases; j++)
    {
             count=0;
             fin>>googlers>>maxSurprising>>bestScore;
             while(googlers>0)
             {
                              fin>>googlerScore;
                               
                              b = c = googlerScore/3;
                              sum = b*3;
                              diff = googlerScore - sum;
                              if(diff == 2)
                              {
                                      if((c+1) >= bestScore) //had best without surprising element (a + (b+1) + (c+1) = googlerScore)
                                      {
                                           count++;
                                      }
                                      else if((c+2) >= bestScore && maxSurprising >0) //had best in surprising element (a + b + (c+2) = googlerScore)
                                      {
                                           count++;
                                           maxSurprising--;
                                      }
                              }
                              else if(diff == 1)
                              {
                                   if((c+1) >= bestScore) //had best without surprising element (a + b + (c+1) = googlerScore)
                                        count++;
                              }
                              else if(diff == 0)
                              {
                                   if(c >= bestScore) //had best without surprising element (a + b + c = googlerScore)
                                   {
                                        count++;           
                                   }                                   
                                   else if((c+1) >= bestScore && maxSurprising>0 && (b-1)>=0) //had best in surprising element (a + (b-1) + (c+1) = googlerScore)
                                   {
                                        count++;
                                        maxSurprising--;
                                   }
                              }
                              googlers--;
             }
             fout<<"Case #"<<j<<": "<<count<<endl;
    }
    return 0;
}

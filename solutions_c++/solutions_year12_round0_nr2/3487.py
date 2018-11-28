#include<iostream>
#include<fstream>
#include<vector>
#include<cmath>
using namespace std;
bool myfunc (int i,int j) { return (i>j); }
int main()
{
    ofstream fout("output.txt");
    ifstream fin("input.txt");
    int t,numGooglers,surprisingTriplets,p,val;
    vector<int>totalScores,temp;
    vector< vector<int> >possible;
    fin>>t;
    int test = 1;
    bool flag;
    while(test <= t)
    {
                fin>>numGooglers;
                fin>>surprisingTriplets;
                fin>>p;
                totalScores.clear();
                temp.clear();
                possible.clear();
                for(int i=0;i<numGooglers;i++)
                {
                        fin>>val;
                        totalScores.push_back(val);
                        }
                sort(totalScores.begin(),totalScores.end(),myfunc);
                for(int i=0;i<numGooglers;i++)
                {
                        flag = false;
                        for(int k=1;k < totalScores[i]/2 ; k++)
                        {
                                for(int l=1;l < totalScores[i]/2; l++)
                                {
                                        if( abs(k-l) <= 2 && abs(k-(totalScores[i]-k-l)) <= 2 && abs(l-(totalScores[i]-k-l) <= 2) && (k>=1 && k<=10) && (l>=1 && l<=10) && (totalScores[i]-k-l>=1 && totalScores[i]-k-l<=10))
                                        {
                                                    if((abs(k-l) == 2 || abs(k-(totalScores[i]-k-l)) == 2) || abs(l-(totalScores[i]-k-l)) == 2 )
                                                    {
                                                                if(surprisingTriplets-->0){
                                                                flag = true;
                                                               // fout<<i<<" "<<k<<" "<<l<<" "<<totalScores[i]-k-l<<"\n";
                                                                temp.clear();
                                                                temp.push_back(k);
                                                                temp.push_back(l);
                                                                temp.push_back(totalScores[i]-k-l);
                                                                //fout<<temp[0]<<temp[1]<<temp[2]<<"\n";
                                                                possible.push_back(temp);
                                                                break;
                                                                }
                                                                }
                                                    else
                                                    {
                                                                flag = true;
                                                                //fout<<i<<" "<<k<<" "<<l<<" "<<totalScores[i]-k-l<<"\n";
                                                                temp.clear();
                                                                temp.push_back(k);
                                                                temp.push_back(l);
                                                                temp.push_back(totalScores[i]-k-l);
                                                                //fout<<temp[0]<<temp[1]<<temp[2]<<"\n";
                                                                possible.push_back(temp);
                                                                break;
                                                                }
                                                    }
                                        if(flag)
                                        break;
                                        }
                                        if(flag)
                                        break;
                                }
                        }
                int len = possible.size();
                int sum = 0;
                for(int i=0;i<len;i++)
                {
                        for(int j=0;j<possible[i].size();j++)
                        {
                               // fout<<possible[i][j]<<" ";
                                if(possible[i][j] >= p)
                                {
                                                    
                                                    sum++;
                                                    break;
                                                    }
                                }
                                //fout<<"\n";
                        }
                
                fout<<"Case #"<<test<<": "<<sum<<"\n";
                test++;
                }   
}

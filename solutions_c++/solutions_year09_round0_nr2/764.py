#include<iostream>
#include<map>
#include<vector>
using namespace std;
int main()
{
    int T;
    cin >> T;
    for(int t=1;t<=T;t++)
    {
    
    vector<int> V[10000];
    int P[100][100], kol[100][100], H,W, dpo[]={0,0,-1,1,0},dpi[]={0,-1,0,0,1}, dna=0;    
    map<int,char> O;
    cin >> H >> W;
    for(int i=0;i<H;i++)
       for(int j=0;j<W;j++)
       {
               cin >> P[i][j];
               kol[i][j]=-1;
               V[P[i][j]].push_back(i*100+j);              
       }
    for(int i=0;i<10000;i++)
            for(int j=0;j<V[i].size();j++)
            {
                    int min=0;
                    for(int k=1;k<5;k++)
                            if((V[i][j]/100 +dpi[k]<H)&&(V[i][j]/100+dpi[k]>=0)&&(V[i][j]%100 +dpo[k]<W)&&(V[i][j]%100+dpo[k]>=0))
                                            if(P[ V[i][j]/100+dpi[k] ][ V[i][j]%100+dpo[k] ] < P[ V[i][j]/100+dpi[min] ][ V[i][j]%100+dpo[min] ])
                                                  min=k;
                   if(min==0)
                        kol[V[i][j]/100][V[i][j]%100] = dna++;
                        else
                        kol[V[i][j]/100][V[i][j]%100]=kol[ V[i][j]/100+dpi[min] ][ V[i][j]%100+dpo[min] ];
            }
    dna=0;
    cout << "Case #"<< t <<":\n";
    for(int i=0;i<H;i++)
    {
     if(O[kol[i][0]]==0) O[kol[i][0]]='a'+dna++;
                           cout << O[kol[i][0]];
            
            for(int j=1;j<W;j++)
                    {
                    if(O[kol[i][j]]==0) O[kol[i][j]]='a'+dna++;
                    cout <<' '<< O[kol[i][j]];
                    }
               cout<< endl;
       }
    }
    return 0;

}          
               


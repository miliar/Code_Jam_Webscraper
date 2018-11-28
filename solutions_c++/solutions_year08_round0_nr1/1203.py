#include <iostream>
#include <vector>
#include <set>
#include <string>

using namespace std;

int main()
{
  int N;
  int S;
  int Q;
  
  int cpt,num,dist;
  string str;
  
  cin>>N;
  vector<string>* vS;
  vector<string>* vQ;
  
  for(int i=0; i<N; i++)
  {
    vS = new vector<string>();
    vQ = new vector<string>();
    cin >> S;
    getline(cin,str);
    for(int j=0; j<S; j++)
    {
      getline(cin,str);
      vS->push_back(str);
    }
    cin >> Q;
    getline(cin,str);
    for(int j=0; j<Q; j++)
    {
      getline(cin,str);
      vQ->push_back(str);
    }
    
    cpt = 0;
    num = 0;
    dist = 0;
    int etat[S];
    int prev=-1, cptP=0;
    bool flag=false;
    for(int j=0; j<S; j++)
    {
      etat[j]=0;
    }
    
    int k;
    for(int j=0; j<Q; j++)
    {
      dist++;
    //  cout << vS->at(num) << "*" << dist << "*";
      if(vS->at(num).compare(vQ->at(j))==0)
      {
        for(k=0; k<(num); k++)
        {
          etat[k] += 1;
        }
        for(k=(num+1); k<S; k++)
        {
          etat[k] += 1;
        }
        
        etat[num]=0;
        
        for(k=0; k<S; k++)
        {
     //     cout << "**"<< etat[k] << "**";
          if( ((etat[k]-dist)>= 1) || ((etat[k]-dist)==0 && (cptP!=cpt || cpt==0) && prev!=num))// || ((etat[k]-dist)>=0 && S!=2))
          { 
           // cout << "******";
            cptP = cpt;
            prev=num;
            num = k;
            break;
          }
        }
        
        if(k==S)
        {  
          num = (num +1) % S;
            prev=num;
          cpt++;
          dist = 0;
        }
      }
      else
      {
        for(k=0; k<S; k++)
        {
          if(vS->at(k).compare(vQ->at(j))==0)
            etat[k] =0;
          else
            etat[k] +=1;
        }
      }
  //    cout << vQ->at(j) << "*" << vS->at(num) << "*" << etat[num] <<"*"<< cpt << endl;
    }
    printf("Case #%d: %d\n",i+1,cpt);
  }

  return 0;
}

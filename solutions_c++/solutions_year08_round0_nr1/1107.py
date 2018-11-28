#include<iostream>
#include<string>
#include<vector>
#include<stack>
#include<queue>
#include<map>

using namespace std;

/*Google Code Jam 

Saving the Universe
4:51Hrs

*/

#define LI long int
#define AND &&

   vector <string> eNames;
   map <string, bool> checkE;
   
   char tName[101];

void resetMap()
{
 vector <string>::iterator it;
 checkE.clear();
 for(it=eNames.begin();it<eNames.end();it++)
 {
  checkE.insert(pair <string, bool>(*it , false));
 }
}

LI saveUniverse()
{
   LI engines, eC ,queries ,qC;
   string name;
   string str;

   cin>>eC;
   //eC = atoi(str.c_str());
   engines = eC;
   eC++;
   
   while(eC--)
   {
            getline(cin, name);
            //cin.getline(tName,101);
            //cout<<eC+1<<tName<<endl;
            //name = tName;
            eNames.push_back(name);
            checkE.insert(pair <string, bool>(name , false));
   }
  // cout<<"took in "<<engines<<" of names"<<endl;
   cin>>qC;
   queries = qC;
   qC++;
   LI count = engines;
   //cout<<"begining procs @EC"<<count<<endl;
   LI switches = 0;
   while(qC--)
   {
           getline(cin, name);      
           //cin.getline(tName,101);
           //cout<<int(tName[0]);
           //cout<<qC+1<<tName<<endl;

           if(qC == queries)continue;
           
           bool value = checkE[name];
           
           //cout<<name<<endl;
           if(value == false AND count == 1)
           {
                //cout<<"needed a switch on name "<<name<<" for value = "<<value<<" count = "<<count<<endl;                    
                switches++;
                count=engines;
                resetMap();
                count--;
                checkE[name] = true;
           }
           else if(value == false AND count >1)
           {
                count--;
                checkE[name] = true;     
           }
           
           
   }
   return switches;
   
}


int main()
{
    LI testCases;
    LI i=1;
    
    cin>>testCases;
    while(testCases--)
    {
                      eNames.clear();
                      checkE.clear();
                      
                      cout<<"Case #"<<i<<": "<<saveUniverse()<<endl;
                      i++;                
                      
    }
    
    
}

#include <iostream>
#include <string>
#include <fstream>
#include <vector>


using namespace std;



bool chk(string inp,string wrd)
{
     cout<<"chk"<<inp<<":"<<wrd<<"w\n";
     int j=-1;
     for(int i=0;i<wrd.length();i++)
     {
        
        j++;cout<<j<<"x";
        if( j>=inp.length() ) return false;
        if(inp[j]=='(') 
        {
                         j++; cout<<j<<"x";
                         while( inp[j]!=')' )
                         {
                           if(wrd[i]==inp[j]) 
                           { 
                             while( inp[j]!=')' ) j++;
                             cout<<":"<<j<<"x";
                             goto mylabel;                        
                           
                           }
                           j++;cout<<j<<"x";
                           
                         
                         
                         }
                         return false;
        }
        
        else
        { if(wrd[i]!=inp[j]) return false;}
        
        mylabel:
                ;
     
     }
     
     return true;
}
                         
        




int main()
{
    ofstream fout("A.txt");
    ifstream fin("A-small.in");
    
    
    int l,d,n;
    fin>>l>>d>>n;
    
    vector <string> words ;
    words.reserve(d);
    
    
    string temp;
    
    for(int i=0;i<d;i++){ fin>>temp; words.push_back(temp);}
    
    for (int i=0;i<n;i++)
    {
    
       fin>>temp;
       int result=0;
       for(int j=0;j<d;j++) if( chk(temp,words[j])==true ) result++;
       
       fout<< "Case #"<<i+1 <<": "<< result<<endl;
    
    
    }
    
    
    
    
    
    
    cin>>l;
    fin.close();
    fout.close();
    
    return 0;
    
}
